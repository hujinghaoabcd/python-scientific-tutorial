# 第01章：Pandas简介和安装

欢迎来到Pandas的世界！

如果你已经学过 Python 基础，并了解一点 NumPy，就可以开始学习 Pandas。它主要面向表格和时间序列数据，能把很多原本需要手工完成的数据整理步骤写成可重复执行的代码。

---

## 什么是Pandas？

### 先来个生活化的比喻

想象一下这些场景：

**场景1：用 Excel 处理较大的表格**
- 你有一个10万行的Excel表格，想要筛选、统计、分析
- Excel 打开较慢，数据量大时操作也可能变得卡顿
- 想做个复杂的数据透视？复杂公式会越来越难维护
- 想合并多个表格？需要大量复制粘贴

**场景2：用Python列表处理数据**
- 数据存在列表里，要找某一列数据得循环
- 想做个分组统计？得写一堆代码
- 想处理缺失值？得自己判断、自己处理
- 想画个图表？还得先整理数据格式

**场景3：用 Pandas 处理数据**
- 10万行数据也可以用代码批量处理
- 筛选数据？一行代码即可完成
- 分组统计？一个函数完成
- 处理缺失值？可以直接调用相应方法
- 画图表？内置方法，直接出图
- 合并表格？几行代码解决

**Pandas 可以理解为面向表格数据的 Python 工具集**。

它保留了表格数据的直观性，同时可以把处理步骤写成可重复执行的 Python 代码。

---

### Pandas的正式定义

**Pandas**（Panel Data的缩写）是Python的一个数据分析库，专门用于处理结构化数据（表格数据）。它提供了：

1. **DataFrame**：类似Excel的二维表格，这是Pandas的核心！
2. **Series**：一维数据结构，可以理解为表格的一列
3. **强大的数据操作功能**：筛选、分组、统计、合并、透视等
4. **时间序列处理**：处理日期时间数据很方便
5. **数据清洗工具**：处理缺失值、重复值、异常值
6. **数据可视化**：内置画图功能

**核心特点**：
- **像操作Excel一样简单**：直观的表格操作
- **像写代码一样强大**：可以处理海量数据
- **高效**：底层基于NumPy，速度快
- **灵活**：从数据读取到分析到可视化，一站式解决

---

### Pandas的小故事

Pandas是由Wes McKinney在2008年创建的。当时他在一家投资公司工作，需要处理大量金融数据。他发现Python虽然强大，但缺少好用的数据分析工具，于是他决定自己写一个！

有趣的是，Pandas这个名字来自"Panel Data"（面板数据，金融学术语），但Wes说他也很喜欢熊猫（Panda），所以这个名字一举两得——既专业又可爱！

Wes后来还写了一本书《利用Python进行数据分析》，这本书成为了数据分析领域的经典教材。现在Pandas已经15岁了，是全球数百万数据分析师、数据科学家每天都在用的工具！

**有趣的事实**：
- Pandas最初是为金融数据分析设计的
- 现在被用于各行各业：电商、医疗、教育、科研等
- GitHub上有超过3000名贡献者参与开发
- 每月被下载超过5000万次！

---

## 为什么要学Pandas？

### 1. 数据分析的瑞士军刀 - 功能全面

**Pandas 能覆盖很多常见的数据处理任务。**

```python
import pandas as pd

# 读取数据（支持Excel、CSV、SQL、JSON等）
df = pd.read_excel('sales.xlsx')
df = pd.read_csv('data.csv')
df = pd.read_sql('SELECT * FROM table', connection)

# 数据清洗（处理缺失值、重复值）
df.dropna()  # 删除缺失值
df.fillna(0)  # 填充缺失值
df.drop_duplicates()  # 删除重复行

# 数据筛选（像Excel筛选一样简单）
df[df['age'] > 18]  # 筛选年龄大于18的
df[df['city'] == '北京']  # 筛选北京的数据

# 数据统计（一行代码完成复杂统计）
df.groupby('city')['sales'].sum()  # 按城市统计销售额
df.describe()  # 查看数据概况

# 数据合并（像SQL JOIN一样）
pd.merge(df1, df2, on='id')

# 数据透视（像Excel数据透视表）
df.pivot_table(values='sales', index='month', columns='product')

# 数据可视化（内置画图）
df.plot()
```

**一句话总结**：从读取、清洗到分组、统计和基础可视化，Pandas 可以覆盖常见的表格数据处理流程。

---

### 2. Excel之外的可编程数据处理方式 - 突破限制

让我们对比一下Excel和Pandas：

| 功能 | Excel | Pandas |
|------|-------|--------|
| **数据量限制** | 单工作表最多约 104 万行 | 主要受可用内存和数据类型影响 |
| **处理速度** | 数据量大时很慢 | 快（底层是C/NumPy） |
| **自动化** | 需要VBA，复杂 | Python脚本，简单 |
| **批量处理** | 难（要写宏） | 易（循环处理多个文件） |
| **版本控制** | 难（文件容易乱） | 易（代码可以用Git管理） |
| **可重复性** | 差（操作步骤难记录） | 好（代码就是文档） |
| **复杂运算** | 公式嵌套复杂 | 代码清晰 |
| **数据清洗** | 手动操作 | 自动化处理 |
| **协作** | 文件传来传去 | 代码共享，协作方便 |

**举个例子**：

**Excel做法**（处理100个Excel文件，统计销售总额）：
1. 手动打开第1个文件
2. 找到销售额列，记录总和
3. 关闭，打开第2个文件
4. 重复100次...
5. 最后手动汇总

**步骤重复，而且容易出错。**

**Pandas做法**：
```python
import pandas as pd
import glob

# 找到所有Excel文件
files = glob.glob('*.xlsx')

# 一次性处理所有文件
total_sales = 0
for file in files:
    df = pd.read_excel(file)
    total_sales += df['销售额'].sum()

print(f"总销售额：{total_sales}元")
```

**几行代码即可批量完成。**

---

### 3. 比SQL更灵活 - 数据库操作的Python版

如果你用过 SQL，会发现筛选、分组、聚合和连接等操作在 Pandas 中也有相似的表达方式。

**SQL vs Pandas对比**：

```sql
-- SQL：查询年龄大于18岁的用户
SELECT * FROM users WHERE age > 18;
```

```python
# Pandas：更直观
df[df['age'] > 18]
```

```sql
-- SQL：分组统计
SELECT city, AVG(salary)
FROM employees
GROUP BY city;
```

```python
# Pandas：一样简单
df.groupby('city')['salary'].mean()
```

```sql
-- SQL：多表连接
SELECT *
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

```python
# Pandas：更灵活
pd.merge(orders, customers, left_on='customer_id', right_on='id')
```

**Pandas的优势**：
- 不需要数据库，本地就能操作
- 可以和Python其他库配合（NumPy、Matplotlib等）
- 可以处理不规则数据
- 可以做更复杂的数据转换
- 可以直接连接数据库，然后在内存中继续处理

---

### 4. 与NumPy的关系 - 珠联璧合

**NumPy和Pandas的关系**：

想象一下：
- **NumPy**：是建筑的钢筋混凝土（底层基础，强大但原始）
- **Pandas**：是装修好的房子（高层接口，美观实用）

**技术上的关系**：
- Pandas的底层是NumPy数组
- DataFrame的每一列都是一个NumPy数组
- 可以无缝互相转换

```python
import numpy as np
import pandas as pd

# NumPy数组
np_array = np.array([[1, 2, 3], [4, 5, 6]])

