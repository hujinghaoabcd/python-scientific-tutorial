# 第03章：DataFrame数据结构

在上一章，我们学习了Series——Pandas的一维数据结构。这一章，我们要学习Pandas最重要、最强大的数据结构：DataFrame。

如果说Series是一列数据，那DataFrame就是一张完整的数据表格。DataFrame是数据分析的核心工具，也是你在实际工作中最常用的数据结构。

学完这一章，你就能够自如地处理各种表格数据了！

---

## 什么是DataFrame？

### 生活化理解

想象一下Excel表格，DataFrame就是Python中的Excel表！

**Excel表格的样子**：
```
     姓名    年龄   城市    工资
0    张三    25    北京    8000
1    李四    30    上海   12000
2    王五    28    广州   10000
```

DataFrame就是这样的一张表格，它有：
- **行**：每一行代表一条记录（比如一个人的信息）
- **列**：每一列代表一个字段（比如姓名、年龄）
- **行索引**：每一行都有编号（0, 1, 2...或者自定义）
- **列索引**：每一列都有名称（姓名、年龄、城市、工资）

**DataFrame = Excel表格 + 超级能力**

DataFrame不仅仅是一张表格，它还拥有：
- 强大的数据筛选能力
- 灵活的数据计算能力
- 快速的数据处理速度
- 丰富的数据分析功能

### 技术定义

DataFrame是Pandas中的二维标记数据结构，它：
- **二维表格**：有行和列的表格结构
- **列类型可以不同**：不同列可以是不同数据类型（整数、浮点数、字符串等）
- **有行索引和列索引**：每行每列都有标签
- **大小可变**：可以添加或删除列
- **是Series的集合**：每一列都是一个Series

**重要概念**：DataFrame可以看作是多个Series按列组合在一起形成的！每一列就是一个Series，它们共享同一个行索引。

```python
import pandas as pd
import numpy as np

# 创建第一个DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
}

df = pd.DataFrame(data)
print(df)
# 输出：
#   姓名  年龄  城市
# 0  张三  25  北京
# 1  李四  30  上海
# 2  王五  28  广州

print(type(df))
# 输出：<class 'pandas.core.frame.DataFrame'>
```

---

## DataFrame的结构

DataFrame由三个核心部分组成：行索引、列索引和数据。理解这三个部分是掌握DataFrame的关键。

### 三大组成部分

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

print(df)
#   姓名  年龄   工资
# 0  张三  25   8000  <- 行索引0
# 1  李四  30  12000  <- 行索引1
# 2  王五  28  10000  <- 行索引2
#   ↑   ↑     ↑
#  列索引（列名）

# 查看各部分
print("行索引:", df.index)      # RangeIndex(start=0, stop=3, step=1)
print("列索引:", df.columns)    # Index(['姓名', '年龄', '工资'])
print("数据:\n", df.values)     # 二维NumPy数组
```

### 行索引（Index）

行索引是每一行的标签，用于标识和访问数据。默认是从0开始的整数，但可以自定义。

```python
import pandas as pd

# 默认行索引（从0开始）
df1 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28]
})
print(df1)
#   姓名  年龄
# 0  张三  25
# 1  李四  30
# 2  王五  28

# 自定义行索引
df2 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28]
}, index=['a', 'b', 'c'])
print(df2)
#   姓名  年龄
# a  张三  25
# b  李四  30
# c  王五  28

# 用员工编号作为索引
df3 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28]
}, index=['E001', 'E002', 'E003'])
print(df3)
#      姓名  年龄
# E001  张三  25
# E002  李四  30
# E003  王五  28
```

**行索引的作用**：
- 标识每一行数据
- 用于快速访问和查询
- 可以是唯一的（像主键），也可以重复
- 可以是任何不可变类型（整数、字符串、日期等）

### 列索引（Columns）

列索引就是列名，用于标识每一列的含义。列名通常是字符串，也可以是其他不可变类型。

```python
import pandas as pd

# 列名就是字典的键
df = pd.DataFrame({
    '姓名': ['张三', '李四'],
    '年龄': [25, 30],
    '城市': ['北京', '上海']
})
print(df.columns)  # Index(['姓名', '年龄', '城市'])

# 英文列名
df_en = pd.DataFrame({
    'name': ['张三', '李四'],
    'age': [25, 30],
    'city': ['北京', '上海']
})
print(df_en.columns)  # Index(['name', 'age', 'city'])

# 可以用数字作为列名（不推荐）
df_num = pd.DataFrame({
    0: ['张三', '李四'],
    1: [25, 30],
    2: ['北京', '上海']
})
print(df_num.columns)  # Int64Index([0, 1, 2])
```

**列索引的作用**：
- 标识每一列的含义
- 用于选择和操作列
- 建议用有意义的名称
- 列名应该唯一（重复会导致混淆）

### 数据（Values）

数据部分是一个二维NumPy数组，存储着所有的数据值。

```python
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

# 获取数据部分（NumPy数组）
print(df.values)
# [['张三' 25 8000]
#  ['李四' 30 12000]
#  ['王五' 28 10000]]

print(type(df.values))  # <class 'numpy.ndarray'>
print(df.values.shape)  # (3, 3) - 3行3列
```

**数据部分特点**：
- 是一个二维NumPy数组
- 同一列的数据类型相同
- 不同列可以是不同类型
- 访问values会失去索引信息

### DataFrame vs Series

DataFrame和Series的关系非常重要，理解这个关系能帮你更好地使用Pandas。

**核心关系**：DataFrame是多个Series的集合！

```python
import pandas as pd

# 创建DataFrame
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

# 每一列都是一个Series
print("'姓名'列的类型:", type(df['姓名']))
# <class 'pandas.core.series.Series'>

print("\n'年龄'列:")
print(df['年龄'])
# 0    25
# 1    30
# 2    28
# Name: 年龄, dtype: int64

print("\n'工资'列:")
print(df['工资'])
# 0     8000
# 1    12000
# 2    10000
# Name: 工资, dtype: int64
```

**DataFrame vs Series对比**：

| 特性 | Series | DataFrame |
|------|--------|-----------|
| **维度** | 一维（一列） | 二维（多列） |
| **索引** | 只有行索引 | 有行索引和列索引 |
| **数据类型** | 单一类型 | 每列可以不同类型 |
| **比喻** | 一列数据 | 一张表格 |
| **关系** | 是DataFrame的组成部分 | 是多个Series的集合 |

```python
import pandas as pd

# Series：一列数据
s = pd.Series([25, 30, 28], name='年龄')
print("Series:")
print(s)
# 0    25
# 1    30
# 2    28
# Name: 年龄, dtype: int64

# DataFrame：多列数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})
print("\nDataFrame:")
print(df)
#   姓名  年龄   工资
# 0  张三  25   8000
# 1  李四  30  12000
# 2  王五  28  10000

# 从DataFrame中提取Series
age_series = df['年龄']
print("\n从DataFrame提取的Series:")
print(age_series)
print(type(age_series))  # <class 'pandas.core.series.Series'>

# 从多个Series创建DataFrame
s1 = pd.Series(['张三', '李四', '王五'], name='姓名')
s2 = pd.Series([25, 30, 28], name='年龄')
s3 = pd.Series([8000, 12000, 10000], name='工资')

df_from_series = pd.DataFrame({
    '姓名': s1,
    '年龄': s2,
    '工资': s3
})
print("\n从Series创建的DataFrame:")
print(df_from_series)
```

**理解要点**：
- DataFrame的每一列是一个Series
- DataFrame的每一行也可以看作是一个Series
- 选择DataFrame的一列，返回的是Series
- 多个Series可以组合成DataFrame

---

## DataFrame的创建

创建DataFrame有很多方式，适应不同的数据来源。掌握这些方法，你就能从各种格式的数据创建DataFrame。

### 从字典创建

最常用的方式！字典的键成为列名，值成为列数据。

```python
import pandas as pd

# 基本方式：字典的值是列表
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
print(df)
#   姓名  年龄  城市
# 0  张三  25  北京
# 1  李四  30  上海
# 2  王五  28  广州

# 指定行索引
df_with_index = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df_with_index)
#   姓名  年龄  城市
# a  张三  25  北京
# b  李四  30  上海
# c  王五  28  广州

# 选择特定列
df_selected = pd.DataFrame(data, columns=['姓名', '城市'])
print(df_selected)
#   姓名  城市
# 0  张三  北京
# 1  李四  上海
# 2  王五  广州

# 列的顺序可以调整
df_reordered = pd.DataFrame(data, columns=['城市', '姓名', '年龄'])
print(df_reordered)
#   城市  姓名  年龄
# 0  北京  张三  25
# 1  上海  李四  30
# 2  广州  王五  28
```

**注意事项**：
- 所有列的长度必须相同
- 字典的键成为列名
- 字典的值可以是列表、元组、Series或NumPy数组

```python
import pandas as pd
import numpy as np

