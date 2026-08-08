<div align="center">

# Python Scientific Tutorial

### A modern Chinese tutorial for Python scientific computing

**Learn Python fundamentals, NumPy, Pandas, SciPy, Statsmodels and LinearModels in one continuous path.**

[![Tutorial Quality](https://github.com/hujinghaoabcd/python-scientific-tutorial/actions/workflows/quality.yml/badge.svg)](https://github.com/hujinghaoabcd/python-scientific-tutorial/actions/workflows/quality.yml)
[![Python](https://img.shields.io/badge/Python-3.12--3.14-blue.svg)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/hujinghaoabcd/python-scientific-tutorial?style=flat)](https://github.com/hujinghaoabcd/python-scientific-tutorial/stargazers)

[简体中文](README.md) · [Quick Start](#-quick-start) · [Course Map](#-course-map) · [Contributing](CONTRIBUTING.md)

</div>

---

> **One repository for a complete scientific Python learning path.**

This project is a Chinese-language tutorial that connects the Python scientific stack into a single curriculum instead of treating each library as an isolated collection of API notes.

## ✨ Highlights

- **Continuous path:** Python → NumPy → Pandas → SciPy → Statsmodels → LinearModels.
- **100+ Markdown lessons/docs and 25 Jupyter Notebooks.**
- **Modern APIs:** organized for the 2026 scientific Python ecosystem and avoids known removed/deprecated teaching patterns.
- **Research-oriented coverage:** numerical methods, optimization, statistics, regression, time series, panel data, instrumental variables, SUR/3SLS and Fama–MacBeth.
- **Reproducible examples:** fixed random seeds and local/generated datasets whenever practical.
- **Automated validation:** repository structure, local Markdown links, Notebook JSON and obsolete API patterns are checked in CI.

## 🧭 Learning Path

```text
Python Fundamentals
       ↓
NumPy Numerical Computing
       ↓
Pandas Data Analysis
       ↓
SciPy Scientific Computing
       ↓
Statsmodels Statistical Modeling
       ↓
LinearModels Panel & Econometric Models
```

## ⚡ Quick Start

```bash
git clone https://github.com/hujinghaoabcd/python-scientific-tutorial.git
cd python-scientific-tutorial
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
jupyter lab
```

macOS / Linux:

```bash
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
jupyter lab
```

## 🗺️ Course Map

| Stage | Module | Topics | Start |
| --- | --- | --- | --- |
| 01 | **Python** | syntax, data structures, functions, modules, files, exceptions, OOP, projects | [Open](01-python/) |
| 02 | **NumPy** | ndarray, indexing, broadcasting, vectorization, statistics, random numbers, linear algebra, I/O | [Open](02-numpy/) |
| 03 | **Pandas** | Series, DataFrame, cleaning, merge, groupby, time series, performance | [Open](03-pandas/) |
| 04 | **SciPy** | interpolation, optimization, statistics, integration, ODEs, linear algebra, signal, spatial, sparse matrices, ndimage | [Open](04-scipy/) |
| 05 | **Statsmodels** | OLS, GLM, mixed models, robust regression, time series, tests, survival analysis | [Open](05-statsmodels/) |
| 06 | **LinearModels** | panel data, fixed/random effects, IV/2SLS, asset pricing, SUR/3SLS, Fama–MacBeth | [Open](06-linearmodels/) |

## 🔎 Search Topics

Python tutorial, NumPy tutorial, Pandas tutorial, SciPy tutorial, Statsmodels tutorial, LinearModels tutorial, scientific computing, data analysis, statistical modeling, numerical methods, linear regression, time series, panel data, instrumental variables, 2SLS, SUR, Fama-MacBeth.

## 🧪 Quality Checks

Recommended environment: **Python 3.12–3.14**.

Run the repository validator with:

```bash
python scripts/validate_tutorial.py
```

GitHub Actions runs the same validation for pushes and pull requests.

## 🤝 Contributing

Corrections, compatibility updates, clearer explanations and new scientific-computing examples are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## ⭐ Support

If this tutorial is useful to you, consider starring the repository so you can find it again and more scientific Python learners can discover it.

## Note

This is a teaching project, not a replacement for the official documentation of the libraries covered. For version-specific behavior and research-grade model specifications, always consult the corresponding official documentation and methodological literature.