# 转换为Pandas DataFrame
df = pd.DataFrame(np_array, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6

# DataFrame转回NumPy
back_to_numpy = df.values
print(type(back_to_numpy))  # <class 'numpy.ndarray'>
```

**什么时候用谁？**

| 场景 | 用NumPy | 用Pandas |
|------|---------|----------|
| 纯数值计算 | ✓ | |
| 矩阵运算 | ✓ | |
| 科学计算 | ✓ | |
| 表格数据 | | ✓ |
| 数据清洗 | | ✓ |
| 数据分析 | | ✓ |
| 时间序列 | | ✓ |
| 分组统计 | | ✓ |

**最佳实践**：
- 学好NumPy是学Pandas的基础
- 数据存储和操作用Pandas
- 复杂数值计算用NumPy
- 两者经常配合使用

**打个比方**：
- NumPy是引擎，Pandas是汽车
- NumPy是原材料，Pandas是成品
- NumPy是食材，Pandas是大厨

---

### 5. 实际应用场景 - 无处不在

Pandas到底能用在哪里？答案是：只要有数据的地方，就有Pandas！

#### 场景1：电商数据分析

```python
import pandas as pd

# 读取订单数据
orders = pd.read_csv('orders.csv')

# 分析问题：
# 1. 哪个月销售额最高？
monthly_sales = orders.groupby('month')['amount'].sum()
best_month = monthly_sales.idxmax()
print(f"销售最好的月份：{best_month}")

# 2. 哪个城市消费能力最强？
city_sales = orders.groupby('city')['amount'].mean()
print(f"人均消费最高的城市：{city_sales.idxmax()}")

# 3. 复购率是多少？
repeat_rate = len(orders[orders['order_count'] > 1]) / len(orders) * 100
print(f"复购率：{repeat_rate:.2f}%")
```

#### 场景2：金融数据分析

```python
import pandas as pd

# 读取股票数据
stock = pd.read_csv('stock_price.csv', parse_dates=['date'])

# 计算收益率
stock['returns'] = stock['close'].pct_change()

# 计算移动平均
stock['MA_5'] = stock['close'].rolling(window=5).mean()
stock['MA_20'] = stock['close'].rolling(window=20).mean()

# 找出最佳买入点（5日均线上穿20日均线）
golden_cross = stock[(stock['MA_5'] > stock['MA_20']) &
                     (stock['MA_5'].shift(1) <= stock['MA_20'].shift(1))]
print("金叉信号（买入时机）：")
print(golden_cross[['date', 'close']])
```

#### 场景3：教育数据分析

```python
import pandas as pd

# 读取学生成绩
scores = pd.read_excel('student_scores.xlsx')

# 统计分析
print("=" * 50)
print("班级成绩分析报告")
print("=" * 50)

# 各科平均分
subject_avg = scores[['语文', '数学', '英语']].mean()
print("\n各科平均分：")
print(subject_avg)

# 优秀学生（总分前10%）
scores['总分'] = scores[['语文', '数学', '英语']].sum(axis=1)
top_10_percent = scores.nlargest(int(len(scores) * 0.1), '总分')
print(f"\n优秀学生（前10%）：")
print(top_10_percent[['姓名', '总分']])

# 各分数段分布
bins = [0, 60, 70, 80, 90, 100]
labels = ['不及格', '及格', '中等', '良好', '优秀']
scores['等级'] = pd.cut(scores['总分'], bins=bins, labels=labels)
print("\n成绩分布：")
print(scores['等级'].value_counts())
```

#### 场景4：网站日志分析

```python
import pandas as pd

# 读取访问日志
logs = pd.read_csv('access_log.csv', parse_dates=['timestamp'])

# 分析访问高峰
logs['hour'] = logs['timestamp'].dt.hour
hourly_traffic = logs.groupby('hour').size()
print(f"访问高峰时段：{hourly_traffic.idxmax()}点")

# 热门页面TOP10
top_pages = logs['page'].value_counts().head(10)
print("最受欢迎的页面：")
print(top_pages)

# 用户留存分析
logs['date'] = logs['timestamp'].dt.date
daily_users = logs.groupby('date')['user_id'].nunique()
print(f"日均活跃用户：{daily_users.mean():.0f}人")
```

#### 场景5：疫情数据分析

```python
import pandas as pd
import matplotlib.pyplot as plt

# 读取疫情数据
covid = pd.read_csv('covid_data.csv', parse_dates=['date'])

# 按日期统计
daily_cases = covid.groupby('date')['confirmed'].sum()

# 计算7日移动平均（平滑曲线）
daily_cases_ma = daily_cases.rolling(window=7).mean()

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(daily_cases.index, daily_cases.values, alpha=0.3, label='每日新增')
plt.plot(daily_cases_ma.index, daily_cases_ma.values, linewidth=2, label='7日均值')
plt.xlabel('日期')
plt.ylabel('确诊人数')
plt.title('疫情趋势分析')
plt.legend()
plt.grid(True)
plt.show()
```

**看到没？无论什么行业，只要有数据，Pandas都能派上用场！**

---

## Pandas的优势总结

让我们用一张表格总结Pandas的核心优势：

| 优势 | 说明 | 举例 |
|------|------|------|
| **简单直观** | 像操作Excel一样 | `df[df['age'] > 18]` |
| **高效快速** | 底层基于NumPy | 处理百万行数据秒级完成 |
| **功能全面** | 读取、清洗、分析、可视化一站式 | 从CSV到图表一条龙 |
| **灵活强大** | 编程语言的无限可能 | 可以写复杂逻辑 |
| **生态丰富** | 与其他库无缝集成 | NumPy、Matplotlib、Sklearn等 |
| **社区活跃** | 问题都有答案 | Stack Overflow、GitHub |
| **文档完善** | 学习资源丰富 | 官方文档、教程、书籍 |
| **免费开源** | 完全免费 | 不像Excel要买Office |

---

## Pandas与其他工具的对比

### Pandas vs Excel

```
Excel：家用轿车
- 适合普通用户
- 可视化操作
- 数据量有限（100万行）
- 自动化能力弱
- 不适合复杂分析

Pandas：专业卡车
- 适合专业人士
- 代码操作
- 数据量几乎无限
- 自动化能力强
- 适合复杂分析
```

### Pandas vs SQL

```
SQL：餐厅点菜
- 数据在数据库
- 结构化查询
- 需要数据库支持
- 适合查询操作

Pandas：自己做饭
- 数据在内存
- 灵活操作
- 不需要数据库
- 适合数据分析
```

### Pandas vs R语言

```
R语言：统计学家的工具
- 专注统计分析
- 语法较难
- 主要用于学术

Pandas：工程师的工具
- 全栈数据分析
- 语法简单（Python）
- 工业界主流
```

**结论**：Pandas 适合常见的表格数据清洗、转换和分析，并且与 Python 科学计算生态衔接良好。

---

## 安装Pandas

说了这么多Pandas的好处，现在让我们把它装到你的电脑上！安装过程非常简单。

### 前提条件

在安装Pandas之前，确保你已经：
- 安装了Python 3（建议Python 3.8或更高版本）
- 安装了pip（Python包管理工具）
- 知道如何打开命令行

**检查Python版本**：
```bash
python --version
# 或者（macOS/Linux）
python3 --version
```

如果显示Python版本号（建议3.8+），说明Python已安装，可以继续！

**检查pip版本**：
```bash
pip --version
# 或者
pip3 --version
```

---

### 方法一：使用pip安装（最简单，推荐）

这是最常用的安装方式，适合大多数人。

#### 步骤1：打开命令行

- **Windows**：按`Win + R`，输入`cmd`，回车
- **macOS**：打开"终端"（Terminal）
- **Linux**：打开终端

#### 步骤2：运行安装命令

```bash
# Windows
pip install pandas

# macOS/Linux（如果上面的不行，用这个）
pip3 install pandas
```

#### 步骤3：等待安装

你会看到类似这样的输出：
```
Collecting pandas
  Downloading pandas-2.1.4-cp312-cp312-win_amd64.whl (11.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 5.2 MB/s eta 0:00:00
Collecting numpy>=1.23.2
  Downloading numpy-1.26.2-cp312-cp312-win_amd64.whl (15.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.5/15.5 MB 6.1 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1
  Downloading pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)
Installing collected packages: pytz, python-dateutil, numpy, pandas
Successfully installed numpy-1.26.2 pandas-2.1.4 python-dateutil-2.8.2 pytz-2023.3.post1
```

**注意**：Pandas会自动安装它的依赖包（NumPy、python-dateutil、pytz等），不用担心！

#### 步骤4：验证安装

```bash
# 在命令行输入
python -c "import pandas as pd; print('Pandas版本:', pd.__version__)"
```

如果显示版本号（比如`Pandas版本: 2.1.4`），恭喜你安装成功！

---

### 方法二：使用Anaconda安装（推荐数据科学方向）

如果你安装了Anaconda，Pandas已经自动包含在里面了，不需要单独安装！

#### 验证Pandas是否已安装

```bash
# 打开Anaconda Prompt或普通命令行
conda list pandas
```

如果看到Pandas的信息，说明已经安装了！

#### 如果没有，手动安装

```bash
conda install pandas
```

#### 使用conda的好处

- 自动处理依赖关系
- 可以创建独立的环境
- 避免版本冲突
- 包含数据科学常用库

**推荐配置**（一次性安装数据分析全家桶）：
```bash
conda install pandas numpy matplotlib seaborn jupyter
```

---

### 方法三：安装特定版本

有时候某些项目需要特定版本的Pandas：

```bash
# 安装特定版本
pip install pandas==2.0.0

# 安装大于某版本
pip install "pandas>=2.0.0"

# 安装小于某版本
pip install "pandas<2.1.0"

# 升级到最新版
pip install --upgrade pandas
```

---

### 方法四：从源代码安装（高级用户，不推荐新手）

这种方法适合需要最新开发版或想贡献代码的开发者：

```bash
# 克隆Pandas仓库
git clone https://github.com/pandas-dev/pandas.git
cd pandas

# 安装依赖
pip install -r requirements-dev.txt

# 编译安装
python setup.py install
```

**警告**：这种方法需要C编译器等开发工具，新手不推荐！

---

### 国内镜像加速（强烈推荐！）

如果你在国内，pip下载可能会很慢，可以使用国内镜像：

#### 临时使用镜像

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

#### 永久配置镜像（推荐）

```bash
# 配置清华镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 验证配置
pip config list
```

**常用国内镜像**：
- 清华大学：`https://pypi.tuna.tsinghua.edu.cn/simple`
- 阿里云：`https://mirrors.aliyun.com/pypi/simple/`
- 中科大：`https://pypi.mirrors.ustc.edu.cn/simple/`
- 豆瓣：`https://pypi.douban.com/simple/`

配置后，配置合适的镜像后，通常可以改善下载速度。

---

### 安装常见问题及解决方案

#### 问题1：提示"pip不是内部或外部命令"

**原因**：pip没有添加到系统PATH

**解决**：
```bash
# 用python -m pip代替pip
python -m pip install pandas
```

#### 问题2：提示"Permission denied"（权限不足）

**原因**：没有管理员权限

**解决（Windows）**：
```bash
# 以管理员身份运行命令行
# 或者安装到用户目录
pip install --user pandas
```

**解决（macOS/Linux）**：
```bash
# 方法1：加sudo
sudo pip3 install pandas

# 方法2：安装到用户目录（推荐）
pip3 install --user pandas
```

#### 问题3：下载速度慢或超时

**原因**：网络问题，服务器在国外

**解决**：使用国内镜像（见上面的"国内镜像加速"部分）

#### 问题4：提示版本冲突

**原因**：与其他包版本不兼容

**解决**：
```bash
# 卸载重装
pip uninstall pandas
pip install pandas

# 或者指定兼容版本
pip install pandas==2.0.0
```

#### 问题5：Import pandas成功，但某些功能报错

**原因**：依赖包（如NumPy）版本不对

**解决**：
```bash
# 重新安装pandas及其依赖
pip install --force-reinstall pandas
```

#### 问题6：安装时提示需要编译器

**原因**：某些版本需要编译C扩展

**解决**：
```bash
# 安装预编译的二进制版本（wheel文件）
pip install pandas --only-binary :all:

# 或者升级pip
pip install --upgrade pip
pip install pandas
```

#### 问题7：在Jupyter Notebook中import失败

**原因**：Jupyter的Python环境和命令行的不同

**解决**：
```bash
# 在Jupyter的单元格中运行
!pip install pandas

# 或者在命令行中指定Jupyter的Python
python -m pip install pandas
```

---

### 验证安装是否成功

安装完成后，让我们全面验证Pandas是否正常工作：

#### 方法1：命令行快速验证

```bash
python -c "import pandas as pd, numpy as np; print('Pandas版本:', pd.__version__); print('NumPy版本:', np.__version__)"
```

#### 方法2：进入Python交互模式验证

```bash
# 打开Python
python

# 然后输入
>>> import pandas as pd
>>> import numpy as np
>>> pd.__version__
# 输出当前环境中的 Pandas 版本
>>> np.__version__
# 输出当前环境中的 NumPy 版本
>>> # 创建一个简单的DataFrame
>>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
>>> print(df)
   A  B
0  1  4
1  2  5
2  3  6
>>> exit()
```

#### 方法3：创建测试脚本

创建一个`test_pandas.py`文件：

```python
import pandas as pd
import numpy as np

print("=" * 60)
print("Pandas环境测试")
print("=" * 60)

# 显示版本
print(f"\nPandas版本：{pd.__version__}")
print(f"NumPy版本：{np.__version__}")

# 测试Series
print("\n" + "-" * 60)
print("测试Series（一维数据）")
print("-" * 60)
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(f"Series类型：{type(s)}")

# 测试DataFrame
print("\n" + "-" * 60)
print("测试DataFrame（二维表格）")
print("-" * 60)
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '深圳']
})
print(df)
print(f"\nDataFrame形状：{df.shape}")
print(f"DataFrame列名：{df.columns.tolist()}")

# 测试基本操作
print("\n" + "-" * 60)
print("测试基本操作")
print("-" * 60)
print("年龄列：")
print(df['年龄'])
print(f"\n平均年龄：{df['年龄'].mean():.1f}岁")
print(f"最大年龄：{df['年龄'].max()}岁")
print(f"最小年龄：{df['年龄'].min()}岁")

# 测试数据筛选
print("\n" + "-" * 60)
print("测试数据筛选")
print("-" * 60)
filtered = df[df['年龄'] > 26]
print("年龄大于26的人：")
print(filtered)

# 测试数据读写（创建CSV文件）
print("\n" + "-" * 60)
print("测试数据读写")
print("-" * 60)
df.to_csv('test_data.csv', index=False, encoding='utf-8-sig')
print("✓ 成功写入CSV文件：test_data.csv")

df_read = pd.read_csv('test_data.csv')
print("✓ 成功读取CSV文件")
print(df_read)

print("\n" + "=" * 60)
print("恭喜！Pandas安装成功，所有功能正常！")
print("=" * 60)
```

运行：
```bash
python test_pandas.py
```

如果看到完整输出，说明Pandas安装成功并且功能正常！

---

## 安装推荐的配套工具

Pandas通常不是单独使用的，以下是推荐一起安装的工具：

### 数据分析三件套（必装）

```bash
# 一次性安装
pip install pandas numpy matplotlib

# 或者用conda
conda install pandas numpy matplotlib
```

- **pandas**：数据处理
- **numpy**：数值计算
- **matplotlib**：数据可视化

### 增强包（推荐）

```bash
# 更美观的数据可视化
pip install seaborn

# 读写Excel文件
pip install openpyxl xlrd xlwt

# 交互式编程环境
pip install jupyter

# 进度条（处理大数据时显示进度）
pip install tqdm

# 科学计算
pip install scipy

# 统计分析
pip install statsmodels
```

### 一次性安装完整数据分析环境

```bash
# 方法1：使用pip
pip install pandas numpy matplotlib seaborn jupyter openpyxl

# 方法2：使用conda（推荐）
conda install pandas numpy matplotlib seaborn jupyter openpyxl scikit-learn
```

---

## 第一个Pandas程序

Pandas安装好了，现在让我们写第一个真正的Pandas程序！

### Hello Pandas！

创建一个文件`hello_pandas.py`：

```python
# 导入Pandas库，通常简称为pd
import pandas as pd
import numpy as np

# 打印欢迎信息
print("=" * 60)
print("欢迎来到Pandas的世界！")
print("=" * 60)

# 创建第一个Series（一维数据）
print("\n【1. Series - 一维数据】")
print("-" * 60)
my_series = pd.Series([10, 20, 30, 40, 50],
                      index=['a', 'b', 'c', 'd', 'e'])
print("我的第一个Series：")
print(my_series)
print(f"Series类型：{type(my_series)}")
print(f"Series形状：{my_series.shape}")

# 创建第一个DataFrame（二维表格）
print("\n【2. DataFrame - 二维表格】")
print("-" * 60)
my_dataframe = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '城市': ['北京', '上海', '深圳', '广州'],
    '工资': [8000, 12000, 10000, 15000]
})
print("我的第一个DataFrame：")
print(my_dataframe)
print(f"\nDataFrame类型：{type(my_dataframe)}")
print(f"DataFrame形状：{my_dataframe.shape}")
print(f"DataFrame列名：{my_dataframe.columns.tolist()}")

# 查看数据信息
print("\n【3. 数据信息】")
print("-" * 60)
print("数据统计：")
print(my_dataframe.describe())

# 基本操作
print("\n【4. 基本操作】")
print("-" * 60)
print(f"平均年龄：{my_dataframe['年龄'].mean():.1f}岁")
print(f"平均工资：{my_dataframe['工资'].mean():.0f}元")
print(f"最高工资：{my_dataframe['工资'].max()}元")
print(f"最低工资：{my_dataframe['工资'].min()}元")

# 数据筛选
print("\n【5. 数据筛选】")
print("-" * 60)
high_salary = my_dataframe[my_dataframe['工资'] > 10000]
print("工资大于10000的员工：")
print(high_salary)

# 数据排序
print("\n【6. 数据排序】")
print("-" * 60)
sorted_df = my_dataframe.sort_values('工资', ascending=False)
print("按工资降序排列：")
print(sorted_df)

print("\n" + "=" * 60)
print("恭喜！你的第一个Pandas程序运行成功！")
print("=" * 60)
```

运行：
```bash
python hello_pandas.py
```

**预期输出**：
```
============================================================
欢迎来到Pandas的世界！
============================================================

【1. Series - 一维数据】
------------------------------------------------------------
我的第一个Series：
a    10
b    20
c    30
d    40
e    50
dtype: int64
Series类型：<class 'pandas.core.series.Series'>
Series形状：(5,)

【2. DataFrame - 二维表格】
------------------------------------------------------------
我的第一个DataFrame：
  姓名  年龄  城市    工资
0  张三  25  北京   8000
1  李四  30  上海  12000
2  王五  28  深圳  10000
3  赵六  35  广州  15000

DataFrame类型：<class 'pandas.core.frame.DataFrame'>
DataFrame形状：(4, 4)
DataFrame列名：['姓名', '年龄', '城市', '工资']

【3. 数据信息】
------------------------------------------------------------
数据统计：
            年龄          工资
count   4.000000      4.000000
mean   29.500000  11250.000000
std     4.203173   3095.695936
min    25.000000   8000.000000
25%    27.250000   9500.000000
50%    29.000000  11000.000000
75%    31.250000  12750.000000
max    35.000000  15000.000000

【4. 基本操作】
------------------------------------------------------------
平均年龄：29.5岁
平均工资：11250元
最高工资：15000元
最低工资：8000元

【5. 数据筛选】
------------------------------------------------------------
工资大于10000的员工：
  姓名  年龄  城市    工资
1  李四  30  上海  12000
2  王五  28  深圳  10000
3  赵六  35  广州  15000

【6. 数据排序】
------------------------------------------------------------
按工资降序排列：
  姓名  年龄  城市    工资
3  赵六  35  广州  15000
1  李四  30  上海  12000
2  王五  28  深圳  10000
0  张三  25  北京   8000

============================================================
恭喜！你的第一个Pandas程序运行成功！
============================================================
```

---

### 稍微复杂一点的例子 - 学生成绩管理系统

让我们写一个更实用的程序：

```python
import pandas as pd
import numpy as np

print("=" * 70)
print("学生成绩管理系统")
print("=" * 70)

# 创建学生成绩数据
students = pd.DataFrame({
    '学号': ['S001', 'S002', 'S003', 'S004', 'S005',
            'S006', 'S007', 'S008', 'S009', 'S010'],
    '姓名': ['张三', '李四', '王五', '赵六', '钱七',
            '孙八', '周九', '吴十', '郑一', '王二'],
    '语文': [85, 92, 78, 88, 90, 76, 95, 82, 89, 91],
    '数学': [90, 88, 85, 92, 87, 80, 93, 86, 91, 89],
    '英语': [88, 90, 82, 85, 92, 78, 91, 84, 87, 90],
    '班级': ['一班', '一班', '一班', '一班', '一班',
            '二班', '二班', '二班', '二班', '二班']
})

print("\n【1. 学生成绩表】")
print("-" * 70)
print(students)

# 计算总分和平均分
students['总分'] = students[['语文', '数学', '英语']].sum(axis=1)
students['平均分'] = students[['语文', '数学', '英语']].mean(axis=1).round(2)

print("\n【2. 添加总分和平均分】")
print("-" * 70)
print(students[['学号', '姓名', '总分', '平均分']])

# 成绩排名
students['排名'] = students['总分'].rank(ascending=False, method='min').astype(int)
sorted_students = students.sort_values('总分', ascending=False)

print("\n【3. 成绩排名】")
print("-" * 70)
print(sorted_students[['排名', '学号', '姓名', '总分', '平均分']])

# 各科成绩分析
print("\n【4. 各科成绩分析】")
print("-" * 70)
subjects = ['语文', '数学', '英语']
for subject in subjects:
    avg = students[subject].mean()
    max_score = students[subject].max()
    min_score = students[subject].min()
    max_student = students[students[subject] == max_score]['姓名'].values[0]
    min_student = students[students[subject] == min_score]['姓名'].values[0]

    print(f"\n{subject}：")
    print(f"  平均分：{avg:.2f}")
    print(f"  最高分：{max_score}（{max_student}）")
    print(f"  最低分：{min_score}（{min_student}）")

# 班级对比
print("\n【5. 班级对比分析】")
print("-" * 70)
class_stats = students.groupby('班级')[subjects + ['总分']].mean().round(2)
print(class_stats)

# 找出优秀学生（总分>=270）
print("\n【6. 优秀学生名单】")
print("-" * 70)
excellent = students[students['总分'] >= 270]
print(f"优秀学生（总分≥270）：{len(excellent)}人")
print(excellent[['学号', '姓名', '总分', '平均分']])

# 找出需要帮助的学生（平均分<85）
print("\n【7. 需要帮助的学生】")
print("-" * 70)
need_help = students[students['平均分'] < 85]
print(f"需要帮助的学生（平均分<85）：{len(need_help)}人")
if len(need_help) > 0:
    print(need_help[['学号', '姓名', '平均分']])
else:
    print("没有学生需要帮助！")

# 各科及格率
print("\n【8. 各科及格率】")
print("-" * 70)
for subject in subjects:
    passed = (students[subject] >= 60).sum()
    pass_rate = passed / len(students) * 100
    print(f"{subject}及格率：{pass_rate:.1f}%（{passed}/{len(students)}人）")

# 保存结果到CSV
output_file = 'student_scores_result.csv'
students.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n【9. 保存结果】")
print("-" * 70)
print(f"✓ 成绩报告已保存到：{output_file}")

print("\n" + "=" * 70)
print("成绩分析完成！")
print("=" * 70)
```

这个程序展示了Pandas的核心功能：
- 创建DataFrame
- 数据计算（总分、平均分）
- 数据排序和排名
- 数据筛选
- 分组统计
- 数据保存

---

### 在Jupyter Notebook中体验Pandas

Jupyter Notebook是学习Pandas的最佳工具！让我们看看如何使用：

#### 1. 启动Jupyter Notebook

```bash
jupyter notebook
```

浏览器会自动打开，点击"New" → "Python 3"创建新的notebook。

#### 2. 在Notebook中体验Pandas

**单元格1：导入库**
```python
import pandas as pd
import numpy as np
print("Pandas版本：", pd.__version__)
```

**单元格2：创建DataFrame**
```python
# 创建一个简单的DataFrame
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '深圳'],
    '工资': [8000, 12000, 10000]
})
df
```

**单元格3：查看数据**
```python
# 查看前几行
df.head()

# 查看数据信息
df.info()

# 查看统计信息
df.describe()
```

**单元格4：数据操作**
```python
# 筛选
high_salary = df[df['工资'] > 9000]
high_salary

# 排序
df.sort_values('工资', ascending=False)

# 添加新列
df['税后工资'] = df['工资'] * 0.8
df
```

**单元格5：读取真实数据**
```python
# 创建一个示例CSV文件
df.to_csv('sample.csv', index=False)

# 读取CSV
df_read = pd.read_csv('sample.csv')
df_read
```

**单元格6：数据可视化**
```python
import matplotlib.pyplot as plt

# 画柱状图
df.plot(x='姓名', y='工资', kind='bar', figsize=(10, 6))
plt.title('员工工资对比')
plt.ylabel('工资（元）')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

**Jupyter的优势**：
- 可以边写边运行，立刻看结果
- DataFrame自动美化显示
- 可以可视化数据
- 可以写Markdown做笔记
- 适合探索性数据分析

---

## Pandas核心概念快速预览

在正式学习之前，让我们快速预览一下Pandas的核心概念：

### 1. Series（一维数据）

Series就像是表格的一列，或者带标签的数组：

```python
import pandas as pd

# 创建Series
s = pd.Series([10, 20, 30, 40, 50],
              index=['a', 'b', 'c', 'd', 'e'])
print(s)
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64

# 访问元素
print(s['a'])  # 10
print(s[0])    # 10

# Series运算
print(s * 2)
print(s + 100)
print(s.mean())  # 平均值
```

**Series的特点**：
- 有索引（index）
- 数据类型统一（dtype）
- 支持NumPy运算
- 可以看作是字典的增强版

---

### 2. DataFrame（二维表格）

DataFrame就像是Excel表格，有行有列：

```python
import pandas as pd

# 创建DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
})
print(df)
#    A   B    C
# 0  1  10  100
# 1  2  20  200
# 2  3  30  300
# 3  4  40  400