# 值可以是不同类型的序列
data = {
    '列表列': [1, 2, 3],
    '元组列': (4, 5, 6),
    'Series列': pd.Series([7, 8, 9]),
    '数组列': np.array([10, 11, 12])
}
df = pd.DataFrame(data)
print(df)
#    列表列  元组列  Series列  数组列
# 0     1     4       7     10
# 1     2     5       8     11
# 2     3     6       9     12
```

### 从列表创建

可以从嵌套列表创建DataFrame，每个子列表代表一行数据。

```python
import pandas as pd

# 列表的列表（每个子列表是一行）
data = [
    ['张三', 25, '北京'],
    ['李四', 30, '上海'],
    ['王五', 28, '广州']
]
df = pd.DataFrame(data, columns=['姓名', '年龄', '城市'])
print(df)
#   姓名  年龄  城市
# 0  张三  25  北京
# 1  李四  30  上海
# 2  王五  28  广州

# 元组的列表
data_tuple = [
    ('张三', 25, '北京'),
    ('李四', 30, '上海'),
    ('王五', 28, '广州')
]
df_tuple = pd.DataFrame(data_tuple, columns=['姓名', '年龄', '城市'])
print(df_tuple)
```

**优点**：适合从文件读取或逐行构建数据
**缺点**：必须手动指定列名

### 从字典列表创建

每个字典代表一行，字典的键是列名。

```python
import pandas as pd

# 字典列表（每个字典是一行）
data = [
    {'姓名': '张三', '年龄': 25, '城市': '北京'},
    {'姓名': '李四', '年龄': 30, '城市': '上海'},
    {'姓名': '王五', '年龄': 28, '城市': '广州'}
]
df = pd.DataFrame(data)
print(df)
#   姓名  年龄  城市
# 0  张三  25  北京
# 1  李四  30  上海
# 2  王五  28  广州

# 字典可以有缺失键（会自动填充NaN）
data_missing = [
    {'姓名': '张三', '年龄': 25, '城市': '北京'},
    {'姓名': '李四', '年龄': 30},  # 缺少'城市'
    {'姓名': '王五', '城市': '广州'}  # 缺少'年龄'
]
df_missing = pd.DataFrame(data_missing)
print(df_missing)
#   姓名    年龄  城市
# 0  张三  25.0  北京
# 1  李四  30.0  NaN
# 2  王五   NaN  广州
```

**优点**：结构清晰，支持缺失值
**常见场景**：从API获取JSON数据

### 从NumPy数组创建

NumPy数组是高效的数值数据源。

```python
import pandas as pd
import numpy as np

# 从二维数组创建
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# 随机数据
random_data = np.random.randn(5, 3)  # 5行3列的随机数
df_random = pd.DataFrame(
    random_data,
    columns=['列1', '列2', '列3'],
    index=['行1', '行2', '行3', '行4', '行5']
)
print(df_random)
#         列1       列2       列3
# 行1  0.496714 -0.138264  0.647689
# 行2  1.523030 -0.234153 -0.234137
# 行3  1.579213  0.767435 -0.469474
# 行4  0.542560 -0.463418 -0.465730
# 行5  0.241962 -1.913280 -1.724918

# 生成有规律的数据
data = np.arange(12).reshape(4, 3)  # 4行3列
df_range = pd.DataFrame(data, columns=['X', 'Y', 'Z'])
print(df_range)
#    X  Y   Z
# 0  0  1   2
# 1  3  4   5
# 2  6  7   8
# 3  9  10 11
```

**适用场景**：
- 科学计算结果转换为DataFrame
- 大量数值数据处理
- 矩阵运算结果展示

### 从Series创建

可以用Series字典或多个Series组合创建DataFrame。

```python
import pandas as pd

# 从Series字典创建
s1 = pd.Series(['张三', '李四', '王五'])
s2 = pd.Series([25, 30, 28])
s3 = pd.Series(['北京', '上海', '广州'])

df = pd.DataFrame({
    '姓名': s1,
    '年龄': s2,
    '城市': s3
})
print(df)
#   姓名  年龄  城市
# 0  张三  25  北京
# 1  李四  30  上海
# 2  王五  28  广州

# 如果Series有自己的索引，会自动对齐
s_name = pd.Series(['张三', '李四', '王五'], index=['a', 'b', 'c'])
s_age = pd.Series([25, 30, 28], index=['a', 'b', 'c'])

df_aligned = pd.DataFrame({
    '姓名': s_name,
    '年龄': s_age
})
print(df_aligned)
#   姓名  年龄
# a  张三  25
# b  李四  30
# c  王五  28

# 索引不对齐的情况
s_age_partial = pd.Series([25, 30], index=['a', 'b'])  # 只有a和b

df_partial = pd.DataFrame({
    '姓名': s_name,
    '年龄': s_age_partial
})
print(df_partial)
#   姓名    年龄
# a  张三  25.0
# b  李四  30.0
# c  王五   NaN  <- 自动填充NaN
```

**重要特性**：Series会根据索引自动对齐！

### 从CSV文件创建

实际工作中最常用的方式！CSV是最通用的数据交换格式。

```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')

# 常用参数示例
df = pd.read_csv(
    'data.csv',
    encoding='utf-8',      # 指定编码（中文用utf-8）
    sep=',',               # 分隔符（默认是逗号）
    header=0,              # 第一行是列名
    index_col=0,           # 第一列作为索引
    names=['列1', '列2']    # 自定义列名
)
```

**创建示例CSV用于测试**：

```python
import pandas as pd

# 创建示例数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '城市': ['北京', '上海', '广州', '深圳'],
    '工资': [8000, 12000, 10000, 15000]
}
df = pd.DataFrame(data)

# 保存为CSV
df.to_csv('employees.csv', index=False, encoding='utf-8')

# 读取CSV
df_from_csv = pd.read_csv('employees.csv', encoding='utf-8')
print(df_from_csv)
#   姓名  年龄  城市   工资
# 0  张三  25  北京   8000
# 1  李四  30  上海  12000
# 2  王五  28  广州  10000
# 3  赵六  35  深圳  15000
```

### 从Excel文件创建

Excel也是非常常见的数据源。

```python
import pandas as pd

# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 读取指定工作表
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 读取多个工作表
dfs = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'Sheet2'])

# 常用参数
df = pd.read_excel(
    'data.xlsx',
    sheet_name=0,        # 第一个工作表
    header=0,            # 第一行是列名
    index_col=0,         # 第一列作为索引
    usecols='A:C',       # 只读取A到C列
    nrows=10             # 只读取前10行
)
```

**示例：创建和读取Excel**：

```python
import pandas as pd

# 创建示例数据
data = {
    '日期': pd.date_range('2024-01-01', periods=5),
    '销售额': [1000, 1500, 1200, 1800, 2000],
    '成本': [600, 900, 720, 1080, 1200]
}
df = pd.DataFrame(data)

# 保存为Excel
df.to_excel('sales.xlsx', index=False)

# 读取Excel
df_from_excel = pd.read_excel('sales.xlsx')
print(df_from_excel)
#         日期  销售额  成本
# 0 2024-01-01  1000  600
# 1 2024-01-02  1500  900
# 2 2024-01-03  1200  720
# 3 2024-01-04  1800 1080
# 4 2024-01-05  2000 1200
```

### 创建空DataFrame

有时需要先创建空的DataFrame，然后逐步添加数据。

```python
import pandas as pd

# 完全空的DataFrame
df_empty = pd.DataFrame()
print(df_empty)
# Empty DataFrame
# Columns: []
# Index: []

# 指定列名的空DataFrame
df_with_columns = pd.DataFrame(columns=['姓名', '年龄', '城市'])
print(df_with_columns)
# Empty DataFrame
# Columns: [姓名, 年龄, 城市]
# Index: []

# 指定行索引和列名的空DataFrame
df_with_both = pd.DataFrame(
    index=['a', 'b', 'c'],
    columns=['姓名', '年龄', '城市']
)
print(df_with_both)
#   姓名  年龄  城市
# a  NaN  NaN  NaN
# b  NaN  NaN  NaN
# c  NaN  NaN  NaN

