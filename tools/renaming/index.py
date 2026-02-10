"""
批量文件重命名工具
==================
支持的重命名规则：
  1. 添加前缀/后缀
  2. 查找替换
  3. 序号重命名 (001, 002, ...)
  4. 正则替换
  5. 大小写转换 (大写/小写/首字母大写)
  6. 删除指定字符
  7. 替换前 N 个字符

用法：
  python index.py
  然后按交互提示操作即可。
"""

import os
import re
from pathlib import Path


# ─── 工具函数 ─────────────────────────────────────────────

def get_files(directory: str, extensions: list[str] | None = None) -> list[Path]:
    """获取目录下的文件列表（不含子目录文件），可按扩展名筛选。"""
    dir_path = Path(directory)
    if not dir_path.is_dir():
        print(f"❌ 路径无效或不是目录: {directory}")
        return []

    files = sorted(f for f in dir_path.iterdir() if f.is_file())
    if extensions:
        exts = {e.lower().lstrip(".") for e in extensions}
        files = [f for f in files if f.suffix.lower().lstrip(".") in exts]
    return files


def preview_and_confirm(rename_pairs: list[tuple[Path, Path]]) -> bool:
    """预览重命名结果并确认。"""
    if not rename_pairs:
        print("⚠️  没有需要重命名的文件。")
        return False

    # 过滤掉名称没有变化的
    rename_pairs = [(src, dst) for src, dst in rename_pairs if src.name != dst.name]
    if not rename_pairs:
        print("⚠️  所有文件名称未发生变化，无需操作。")
        return False

    print(f"\n{'─' * 60}")
    print(f"  即将重命名 {len(rename_pairs)} 个文件：")
    print(f"{'─' * 60}")
    for i, (src, dst) in enumerate(rename_pairs, 1):
        print(f"  {i:>3}. {src.name}")
        print(f"    ➜  {dst.name}")
    print(f"{'─' * 60}")

    # 检查冲突
    dst_names = [dst.name for _, dst in rename_pairs]
    if len(dst_names) != len(set(dst_names)):
        print("❌ 目标文件名存在重复，请调整规则！")
        return False

    for _, dst in rename_pairs:
        if dst.exists():
            print(f"❌ 目标文件已存在: {dst.name}，请调整规则！")
            return False

    choice = input("\n确认执行? (y/n): ").strip().lower()
    return choice in ("y", "yes")


def execute_rename(rename_pairs: list[tuple[Path, Path]]) -> None:
    """执行重命名操作。"""
    rename_pairs = [(s, d) for s, d in rename_pairs if s.name != d.name]
    success = 0
    for src, dst in rename_pairs:
        try:
            src.rename(dst)
            success += 1
        except OSError as e:
            print(f"❌ 重命名失败 {src.name}: {e}")
    print(f"\n✅ 成功重命名 {success}/{len(rename_pairs)} 个文件。")


# ─── 重命名规则 ───────────────────────────────────────────

def rule_add_prefix_suffix(files: list[Path]) -> list[tuple[Path, Path]]:
    """添加前缀或后缀。"""
    prefix = input("  输入前缀 (留空跳过): ").strip()
    suffix = input("  输入后缀 (留空跳过): ").strip()
    pairs = []
    for f in files:
        stem, ext = f.stem, f.suffix
        new_name = f"{prefix}{stem}{suffix}{ext}"
        pairs.append((f, f.parent / new_name))
    return pairs


def rule_find_replace(files: list[Path]) -> list[tuple[Path, Path]]:
    """查找并替换文件名中的文本。"""
    old = input("  查找文本: ").strip()
    if not old:
        print("  ⚠️  查找文本不能为空。")
        return []
    new = input("  替换为: ").strip()
    pairs = []
    for f in files:
        new_stem = f.stem.replace(old, new)
        pairs.append((f, f.parent / f"{new_stem}{f.suffix}"))
    return pairs


def rule_sequential(files: list[Path]) -> list[tuple[Path, Path]]:
    """按序号重命名。"""
    template = input("  命名模板 (用 {n} 代表序号，如 photo_{n}): ").strip()
    if "{n}" not in template:
        print("  ⚠️  模板必须包含 {n} 占位符。")
        return []
    start = int(input("  起始编号 (默认 1): ").strip() or "1")
    width = int(input("  序号位数 (默认 3，如 001): ").strip() or "3")
    pairs = []
    for i, f in enumerate(files, start):
        num = str(i).zfill(width)
        new_name = template.replace("{n}", num) + f.suffix
        pairs.append((f, f.parent / new_name))
    return pairs


def rule_regex_replace(files: list[Path]) -> list[tuple[Path, Path]]:
    """正则表达式替换。"""
    pattern = input("  正则表达式: ").strip()
    replacement = input("  替换为 (支持 \\1 反向引用): ").strip()
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"  ❌ 正则表达式无效: {e}")
        return []
    pairs = []
    for f in files:
        new_stem = regex.sub(replacement, f.stem)
        pairs.append((f, f.parent / f"{new_stem}{f.suffix}"))
    return pairs