# 查看列
print(df['A'])

# 查看行
print(df.loc[0])  # 第一行

# 查看特定单元格
print(df.loc[0, 'A'])  # 第一行A列

# DataFrame属性
print(df.shape)    # (4, 3) - 4行3列
print(df.columns)  # Index(['A', 'B', 'C'])
print(df.index)    # RangeIndex(start=0, stop=4, step=1)
```

**DataFrame的特点**：
- 有行索引和列索引
- 每列可以是不同类型
- 可以看作是多个Series组合
- 就像数据库表或Excel表格

---

### 3. 数据读取

Pandas支持读取多种格式的数据：

```python
import pandas as pd

# 读取CSV
df = pd.read_csv('data.csv')

# 读取Excel
df = pd.read_excel('data.xlsx')

# 读取JSON
df = pd.read_json('data.json')

# 从SQL读取
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table', conn)

# 从剪贴板读取（复制Excel数据后）
df = pd.read_clipboard()

# 从字典创建
df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [4, 5, 6]
})
```

---

### 4. 数据查看

```python
import pandas as pd

df = pd.read_csv('data.csv')

# 查看前几行
df.head()      # 前5行
df.head(10)    # 前10行

# 查看后几行
df.tail()      # 后5行

# 查看数据信息
df.info()      # 数据类型、缺失值等信息

