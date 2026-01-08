#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF压缩工具
支持通过调整图像质量和优化来压缩PDF文件大小
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, Tuple
import fitz  # PyMuPDF
from PIL import Image
import io


class PDFCompressor:
    """PDF压缩工具类"""

    def __init__(self):
        self.supported_formats = [".pdf"]

    def validate_file(self, file_path: str) -> bool:
        """验证输入文件是否有效"""
        if not os.path.exists(file_path):
            print(f"错误: 文件 '{file_path}' 不存在")
            return False

        if not file_path.lower().endswith(".pdf"):
            print("错误: 不支持的文件格式，仅支持PDF文件")
            return False

        return True

    def get_file_size(self, file_path: str) -> int:
        """获取文件大小（字节）"""
        return os.path.getsize(file_path)

    def format_size(self, size_bytes: int) -> str:
        """格式化文件大小显示"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

    def compress_image(self, image_data: bytes, quality: int = 50) -> bytes:
        """压缩图像数据"""
        try:
            # 打开图像
            image = Image.open(io.BytesIO(image_data))

            # 转换为RGB（如果需要）
            if image.mode in ("RGBA", "LA", "P"):
                # 创建白色背景
                background = Image.new("RGB", image.size, (255, 255, 255))
                if image.mode == "P":
                    image = image.convert("RGBA")
                background.paste(
                    image,
                    mask=image.split()[-1] if image.mode in ("RGBA", "LA") else None,
                )
                image = background
            elif image.mode != "RGB":
                image = image.convert("RGB")

            # 压缩图像
            output = io.BytesIO()
            image.save(output, format="JPEG", quality=quality, optimize=True)
            return output.getvalue()

        except Exception as e:
            print(f"警告: 图像压缩失败: {e}")
            return image_data

    def compress_pdf_method1(
        self, input_path: str, output_path: str, compression_level: int = 50
    ) -> bool:
        """
        方法1: 使用PyMuPDF进行PDF压缩
        compression_level: 0-100, 100为无压缩，0为最大压缩
        """
        try:
            # 打开PDF文档
            doc = fitz.open(input_path)

            # 计算图像质量 (compression_level转换为质量参数)
            image_quality = max(10, min(95, compression_level))

            # 处理每一页
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)

                # 获取页面中的图像
                image_list = page.get_images()

                for img_index, img in enumerate(image_list):
                    try:
                        # 获取图像数据
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_data = base_image["image"]

                        # 压缩图像
                        compressed_data = self.compress_image(
                            image_data, quality=image_quality
                        )

                        # 如果压缩后的图像更小，则替换
                        if len(compressed_data) < len(image_data):
                            # 创建新的图像对象
                            # compressed_image = fitz.Pixmap(compressed_data)
                            # 替换原图像
                            doc.update_stream(xref, compressed_data)

                    except Exception as e:
                        print(
                            f"警告: 处理第{page_num + 1}页的图像{img_index + 1}时出错: {e}"
                        )
                        continue

            # 保存压缩后的PDF
            doc.save(output_path, garbage=4, deflate=True, clean=True)
            doc.close()

            return True

        except Exception as e:
            print(f"错误: PDF压缩失败: {e}")
            return False

    def compress_pdf_method2(
        self, input_path: str, output_path: str, compression_level: int = 50
    ) -> bool:
        """
        方法2: 使用重新渲染的方式压缩PDF
        compression_level: 0-100, 100为无压缩，0为最大压缩
        """
        try:
            # 打开PDF文档
            doc = fitz.open(input_path)

            # 创建新的PDF文档
            new_doc = fitz.open()

            # 计算DPI (compression_level转换为DPI)
            # 100% = 150 DPI, 50% = 100 DPI, 0% = 72 DPI
            dpi = int(72 + (compression_level / 100) * 78)

            for page_num in range(len(doc)):
                page = doc.load_page(page_num)

                # 渲染页面为图像
                mat = fitz.Matrix(dpi / 72, dpi / 72)
                pix = page.get_pixmap(matrix=mat)

                # 转换为PIL图像并压缩
                img_data = pix.tobytes("png")
                compressed_data = self.compress_image(
                    img_data, quality=compression_level
                )

                # 创建新页面
                img_doc = fitz.open("png", compressed_data)
                new_page = new_doc.new_page(
                    width=page.rect.width, height=page.rect.height
                )
                new_page.show_pdf_page(page.rect, img_doc, 0)
                img_doc.close()

            # 保存新文档
            new_doc.save(output_path, garbage=4, deflate=True, clean=True)
            new_doc.close()
            doc.close()

            return True

        except Exception as e:
            print(f"错误: PDF压缩失败: {e}")
            return False

    def compress_pdf(
        self,
        input_path: str,
        output_path: str = None,
        compression_percent: int = 50,
        method: str = "smart",
    ) -> Tuple[bool, Optional[str]]:
        """
        压缩PDF文件

        Args:
            input_path: 输入PDF文件路径
            output_path: 输出PDF文件路径（可选）
            compression_percent: 压缩百分比 (0-100)，0为最大压缩，100为无压缩
            method: 压缩方法 ("smart", "image", "render")

        Returns:
            (成功标志, 输出文件路径)
        """
        # 验证输入文件
        if not self.validate_file(input_path):
            return False, None

        # 验证压缩百分比
        if not 0 <= compression_percent <= 100:
            print("错误: 压缩百分比必须在0-100之间")
            return False, None

        # 生成输出文件路径
        if output_path is None:
            input_file = Path(input_path)
            output_path = str(
                input_file.parent / f"{input_file.stem}_compressed{input_file.suffix}"
            )

        # 获取原始文件大小
        original_size = self.get_file_size(input_path)
        print(f"原始文件大小: {self.format_size(original_size)}")

        # 选择压缩方法
        success = False

        if method in ("smart", "image"):
            print("使用图像优化方法压缩...")
            success = self.compress_pdf_method1(
                input_path, output_path, compression_percent
            )

            # 如果smart模式且第一种方法效果不好，尝试第二种方法
            if method == "smart" and success:
                compressed_size = self.get_file_size(output_path)
                compression_ratio = (original_size - compressed_size) / original_size

                # 如果压缩效果不明显（小于10%），尝试第二种方法
                if compression_ratio < 0.1:
                    print("压缩效果不明显，尝试重新渲染方法...")
                    temp_output = output_path + ".temp"
                    if self.compress_pdf_method2(
                        input_path, temp_output, compression_percent
                    ):
                        temp_size = self.get_file_size(temp_output)
                        # 如果第二种方法效果更好，使用第二种方法的结果
                        if temp_size < compressed_size:
                            os.replace(temp_output, output_path)
                        else:
                            os.remove(temp_output)

        elif method == "render":
            print("使用重新渲染方法压缩...")
            success = self.compress_pdf_method2(
                input_path, output_path, compression_percent
            )

        else:
            print(f"错误: 不支持的压缩方法 '{method}'")
            return False, None

        if success:
            compressed_size = self.get_file_size(output_path)
            compression_ratio = (original_size - compressed_size) / original_size * 100

            print("压缩完成!")
            print(f"压缩后大小: {self.format_size(compressed_size)}")
            print(f"压缩率: {compression_ratio:.1f}%")
            print(f"输出文件: {output_path}")

            return True, output_path
        else:
            return False, None


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="PDF压缩工具 - 减少PDF文件大小",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  %(prog)s input.pdf                          # 使用默认50%%压缩
  %(prog)s input.pdf -c 30                    # 30%%压缩级别
  %(prog)s input.pdf -o compressed.pdf        # 指定输出文件
  %(prog)s input.pdf -c 20 -m render          # 使用重新渲染方法
  
压缩级别说明:
  0   - 最大压缩（文件最小，可能损失较多质量）
  50  - 平衡压缩（默认，文件大小和质量平衡）
  100 - 无压缩（保持原始质量）
  
压缩方法说明:
  smart  - 智能选择最佳方法（默认）
  image  - 仅优化图像
  render - 重新渲染页面
        """,
    )

    parser.add_argument("input", help="输入PDF文件路径")
    parser.add_argument("-o", "--output", help="输出PDF文件路径")
    parser.add_argument(
        "-c", "--compression", type=int, default=50, help="压缩级别 (0-100, 默认: 50)"
    )
    parser.add_argument(
        "-m",
        "--method",
        choices=["smart", "image", "render"],
        default="smart",
        help="压缩方法 (默认: smart)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="显示详细信息")

    args = parser.parse_args()

    # 创建压缩器实例
    compressor = PDFCompressor()

    # 执行压缩
    success, output_path = compressor.compress_pdf(
        input_path=args.input,
        output_path=args.output,
        compression_percent=args.compression,
        method=args.method,
    )

    if success:
        print(f"\n✅ 压缩成功！输出文件: {output_path}")
        sys.exit(0)
    else:
        print("\n❌ 压缩失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()