# 创建指定形状的全NaN DataFrame
df_nan = pd.DataFrame(
    index=range(3),
    columns=['A', 'B', 'C']
)
print(df_nan)
#      A    B    C
# 0  NaN  NaN  NaN
# 1  NaN  NaN  NaN
# 2  NaN  NaN  NaN
```

**使用场景**：
- 逐行添加数据
- 数据预处理框架
- 动态构建表格

---

## DataFrame的属性

DataFrame有很多有用的属性，可以快速了解数据的基本信息。这些属性不需要加括号，直接访问即可。

### 基本属性

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '身高': [175.5, 168.0, 180.3, 172.8],
    '城市': ['北京', '上海', '广州', '深圳'],
    '入职日期': pd.date_range('2020-01-01', periods=4)
})

print("DataFrame:")
print(df)
print()

# 1. shape - 形状（行数，列数）
print("shape:", df.shape)
# shape: (4, 5)
print("行数:", df.shape[0])  # 4
print("列数:", df.shape[1])  # 5
print()

# 2. size - 元素总数（行数 × 列数）
print("size:", df.size)  # 20 (4行×5列)
print()

# 3. ndim - 维度（DataFrame总是2）
print("ndim:", df.ndim)  # 2
print()

# 4. columns - 列索引
print("columns:", df.columns)
# Index(['姓名', '年龄', '身高', '城市', '入职日期'])
print("列名列表:", df.columns.tolist())
# ['姓名', '年龄', '身高', '城市', '入职日期']
print()

# 5. index - 行索引
print("index:", df.index)
# RangeIndex(start=0, stop=4, step=1)
print("行索引列表:", df.index.tolist())
# [0, 1, 2, 3]
print()

# 6. dtypes - 每列的数据类型
print("dtypes:")
print(df.dtypes)
# 姓名            object
# 年龄             int64
# 身高           float64
# 城市            object
# 入职日期    datetime64[ns]
# dtype: object
print()

# 7. values - 数据部分（NumPy数组）
print("values:")
print(df.values)
# [['张三' 25 175.5 '北京' Timestamp('2020-01-01 00:00:00')]
#  ['李四' 30 168.0 '上海' Timestamp('2020-01-02 00:00:00')]
#  ['王五' 28 180.3 '广州' Timestamp('2020-01-03 00:00:00')]
#  ['赵六' 35 172.8 '深圳' Timestamp('2020-01-04 00:00:00')]]
print()

# 8. T - 转置（行列互换）
print("T (转置):")
print(df.T)
#                      0           1           2           3
# 姓名                张三          李四          王五          赵六
# 年龄                25          30          28          35
# 身高             175.5       168.0       180.3       172.8
# 城市                北京          上海          广州          深圳
# 入职日期    2020-01-01  2020-01-02  2020-01-03  2020-01-04
print()

# 9. empty - 是否为空
print("empty:", df.empty)  # False

df_empty = pd.DataFrame()
print("空DataFrame的empty:", df_empty.empty)  # True
```

### 数据类型详解

DataFrame中的数据类型（dtype）非常重要，影响内存占用和运算性能。

```python
import pandas as pd
import numpy as np

# 创建包含多种类型的DataFrame
df = pd.DataFrame({
    '整数': [1, 2, 3],
    '浮点数': [1.1, 2.2, 3.3],
    '字符串': ['a', 'b', 'c'],
    '布尔值': [True, False, True],
    '日期': pd.date_range('2024-01-01', periods=3),
    '分类': pd.Categorical(['A', 'B', 'A'])
})

print("各列数据类型:")
print(df.dtypes)
# 整数             int64
# 浮点数          float64
# 字符串           object
# 布尔值             bool
# 日期     datetime64[ns]
# 分类         category
# dtype: object

# 查看单列类型
print("\n'整数'列的类型:", df['整数'].dtype)  # int64

# 统计各类型的列数
print("\n类型统计:")
print(df.dtypes.value_counts())
```

**常见数据类型**：

| 类型 | 说明 | 示例 |
|------|------|------|
| `int64` | 64位整数 | 1, 2, 3 |
| `float64` | 64位浮点数 | 1.5, 2.3 |
| `object` | 字符串或混合类型 | 'abc', '北京' |
| `bool` | 布尔值 | True, False |
| `datetime64[ns]` | 日期时间 | 2024-01-01 |
| `timedelta64[ns]` | 时间差 | 3 days |
| `category` | 分类数据 | 'A', 'B', 'C' |

### 内存占用

了解DataFrame占用多少内存，对于处理大数据很重要。

```python
import pandas as pd
import numpy as np

# 创建较大的DataFrame
df = pd.DataFrame({
    '整数': np.arange(10000),
    '浮点数': np.random.randn(10000),
    '字符串': ['hello'] * 10000
})

# 查看内存占用
print("内存信息:")
print(df.info(memory_usage='deep'))
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10000 entries, 0 to 9999
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   整数      10000 non-null  int64
#  1   浮点数     10000 non-null  float64
#  2   字符串     10000 non-null  object
# dtypes: float64(1), int64(1), object(1)
# memory usage: 312.7 KB

# 查看各列内存占用
print("\n各列内存:")
print(df.memory_usage(deep=True))
# Index     132
# 整数       80000
# 浮点数      80000
# 字符串     650000  <- object类型占用较多
# dtype: int64

# 总内存（字节）
total_memory = df.memory_usage(deep=True).sum()
print(f"\n总内存: {total_memory / 1024:.2f} KB")
print(f"总内存: {total_memory / 1024 / 1024:.2f} MB")
```

**优化内存技巧**：

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '年龄': [25, 30, 28, 35],  # 用int64
    '性别': ['男', '女', '男', '女']  # 用object
})

print("原始内存:")
print(df.memory_usage(deep=True))
# Index    132
# 年龄       32
# 性别      328  <- object类型占用多
# dtype: int64

# 优化1：降低整数精度
df['年龄'] = df['年龄'].astype('int8')  # int64 -> int8

# 优化2：使用category类型
df['性别'] = df['性别'].astype('category')

print("\n优化后内存:")
print(df.memory_usage(deep=True))
# Index    132
# 年龄        4  <- 减少了87.5%
# 性别      213  <- 减少了35%
# dtype: int64

print("\n数据类型:")
print(df.dtypes)
# 年龄          int8
# 性别      category
# dtype: object
```

---

## DataFrame的查看方法

创建DataFrame后，我们需要查看数据。Pandas提供了多种查看方法，可以快速了解数据的内容和特征。

### head() 和 tail()

最常用的查看方法！查看前几行或后几行数据。

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '日期': pd.date_range('2024-01-01', periods=100),
    '销售额': np.random.randint(1000, 5000, 100),
    '成本': np.random.randint(500, 3000, 100)
})

# head() - 查看前5行（默认）
print("前5行:")
print(df.head())
#          日期  销售额  成本
# 0 2024-01-01  2345  1234
# 1 2024-01-02  3456  2345
# 2 2024-01-03  1234  987
# 3 2024-01-04  4321  2876
# 4 2024-01-05  2987  1543

# head(n) - 查看前n行
print("\n前3行:")
print(df.head(3))

# tail() - 查看后5行（默认）
print("\n后5行:")
print(df.tail())
#           日期  销售额  成本
# 95 2024-04-05  2234  1432
# 96 2024-04-06  3456  2123
# 97 2024-04-07  1987  1234
# 98 2024-04-08  4123  2987
# 99 2024-04-09  2876  1765

# tail(n) - 查看后n行
print("\n后3行:")
print(df.tail(3))
```

**使用场景**：
- 快速预览数据
- 检查数据导入是否正确
- 查看数据的开始和结尾

### info()

显示DataFrame的概览信息，包括索引类型、列数据类型、非空值数量、内存占用等。

```python
import pandas as pd
import numpy as np

# 创建示例数据（包含缺失值）
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', None, '赵六'],
    '年龄': [25, 30, None, 35, 28],
    '工资': [8000.0, 12000.0, 10000.0, 15000.0, 9500.0],
    '城市': ['北京', '上海', '广州', '深圳', None]
})

# 显示详细信息
print("DataFrame信息:")
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   姓名      4 non-null      object
#  1   年龄      4 non-null      float64
#  2   工资      5 non-null      float64
#  3   城市      4 non-null      object
# dtypes: float64(2), object(2)
# memory usage: 292.0+ bytes

# 显示内存详细信息
print("\n详细内存信息:")
df.info(memory_usage='deep')
```

**info()显示的关键信息**：
- DataFrame类型
- 行索引范围
- 列数和列名
- 每列的非空值数量（可以发现缺失值）
- 每列的数据类型
- 内存占用

### describe()

生成描述性统计信息，快速了解数值列的统计特征。

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 28, 35, 32],
    '工资': [8000, 12000, 10000, 15000, 11000],
    '工作年限': [3, 8, 5, 12, 9]
})

# 数值列的描述统计
print("数值列统计:")
print(df.describe())
#             年龄          工资       工作年限
# count   5.000000      5.000000   5.000000
# mean   30.000000  11200.000000   7.400000
# std     3.807887   2588.435821   3.577709
# min    25.000000   8000.000000   3.000000
# 25%    28.000000  10000.000000   5.000000
# 50%    30.000000  11000.000000   8.000000
# 75%    32.000000  12000.000000   9.000000
# max    35.000000  15000.000000  12.000000