# 查看统计信息
df.describe()  # 数值列的统计信息

# 查看形状
df.shape       # (行数, 列数)

# 查看列名
df.columns     # 所有列名

# 查看数据类型
df.dtypes      # 每列的数据类型
```

---

### 5. 数据选择

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '深圳']
})

# 选择列
df['姓名']           # 单列
df[['姓名', '年龄']]  # 多列

# 选择行
df.loc[0]           # 第一行
df.loc[0:2]         # 前三行
df.iloc[0]          # 第一行（按位置）

# 选择单元格
df.loc[0, '姓名']    # 第一行的姓名
df.iloc[0, 0]       # 第一行第一列

# 条件筛选
df[df['年龄'] > 26]  # 年龄大于26
df[df['城市'] == '北京']  # 城市是北京
```

---

### 6. 数据操作

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28]
})

# 添加列
df['城市'] = ['北京', '上海', '深圳']

# 删除列
df = df.drop('城市', axis=1)

# 删除行
df = df.drop(0, axis=0)

# 重命名列
df = df.rename(columns={'姓名': 'name', '年龄': 'age'})

# 排序
df = df.sort_values('年龄')              # 按年龄升序
df = df.sort_values('年龄', ascending=False)  # 降序

# 重置索引
df = df.reset_index(drop=True)
```

---

### 7. 数据统计

```python
import pandas as pd

