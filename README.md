<div align="center"><img src="./assets/logo-readme.png" alt="Python Scientific Tutorial Logo" width="260" />

### 从 Python 基础一路学到科学计算、数据分析、统计建模与面板计量

**一套连续、现代、可复现的 Python 科学计算中文教程**

[![Tutorial Quality](https://github.com/hujinghaoabcd/python-scientific-tutorial/actions/workflows/quality.yml/badge.svg)](https://github.com/hujinghaoabcd/python-scientific-tutorial/actions/workflows/quality.yml)
[![Python](https://img.shields.io/badge/Python-3.12--3.14-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F5C344.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hujinghaoabcd/python-scientific-tutorial?style=flat)](https://github.com/hujinghaoabcd/python-scientific-tutorial/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/hujinghaoabcd/python-scientific-tutorial)](https://github.com/hujinghaoabcd/python-scientific-tutorial/commits/main)

[开始学习](#-学习路线) · [30 秒开始](#-30-秒开始) · [课程地图](#-课程地图) · [English](README_EN.md) · [参与贡献](CONTRIBUTING.md)

</div>

---

> **一个仓库，系统掌握 Python 科学计算。**  
> 不再分别收藏 Python、NumPy、Pandas、SciPy 和统计建模教程：这里把它们组织成一条连续、可复现、面向现代科学 Python 生态的学习路线。

## ✨ 为什么这个项目值得收藏

- **完整学习链路**：Python → NumPy → Pandas → SciPy → Statsmodels → LinearModels。
- **100+ Markdown 教程与文档 + 25 个 Jupyter Notebook**，既适合系统学习，也适合日常查阅。
- **面向现代科学 Python**：重点清理已经移除或不再推荐的旧 API，覆盖 NumPy 2.x、Pandas 3.x、SciPy、Statsmodels 与 LinearModels 的现代接口习惯。
- **不只讲 API**：覆盖数据处理、数值计算、优化、统计检验、回归、时间序列、面板数据、IV/2SLS、SUR/3SLS 等科研常用方法。
- **强调可复现**：示例尽量采用固定随机种子、本地生成数据或随包数据，减少网络依赖。
- **持续自动检查**：GitHub Actions 自动验证目录结构、Markdown 相对链接、Notebook JSON 与已知废弃 API。

## 🧭 学习路线

```text
Python 基础
   ↓
NumPy 数值计算
   ↓
Pandas 数据分析
   ↓
SciPy 科学计算
   ↓
Statsmodels 统计建模
   ↓
LinearModels 面板与计量模型
```

如果你是初学者，建议直接按 `01 → 06` 顺序学习；如果已经有 Python 基础，可以从需要的模块直接进入。

## ⚡ 30 秒开始

```bash
git clone https://github.com/hujinghaoabcd/python-scientific-tutorial.git
cd python-scientific-tutorial
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
jupyter lab
```

macOS / Linux：

```bash
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
jupyter lab
```

## 🗺️ 课程地图

| 阶段 | 模块 | 你会学到什么 | 入口 |
| --- | --- | --- | --- |
| 01 | **Python** | 语法、数据结构、函数、模块、文件、异常、OOP、综合项目 | [开始](01-python/) |
| 02 | **NumPy** | ndarray、索引、广播、向量化、统计、随机数、线性代数、I/O | [开始](02-numpy/) |
| 03 | **Pandas** | Series、DataFrame、清洗、合并、分组、时间序列、性能优化 | [开始](03-pandas/) |
| 04 | **SciPy** | 插值、优化、统计、积分、ODE、线代、信号、空间、稀疏矩阵、ndimage | [开始](04-scipy/) |
| 05 | **Statsmodels** | OLS、GLM、混合模型、稳健回归、时间序列、统计检验、生存分析 | [开始](05-statsmodels/) |
| 06 | **LinearModels** | 面板数据、固定/随机效应、IV/2SLS、资产定价、SUR/3SLS、Fama–MacBeth | [开始](06-linearmodels/) |

## 🎯 三条推荐路线

### 路线 A：从零系统学习

```text
Python → NumPy → Pandas → SciPy → Statsmodels → LinearModels
```

适合希望建立完整 Python 科学计算知识体系的学习者。

### 路线 B：数据分析与科学计算

```text
Python → NumPy → Pandas → SciPy.stats / optimize / integrate
```

适合数据处理、科研计算、数值分析与工程计算。

### 路线 C：统计建模与科研

```text
Python → NumPy → Pandas → Statsmodels → LinearModels
```

重点覆盖模型设定、估计结果解释、稳健标准误、统计检验、时间序列、面板数据和工具变量方法。

## 📁 项目结构

```text
python-scientific-tutorial/
├── 01-python/          # Python 基础
├── 02-numpy/           # NumPy 数值计算
├── 03-pandas/          # Pandas 数据分析
├── 04-scipy/           # SciPy 科学计算
├── 05-statsmodels/     # Statsmodels 统计建模
├── 06-linearmodels/    # LinearModels 面板与计量模型
├── assets/             # 项目视觉资源
├── scripts/            # 仓库质量检查
├── README.md
├── README_EN.md
├── CONTRIBUTING.md
├── requirements.txt
└── LICENSE
```

## 🤝 参与贡献

欢迎修正错误、改善解释、更新新版本兼容性或补充真正重要的科学计算主题。

提交前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果这个项目对你有帮助，也欢迎点一个 **Star**，这样以后需要 NumPy、Pandas、SciPy 或统计建模示例时可以快速找到它。

## 📄 License

本项目采用 [MIT License](LICENSE)。

## ℹ️ 说明

本仓库是一套教学型项目，不是各库官方文档的替代品。遇到版本差异、边界行为或科研级模型设定时，应同时查阅对应项目的官方文档与方法论文。