# 包含所有列（包括非数值列）
print("\n所有列统计:")
print(df.describe(include='all'))
#          姓名        年龄          工资       工作年限
# count     5   5.000000      5.000000   5.000000
# unique    5        NaN           NaN        NaN
# top      张三        NaN           NaN        NaN
# freq      1        NaN           NaN        NaN
# mean    NaN  30.000000  11200.000000   7.400000
# std     NaN   3.807887   2588.435821   3.577709
# min     NaN  25.000000   8000.000000   3.000000
# 25%     NaN  28.000000  10000.000000   5.000000
# 50%     NaN  30.000000  11000.000000   8.000000
# 75%     NaN  32.000000  12000.000000   9.000000
# max     NaN  35.000000  15000.000000  12.000000

# 只看特定列
print("\n只看工资统计:")
print(df['工资'].describe())
# count        5.000000
# mean     11200.000000
# std       2588.435821
# min       8000.000000
# 25%      10000.000000
# 50%      11000.000000
# 75%      12000.000000
# max      15000.000000
# Name: 工资, dtype: float64
```

**describe()的统计指标**：
- `count`: 非空值数量
- `mean`: 平均值
- `std`: 标准差
- `min`: 最小值
- `25%`: 第一四分位数
- `50%`: 中位数
- `75%`: 第三四分位数
- `max`: 最大值

### 查看数据的其他方法

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '城市': ['北京', '上海', '广州', '深圳']
})

# 1. 直接打印（显示全部或部分数据）
print("直接打印:")
print(df)

# 2. sample() - 随机抽样
print("\n随机抽取2行:")
print(df.sample(n=2))

# 按比例抽样
print("\n随机抽取50%的数据:")
print(df.sample(frac=0.5))

# 3. 查看唯一值
print("\n城市的唯一值:")
print(df['城市'].unique())
# ['北京' '上海' '广州' '深圳']

print("唯一值数量:")
print(df['城市'].nunique())  # 4

# 4. 值计数
print("\n城市出现次数:")
print(df['城市'].value_counts())
# 北京    1
# 上海    1
# 广州    1
# 深圳    1
# Name: 城市, dtype: int64

# 5. 查看缺失值
df_with_nan = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, None, 8]
})

print("\n是否有缺失值:")
print(df_with_nan.isnull())
#        A      B
# 0  False  False
# 1  False   True
# 2   True   True
# 3  False  False

print("\n每列缺失值数量:")
print(df_with_nan.isnull().sum())
# A    1
# B    2
# dtype: int64
```

---

## 列操作

DataFrame最常见的操作就是对列进行操作。选择列、添加列、删除列、重命名列，这些是日常数据处理的基础。

### 选择列

选择列有多种方式，灵活掌握可以提高代码效率。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州'],
    '工资': [8000, 12000, 10000]
})

print("原始DataFrame:")
print(df)
print()

# 1. 选择单列（返回Series）
print("选择'姓名'列 (Series):")
name_series = df['姓名']
print(name_series)
print(type(name_series))  # <class 'pandas.core.series.Series'>
print()

# 2. 用属性方式选择（列名是有效的Python标识符时）
print("用属性方式选择:")
print(df.姓名)  # 等同于 df['姓名']
# 注意：列名不能有空格、不能以数字开头、不能是关键字
print()

# 3. 选择单列（返回DataFrame）
print("选择单列返回DataFrame:")
name_df = df[['姓名']]  # 注意双层方括号
print(name_df)
print(type(name_df))  # <class 'pandas.core.frame.DataFrame'>
print()

# 4. 选择多列（返回DataFrame）
print("选择多列:")
subset = df[['姓名', '工资']]
print(subset)
#   姓名   工资
# 0  张三   8000
# 1  李四  12000
# 2  王五  10000
print()

# 5. 调整列的顺序
print("调整列顺序:")
reordered = df[['工资', '姓名', '城市', '年龄']]
print(reordered)
print()

# 6. 选择部分列
print("选择前两列:")
first_two = df.iloc[:, :2]  # 所有行，前两列
print(first_two)
print()

# 7. 用loc选择列
print("用loc选择列:")
selected = df.loc[:, ['姓名', '年龄']]  # 所有行，指定列
print(selected)
```

**选择方式对比**：

| 方式 | 语法 | 返回类型 | 说明 |
|------|------|---------|------|
| `df['列名']` | `df['姓名']` | Series | 最常用 |
| `df.列名` | `df.姓名` | Series | 简洁，但有限制 |
| `df[['列名']]` | `df[['姓名']]` | DataFrame | 单列返回DataFrame |
| `df[['列1', '列2']]` | `df[['姓名', '年龄']]` | DataFrame | 多列选择 |
| `df.loc[:, '列名']` | `df.loc[:, '姓名']` | Series | 显式标签选择 |
| `df.iloc[:, 索引]` | `df.iloc[:, 0]` | Series | 按位置选择 |

### 添加列

DataFrame是可变的，可以随时添加新列。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

print("原始DataFrame:")
print(df)
print()

# 1. 直接赋值添加列
df['城市'] = ['北京', '上海', '广州']
print("添加'城市'列:")
print(df)
print()

# 2. 用标量值添加列（所有行都是同一个值）
df['国家'] = '中国'
print("添加'国家'列 (标量):")
print(df)
print()

# 3. 通过计算添加列
df['年薪'] = df['工资'] * 12
print("添加'年薪'列 (计算得出):")
print(df)
print()

# 4. 用函数添加列
df['工资等级'] = df['工资'].apply(lambda x: '高' if x > 10000 else '中等')
print("添加'工资等级'列:")
print(df)
print()

# 5. 用多列计算添加新列
df['月薪千元'] = df['工资'] / 1000
print("添加'月薪千元'列:")
print(df)
print()

# 6. 用insert()在指定位置插入列
df.insert(1, '性别', ['男', '女', '男'])  # 在位置1插入
print("在位置1插入'性别'列:")
print(df)
#   姓名 性别  年龄   工资  城市 国家    年薪 工资等级  月薪千元
# 0  张三  男  25   8000  北京  中国   96000   中等      8.0
# 1  李四  女  30  12000  上海  中国  144000    高     12.0
# 2  王五  男  28  10000  广州  中国  120000   中等     10.0
print()

# 7. 用assign()添加多列（返回新DataFrame，不修改原数据）
df_new = df.assign(
    奖金=df['工资'] * 0.1,
    总收入=lambda x: x['工资'] + x['工资'] * 0.1
)
print("用assign添加列 (返回新DataFrame):")
print(df_new)
```

**添加列的注意事项**：
- 新列的长度必须和DataFrame的行数一致（标量值除外）
- 列名可以是字符串、整数等不可变类型
- 建议用有意义的列名
- `insert()`会修改原DataFrame，`assign()`返回新DataFrame

### 删除列

删除不需要的列可以节省内存，让数据更清晰。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州'],
    '工资': [8000, 12000, 10000],
    '部门': ['技术', '销售', '技术']
})

print("原始DataFrame:")
print(df)
print()

# 1. drop()方法删除列（默认不修改原数据）
df_dropped = df.drop(columns=['部门'])
print("删除'部门'列 (返回新DataFrame):")
print(df_dropped)
print("原DataFrame不变:")
print(df)
print()

# 2. drop()方法删除列（inplace=True修改原数据）
df_copy = df.copy()
df_copy.drop(columns=['部门'], inplace=True)
print("删除'部门'列 (inplace=True):")
print(df_copy)
print()

# 3. 删除多列
df_multi_drop = df.drop(columns=['城市', '部门'])
print("删除多列:")
print(df_multi_drop)
print()

# 4. 用del删除列（直接修改原数据）
df_del = df.copy()
del df_del['部门']
print("用del删除列:")
print(df_del)
print()

# 5. pop()方法删除列并返回该列
df_pop = df.copy()
dept_series = df_pop.pop('部门')
print("pop()删除列并返回:")
print("返回的Series:")
print(dept_series)
print("删除后的DataFrame:")
print(df_pop)
print()

# 6. 用None选择要保留的列
df_keep = df[['姓名', '年龄', '工资']]  # 只选择需要的列
print("只选择需要的列:")
print(df_keep)
```

**删除方式对比**：

| 方式 | 修改原数据 | 返回值 | 说明 |
|------|-----------|--------|------|
| `drop(columns=)` | 否（默认） | 新DataFrame | 最常用，安全 |
| `drop(columns=, inplace=True)` | 是 | None | 直接修改原数据 |
| `del df['列名']` | 是 | None | 简单直接 |
| `df.pop('列名')` | 是 | Series | 删除并返回该列 |

### 重命名列

清晰的列名很重要，重命名列可以让数据更易理解。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'age': [25, 30, 28],
    'salary': [8000, 12000, 10000]
})

print("原始DataFrame:")
print(df)
print()

# 1. rename()方法重命名（不修改原数据）
df_renamed = df.rename(columns={
    'name': '姓名',
    'age': '年龄',
    'salary': '工资'
})
print("重命名列:")
print(df_renamed)
print("原DataFrame不变:")
print(df)
print()

# 2. rename()方法（inplace=True修改原数据）
df_copy = df.copy()
df_copy.rename(columns={
    'name': '姓名',
    'age': '年龄'
}, inplace=True)
print("重命名列 (inplace=True):")
print(df_copy)
print()

# 3. 直接修改columns属性
df_direct = df.copy()
df_direct.columns = ['姓名', '年龄', '工资']
print("直接修改columns:")
print(df_direct)
print()

# 4. 用函数批量重命名
df_func = df.copy()
df_func.rename(columns=str.upper, inplace=True)  # 转为大写
print("用函数重命名 (转大写):")
print(df_func)
print()

# 5. 用lambda重命名
df_lambda = df.copy()
df_lambda.rename(columns=lambda x: x + '_新', inplace=True)
print("用lambda重命名 (加后缀):")
print(df_lambda)
print()

# 6. 只重命名部分列
df_partial = df.copy()
df_partial.rename(columns={'name': '姓名'}, inplace=True)
print("只重命名部分列:")
print(df_partial)
```