df = pd.DataFrame({
    '科目': ['语文', '数学', '英语', '语文', '数学'],
    '成绩': [85, 90, 88, 92, 87],
    '班级': ['一班', '一班', '一班', '二班', '二班']
})

# 基本统计
df['成绩'].mean()    # 平均值
df['成绩'].sum()     # 总和
df['成绩'].max()     # 最大值
df['成绩'].min()     # 最小值
df['成绩'].std()     # 标准差

# 分组统计
df.groupby('班级')['成绩'].mean()  # 各班级平均分
df.groupby('科目')['成绩'].max()   # 各科目最高分

# 透视表
df.pivot_table(values='成绩', index='班级', columns='科目')
```

---

### 8. 数据清洗

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

# 查看缺失值
df.isnull()        # 返回布尔DataFrame
df.isnull().sum()  # 每列缺失值数量

# 删除缺失值
df.dropna()        # 删除有缺失值的行
df.dropna(axis=1)  # 删除有缺失值的列

# 填充缺失值
df.fillna(0)       # 用0填充
df.fillna(df.mean())  # 用平均值填充

# 删除重复值
df.drop_duplicates()
```

---

### 9. 数据合并

```python
import pandas as pd

# 创建两个DataFrame
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['张三', '李四', '王五']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'score': [85, 90, 88]
})

# 合并（类似SQL JOIN）
result = pd.merge(df1, df2, on='id')
print(result)
#    id name  score
# 0   1   张三     85
# 1   2   李四     90
# 2   3   王五     88

# 纵向拼接
df3 = pd.DataFrame({
    'id': [4, 5],
    'name': ['赵六', '钱七']
})
result = pd.concat([df1, df3], ignore_index=True)
```

