# Python 学习项目

## uv 常用命令

### 初始化

```bash
# 初始化新项目
uv init

# 初始化带有特定 Python 版本的项目
uv init --python 3.12
```

### Python 版本管理

```bash
# 安装指定 Python 版本
uv python install 3.12

# 列出已安装的 Python 版本
uv python list

# 查找可用的 Python 版本
uv python find

# 固定项目使用的 Python 版本
uv python pin 3.12
```

### 依赖管理

```bash
# 添加依赖
uv add requests
uv add numpy pandas

# 添加开发依赖
uv add --dev pytest black ruff

# 添加指定版本的依赖
uv add "requests>=2.31.0"
uv add "django==4.2.0"

# 移除依赖
uv remove requests

# 更新依赖
uv lock --upgrade
uv lock --upgrade-package requests

# 同步依赖（安装 pyproject.toml 中的所有依赖）
uv sync

# 仅同步生产依赖
uv sync --no-dev
```

### 运行命令

```bash
# 运行 Python 脚本
uv run main.py
uv run python main.py

# 运行指定的命令
uv run pytest
uv run black .
uv run ruff check .

# 在虚拟环境中执行命令
uv run --python 3.12 python script.py
```

### 虚拟环境管理

```bash
# 创建虚拟环境
uv venv

# 创建指定 Python 版本的虚拟环境
uv venv --python 3.12

# 激活虚拟环境 (macOS/Linux)
source .venv/bin/activate

# 停用虚拟环境
deactivate
```



### 锁文件操作

```bash
# 生成/更新锁文件
uv lock

# 升级所有依赖到最新版本
uv lock --upgrade

# 升级指定包
uv lock --upgrade-package requests
```

### 构建与发布

```bash
# 构建项目
uv build

# 构建为 wheel
uv build --wheel

# 构建为源码分发
uv build --sdist
```

### 工具运行

```bash
# 临时运行工具（无需安装）
uvx black .
uvx ruff check .
uvx pytest

# 指定工具版本运行
uvx black@23.0.0 .
```

### 缓存管理

```bash
# 清理缓存
uv cache clean

# 查看缓存目录
uv cache dir
```

### 其他常用命令

```bash
# 查看 uv 版本
uv --version

# 查看帮助
uv --help
uv add --help

# 自我更新
uv self update

# 生成 requirements.txt
uv pip freeze > requirements.txt

# 检查项目配置
uv tree
```

### 常见工作流

#### 创建新项目
```bash
# 1. 创建项目目录
mkdir my-project && cd my-project

# 2. 初始化项目
uv init --python 3.12

# 3. 添加依赖
uv add requests pandas

# 4. 运行项目
uv run python main.py
```

#### 克隆现有项目
```bash
# 1. 克隆仓库
git clone <repo-url>
cd <repo-name>

# 2. 同步依赖
uv sync

# 3. 运行项目
uv run python main.py
```

### uv vs pip 命令对照

| pip 命令 | uv 命令 |
|---------|---------|
| `pip install package` | `uv add package` 或 `uv pip install package` |
| `pip install -r requirements.txt` | `uv sync` 或 `uv pip install -r requirements.txt` |
| `pip uninstall package` | `uv remove package` 或 `uv pip uninstall package` |
| `pip list` | `uv pip list` |
| `pip freeze` | `uv pip freeze` |
| `pip show package` | `uv pip show package` |
| `python -m venv .venv` | `uv venv` |

### 配置文件

uv 主要使用 `pyproject.toml` 来管理项目配置和依赖：

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project description"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
]
```

### 提示

- uv 比 pip 快得多（10-100 倍）
- `uv add` 会自动更新 `pyproject.toml` 和 `uv.lock`
- `uv sync` 会根据锁文件安装确切的依赖版本
- 使用 `uv run` 可以确保在正确的虚拟环境中运行命令
- `uvx` 适合临时运行工具，无需全局安装