**重命名技巧**：
- `rename(columns=字典)`: 精确控制重命名
- `rename(columns=函数)`: 批量处理列名
- 直接赋值`df.columns`: 必须提供所有列名
- 建议用`rename()`，更安全更灵活

### 列的排序

调整列的顺序可以让数据展示更合理。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '工资': [8000, 12000, 10000],
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
})

print("原始DataFrame:")
print(df)
print()

# 1. 手动指定列顺序
df_reordered = df[['姓名', '年龄', '城市', '工资']]
print("调整列顺序:")
print(df_reordered)
print()

# 2. 字母顺序排列列名
df_sorted = df[sorted(df.columns)]
print("按字母排序列名:")
print(df_sorted)
print()

# 3. 反转列顺序
df_reversed = df[df.columns[::-1]]
print("反转列顺序:")
print(df_reversed)
print()

# 4. 把某列移到最前面
cols = df.columns.tolist()
cols = ['姓名'] + [col for col in cols if col != '姓名']
df_name_first = df[cols]
print("把'姓名'移到最前:")
print(df_name_first)
```

---

## 行操作

除了列操作，DataFrame也支持丰富的行操作。增加行、删除行、修改行、查询行，这些操作在数据清洗和分析中非常重要。

### 选择行

选择行的方式有多种，可以按位置、按标签、按条件选择。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 28, 35, 32],
    '工资': [8000, 12000, 10000, 15000, 11000],
    '城市': ['北京', '上海', '广州', '深圳', '北京']
}, index=['a', 'b', 'c', 'd', 'e'])

print("原始DataFrame:")
print(df)
print()

# 1. 用iloc按位置选择（整数索引）
print("选择第1行 (iloc):")
print(df.iloc[0])  # 第一行，返回Series
# 姓名    张三
# 年龄    25
# 工资    8000
# 城市    北京
# Name: a, dtype: object
print()

print("选择第1到3行 (iloc):")
print(df.iloc[0:3])  # 切片：0, 1, 2行
print()

print("选择第1、3、5行 (iloc):")
print(df.iloc[[0, 2, 4]])  # 指定位置列表
print()

# 2. 用loc按标签选择
print("选择标签'a'的行 (loc):")
print(df.loc['a'])  # 返回Series
print()

print("选择标签'a'到'c'的行 (loc):")
print(df.loc['a':'c'])  # 注意：包含'c'
print()

print("选择多个标签的行 (loc):")
print(df.loc[['a', 'c', 'e']])
print()

# 3. 条件选择（布尔索引）
print("选择年龄大于30的行:")
print(df[df['年龄'] > 30])
#   姓名  年龄   工资  城市
# d  赵六  35  15000  深圳
# e  钱七  32  11000  北京
print()

print("选择工资在10000到12000之间的行:")
print(df[(df['工资'] >= 10000) & (df['工资'] <= 12000)])
# 注意：多条件用 & (且) 或 | (或)，每个条件要加括号
print()

print("选择城市是北京的行:")
print(df[df['城市'] == '北京'])
print()

print("选择城市是北京或上海的行:")
print(df[df['城市'].isin(['北京', '上海'])])
print()

# 4. query()方法（用字符串表达式）
print("用query选择:")
print(df.query('年龄 > 30'))
print()

print("用query的复杂条件:")
print(df.query('年龄 > 28 and 工资 < 15000'))
print()

# 5. head()和tail()
print("前3行:")
print(df.head(3))
print()

print("后2行:")
print(df.tail(2))
```

**行选择方式对比**：

| 方式 | 语法示例 | 说明 |
|------|---------|------|
| `iloc` | `df.iloc[0]` | 按整数位置选择 |
| `loc` | `df.loc['a']` | 按标签选择 |
| 布尔索引 | `df[df['年龄'] > 30]` | 按条件选择，最常用 |
| `query()` | `df.query('年龄 > 30')` | 字符串表达式，简洁 |

### 添加行

向DataFrame添加新行的方式有多种。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

print("原始DataFrame:")
print(df)
print()

# 1. concat()方法添加行（推荐）
new_row = pd.DataFrame({
    '姓名': ['赵六'],
    '年龄': [35],
    '工资': [15000]
})
df_concat = pd.concat([df, new_row], ignore_index=True)
print("用concat添加行:")
print(df_concat)
#   姓名  年龄   工资
# 0  张三  25   8000
# 1  李四  30  12000
# 2  王五  28  10000
# 3  赵六  35  15000
print()

# 2. loc添加行（用新的索引标签）
df_loc = df.copy()
df_loc.loc[3] = ['赵六', 35, 15000]
print("用loc添加行:")
print(df_loc)
print()

# 3. 添加多行
new_rows = pd.DataFrame({
    '姓名': ['赵六', '钱七'],
    '年龄': [35, 32],
    '工资': [15000, 11000]
})
df_multi = pd.concat([df, new_rows], ignore_index=True)
print("添加多行:")
print(df_multi)
print()

# 4. append()方法（已弃用，不推荐）
# df.append(new_row)  # 这个方法在新版本中已经被弃用
```

**添加行的注意事项**：
- 推荐用`pd.concat()`添加行
- 新行的列必须和原DataFrame匹配
- `ignore_index=True`会重置索引
- 添加行会创建新DataFrame，不修改原数据

### 删除行

删除不需要的行可以过滤数据。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 28, 35, 32],
    '工资': [8000, 12000, 10000, 15000, 11000]
}, index=['a', 'b', 'c', 'd', 'e'])

print("原始DataFrame:")
print(df)
print()

# 1. drop()按标签删除行
df_drop = df.drop('a')  # 删除标签为'a'的行
print("删除标签'a'的行:")
print(df_drop)
print()

# 2. drop()删除多行
df_multi_drop = df.drop(['a', 'c', 'e'])
print("删除多行:")
print(df_multi_drop)
print()

# 3. drop()按位置删除（用索引）
df_drop_pos = df.drop(df.index[0])  # 删除第一行
print("删除第一行:")
print(df_drop_pos)
print()

# 4. 条件删除（用布尔索引的反向）
df_cond = df[df['年龄'] <= 30]  # 保留年龄<=30的行
print("保留年龄<=30的行 (等于删除年龄>30的行):")
print(df_cond)
print()

# 5. 删除重复行
df_dup = pd.DataFrame({
    '姓名': ['张三', '李四', '张三'],
    '年龄': [25, 30, 25]
})
print("有重复的DataFrame:")
print(df_dup)
print()

df_no_dup = df_dup.drop_duplicates()
print("删除重复行:")
print(df_no_dup)
#   姓名  年龄
# 0  张三  25
# 1  李四  30
print()

# 6. 按特定列删除重复
df_dup2 = pd.DataFrame({
    '姓名': ['张三', '李四', '张三'],
    '年龄': [25, 30, 28]  # 年龄不同
})
df_no_dup2 = df_dup2.drop_duplicates(subset=['姓名'])
print("按'姓名'列删除重复:")
print(df_no_dup2)
#   姓名  年龄
# 0  张三  25  <- 保留第一个张三
# 1  李四  30
```

### 修改行

修改行中的值是常见操作。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '工资': [8000, 12000, 10000]
})

print("原始DataFrame:")
print(df)
print()

# 1. 用loc修改单个值
df.loc[0, '年龄'] = 26
print("修改第一行的年龄:")
print(df)
print()

# 2. 修改整行
df.loc[1] = ['李四四', 31, 13000]
print("修改第二行:")
print(df)
print()

# 3. 修改多行的某列
df.loc[0:1, '工资'] = [8500, 13500]
print("修改前两行的工资:")
print(df)
print()

# 4. 条件修改
df_cond = df.copy()
df_cond.loc[df_cond['年龄'] > 28, '工资'] = df_cond['工资'] * 1.1
print("给年龄>28的人涨薪10%:")
print(df_cond)
print()