---

### 10. 数据保存

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四'],
    '年龄': [25, 30]
})

# 保存为CSV
df.to_csv('output.csv', index=False, encoding='utf-8-sig')

# 保存为Excel
df.to_excel('output.xlsx', index=False)

# 保存为JSON
df.to_json('output.json', orient='records', force_ascii=False)

# 保存到SQL
import sqlite3
conn = sqlite3.connect('database.db')
df.to_sql('table_name', conn, if_exists='replace', index=False)
```

**别担心**！这些概念看起来多，但我们会在后续章节一个个详细讲解。现在只是快速预览，让你有个整体印象！

---

## 实战练习

学习最好的方式就是动手！让我们做几个练习巩固一下：

### 练习1：创建你的第一个数据表

**任务**：创建一个包含你朋友信息的DataFrame。

```python
import pandas as pd

# TODO: 创建一个DataFrame，包含以下列：
# - 姓名
# - 年龄
# - 城市
# - 爱好
# 至少3个人的信息

# 参考答案在下面...
```

**参考答案**：
```python
import pandas as pd

friends = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 28, 22, 30],
    '城市': ['北京', '上海', '深圳', '广州'],
    '爱好': ['篮球', '音乐', '阅读', '旅游']
})

print("=" * 50)
print("我的朋友列表")
print("=" * 50)
print(friends)

print("\n基本信息：")
print(f"朋友数量：{len(friends)}人")
print(f"平均年龄：{friends['年龄'].mean():.1f}岁")
print(f"最大年龄：{friends['年龄'].max()}岁")
print(f"最小年龄：{friends['年龄'].min()}岁")

# 筛选特定城市的朋友
beijing_friends = friends[friends['城市'] == '北京']
print(f"\n在北京的朋友：{len(beijing_friends)}人")
print(beijing_friends)
```

---

### 练习2：读取和分析CSV文件

**任务**：创建一个CSV文件，然后读取并分析。

```python
import pandas as pd

# 第1步：创建数据并保存为CSV
sales_data = pd.DataFrame({
    '日期': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    '产品': ['手机', '电脑', '手机', '平板', '电脑'],
    '销量': [5, 3, 8, 4, 6],
    '单价': [3000, 5000, 3000, 2000, 5000]
})

sales_data.to_csv('sales.csv', index=False, encoding='utf-8-sig')
print("✓ CSV文件已创建")

# 第2步：读取CSV
df = pd.read_csv('sales.csv')

# TODO:
# 1. 计算每天的销售额（销量 × 单价）
# 2. 找出销售额最高的一天
# 3. 统计各产品的总销量
# 4. 计算总销售额

# 参考答案在下面...
```

**参考答案**：
```python
import pandas as pd

# 创建数据
sales_data = pd.DataFrame({
    '日期': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    '产品': ['手机', '电脑', '手机', '平板', '电脑'],
    '销量': [5, 3, 8, 4, 6],
    '单价': [3000, 5000, 3000, 2000, 5000]
})

sales_data.to_csv('sales.csv', index=False, encoding='utf-8-sig')
print("✓ CSV文件已创建：sales.csv\n")

# 读取CSV
df = pd.read_csv('sales.csv')

print("=" * 60)
print("销售数据分析")
print("=" * 60)

# 1. 计算每天的销售额
df['销售额'] = df['销量'] * df['单价']

print("\n【1. 每日销售明细】")
print(df)

# 2. 找出销售额最高的一天
max_sales_day = df.loc[df['销售额'].idxmax()]
print("\n【2. 销售额最高的一天】")
print(f"日期：{max_sales_day['日期']}")
print(f"产品：{max_sales_day['产品']}")
print(f"销售额：{max_sales_day['销售额']}元")

# 3. 统计各产品的总销量
product_sales = df.groupby('产品')['销量'].sum().sort_values(ascending=False)
print("\n【3. 各产品总销量】")
print(product_sales)

# 4. 计算总销售额
total_revenue = df['销售额'].sum()
print(f"\n【4. 总销售额】")
print(f"总计：{total_revenue:,}元")

# 额外分析：各产品销售额占比
product_revenue = df.groupby('产品')['销售额'].sum()
print("\n【5. 各产品销售额占比】")
for product, revenue in product_revenue.items():
    percentage = revenue / total_revenue * 100
    print(f"{product}：{revenue:,}元（{percentage:.1f}%）")
```

---

### 练习3：学生成绩分析

**任务**：分析学生成绩，找出各种统计信息。

```python
import pandas as pd
import numpy as np

# 创建学生成绩数据
np.random.seed(42)
students = pd.DataFrame({
    '姓名': [f'学生{i}' for i in range(1, 21)],
    '语文': np.random.randint(60, 100, 20),
    '数学': np.random.randint(60, 100, 20),
    '英语': np.random.randint(60, 100, 20)
})

# TODO:
# 1. 计算每个学生的总分和平均分
# 2. 找出总分最高和最低的学生
# 3. 计算各科的平均分
# 4. 找出各科成绩最好的学生
# 5. 统计各科及格率（≥60分）
# 6. 找出三科都超过80分的学生

# 参考答案在下面...
```

**参考答案**：
```python
import pandas as pd
import numpy as np

# 创建学生成绩数据
np.random.seed(42)
students = pd.DataFrame({
    '姓名': [f'学生{i}' for i in range(1, 21)],
    '语文': np.random.randint(60, 100, 20),
    '数学': np.random.randint(60, 100, 20),
    '英语': np.random.randint(60, 100, 20)
})

print("=" * 70)
print("学生成绩分析报告")
print("=" * 70)

# 1. 计算每个学生的总分和平均分
students['总分'] = students[['语文', '数学', '英语']].sum(axis=1)
students['平均分'] = students[['语文', '数学', '英语']].mean(axis=1).round(2)

print("\n【1. 学生成绩表】")
print(students)

# 2. 找出总分最高和最低的学生
print("\n【2. 总分排名】")
max_student = students.loc[students['总分'].idxmax()]
min_student = students.loc[students['总分'].idxmin()]
print(f"总分最高：{max_student['姓名']}，总分{max_student['总分']}，平均分{max_student['平均分']}")
print(f"总分最低：{min_student['姓名']}，总分{min_student['总分']}，平均分{min_student['平均分']}")

