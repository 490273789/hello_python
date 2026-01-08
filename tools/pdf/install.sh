#!/bin/bash
# PDF压缩工具安装脚本

echo "🔧 PDF压缩工具安装程序"
echo "========================"

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3，请先安装Python3"
    exit 1
fi

echo "✅ Python3已安装"

# 检查pip是否已安装
if ! command -v pip3 &> /dev/null; then
    echo "❌ 错误: 未找到pip3，请先安装pip3"
    exit 1
fi

echo "✅ pip3已安装"

# 安装依赖包
echo "📦 正在安装依赖包..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ 依赖包安装成功！"
else
    echo "❌ 依赖包安装失败"
    exit 1
fi

# 使脚本可执行
chmod +x pdf_compressor.py
chmod +x example_usage.py

echo "🎉 安装完成！"
echo ""
echo "使用方法:"
echo "  python3 pdf_compressor.py input.pdf"
echo "  python3 pdf_compressor.py input.pdf -c 30"
echo "  python3 pdf_compressor.py input.pdf -o output.pdf"
echo ""
echo "查看帮助:"
echo "  python3 pdf_compressor.py --help"
echo ""
echo "运行示例:"
echo "  python3 example_usage.py"