# 5. 用iloc按位置修改
df.iloc[2, 1] = 29  # 第3行第2列
print("用iloc修改值:")
print(df)
print()

# 6. 批量修改
df['工资'] = df['工资'] + 1000  # 所有人涨薪1000
print("所有人涨薪1000:")
print(df)
```

### 行的排序

按某列或多列对行进行排序。

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '工资': [12000, 8000, 10000, 15000],
    '城市': ['北京', '上海', '广州', '北京']
})

print("原始DataFrame:")
print(df)
print()

# 1. 按单列排序
df_sorted = df.sort_values('年龄')
print("按年龄升序排序:")
print(df_sorted)
#   姓名  年龄   工资  城市
# 0  张三  25  12000  北京
# 2  王五  28  10000  广州
# 1  李四  30   8000  上海
# 3  赵六  35  15000  北京
print()

# 2. 降序排序
df_desc = df.sort_values('工资', ascending=False)
print("按工资降序排序:")
print(df_desc)
#   姓名  年龄   工资  城市
# 3  赵六  35  15000  北京
# 0  张三  25  12000  北京
# 2  王五  28  10000  广州
# 1  李四  30   8000  上海
print()

# 3. 按多列排序
df_multi = df.sort_values(['城市', '年龄'])
print("先按城市，再按年龄排序:")
print(df_multi)
#   姓名  年龄   工资  城市
# 2  王五  28  10000  广州
# 0  张三  25  12000  北京
# 3  赵六  35  15000  北京
# 1  李四  30   8000  上海
print()

# 4. 不同列不同排序方向
df_mixed = df.sort_values(
    ['城市', '工资'],
    ascending=[True, False]  # 城市升序，工资降序
)
print("城市升序，工资降序:")
print(df_mixed)
print()

# 5. 重置索引
df_reset = df.sort_values('年龄').reset_index(drop=True)
print("排序后重置索引:")
print(df_reset)
#   姓名  年龄   工资  城市
# 0  张三  25  12000  北京
# 1  王五  28  10000  广州
# 2  李四  30   8000  上海
# 3  赵六  35  15000  北京
```

---

## DataFrame与Excel对比

很多人最熟悉的表格工具是Excel，理解DataFrame和Excel的异同可以帮助快速上手Pandas。

### 相似之处

DataFrame和Excel有很多相似的概念：

| Excel | DataFrame | 说明 |
|-------|-----------|------|
| 工作表 | DataFrame | 一张表格 |
| 行号 (1, 2, 3...) | 行索引 (0, 1, 2...) | 标识行 |
| 列名 (A, B, C...) | 列名 | 标识列 |
| 单元格 | 元素 | 一个数据值 |
| 筛选 | 布尔索引 | 按条件选择 |
| 排序 | sort_values() | 排序数据 |
| 公式 | 向量化运算 | 批量计算 |
| 数据透视表 | pivot_table() | 数据汇总 |

### 主要区别

```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 28, 35],
    '工资': [8000, 12000, 10000, 15000]
})

print("1. DataFrame支持向量化运算（比Excel快得多）")
# Excel: 需要写公式，拖拽单元格
# DataFrame: 一行代码完成
df['年薪'] = df['工资'] * 12  # 所有行同时计算
print(df)
print()

print("2. DataFrame可以轻松处理大数据")
# Excel: 最多104万行，数据多了会卡
# DataFrame: 可以处理数百万、千万行数据
large_df = pd.DataFrame({
    'A': np.random.randn(1000000)  # 100万行
})
print(f"轻松创建{len(large_df)}行数据")
print()

print("3. DataFrame支持链式操作")
# Excel: 需要分步操作
# DataFrame: 可以连续操作
result = (df[df['年龄'] > 28]        # 筛选
           .sort_values('工资')      # 排序
           .head(2))                # 取前2行
print("链式操作结果:")
print(result)
print()

print("4. DataFrame更容易自动化")
# Excel: 需要VBA宏
# DataFrame: Python代码直接运行
for i in range(3):
    df_temp = pd.DataFrame({
        '日期': [f'2024-01-0{i+1}'],
        '销售': [np.random.randint(1000, 5000)]
    })
    print(df_temp)
print()

print("5. DataFrame支持更复杂的数据类型")
df_complex = pd.DataFrame({
    '日期': pd.date_range('2024-01-01', periods=3),
    '时间差': pd.to_timedelta(['1 days', '2 days', '3 days']),
    '分类': pd.Categorical(['A', 'B', 'A'])
})
print(df_complex)
print(df_complex.dtypes)
```

### 常见操作对比

让我们看看同样的操作在Excel和DataFrame中如何实现：

```python
import pandas as pd

# 示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '部门': ['销售', '技术', '销售', '技术', '销售'],
    '年龄': [25, 30, 28, 35, 32],
    '工资': [8000, 12000, 10000, 15000, 11000]
})

print("原始数据:")
print(df)
print("\n" + "="*50 + "\n")

# 操作1: 筛选工资大于10000的记录
print("【筛选】工资大于10000的记录")
print("\nExcel操作:")
print("  1. 选中数据区域")
print("  2. 点击'数据' -> '筛选'")
print("  3. 在'工资'列下拉框中设置条件")
print("\nDataFrame操作:")
print("  df[df['工资'] > 10000]")
print("\n结果:")
print(df[df['工资'] > 10000])
print("\n" + "="*50 + "\n")

# 操作2: 计算平均工资
print("【统计】计算平均工资")
print("\nExcel操作:")
print("  =AVERAGE(D2:D6)")
print("\nDataFrame操作:")
print("  df['工资'].mean()")
print(f"\n结果: {df['工资'].mean()}")
print("\n" + "="*50 + "\n")

# 操作3: 按部门分组统计
print("【分组】按部门统计平均工资")
print("\nExcel操作:")
print("  1. 插入数据透视表")
print("  2. 拖拽'部门'到行")
print("  3. 拖拽'工资'到值，选择平均值")
print("\nDataFrame操作:")
print("  df.groupby('部门')['工资'].mean()")
print("\n结果:")
print(df.groupby('部门')['工资'].mean())
print("\n" + "="*50 + "\n")

# 操作4: 添加新列
print("【计算】添加'年薪'列")
print("\nExcel操作:")
print("  1. 在E列输入 =D2*12")
print("  2. 下拉复制公式")
print("\nDataFrame操作:")
print("  df['年薪'] = df['工资'] * 12")
df['年薪'] = df['工资'] * 12
print("\n结果:")
print(df)
print("\n" + "="*50 + "\n")

# 操作5: 排序
print("【排序】按年龄降序排序")
print("\nExcel操作:")
print("  1. 选中数据")
print("  2. 点击'数据' -> '排序'")
print("  3. 选择'年龄'列，降序")
print("\nDataFrame操作:")
print("  df.sort_values('年龄', ascending=False)")
print("\n结果:")
print(df.sort_values('年龄', ascending=False))
```

### 何时用Excel，何时用DataFrame？

**用Excel的场景**：
- 数据量小（几千行以内）
- 需要手动录入和修改数据
- 需要图形化界面操作
- 简单的一次性分析
- 需要和非技术人员协作

**用DataFrame的场景**：
- 数据量大（数万行以上）
- 需要自动化、批量处理
- 需要复杂的数据清洗和转换
- 需要重复执行的分析流程
- 数据来源多样（数据库、API、文件等）
- 需要版本控制和团队协作

---

## 实战案例

让我们通过几个实际案例来综合运用DataFrame的知识。

### 案例1：员工数据分析

```python
import pandas as pd
import numpy as np

# 创建员工数据
np.random.seed(42)
employees = pd.DataFrame({
    '员工ID': range(1001, 1021),
    '姓名': [f'员工{i}' for i in range(1, 21)],
    '部门': np.random.choice(['销售', '技术', '市场', '人事'], 20),
    '性别': np.random.choice(['男', '女'], 20),
    '年龄': np.random.randint(22, 45, 20),
    '入职年份': np.random.randint(2015, 2024, 20),
    '基本工资': np.random.randint(6000, 20000, 20),
    '绩效等级': np.random.choice(['A', 'B', 'C'], 20)
})

print("原始员工数据:")
print(employees.head())
print()

# 1. 计算工作年限
employees['工作年限'] = 2024 - employees['入职年份']
print("添加工作年限:")
print(employees[['姓名', '入职年份', '工作年限']].head())
print()

# 2. 根据绩效计算奖金
bonus_map = {'A': 0.2, 'B': 0.1, 'C': 0.05}
employees['奖金'] = employees.apply(
    lambda row: row['基本工资'] * bonus_map[row['绩效等级']],
    axis=1
)
print("添加奖金:")
print(employees[['姓名', '基本工资', '绩效等级', '奖金']].head())
print()

# 3. 计算总收入
employees['总收入'] = employees['基本工资'] + employees['奖金']
print("添加总收入:")
print(employees[['姓名', '基本工资', '奖金', '总收入']].head())
print()

# 4. 按部门统计
print("部门统计:")
dept_stats = employees.groupby('部门').agg({
    '员工ID': 'count',
    '年龄': 'mean',
    '基本工资': 'mean',
    '总收入': 'sum'
}).round(2)
dept_stats.columns = ['人数', '平均年龄', '平均工资', '总支出']
print(dept_stats)
print()

# 5. 筛选高薪员工
high_salary = employees[employees['总收入'] > 15000].sort_values('总收入', ascending=False)
print("总收入超过15000的员工:")
print(high_salary[['姓名', '部门', '总收入']])
print()

# 6. 性别和部门交叉统计
print("性别-部门交叉统计:")
cross_tab = pd.crosstab(employees['部门'], employees['性别'])
print(cross_tab)
```