# 3. 计算各科的平均分
print("\n【3. 各科平均分】")
subjects = ['语文', '数学', '英语']
for subject in subjects:
    avg = students[subject].mean()
    print(f"{subject}：{avg:.2f}分")

# 4. 找出各科成绩最好的学生
print("\n【4. 各科状元】")
for subject in subjects:
    best = students.loc[students[subject].idxmax()]
    print(f"{subject}状元：{best['姓名']}（{best[subject]}分）")

# 5. 统计各科及格率
print("\n【5. 各科及格率】")
for subject in subjects:
    passed = (students[subject] >= 60).sum()
    pass_rate = passed / len(students) * 100
    print(f"{subject}：{pass_rate:.1f}%（{passed}/{len(students)}人）")

# 6. 找出三科都超过80分的学生
print("\n【6. 优秀学生（三科都≥80分）】")
excellent = students[(students['语文'] >= 80) &
                     (students['数学'] >= 80) &
                     (students['英语'] >= 80)]
if len(excellent) > 0:
    print(f"共{len(excellent)}人：")
    print(excellent[['姓名', '语文', '数学', '英语', '总分']])
else:
    print("暂无三科都超过80分的学生")

# 7. 成绩分布
print("\n【7. 成绩分布】")
bins = [0, 60, 70, 80, 90, 100]
labels = ['不及格', '及格', '中等', '良好', '优秀']
students['等级'] = pd.cut(students['平均分'], bins=bins, labels=labels)
grade_dist = students['等级'].value_counts().sort_index()
print(grade_dist)

print("\n" + "=" * 70)
```

---

### 练习4：销售数据透视

**任务**：创建销售数据，进行透视分析。

```python
import pandas as pd
import numpy as np

# 创建销售数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
sales = pd.DataFrame({
    '日期': np.repeat(dates, 3),
    '产品': ['产品A', '产品B', '产品C'] * 30,
    '销量': np.random.randint(10, 100, 90),
    '单价': np.random.randint(50, 200, 90)
})

sales['销售额'] = sales['销量'] * sales['单价']

# TODO:
# 1. 创建透视表，显示每个产品每天的销售额
# 2. 计算每个产品的总销售额
# 3. 找出销售额最高的一天
# 4. 分析每周的销售趋势

# 参考答案在下面...
```

**参考答案**：
```python
import pandas as pd
import numpy as np

# 创建销售数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
sales = pd.DataFrame({
    '日期': np.repeat(dates, 3),
    '产品': ['产品A', '产品B', '产品C'] * 30,
    '销量': np.random.randint(10, 100, 90),
    '单价': np.random.randint(50, 200, 90)
})

sales['销售额'] = sales['销量'] * sales['单价']

print("=" * 70)
print("销售数据透视分析")
print("=" * 70)

# 1. 创建透视表
print("\n【1. 每日各产品销售额】")
pivot = sales.pivot_table(
    values='销售额',
    index='日期',
    columns='产品',
    aggfunc='sum'
)
print(pivot.head(10))  # 显示前10天

# 2. 各产品总销售额
print("\n【2. 各产品总销售额】")
product_total = sales.groupby('产品')['销售额'].sum().sort_values(ascending=False)
print(product_total)
print(f"\n总销售额：{product_total.sum():,}元")

# 3. 销售额最高的一天
print("\n【3. 销售额最高的一天】")
daily_sales = sales.groupby('日期')['销售额'].sum()
best_day = daily_sales.idxmax()
best_sales = daily_sales.max()
print(f"日期：{best_day.strftime('%Y-%m-%d')}")
print(f"销售额：{best_sales:,}元")

# 4. 每周销售趋势
print("\n【4. 每周销售趋势】")
sales['周'] = pd.to_datetime(sales['日期']).dt.isocalendar().week
weekly_sales = sales.groupby('周')['销售额'].sum()
print(weekly_sales)

# 5. 各产品销售量统计
print("\n【5. 各产品销售量统计】")
product_quantity = sales.groupby('产品')['销量'].agg(['sum', 'mean', 'max', 'min'])
product_quantity.columns = ['总销量', '平均销量', '最高销量', '最低销量']
print(product_quantity)

print("\n" + "=" * 70)
```

---

### 练习5：数据清洗实战

**任务**：处理一个包含脏数据的DataFrame。

```python
import pandas as pd
import numpy as np

# 创建包含问题的数据
dirty_data = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '张三', '赵六', None, '钱七'],
    '年龄': [25, 30, np.nan, 25, 35, 28, 40],
    '城市': ['北京', '上海', '深圳', '北京', None, '广州', ''],
    '工资': [8000, 12000, 10000, 8000, np.nan, 9000, 11000]
})

print("原始数据（有问题）：")
print(dirty_data)

# TODO:
# 1. 检查缺失值
# 2. 填充缺失值（年龄用平均值，城市用"未知"，工资用中位数）
# 3. 删除重复行
# 4. 删除空字符串的城市行
# 5. 重置索引
# 6. 查看清洗后的数据

# 参考答案在下面...
```

**参考答案**：
```python
import pandas as pd
import numpy as np

# 创建包含问题的数据
dirty_data = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '张三', '赵六', None, '钱七'],
    '年龄': [25, 30, np.nan, 25, 35, 28, 40],
    '城市': ['北京', '上海', '深圳', '北京', None, '广州', ''],
    '工资': [8000, 12000, 10000, 8000, np.nan, 9000, 11000]
})

print("=" * 70)
print("数据清洗实战")
print("=" * 70)

print("\n【原始数据（有问题）】")
print(dirty_data)

# 1. 检查缺失值
print("\n【1. 检查缺失值】")
print(dirty_data.isnull().sum())

# 2. 填充缺失值
print("\n【2. 填充缺失值】")
# 复制数据以保留原始数据
clean_data = dirty_data.copy()

# 年龄用平均值填充
age_mean = clean_data['年龄'].mean()
clean_data['年龄'].fillna(age_mean, inplace=True)
print(f"✓ 年龄缺失值已用平均值填充（{age_mean:.1f}）")

# 城市用"未知"填充
clean_data['城市'].fillna('未知', inplace=True)
print("✓ 城市缺失值已用'未知'填充")

# 工资用中位数填充
salary_median = clean_data['工资'].median()
clean_data['工资'].fillna(salary_median, inplace=True)
print(f"✓ 工资缺失值已用中位数填充（{salary_median:.0f}）")

# 姓名缺失值填充为"未知"
clean_data['姓名'].fillna('未知', inplace=True)

print("\n填充后的数据：")
print(clean_data)

# 3. 删除重复行
print("\n【3. 删除重复行】")
before_count = len(clean_data)
clean_data = clean_data.drop_duplicates()
after_count = len(clean_data)
print(f"✓ 删除了{before_count - after_count}行重复数据")

# 4. 删除空字符串的城市行
print("\n【4. 删除空字符串的城市行】")
before_count = len(clean_data)
clean_data = clean_data[clean_data['城市'] != '']
after_count = len(clean_data)
print(f"✓ 删除了{before_count - after_count}行空城市数据")

# 5. 重置索引
clean_data = clean_data.reset_index(drop=True)
print("✓ 索引已重置")

# 6. 查看清洗后的数据
print("\n【清洗后的数据】")
print(clean_data)

