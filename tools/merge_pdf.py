#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将多个 PDF 合并成一个 PDF 的小工具
依赖: pip install pypdf
"""

import argparse
import sys
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
import glob

from pypdf import PdfReader, PdfWriter


def collect_from_dir(directory: Path, recursive: bool) -> list[Path]:
    if not directory.exists():
        print(f"[警告] 目录不存在: {directory}", file=sys.stderr)
        return []
    pattern = "**/*.pdf" if recursive else "*.pdf"
    # 目录收集结果按自然字母顺序排序
    paths = sorted(directory.glob(pattern), key=lambda p: p.name.lower())
    return [p for p in paths if p.is_file() and p.suffix.lower() == ".pdf"]


def expand_inputs(inputs: list[str]) -> list[Path]:
    # 对命令行直接给出的文件或通配符进行展开，保持用户给定的顺序
    result: list[Path] = []
    for item in inputs:
        matches = [Path(m) for m in glob.glob(item, recursive=True)]
        if not matches:
            p = Path(item)
            if p.exists():
                matches = [p]
        if not matches:
            print(f"[警告] 未找到: {item}", file=sys.stderr)
            continue
        for p in matches:
            if p.is_file() and p.suffix.lower() == ".pdf":
                result.append(p)
            else:
                print(f"[跳过] 非PDF或不是文件: {p}", file=sys.stderr)
    return result


def append_pdf(writer: PdfWriter, path: Path, password: str | None) -> bool:
    try:
        reader = PdfReader(str(path))
        if getattr(reader, "is_encrypted", False):
            ok = False
            # 尝试给定密码
            if password is not None:
                try:
                    ok = bool(reader.decrypt(password))
                except Exception:
                    ok = False
            # 尝试空密码
            if not ok:
                try:
                    ok = bool(reader.decrypt(""))
                except Exception:
                    ok = False
            if not ok:
                print(f"[跳过] 加密且需要密码: {path}", file=sys.stderr)
                return False
        writer.append(reader)
        return True
    except Exception as e:
        print(f"[错误] 读取/追加失败: {path} | {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="合并多个 PDF 到一个输出文件")
    parser.add_argument(
        "inputs",
        nargs="*",
        help="输入PDF文件或通配符(按给定顺序合并)，例如 a.pdf b.pdf 或 ./in/*.pdf",
    )
    parser.add_argument(
        "-d", "--dir", type=str, help="从目录批量收集PDF；默认只扫描该目录一级"
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="配合 --dir 递归扫描所有子目录"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="输出PDF文件路径，例如 merged.pdf",
    )
    parser.add_argument(
        "--password", type=str, default=None, help="用于解密所有加密PDF的密码（可选）"
    )
    parser.add_argument(
        "--unique", action="store_true", help="去重输入路径（按首次出现保留）"
    )

    args = parser.parse_args()

    output_path = Path(args.output).resolve()
    input_paths: list[Path] = []

    # 目录收集
    if args.dir:
        input_paths.extend(collect_from_dir(Path(args.dir), args.recursive))

    # 参数输入/通配符
    if args.inputs:
        input_paths.extend(expand_inputs(args.inputs))

    if not input_paths:
        print("[错误] 未找到任何输入PDF。可用示例：", file=sys.stderr)
        print("  python merge_pdfs.py -o merged.pdf a.pdf b.pdf", file=sys.stderr)
        print("  python merge_pdfs.py -o merged.pdf './in/*.pdf'", file=sys.stderr)
        print("  python merge_pdfs.py -d ./in -r -o merged.pdf", file=sys.stderr)
        sys.exit(2)

    # 去重（按首次出现保留）
    if args.unique:
        seen = set()
        deduped = []
        for p in input_paths:
            rp = p.resolve()
            if rp not in seen:
                seen.add(rp)
                deduped.append(p)
        input_paths = deduped

    writer = PdfWriter()

    added = 0
    for p in input_paths:
        ok = append_pdf(writer, p, args.password)
        if ok:
            added += 1

    if added == 0:
        print("[错误] 没有成功追加任何PDF。", file=sys.stderr)
        sys.exit(3)

    # 始终先写入临时文件，避免与输入文件冲突
    try:
        with NamedTemporaryFile(prefix="merged_", suffix=".pdf", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        with open(tmp_path, "wb") as fh:
            writer.write(fh)
        writer.close()

        # 确保输出目录存在
        output_path.parent.mkdir(parents=True, exist_ok=True)
        # 原子替换
        if output_path.exists():
            try:
                os.replace(tmp_path, output_path)
            except Exception:
                # 跨盘符时用移动
                shutil.move(str(tmp_path), str(output_path))
        else:
            shutil.move(str(tmp_path), str(output_path))

        print(f"[完成] 合并 {added} 个PDF -> {output_path}")
    except Exception as e:
        print(f"[错误] 写出失败: {e}", file=sys.stderr)
        try:
            writer.close()
        except Exception:
            pass
        sys.exit(4)


if __name__ == "__main__":
    main()
