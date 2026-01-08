# PDF 压缩工具

一个简单而强大的 Python PDF 压缩工具，可以显著减少 PDF 文件的大小，同时保持良好的视觉质量。

## 功能特性

- 🗜️ **多种压缩方法**: 智能选择、图像优化、重新渲染
- 🎛️ **可调压缩级别**: 0-100 的压缩级别，自由控制文件大小和质量
- 📊 **压缩统计**: 显示压缩前后的文件大小和压缩率
- 🛡️ **安全可靠**: 不会覆盖原文件，自动生成新的压缩文件
- 🖼️ **图像优化**: 智能压缩 PDF 中的图像，减少文件体积
- 🔧 **命令行友好**: 支持批处理和脚本自动化

## 安装依赖

在使用之前，请安装所需的 Python 包：

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install PyMuPDF Pillow
```

## 使用方法

### 基本用法

```bash
# 使用默认设置压缩PDF（50%压缩级别）
python pdf_compressor.py input.pdf

# 指定压缩级别（0-100）
python pdf_compressor.py input.pdf -c 30

# 指定输出文件名
python pdf_compressor.py input.pdf -o compressed_output.pdf

# 指定压缩方法
python pdf_compressor.py input.pdf -c 20 -m render
```

### 命令行参数

| 参数            | 简写 | 说明              | 默认值                      |
| --------------- | ---- | ----------------- | --------------------------- |
| `input`         | -    | 输入 PDF 文件路径 | **必需**                    |
| `--output`      | `-o` | 输出 PDF 文件路径 | `{原文件名}_compressed.pdf` |
| `--compression` | `-c` | 压缩级别 (0-100)  | `50`                        |
| `--method`      | `-m` | 压缩方法          | `smart`                     |
| `--verbose`     | `-v` | 显示详细信息      | `False`                     |

### 压缩级别说明

| 级别     | 说明         | 适用场景                       |
| -------- | ------------ | ------------------------------ |
| `0-20`   | **最大压缩** | 文件大小优先，可接受质量损失   |
| `30-50`  | **平衡压缩** | 文件大小和质量平衡 ⭐ **推荐** |
| `60-80`  | **轻度压缩** | 质量优先，适度减小文件         |
| `90-100` | **最小压缩** | 保持高质量，轻微压缩           |

### 压缩方法说明

| 方法     | 说明         | 优点                   | 缺点                  |
| -------- | ------------ | ---------------------- | --------------------- |
| `smart`  | **智能选择** | 自动选择最佳方法       | -                     |
| `image`  | **图像优化** | 保持文本清晰，压缩图像 | 对纯文本 PDF 效果有限 |
| `render` | **重新渲染** | 压缩效果明显           | 可能影响文本质量      |

## 使用示例

### 1. 快速压缩

```bash
# 最简单的用法，使用默认设置
python pdf_compressor.py document.pdf
```

输出：

```
原始文件大小: 15.2 MB
使用图像优化方法压缩...
压缩完成!
压缩后大小: 8.7 MB
压缩率: 42.8%
输出文件: document_compressed.pdf

✅ 压缩成功！输出文件: document_compressed.pdf
```

### 2. 自定义压缩级别

```bash
# 使用30%压缩级别（更强的压缩）
python pdf_compressor.py large_document.pdf -c 30
```

### 3. 指定输出文件

```bash
# 将压缩后的文件保存为指定名称
python pdf_compressor.py report.pdf -o report_small.pdf -c 40
```

### 4. 最大压缩

```bash
# 追求最小文件大小
python pdf_compressor.py presentation.pdf -c 10 -m render
```

### 5. 批量处理（使用 Shell 脚本）

```bash
# 批量压缩当前目录下的所有PDF文件
for file in *.pdf; do
    python pdf_compressor.py "$file" -c 40
done
```

## 在 Python 脚本中使用

你也可以在 Python 脚本中直接使用 PDFCompressor 类：

```python
from pdf_compressor import PDFCompressor

# 创建压缩器实例
compressor = PDFCompressor()

# 压缩PDF文件
success, output_path = compressor.compress_pdf(
    input_path="input.pdf",
    output_path="compressed.pdf",
    compression_percent=30,
    method="smart"
)

if success:
    print(f"压缩成功：{output_path}")
else:
    print("压缩失败")
```

## 性能优化建议

1. **选择合适的压缩级别**：

   - 对于网络分享：使用 20-40%的压缩级别
   - 对于存档保存：使用 60-80%的压缩级别
   - 对于临时查看：使用 10-30%的压缩级别

2. **根据 PDF 类型选择方法**：

   - 图像丰富的 PDF：使用`image`方法
   - 扫描文档：使用`render`方法
   - 混合内容：使用`smart`方法（默认）

3. **批量处理**：
   - 对于大量文件，建议使用 Shell 脚本或 Python 脚本批量处理

## 常见问题

### Q: 压缩后的 PDF 能否正常打开？

A: 是的，压缩后的 PDF 完全兼容标准 PDF 阅读器，可以正常打开和使用。

### Q: 会损失文档质量吗？

A: 压缩主要影响图像质量，文本通常保持清晰。可以通过调整压缩级别来平衡文件大小和质量。

### Q: 原文件会被覆盖吗？

A: 不会，工具会创建新的压缩文件，原文件保持不变。

### Q: 支持哪些 PDF 版本？

A: 支持所有常见的 PDF 版本，包括 PDF 1.3 到 PDF 2.0。

### Q: 压缩需要多长时间？

A: 压缩时间取决于文件大小和复杂度，通常几秒到几分钟不等。

## 技术细节

- **PDF 处理库**: PyMuPDF (fitz)
- **图像处理库**: Pillow (PIL)
- **压缩算法**: JPEG 压缩 + PDF 优化
- **支持格式**: PDF 输入和输出

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

---

**提示**: 建议在压缩重要文档前先备份原文件，并测试压缩效果是否满足需求。