print("\n【清洗总结】")
print(f"原始数据：{len(dirty_data)}行")
print(f"清洗后：{len(clean_data)}行")
print(f"删除：{len(dirty_data) - len(clean_data)}行")
print("✓ 数据清洗完成！")

print("\n" + "=" * 70)
```

---

## 学习资源推荐

学完这一章，如果你想深入学习Pandas，这里有一些推荐资源：

### 官方资源

1. **Pandas官方文档**
   - 网址：https://pandas.pydata.org/docs/
   - 特点：最权威、最全面
   - 适合：查API、看示例

2. **Pandas官方教程**
   - 网址：https://pandas.pydata.org/docs/getting_started/intro_tutorials/
   - 特点：交互式教程
   - 适合：系统学习

3. **Pandas Cheat Sheet**
   - 网址：https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
   - 特点：快速参考卡
   - 适合：随时查阅

### 中文资源

4. **Pandas中文文档**
   - 网址：https://www.pypandas.cn/
   - 特点：中文版，方便阅读
   - 适合：中文母语者

5. **菜鸟教程 - Pandas**
   - 网址：https://www.runoob.com/pandas/pandas-tutorial.html
   - 特点：通俗易懂，例子丰富
   - 适合：快速入门

### 书籍推荐

6. **《利用Python进行数据分析》**
   - 作者：Wes McKinney（Pandas创始人）
   - 特点：官方教材，权威系统
   - 适合：想深入学习的人

7. **《Python数据分析实战》**
   - 作者：Fabio Nelli
   - 特点：实战案例丰富
   - 适合：想做项目的人

8. **《Pandas Cookbook》**
   - 作者：Theodore Petrou
   - 特点：食谱式教学，查询方便
   - 适合：解决具体问题

### 视频课程

9. **B站**
   - 搜索"Pandas教程"
   - 特点：免费，选择多
   - 推荐UP主：鱼C工作室、莫烦Python

10. **Coursera/Udemy**
    - 搜索"Pandas"或"Data Analysis with Python"
    - 特点：系统完整，有证书
    - 适合：想要系统学习

### 实战平台

11. **Kaggle**
    - 网址：https://www.kaggle.com/
    - 特点：真实数据集，实战项目
    - 适合：想做数据科学的人

12. **DataCamp**
    - 网址：https://www.datacamp.com/
    - 特点：交互式练习
    - 适合：边学边练

### 社区

13. **Stack Overflow**
    - 网址：https://stackoverflow.com/questions/tagged/pandas
    - 特点：遇到问题可以搜索或提问
    - 适合：解决实际问题

14. **Pandas GitHub**
    - 网址：https://github.com/pandas-dev/pandas
    - 特点：源代码、Issue、讨论
    - 适合：深入研究

15. **Reddit r/pandas**
    - 网址：https://www.reddit.com/r/pandas/
    - 特点：社区讨论，经验分享
    - 适合：学习交流

---

## 学习建议

### 学习路线

```
第1周：基础篇
  ├─ Series和DataFrame基础
  ├─ 数据读取和查看
  └─ 基本索引和选择

第2周：操作篇
  ├─ 数据筛选和排序
  ├─ 数据清洗（缺失值、重复值）
  └─ 数据转换和计算

第3周：分析篇
  ├─ 分组统计（groupby）
  ├─ 数据透视表（pivot_table）
  └─ 时间序列处理

第4周：进阶篇
  ├─ 数据合并和连接
  ├─ 数据可视化
  └─ 综合实战项目
```

### 学习方法

1. **边学边练**：看完一个知识点，马上写代码试试
2. **做笔记**：记录常用操作和容易忘的点
3. **查文档**：养成查官方文档的习惯
4. **做项目**：找真实数据集练手
5. **看别人的代码**：Kaggle上有很多优秀的Notebook
6. **总结经验**：把常用操作整理成自己的代码库

### 常见误区

1. **误区1**：只看不练
   - **正确做法**：每个例子都亲手敲一遍

2. **误区2**：死记硬背所有函数
   - **正确做法**：理解核心概念，需要时查文档

3. **误区3**：遇到问题就放弃
   - **正确做法**：学会调试，查错误信息，Google搜索

4. **误区4**：追求完美代码
   - **正确做法**：先实现功能，再优化

5. **误区5**：不看数据就操作
   - **正确做法**：先用head()、info()了解数据

### 实用技巧

1. **Jupyter Notebook是最好的学习工具**
   - 边写边运行
   - 可以可视化
   - 保存学习记录

2. **养成好习惯**
   - 操作前先备份数据：`df_copy = df.copy()`
   - 经常保存中间结果
   - 给变量起有意义的名字

3. **学会Debug**
   - 用`print(df.head())`查看数据
   - 用`print(df.shape)`检查数据形状
   - 用`print(df.dtypes)`查看数据类型

4. **掌握核心20%**
   - 80%的工作只需要20%的功能
   - 先掌握最常用的操作
   - 其他的用到再学

5. **做笔记和代码片段库**
   - 把常用代码保存起来
   - 下次直接复制修改
   - 提高效率

---

## 下一步

太棒了！现在你已经：
- 了解了Pandas是什么，为什么要学它
- 知道了Pandas的优势和应用场景
- 成功安装了Pandas
- 运行了第一个Pandas程序
- 了解了Pandas的核心概念（Series、DataFrame）
- 完成了5个实战练习

**你已经迈出了数据分析的第一步！**

Pandas的大门已经为你敞开，接下来我们将深入学习：
- Series详解
- DataFrame详解
- 数据读取和保存
- 数据选择和索引
- 数据清洗
- 数据分组和聚合
- 数据透视表
- 时间序列
- 数据可视化
- 综合实战项目

准备好了吗？让我们继续Pandas的学习之旅！

[下一章：第02章 - Pandas核心数据结构 →](../02-Series数据结构/02-Series数据结构.md)

---

## 本章重点总结

### 核心概念

1. **Pandas是什么**
   - Python的数据分析库
   - Excel之外的可编程数据处理方式
   - 数据分析的瑞士军刀

2. **为什么学Pandas**
   - 功能全面（读取、清洗、分析、可视化）
   - 简单直观（像操作Excel）
   - 高效强大（底层是NumPy）
   - 生态丰富（与其他库无缝集成）

3. **Pandas vs Excel/SQL**
   - 比Excel：数据量无限制，可自动化，速度快
   - 比SQL：更灵活，可本地操作，Python生态

4. **Pandas与NumPy**
   - Pandas基于NumPy构建
   - NumPy做数值计算，Pandas做数据分析
   - 两者经常配合使用

### 技能清单

- 能够安装Pandas
- 能够导入Pandas并创建Series和DataFrame
- 了解Pandas的核心概念
- 能够做简单的数据操作
- 知道如何查文档和找资源

### 常用命令

```python
# 导入Pandas
import pandas as pd

# 创建Series
s = pd.Series([1, 2, 3])

# 创建DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# 查看版本
print(pd.__version__)

# 读取数据
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')

# 查看数据
df.head()
df.info()
df.describe()

# 基本操作
df['列名']
df[df['age'] > 18]
df.groupby('city')['sales'].sum()
```

### 记住这些

1. **Pandas是Excel之外的可编程数据处理方式**
2. **DataFrame是Pandas的核心（二维表格）**
3. **Pandas是数据分析的必备工具**
4. **遇到问题先查官方文档**
5. **多练习，多写代码，多做项目**

---

**准备好了吗？下一章我们将深入学习Pandas的核心数据结构！**
