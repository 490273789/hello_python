#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF压缩工具使用示例
演示如何在Python脚本中使用PDFCompressor类
"""

from pdf_compressor import PDFCompressor
import os


def example_basic_compression():
    """基本压缩示例"""
    print("=== 基本压缩示例 ===")

    # 创建压缩器实例
    compressor = PDFCompressor()

    # 假设有一个名为 test.pdf 的文件
    input_file = "test.pdf"

    if not os.path.exists(input_file):
        print(f"请将要压缩的PDF文件重命名为 '{input_file}' 并放在当前目录")
        return False

    # 使用默认设置压缩（50%压缩级别）
    success, output_path = compressor.compress_pdf(
        input_path=input_file, compression_percent=50, method="smart"
    )

    if success:
        print(f"✅ 压缩成功！输出文件: {output_path}")
        return True
    else:
        print("❌ 压缩失败")
        return False


def example_custom_compression():
    """自定义压缩示例"""
    print("\n=== 自定义压缩示例 ===")

    compressor = PDFCompressor()
    input_file = "test.pdf"

    if not os.path.exists(input_file):
        print(f"请将要压缩的PDF文件重命名为 '{input_file}' 并放在当前目录")
        return False

    # 自定义压缩参数
    success, output_path = compressor.compress_pdf(
        input_path=input_file,
        output_path="test_custom_compressed.pdf",
        compression_percent=30,  # 更强的压缩
        method="image",  # 使用图像优化方法
    )

    if success:
        print(f"✅ 自定义压缩成功！输出文件: {output_path}")
        return True
    else:
        print("❌ 自定义压缩失败")
        return False


def example_batch_compression():
    """批量压缩示例"""
    print("\n=== 批量压缩示例 ===")

    compressor = PDFCompressor()

    # 查找当前目录下的所有PDF文件
    pdf_files = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("当前目录下没有找到PDF文件")
        return False

    print(f"找到 {len(pdf_files)} 个PDF文件:")
    for file in pdf_files:
        print(f"  - {file}")

    # 批量压缩
    successful_compressions = 0

    for pdf_file in pdf_files:
        print(f"\n正在压缩: {pdf_file}")

        # 跳过已经压缩过的文件
        if "_compressed" in pdf_file:
            print("  跳过（已压缩文件）")
            continue

        success, output_path = compressor.compress_pdf(
            input_path=pdf_file, compression_percent=40, method="smart"
        )

        if success:
            print(f"  ✅ 压缩成功: {output_path}")
            successful_compressions += 1
        else:
            print(f"  ❌ 压缩失败: {pdf_file}")

    print(f"\n批量压缩完成！成功压缩 {successful_compressions} 个文件")
    return successful_compressions > 0


def example_compression_levels():
    """不同压缩级别对比示例"""
    print("\n=== 压缩级别对比示例 ===")

    compressor = PDFCompressor()
    input_file = "test.pdf"

    if not os.path.exists(input_file):
        print(f"请将要压缩的PDF文件重命名为 '{input_file}' 并放在当前目录")
        return False

    # 获取原始文件大小
    original_size = compressor.get_file_size(input_file)
    print(f"原始文件大小: {compressor.format_size(original_size)}")

    # 测试不同压缩级别
    compression_levels = [20, 50, 80]

    for level in compression_levels:
        print(f"\n测试压缩级别: {level}%")

        output_file = f"test_level_{level}.pdf"
        success, output_path = compressor.compress_pdf(
            input_path=input_file,
            output_path=output_file,
            compression_percent=level,
            method="smart",
        )

        if success:
            compressed_size = compressor.get_file_size(output_path)
            ratio = (original_size - compressed_size) / original_size * 100
            print(f"  压缩后大小: {compressor.format_size(compressed_size)}")
            print(f"  压缩率: {ratio:.1f}%")
        else:
            print("  压缩失败")

    return True


def main():
    """主函数"""
    print("PDF压缩工具使用示例")
    print("=" * 50)

    try:
        # 检查依赖
        import fitz
        from PIL import Image

        print("✅ 依赖检查通过")
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return

    # 运行示例
    examples = [
        ("基本压缩", example_basic_compression),
        ("自定义压缩", example_custom_compression),
        ("批量压缩", example_batch_compression),
        ("压缩级别对比", example_compression_levels),
    ]

    for name, func in examples:
        try:
            print(f"\n{'=' * 20} {name} {'=' * 20}")
            func()
        except Exception as e:
            print(f"❌ {name}示例运行出错: {e}")

    print("\n" + "=" * 50)
    print("示例运行完成！")
    print("\n使用说明:")
    print("1. 将要压缩的PDF文件重命名为 'test.pdf' 并放在当前目录")
    print("2. 运行 python example_usage.py")
    print("3. 查看生成的压缩文件")


if __name__ == "__main__":
    main()