### 案例2：销售数据分析

```python
import pandas as pd
import numpy as np

# 创建销售数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')
sales = pd.DataFrame({
    '日期': dates,
    '产品': np.random.choice(['产品A', '产品B', '产品C'], len(dates)),
    '销售额': np.random.randint(1000, 10000, len(dates)),
    '成本': np.random.randint(500, 5000, len(dates)),
    '销售人员': np.random.choice(['张三', '李四', '王五'], len(dates))
})

print("销售数据样本:")
print(sales.head())
print()

# 1. 添加计算列
sales['利润'] = sales['销售额'] - sales['成本']
sales['利润率'] = (sales['利润'] / sales['销售额'] * 100).round(2)
sales['月份'] = sales['日期'].dt.month
sales['星期'] = sales['日期'].dt.day_name()

print("添加计算列后:")
print(sales.head())
print()

# 2. 月度销售统计
print("月度销售统计:")
monthly = sales.groupby('月份').agg({
    '销售额': 'sum',
    '成本': 'sum',
    '利润': 'sum'
})
monthly['利润率%'] = (monthly['利润'] / monthly['销售额'] * 100).round(2)
print(monthly)
print()

# 3. 产品销售排名
print("产品销售排名:")
product_sales = sales.groupby('产品').agg({
    '销售额': 'sum',
    '利润': 'sum'
}).sort_values('销售额', ascending=False)
print(product_sales)
print()

# 4. 销售人员绩效
print("销售人员绩效:")
staff_performance = sales.groupby('销售人员').agg({
    '销售额': ['sum', 'mean'],
    '利润': 'sum',
    '日期': 'count'
})
staff_performance.columns = ['总销售额', '平均销售额', '总利润', '成交次数']
print(staff_performance.sort_values('总销售额', ascending=False))
print()

# 5. 最佳销售日
print("Top 5 销售日:")
top_days = sales.nlargest(5, '销售额')[['日期', '产品', '销售额', '销售人员']]
print(top_days)
```

### 案例3：学生成绩分析

```python
import pandas as pd
import numpy as np

# 创建学生成绩数据
np.random.seed(42)
students = pd.DataFrame({
    '学号': [f'S{i:04d}' for i in range(1, 51)],
    '姓名': [f'学生{i}' for i in range(1, 51)],
    '班级': np.random.choice(['1班', '2班', '3班'], 50),
    '语文': np.random.randint(60, 100, 50),
    '数学': np.random.randint(50, 100, 50),
    '英语': np.random.randint(55, 100, 50),
    '物理': np.random.randint(50, 100, 50),
    '化学': np.random.randint(55, 100, 50)
})

print("学生成绩数据:")
print(students.head())
print()

# 1. 计算总分和平均分
subject_cols = ['语文', '数学', '英语', '物理', '化学']
students['总分'] = students[subject_cols].sum(axis=1)
students['平均分'] = students[subject_cols].mean(axis=1).round(2)

print("添加总分和平均分:")
print(students[['姓名', '总分', '平均分']].head())
print()

# 2. 计算排名
students['排名'] = students['总分'].rank(ascending=False, method='min').astype(int)
print("Top 10 学生:")
print(students.nsmallest(10, '排名')[['排名', '姓名', '班级', '总分', '平均分']])
print()

# 3. 各科成绩统计
print("各科成绩统计:")
subject_stats = students[subject_cols].describe().T
subject_stats['及格率%'] = (students[subject_cols] >= 60).sum() / len(students) * 100
subject_stats['及格率%'] = subject_stats['及格率%'].round(2)
print(subject_stats[['mean', 'min', 'max', '及格率%']])
print()

# 4. 班级平均分
print("班级平均分:")
class_avg = students.groupby('班级')[subject_cols + ['总分', '平均分']].mean().round(2)
print(class_avg)
print()

# 5. 找出偏科学生（最高分和最低分相差超过30）
students['分数极差'] = students[subject_cols].max(axis=1) - students[subject_cols].min(axis=1)
biased_students = students[students['分数极差'] > 30].sort_values('分数极差', ascending=False)
print("偏科学生（科目分数极差>30）:")
print(biased_students[['姓名', '班级'] + subject_cols + ['分数极差']].head(10))
print()

# 6. 优秀学生（总分前20%）
threshold = students['总分'].quantile(0.8)
excellent = students[students['总分'] >= threshold].sort_values('总分', ascending=False)
print(f"优秀学生（总分>={threshold:.0f}）:")
print(excellent[['姓名', '班级', '总分', '平均分']])
```

---

## 练习题

通过练习巩固所学知识。每道题都提供了完整的解答。

### 练习1：创建和查看DataFrame

**题目**：
创建一个包含5个人信息的DataFrame，包括姓名、年龄、城市、职业、月薪。然后：
1. 查看前3行数据
2. 查看DataFrame的基本信息
3. 查看数值列的统计信息
4. 查看所有列名和数据类型

**解答**：

```python
import pandas as pd

# 创建DataFrame
people = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 28, 35, 32],
    '城市': ['北京', '上海', '广州', '深圳', '杭州'],
    '职业': ['工程师', '设计师', '产品经理', '数据分析师', '运营'],
    '月薪': [15000, 12000, 18000, 20000, 14000]
})

# 1. 查看前3行
print("前3行数据:")
print(people.head(3))
print()

# 2. 查看基本信息
print("DataFrame基本信息:")
people.info()
print()

# 3. 查看数值列统计
print("数值列统计:")
print(people.describe())
print()

# 4. 查看列名和数据类型
print("列名:")
print(people.columns.tolist())
print("\n数据类型:")
print(people.dtypes)
```

### 练习2：列操作

**题目**：
基于练习1的DataFrame，完成以下操作：
1. 添加一列"年薪"（月薪×12）
2. 添加一列"工资等级"（月薪>=18000为"高"，>=15000为"中"，否则为"低"）
3. 删除"职业"列
4. 重命名"月薪"为"monthly_salary"
5. 调整列顺序为：姓名、年龄、城市、年薪、工资等级、monthly_salary

**解答**：

```python
import pandas as pd

# 创建DataFrame
people = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 28, 35, 32],
    '城市': ['北京', '上海', '广州', '深圳', '杭州'],
    '职业': ['工程师', '设计师', '产品经理', '数据分析师', '运营'],
    '月薪': [15000, 12000, 18000, 20000, 14000]
})

print("原始DataFrame:")
print(people)
print()

# 1. 添加年薪列
people['年薪'] = people['月薪'] * 12
print("添加年薪列:")
print(people)
print()

# 2. 添加工资等级列
def salary_level(salary):
    if salary >= 18000:
        return '高'
    elif salary >= 15000:
        return '中'
    else:
        return '低'

people['工资等级'] = people['月薪'].apply(salary_level)
print("添加工资等级列:")
print(people)
print()

# 3. 删除职业列
people = people.drop(columns=['职业'])
print("删除职业列:")
print(people)
print()

# 4. 重命名月薪列
people = people.rename(columns={'月薪': 'monthly_salary'})
print("重命名月薪列:")
print(people)
print()

# 5. 调整列顺序
people = people[['姓名', '年龄', '城市', '年薪', '工资等级', 'monthly_salary']]
print("调整列顺序:")
print(people)
```

### 练习3：行操作和筛选

**题目**：
创建一个商品销售DataFrame，包含商品名称、类别、单价、库存、销量。然后：
1. 添加一行新商品
2. 删除库存为0的商品
3. 筛选出销量大于100的商品
4. 按销售额（单价×销量）降序排序
5. 找出每个类别中销售额最高的商品

**解答**：

