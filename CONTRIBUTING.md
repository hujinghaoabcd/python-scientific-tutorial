# Contributing

感谢你愿意帮助改进 **Python Scientific Tutorial**。

这个仓库的目标是保持一条清晰、现代、可运行的 Python 科学计算学习路线，因此贡献优先关注：**正确性、可运行性、教学清晰度和版本兼容性**。

## 适合贡献的内容

欢迎提交：

- 错别字、公式、代码或链接修正；
- NumPy / Pandas / SciPy / Statsmodels / LinearModels 新版本兼容性更新；
- 更清晰的解释、图示思路或更小的教学示例；
- 缺失的重要科学计算主题；
- 能帮助学习者理解统计模型、数值方法或数据分析流程的案例；
- 失效链接、废弃 API、Notebook 格式等维护问题。

## 不建议的贡献

为了避免项目重新变成零散资料合集，通常不接受：

- 与现有学习路线无关的大型框架教程；
- 单纯复制官方文档的大段内容；
- 只增加依赖、但没有明显教学价值的示例；
- 无法复现的数据或必须依赖私人服务才能运行的代码；
- 已被当前科学 Python 生态淘汰的 API 写法。

## 教程风格

新增或修改内容时，尽量遵循这些原则：

1. 先解释“为什么需要它”，再解释 API。
2. 示例保持短小，可以直接复制运行。
3. 随机示例尽量设置固定随机种子。
4. 优先使用本地生成数据或随包数据。
5. 对统计方法说明基本假设、输入、输出和结果解释。
6. 不为了展示高级技巧而增加不必要复杂度。
7. 优先使用当前稳定、推荐的 API。

## 提交前检查

在仓库根目录运行：

```bash
python scripts/validate_tutorial.py
```

该脚本会检查：

- 六个教程模块是否存在；
- Markdown 本地相对链接；
- Jupyter Notebook JSON；
- 一些已知不应重新出现的废弃 API。

如果修改了代码示例，也建议在对应 Python 环境中实际运行一次。

## Pull Request 建议

一个 Pull Request 尽量只解决一个明确问题，例如：

- `Fix Pandas 3.x compatibility in missing-data chapter`
- `Improve SciPy solve_ivp explanation`
- `Add robust covariance example to Statsmodels OLS chapter`

PR 描述中请简单说明：

- 修改了什么；
- 为什么需要修改；
- 是否实际运行过示例；
- 是否涉及版本兼容性变化。

## Issue 建议

报告问题时，如果可能，请提供：

- 文件路径或章节名称；
- Python 版本；
- 相关库版本；
- 报错信息或错误结果；
- 你认为正确的行为。

## Language

教程正文以中文为主。Issue 和 Pull Request 可以使用中文或英文。

---

Thanks for helping make this repository a clearer and more reliable scientific Python learning resource.