def rule_change_case(files: list[Path]) -> list[tuple[Path, Path]]:
    """大小写转换。"""
    print("  转换方式:")
    print("    1. 全部大写")
    print("    2. 全部小写")
    print("    3. 首字母大写 (Title Case)")
    choice = input("  选择 (1-3): ").strip()
    pairs = []
    for f in files:
        stem = f.stem
        match choice:
            case "1":
                new_stem = stem.upper()
            case "2":
                new_stem = stem.lower()
            case "3":
                new_stem = stem.title()
            case _:
                print("  ⚠️  无效选择。")
                return []
        pairs.append((f, f.parent / f"{new_stem}{f.suffix}"))
    return pairs


def rule_remove_chars(files: list[Path]) -> list[tuple[Path, Path]]:
    """删除指定字符。"""
    print("  删除选项:")
    print("    1. 删除所有空格")
    print("    2. 删除指定字符")
    print("    3. 删除所有非字母数字字符 (保留中文)")
    choice = input("  选择 (1-3): ").strip()
    pairs = []
    for f in files:
        stem = f.stem
        match choice:
            case "1":
                new_stem = stem.replace(" ", "")
            case "2":
                chars = input("  要删除的字符: ").strip()
                new_stem = stem
                for ch in chars:
                    new_stem = new_stem.replace(ch, "")
            case "3":
                # 保留字母、数字、中文、下划线、连字符
                new_stem = re.sub(r"[^\w\u4e00-\u9fff\-]", "", stem)
            case _:
                print("  ⚠️  无效选择。")
                return []
        pairs.append((f, f.parent / f"{new_stem}{f.suffix}"))
    return pairs


def rule_replace_first_n(files: list[Path]) -> list[tuple[Path, Path]]:
    """替换前 N 个字符。"""
    n = input("  替换前几个字符 (N): ").strip()
    if not n.isdigit() or int(n) <= 0:
        print("  ⚠️  请输入正整数。")
        return []
    n = int(n)
    replacement = input("  替换为 (可留空表示删除): ").strip()
    pairs = []
    for f in files:
        stem = f.stem
        if len(stem) < n:
            print(f"  ⚠️  文件名 '{stem}' 长度不足 {n}，跳过。")
            pairs.append((f, f))
        else:
            new_stem = replacement + stem[n:]
            pairs.append((f, f.parent / f"{new_stem}{f.suffix}"))
    return pairs


# ─── 扩展名筛选 ───────────────────────────────────────────

def ask_extension_filter() -> list[str] | None:
    """询问是否按扩展名筛选。"""
    ext_input = input("筛选文件扩展名 (如 jpg,png 留空表示所有文件): ").strip()
    if ext_input:
        return [e.strip() for e in ext_input.split(",")]
    return None


# ─── 主程序 ───────────────────────────────────────────────

RULES = {
    "1": ("添加前缀/后缀", rule_add_prefix_suffix),
    "2": ("查找替换", rule_find_replace),
    "3": ("序号重命名", rule_sequential),
    "4": ("正则替换", rule_regex_replace),
    "5": ("大小写转换", rule_change_case),
    "6": ("删除指定字符", rule_remove_chars),
    "7": ("替换前 N 个字符", rule_replace_first_n),
}


def main():
    print("=" * 60)
    print("  📁 批量文件重命名工具")
    print("=" * 60)

    while True:
        # 1. 输入目录
        directory = input("\n请输入文件夹路径 (输入 q 退出): ").strip()
        if directory.lower() == "q":
            print("👋 再见！")
            break

        # 展开 ~ 并转为绝对路径
        directory = os.path.expanduser(directory)
        directory = os.path.abspath(directory)

        if not os.path.isdir(directory):
            print(f"❌ 无效路径: {directory}")
            continue

        # 2. 扩展名筛选
        extensions = ask_extension_filter()

        # 3. 获取文件列表
        files = get_files(directory, extensions)
        if not files:
            print("⚠️  目录中没有找到匹配的文件。")
            continue

        print(f"\n📂 目录: {directory}")
        print(f"📄 共 {len(files)} 个文件:")
        for i, f in enumerate(files, 1):
            print(f"  {i:>3}. {f.name}")

        # 4. 选择规则
        print("\n重命名规则:")
        for key, (name, _) in RULES.items():
            print(f"  {key}. {name}")

        rule_choice = input("\n选择规则 (1-7): ").strip()
        if rule_choice not in RULES:
            print("⚠️  无效选择。")
            continue

        rule_name, rule_func = RULES[rule_choice]
        print(f"\n▶ {rule_name}")

        # 5. 执行规则生成重命名对
        rename_pairs = rule_func(files)

        # 6. 预览并确认
        if preview_and_confirm(rename_pairs):
            execute_rename(rename_pairs)
        else:
            print("⏭️  已跳过。")


if __name__ == "__main__":
    main()