```python
import pandas as pd

# 创建商品数据
products = pd.DataFrame({
    '商品名称': ['手机', '电脑', '平板', '耳机', '键盘'],
    '类别': ['电子产品', '电子产品', '电子产品', '配件', '配件'],
    '单价': [2999, 5999, 1999, 299, 199],
    '库存': [50, 30, 0, 100, 80],
    '销量': [150, 80, 50, 200, 120]
})

print("原始商品数据:")
print(products)
print()

# 1. 添加一行新商品
new_product = pd.DataFrame({
    '商品名称': ['鼠标'],
    '类别': ['配件'],
    '单价': [99],
    '库存': [150],
    '销量': [180]
})
products = pd.concat([products, new_product], ignore_index=True)
print("添加新商品后:")
print(products)
print()

# 2. 删除库存为0的商品
products = products[products['库存'] > 0]
print("删除库存为0的商品:")
print(products)
print()

# 3. 筛选销量大于100的商品
high_sales = products[products['销量'] > 100]
print("销量大于100的商品:")
print(high_sales)
print()

# 4. 按销售额降序排序
products['销售额'] = products['单价'] * products['销量']
products_sorted = products.sort_values('销售额', ascending=False)
print("按销售额降序排序:")
print(products_sorted)
print()

# 5. 每个类别销售额最高的商品
top_by_category = products.loc[products.groupby('类别')['销售额'].idxmax()]
print("每个类别销售额最高的商品:")
print(top_by_category[['类别', '商品名称', '销售额']])
```

### 练习4：数据分析综合

**题目**：
创建一个月度销售数据DataFrame，包含日期、产品、销售额、成本。然后分析：
1. 总销售额和总利润
2. 平均每天的销售额
3. 销售额最高和最低的日期
4. 每个产品的总销售额和平均利润率
5. 哪个产品的利润最高

**解答**：

```python
import pandas as pd
import numpy as np

# 创建月度销售数据
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-01-31', freq='D')
n_records = len(dates) * 3  # 每天3条记录

sales_data = pd.DataFrame({
    '日期': np.repeat(dates, 3),
    '产品': np.tile(['产品A', '产品B', '产品C'], len(dates)),
    '销售额': np.random.randint(1000, 5000, n_records),
    '成本': np.random.randint(500, 3000, n_records)
})

print("销售数据样本:")
print(sales_data.head(10))
print(f"\n总记录数: {len(sales_data)}")
print()

# 计算利润
sales_data['利润'] = sales_data['销售额'] - sales_data['成本']
sales_data['利润率'] = (sales_data['利润'] / sales_data['销售额'] * 100).round(2)

# 1. 总销售额和总利润
total_sales = sales_data['销售额'].sum()
total_profit = sales_data['利润'].sum()
print(f"1. 总销售额: {total_sales:,} 元")
print(f"   总利润: {total_profit:,} 元")
print(f"   总利润率: {(total_profit/total_sales*100):.2f}%")
print()

# 2. 平均每天的销售额
daily_sales = sales_data.groupby('日期')['销售额'].sum()
avg_daily_sales = daily_sales.mean()
print(f"2. 平均每天销售额: {avg_daily_sales:,.2f} 元")
print()

# 3. 销售额最高和最低的日期
max_sales_date = daily_sales.idxmax()
min_sales_date = daily_sales.idxmin()
print(f"3. 销售额最高的日期: {max_sales_date.date()} ({daily_sales.max():,} 元)")
print(f"   销售额最低的日期: {min_sales_date.date()} ({daily_sales.min():,} 元)")
print()

# 4. 每个产品的总销售额和平均利润率
product_analysis = sales_data.groupby('产品').agg({
    '销售额': 'sum',
    '利润': 'sum',
    '利润率': 'mean'
}).round(2)
product_analysis.columns = ['总销售额', '总利润', '平均利润率%']
print("4. 各产品分析:")
print(product_analysis)
print()

# 5. 利润最高的产品
max_profit_product = product_analysis['总利润'].idxmax()
max_profit_value = product_analysis['总利润'].max()
print(f"5. 利润最高的产品: {max_profit_product} (利润: {max_profit_value:,} 元)")
```

### 练习5：数据清洗和转换

**题目**：
创建一个包含缺失值和异常值的学生数据，然后进行清洗：
1. 检查并显示缺失值情况
2. 填充缺失的年龄（用平均值）
3. 填充缺失的班级（用"未分配"）
4. 删除成绩为负数的异常数据
5. 将性别统一为"男"/"女"（处理"M"/"F"等不规范数据）
6. 显示清洗后的数据

**解答**：

```python
import pandas as pd
import numpy as np

# 创建包含问题的数据
students = pd.DataFrame({
    '学号': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007'],
    '姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九'],
    '性别': ['男', 'F', '女', 'M', '男', '女', None],
    '年龄': [20, 21, None, 22, None, 23, 20],
    '班级': ['1班', '2班', None, '1班', '2班', None, '3班'],
    '成绩': [85, 92, 78, -5, 88, 95, 82]  # -5是异常值
})

print("原始数据（包含问题）:")
print(students)
print()

# 1. 检查缺失值
print("1. 缺失值情况:")
print(students.isnull().sum())
print()

# 2. 填充缺失的年龄（用平均值）
mean_age = students['年龄'].mean()
students['年龄'] = students['年龄'].fillna(mean_age)
print(f"2. 填充年龄缺失值（平均值: {mean_age:.1f}）:")
print(students[['姓名', '年龄']])
print()

# 3. 填充缺失的班级
students['班级'] = students['班级'].fillna('未分配')
print("3. 填充班级缺失值:")
print(students[['姓名', '班级']])
print()

# 4. 删除成绩异常的数据
print(f"4. 删除前记录数: {len(students)}")
students = students[students['成绩'] >= 0]
print(f"   删除成绩异常数据后记录数: {len(students)}")
print()

# 5. 统一性别格式
gender_map = {'M': '男', 'F': '女', 'Male': '男', 'Female': '女'}
students['性别'] = students['性别'].replace(gender_map)
students['性别'] = students['性别'].fillna('未知')
print("5. 统一性别格式:")
print(students[['姓名', '性别']])
print()

# 6. 显示清洗后的完整数据
print("6. 清洗后的完整数据:")
print(students)
print()

# 验证清洗效果
print("清洗效果验证:")
print(f"  - 缺失值总数: {students.isnull().sum().sum()}")
print(f"  - 异常成绩数: {(students['成绩'] < 0).sum()}")
print(f"  - 数据记录数: {len(students)}")
```

---

## 总结

在这一章，我们系统学习了DataFrame——Pandas中最重要的数据结构。

### 核心要点

1. **DataFrame是什么**
   - 二维表格结构，类似Excel
   - 由行索引、列索引和数据组成
   - 是多个Series的集合

2. **DataFrame的创建**
   - 从字典、列表、NumPy数组创建
   - 从CSV、Excel文件读取
   - 创建空DataFrame

3. **DataFrame的属性**
   - shape, size, ndim：形状和维度
   - columns, index：列索引和行索引
   - dtypes：数据类型
   - values：数据部分（NumPy数组）

4. **查看DataFrame**
   - head(), tail()：查看头尾数据
   - info()：概览信息
   - describe()：统计信息

5. **列操作**
   - 选择：df['列名'] 或 df[['列1', '列2']]
   - 添加：df['新列'] = 数据
   - 删除：df.drop(columns=['列名'])
   - 重命名：df.rename(columns={'旧名': '新名'})

6. **行操作**
   - 选择：iloc（位置），loc（标签），布尔索引
   - 添加：pd.concat()
   - 删除：df.drop()
   - 排序：sort_values()

7. **DataFrame vs Excel**
   - 相似：都是表格结构
   - 不同：DataFrame更强大、更快、更适合大数据和自动化

### 关键技能

完成本章学习，你应该能够：
- ✅ 理解DataFrame的结构和原理
- ✅ 用多种方式创建DataFrame
- ✅ 查看和理解DataFrame的基本信息
- ✅ 熟练进行列的增删改查
- ✅ 熟练进行行的增删改查
- ✅ 用布尔索引筛选数据
- ✅ 对数据进行排序和统计
- ✅ 完成基本的数据分析任务

### 学习建议

1. **多练习**：DataFrame的操作需要大量练习才能熟练
2. **理解原理**：明白DataFrame是Series的集合很重要
3. **对比Excel**：用Excel类比帮助理解
4. **实际应用**：用真实数据练习
5. **查阅文档**：遇到问题查看官方文档

### 下一步

学完DataFrame基础后，建议继续学习：
- 数据选择和索引（loc, iloc, at, iat的详细用法）
- 数据清洗（处理缺失值、重复值、异常值）
- 数据合并（merge, join, concat）
- 数据分组和聚合（groupby）
- 数据透视表（pivot_table）

DataFrame是数据分析的核心工具，掌握它之后，你就能处理各种实际的数据分析任务了！

---

## 参考资源

- [Pandas官方文档 - DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [Pandas用户指南](https://pandas.pydata.org/docs/user_guide/index.html)
- [10分钟入门Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

---

**下一章预告**：[第04章 - 数据选择和索引 →](../04-数据选择和索引/04-数据选择和索引.md)

在下一章，我们将深入学习loc、iloc、at、iat等数据选择方法，掌握Pandas中最强大的数据索引技术！
