# 第02章：Series数据结构

在上一章，我们初步认识了Pandas这个强大的数据分析库。这一章，我们要深入学习Pandas的第一个核心数据结构——Series。

Series是Pandas最基础的数据结构，可以理解为"带标签的一维数组"。掌握Series是学习Pandas的第一步，也是理解DataFrame的基础。

学完这一章，你会明白为什么Series比普通的Python列表和NumPy数组更适合数据分析工作。

---

## 什么是Series？

### 生活化理解

想象一下你在记录班级学生的成绩。用Python列表的话，你会这样记录：

```python
# Python列表
scores = [85, 92, 78, 95, 88]
```

这样记录有个问题：你只知道成绩是85、92、78...，但不知道这些成绩分别是谁的！

如果用字典，你可以这样：

```python
# Python字典
scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 95,
    "孙七": 88
}
```

这样好多了！但字典不支持NumPy那样的快速向量化运算，处理大量数据时效率不高。

**Series就是两者的完美结合**：
- 像字典一样，有标签（学生姓名）
- 像NumPy数组一样，支持快速的向量化运算
- 还有很多方便的数据分析方法

```python
import pandas as pd

# Pandas Series：既有标签，又能快速计算
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

print(scores)
```

输出：
```
张三    85
李四    92
王五    78
赵六    95
孙七    88
dtype: int64
```

看到了吗？每个成绩都有对应的学生姓名，这就是Series的魅力！

### 技术定义

Series是Pandas的一维数据结构，它具有以下特点：

1. **带标签的数组**：每个元素都有一个索引标签
2. **同质化数据**：所有元素类型相同（和NumPy数组一样）
3. **向量化运算**：支持快速的数学运算
4. **灵活索引**：既可以用位置索引，也可以用标签索引
5. **丰富的方法**：内置大量数据分析方法

### Series的组成部分

一个Series由三部分组成：

```python
import pandas as pd
import numpy as np

# 创建一个Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s)
print("\n数据值（values）:", s.values)
print("索引（index）:", s.index)
print("数据类型（dtype）:", s.dtype)
```

输出：
```
a    10
b    20
c    30
d    40
dtype: int64

数据值（values）: [10 20 30 40]
索引（index）: Index(['a', 'b', 'c', 'd'], dtype='object')
数据类型（dtype）: int64
```

**三个核心组成部分**：

1. **values（值）**：实际的数据，是一个NumPy数组
2. **index（索引）**：每个值对应的标签
3. **dtype（数据类型）**：数据的类型（整数、浮点数、字符串等）

---

## 为什么要用Series？

很多初学者会问：既然Python已经有列表和字典，NumPy已经有数组，为什么还要学Series？

让我们从多个角度对比一下：

### Series vs Python列表

```python
import pandas as pd

# Python列表
py_list = [85, 92, 78, 95, 88]

# 问题1：没有标签，不知道数据的含义
print(py_list[0])  # 85，但这是谁的成绩？

# 问题2：不支持向量化运算
# py_list + 10  # 这样会报错！
result = [x + 10 for x in py_list]  # 必须用循环

# Pandas Series
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 优势1：有标签，数据含义清晰
print(scores["张三"])  # 85，知道是张三的成绩

# 优势2：支持向量化运算，简洁高效
result = scores + 10  # 所有成绩加10分，一行即可完成。
print(result)
```

### Series vs Python字典

```python
import pandas as pd

# Python字典
py_dict = {"张三": 85, "李四": 92, "王五": 78}

# 问题1：不支持向量化运算
# py_dict + 10  # 报错！

# 问题2：没有方便的数据分析方法
# 要计算平均分，需要手动处理
average = sum(py_dict.values()) / len(py_dict)

# Pandas Series
scores = pd.Series({"张三": 85, "李四": 92, "王五": 78})

# 优势1：支持向量化运算
result = scores + 10

# 优势2：丰富的数据分析方法
print(scores.mean())  # 平均分
print(scores.max())   # 最高分
print(scores.min())   # 最低分
print(scores.describe())  # 完整的统计信息
```

### Series vs NumPy数组

```python
import pandas as pd
import numpy as np

# NumPy数组
np_array = np.array([85, 92, 78, 95, 88])

# 问题1：没有标签
print(np_array[0])  # 85，但不知道是谁的

# 问题2：索引只能用数字位置
# 不能通过姓名访问数据

# Pandas Series
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 优势1：有标签
print(scores["张三"])  # 可以用姓名访问

# 优势2：既能用标签，也能用位置
print(scores["张三"])  # 用标签
print(scores[0])      # 用位置（和NumPy一样）

# 优势3：更多数据分析功能
print(scores.describe())  # NumPy数组没有这个方法
```

### 对比总结表

| 特性 | Python列表 | Python字典 | NumPy数组 | Pandas Series |
|------|-----------|-----------|----------|--------------|
| **有标签** | | | | |
| **向量化运算** | | | | |
| **快速计算** | | | | |
| **位置索引** | | | | |
| **标签索引** | | | | |
| **数据分析方法** | | | 部分 | |
| **处理缺失值** | | | 部分 | |
| **适用场景** | 通用存储 | 键值映射 | 科学计算 | 数据分析 |

**结论**：Series集合了列表、字典、NumPy数组的优点，是专为数据分析设计的数据结构！

---

## 创建Series

创建Series有很多种方法，每种方法适用于不同的场景。让我们从简单到复杂，逐一学习。

---

### 从列表创建

最简单的方式就是从Python列表创建Series。

```python
import pandas as pd

# 创建最简单的Series（自动生成索引0, 1, 2...）
s = pd.Series([10, 20, 30, 40, 50])
print(s)
```

输出：
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

**注意**：如果不指定索引，Pandas会自动创建从0开始的整数索引。

```python
# 创建Series并指定索引
s = pd.Series([10, 20, 30, 40, 50],
              index=['a', 'b', 'c', 'd', 'e'])
print(s)
```

输出：
```
a    10
b    20
c    30
d    40
e    50
dtype: int64
```

**实际应用示例**：

```python
# 记录一周的气温
temperatures = pd.Series(
    [22.5, 24.1, 23.8, 25.3, 26.0, 24.7, 23.2],
    index=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
)
print(temperatures)
print("\n周三的气温:", temperatures['周三'])
print("平均气温:", temperatures.mean())
```

**注意事项**：
- 索引的长度必须和数据的长度一致
- 索引可以重复（虽然不推荐）
- 索引可以是任何不可变类型（字符串、数字、元组等）

```python
# 错误示例：索引长度不匹配
# s = pd.Series([1, 2, 3], index=['a', 'b'])  # ValueError!

# 索引可以重复（但会导致混淆）
s = pd.Series([1, 2, 3], index=['a', 'a', 'b'])
print(s['a'])  # 返回多个值
```

---

### 从字典创建

从字典创建Series非常直观，字典的键会自动成为索引，值成为数据。

```python
import pandas as pd

# 从字典创建
data = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 95,
    "孙七": 88
}

scores = pd.Series(data)
print(scores)
```

输出：
```
张三    85
李四    92
王五    78
赵六    95
孙七    88
dtype: int64
```

**为什么从字典创建很常用？**

1. 字典本身就是键值对，和Series的索引-值结构天然匹配
2. 代码可读性强，一眼就能看出数据的含义
3. 适合表示有意义的数据（如人名-成绩、城市-人口等）

```python
# 更多示例

# 城市人口（单位：万人）
population = pd.Series({
    "北京": 2189,
    "上海": 2428,
    "广州": 1868,
    "深圳": 1756
})

# 产品价格
prices = pd.Series({
    "苹果": 5.5,
    "香蕉": 3.2,
    "橙子": 4.8,
    "葡萄": 8.9
})

# 学生信息
info = pd.Series({
    "姓名": "张三",
    "年龄": 18,
    "性别": "男",
    "班级": "高三(1)班"
})

print("城市人口：\n", population)
print("\n产品价格：\n", prices)
print("\n学生信息：\n", info)
```

**指定索引顺序**：

从字典创建时，可以通过`index`参数指定索引的顺序，甚至筛选部分数据。

```python
data = {"a": 10, "b": 20, "c": 30, "d": 40}

# 不指定索引，使用字典的顺序（Python 3.7+保证顺序）
s1 = pd.Series(data)
print("默认顺序：\n", s1)

# 指定索引顺序
s2 = pd.Series(data, index=['d', 'c', 'b', 'a'])
print("\n自定义顺序：\n", s2)

# 只选择部分键
s3 = pd.Series(data, index=['a', 'c'])
print("\n只选择a和c：\n", s3)

# 索引中包含字典中不存在的键，会产生NaN（缺失值）
s4 = pd.Series(data, index=['a', 'b', 'e', 'f'])
print("\n包含不存在的键：\n", s4)
```

输出：
```
默认顺序：
 a    10
b    20
c    30
d    40
dtype: int64

自定义顺序：
 d    40
c    30
b    20
a    10
dtype: int64

只选择a和c：
 a    10
c    30
dtype: int64

包含不存在的键：
 a    10.0
b    20.0
e     NaN
f     NaN
dtype: float64
```

**注意**：当索引中有不存在的键时，Series会自动填充NaN（Not a Number，表示缺失值），并且数据类型会变成float64。

---

### 从NumPy数组创建

如果你已经有NumPy数组，可以直接转换成Series。这在科学计算和数据分析中非常常见。

```python
import pandas as pd
import numpy as np

# 从NumPy数组创建
arr = np.array([10, 20, 30, 40, 50])
s = pd.Series(arr)
print(s)
```

输出：
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

**实际应用示例**：

```python
import numpy as np
import pandas as pd

# 生成随机数据
random_data = np.random.randn(7)  # 7个标准正态分布的随机数

# 转换成Series，添加有意义的索引
weekly_returns = pd.Series(
    random_data,
    index=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
)

print("本周股票收益率：")
print(weekly_returns)
print("\n平均收益率:", weekly_returns.mean())
print("最大收益:", weekly_returns.max())
print("最小收益:", weekly_returns.min())
```

**NumPy特性的保留**：

```python
# NumPy的数学运算和函数可以直接用在Series上
arr = np.array([1, 4, 9, 16, 25])
s = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e'])

# NumPy函数
print("平方根:", np.sqrt(s))
print("指数:", np.exp(s))
print("对数:", np.log(s))

# Series的方法
print("\n总和:", s.sum())
print("平均值:", s.mean())
print("标准差:", s.std())
```

---

### 从标量值创建

可以从单个值（标量）创建Series，需要指定索引的长度。

```python
import pandas as pd

# 从标量值创建（必须提供索引）
s = pd.Series(100, index=['a', 'b', 'c', 'd', 'e'])
print(s)
```

输出：
```
a    100
b    100
c    100
d    100
e    100
dtype: int64
```

**使用场景**：

1. **初始化**：创建一个所有值相同的Series作为起点

```python
# 初始化学生成绩为0
initial_scores = pd.Series(0, index=["张三", "李四", "王五"])
print(initial_scores)
```

2. **填充默认值**：

```python
# 所有产品的默认价格为9.9元
default_prices = pd.Series(9.9, index=["产品A", "产品B", "产品C"])
print(default_prices)
```

3. **创建常数序列**：

```python
# 创建权重序列（所有权重相同）
weights = pd.Series(1.0, index=['特征1', '特征2', '特征3', '特征4'])
print(weights)
```

---

### 创建方法对比

让我们总结一下不同创建方法的适用场景：

```python
import pandas as pd
import numpy as np

# 方法1：从列表（最常用，简单直接）
s1 = pd.Series([1, 2, 3, 4, 5])

# 方法2：从列表+索引（需要自定义标签时）
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 方法3：从字典（数据本身就是键值对时）
s3 = pd.Series({'a': 1, 'b': 2, 'c': 3})

# 方法4：从NumPy数组（科学计算数据转换时）
s4 = pd.Series(np.array([1, 2, 3]))

# 方法5：从标量（初始化相同值时）
s5 = pd.Series(100, index=['a', 'b', 'c'])

print("从列表:\n", s1)
print("\n从列表+索引:\n", s2)
print("\n从字典:\n", s3)
print("\n从NumPy:\n", s4)
print("\n从标量:\n", s5)
```

**选择建议**：

| 数据来源 | 推荐方法 | 原因 |
|---------|---------|------|
| 已有列表数据 | `pd.Series(list)` | 最简单 |
| 需要有意义的标签 | `pd.Series(list, index=labels)` | 增强可读性 |
| 字典数据 | `pd.Series(dict)` | 天然匹配 |
| NumPy计算结果 | `pd.Series(array)` | 无缝衔接 |
| 初始化相同值 | `pd.Series(scalar, index=...)` | 方便快捷 |

---

## Series的索引

索引是Series最重要的特性之一，也是Series区别于普通数组的核心。Series支持两种索引方式：**位置索引**和**标签索引**。

这种双重索引机制让Series既保持了NumPy数组的高效性，又具有了字典的灵活性。

---

### 位置索引（整数索引）

位置索引就是通过元素的位置（从0开始）来访问数据，这和Python列表、NumPy数组完全一样。

```python
import pandas as pd

# 创建Series
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])
print(scores)
print()

# 位置索引（从0开始）
print("第1个元素:", scores.iloc[0])  # 85
print("第3个元素:", scores.iloc[2])  # 78
print("最后一个:", scores.iloc[-1])  # 88
```

输出：
```
张三    85
李四    92
王五    78
赵六    95
孙七    88
dtype: int64

第1个元素: 85
第3个元素: 78
最后一个: 88
```

**重要**：使用位置索引必须用`.iloc[]`，而不是直接用方括号！

```python
# 正确的位置索引方式
print(scores.iloc[0])  # 正确

# 错误的方式（可能会混淆）
# print(scores[0])  # 如果索引不是整数，这会报错！
```

**为什么要用.iloc？**

因为Series的索引可以是整数，如果直接用方括号，会产生歧义：你是想用位置索引还是标签索引？

```python
# 看这个例子
s = pd.Series([10, 20, 30], index=[0, 1, 2])
print(s[0])  # 10，这是位置索引还是标签索引？模糊！

# 清晰的方式
print(s.iloc[0])  # 10，明确是位置索引
print(s.loc[0])   # 10，明确是标签索引
```

**位置索引的切片**：

```python
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 切片：前3个元素
print("前3个:\n", scores.iloc[:3])

# 切片：第2到第4个元素
print("\n第2-4个:\n", scores.iloc[1:4])

# 切片：每隔一个取一个
print("\n隔一个取一个:\n", scores.iloc[::2])

# 切片：倒序
print("\n倒序:\n", scores.iloc[::-1])
```

输出：
```
前3个:
 张三    85
李四    92
王五    78
dtype: int64

第2-4个:
 李四    92
王五    78
赵六    95
dtype: int64

隔一个取一个:
 张三    85
王五    78
孙七    88
dtype: int64

倒序:
 孙七    88
赵六    95
王五    78
李四    92
张三    85
dtype: int64
```

**注意**：位置索引的切片遵循"左闭右开"原则，即`[start:end)`不包含end位置。

---

### 标签索引（显式索引）

标签索引是通过索引标签来访问数据，这是Series最强大的特性！

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 标签索引
print("张三的成绩:", scores["张三"])   # 85
print("赵六的成绩:", scores["赵六"])   # 95

# 用.loc明确表示标签索引（推荐）
print("李四的成绩:", scores.loc["李四"])  # 92
```

**标签索引的优势**：

1. **可读性强**：一眼就能看出访问的是什么数据
2. **不受顺序影响**：即使数据顺序改变，标签依然有效
3. **语义清晰**：代码更接近自然语言

```python
# 对比：位置索引 vs 标签索引

# 位置索引：需要知道张三是第几个
score1 = scores.iloc[0]  # 张三是第0个，但你必须记住这个位置

# 标签索引：直接用名字，直观清晰
score2 = scores["张三"]  # 直接用名字，不用记位置
score3 = scores.loc["张三"]  # 更明确的写法

print(score1, score2, score3)  # 都是85
```

**标签索引的切片**：

```python
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 标签切片：从"李四"到"赵六"
print("李四到赵六:\n", scores.loc["李四":"赵六"])

# 标签切片：从开始到"王五"
print("\n开始到王五:\n", scores.loc[:"王五"])

# 标签切片：从"赵六"到结束
print("\n赵六到结束:\n", scores.loc["赵六":])
```

输出：
```
李四到赵六:
 李四    92
王五    78
赵六    95
dtype: int64

开始到王五:
 张三    85
李四    92
王五    78
dtype: int64

赵六到结束:
 赵六    95
孙七    88
dtype: int64
```

**重要区别**：标签切片是"两端都包含"的，即`[start:end]`包含start和end！

```python
# 位置索引：左闭右开 [0:3) 不包含索引3
print(scores.iloc[0:3])  # 张三、李四、王五

# 标签索引：两端都包含 ["张三":"王五"] 包含两端
print(scores.loc["张三":"王五"])  # 张三、李四、王五
```

---

### 多个元素的索引

可以一次性访问多个元素，用列表传入多个索引。

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 用列表获取多个元素（标签索引）
print("多个学生成绩:")
print(scores[["张三", "王五", "孙七"]])

# 用列表获取多个元素（位置索引）
print("\n用位置获取多个元素:")
print(scores.iloc[[0, 2, 4]])
```

输出：
```
多个学生成绩:
张三    85
王五    78
孙七    88
dtype: int64

用位置获取多个元素:
张三    85
王五    78
孙七    88
dtype: int64
```

**注意双重方括号**：外层方括号是索引操作，内层方括号是列表。

```python
# 正确：双重方括号
scores[["张三", "王五"]]  # 

# 错误：单层方括号
# scores["张三", "王五"]  # 会报错！
```

---

### 布尔索引（条件筛选）

布尔索引是最强大的索引方式，可以根据条件筛选数据。这在数据分析中极其常用！

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 找出成绩大于90的学生
print("成绩大于90的学生:")
print(scores[scores > 90])

# 找出成绩在80-90之间的学生
print("\n成绩在80-90之间的学生:")
print(scores[(scores >= 80) & (scores <= 90)])

# 找出成绩不及格的学生（假设60分及格）
print("\n成绩不及格的学生:")
print(scores[scores < 60])
```

输出：
```
成绩大于90的学生:
李四    92
赵六    95
dtype: int64

成绩在80-90之间的学生:
张三    85
孙七    88
dtype: int64

成绩不及格的学生:
Series([], dtype: int64)
```

**理解布尔索引的原理**：

```python
# 第1步：比较运算返回布尔Series
mask = scores > 90
print("布尔掩码:")
print(mask)

# 第2步：用布尔Series做索引
result = scores[mask]
print("\n筛选结果:")
print(result)
```

输出：
```
布尔掩码:
张三    False
李四     True
王五    False
赵六     True
孙七    False
dtype: bool

筛选结果:
李四    92
赵六    95
dtype: int64
```

**多条件组合**：

```python
# AND条件：成绩大于80且小于95
print("80 < 成绩 < 95:")
print(scores[(scores > 80) & (scores < 95)])

# OR条件：成绩小于80或大于90
print("\n成绩<80 或 >90:")
print(scores[(scores < 80) | (scores > 90)])

# NOT条件：成绩不等于92
print("\n成绩不等于92:")
print(scores[scores != 92])
```

**注意事项**：
- 使用`&`（AND）、`|`（OR）、`~`（NOT），而不是`and`、`or`、`not`
- 每个条件必须用括号包起来
- 布尔索引返回的是原Series的副本

---

### 索引方法总结

让我们用一个完整的例子总结所有索引方法：

```python
import pandas as pd

# 创建示例数据
scores = pd.Series([85, 92, 78, 95, 88, 76, 90],
                   index=["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九"])

print("原始数据:")
print(scores)
print()

# 1. 单个元素 - 标签索引
print("1. 张三的成绩:", scores["张三"])

# 2. 单个元素 - 位置索引
print("2. 第一个学生成绩:", scores.iloc[0])

# 3. 多个元素 - 标签索引
print("3. 张三和李四的成绩:")
print(scores[["张三", "李四"]])

# 4. 多个元素 - 位置索引
print("\n4. 前两个学生成绩:")
print(scores.iloc[[0, 1]])

# 5. 切片 - 标签索引（两端都包含）
print("\n5. 张三到王五的成绩:")
print(scores.loc["张三":"王五"])

# 6. 切片 - 位置索引（左闭右开）
print("\n6. 前3个学生成绩:")
print(scores.iloc[:3])

# 7. 布尔索引 - 单条件
print("\n7. 成绩大于90的学生:")
print(scores[scores > 90])

# 8. 布尔索引 - 多条件
print("\n8. 成绩在85-90之间的学生:")
print(scores[(scores >= 85) & (scores <= 90)])
```

**索引选择建议**：

| 场景 | 推荐方法 | 示例 |
|------|---------|------|
| 已知标签，访问单个 | `s["label"]` | `scores["张三"]` |
| 已知位置，访问单个 | `s.iloc[pos]` | `scores.iloc[0]` |
| 访问多个标签 | `s[["l1", "l2"]]` | `scores[["张三", "李四"]]` |
| 访问多个位置 | `s.iloc[[p1, p2]]` | `scores.iloc[[0, 1]]` |
| 标签范围切片 | `s.loc["l1":"l2"]` | `scores.loc["张三":"王五"]` |
| 位置范围切片 | `s.iloc[p1:p2]` | `scores.iloc[0:3]` |
| 条件筛选 | `s[condition]` | `scores[scores > 90]` |

---

## Series的属性

Series有很多有用的属性，可以帮助我们了解Series的基本信息。这些属性不需要加括号，直接访问即可。

---

### 基本属性

```python
import pandas as pd
import numpy as np

# 创建Series
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# values - 获取数据值（返回NumPy数组）
print("数据值:", scores.values)
print("类型:", type(scores.values))

# index - 获取索引
print("\n索引:", scores.index)
print("类型:", type(scores.index))

# dtype - 获取数据类型
print("\n数据类型:", scores.dtype)

# shape - 获取形状（元素个数）
print("\n形状:", scores.shape)

# size - 获取元素个数
print("\n元素个数:", scores.size)

# name - Series的名称（可选）
scores.name = "期末成绩"
print("\nSeries名称:", scores.name)

# index.name - 索引的名称（可选）
scores.index.name = "学生姓名"
print("索引名称:", scores.index.name)

print("\n完整显示:")
print(scores)
```

输出：
```
数据值: [85 92 78 95 88]
类型: <class 'numpy.ndarray'>

索引: Index(['张三', '李四', '王五', '赵六', '孙七'], dtype='object')
类型: <class 'pandas.core.indexes.base.Index'>

数据类型: int64

形状: (5,)

元素个数: 5

Series名称: 期末成绩
索引名称: 学生姓名

完整显示:
学生姓名
张三    85
李四    92
王五    78
赵六    95
孙七    88
Name: 期末成绩, dtype: int64
```

**属性详解**：

1. **values**：返回NumPy数组，可以用NumPy的所有功能
2. **index**：返回Index对象，包含所有索引标签
3. **dtype**：数据类型，和NumPy的dtype一样
4. **shape**：形状，是一个元组，对于Series总是`(n,)`形式
5. **size**：元素总数，等于`len(series)`
6. **name**：Series的名称，在DataFrame中会成为列名
7. **index.name**：索引的名称，用于标识索引的含义

---

### 属性的实际应用

```python
import pandas as pd
import numpy as np

# 股票价格数据
stock_prices = pd.Series(
    [152.3, 153.1, 151.8, 154.2, 155.6],
    index=['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19']
)
stock_prices.name = "股票价格"
stock_prices.index.name = "日期"

print("股票数据:")
print(stock_prices)
print()

# 使用属性获取信息
print(f"数据类型: {stock_prices.dtype}")
print(f"数据天数: {stock_prices.size}天")
print(f"价格范围: {stock_prices.values.min():.2f} - {stock_prices.values.max():.2f}")
print(f"起始日期: {stock_prices.index[0]}")
print(f"结束日期: {stock_prices.index[-1]}")

# values属性可以直接用NumPy函数
print(f"\n平均价格: {np.mean(stock_prices.values):.2f}")
print(f"标准差: {np.std(stock_prices.values):.2f}")
print(f"中位数: {np.median(stock_prices.values):.2f}")
```

---

### ndim和empty属性

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

# ndim - 维度（Series总是1维）
print("维度:", s.ndim)  # 1

# empty - 是否为空
print("是否为空:", s.empty)  # False

# 空Series
empty_s = pd.Series([])
print("空Series:", empty_s.empty)  # True
```

---

### hasnans属性

检查Series是否包含缺失值（NaN）。

```python
import pandas as pd
import numpy as np

# 包含NaN的Series
s1 = pd.Series([1, 2, np.nan, 4, 5])
print("s1包含NaN:", s1.hasnans)  # True

# 不包含NaN的Series
s2 pd.Series([1, 2, 3, 4, 5])
print("s2包含NaN:", s2.hasnans)  # False

# 实际应用：数据质量检查
if s1.hasnans:
    print(f"警告：数据中有 {s1.isna().sum()} 个缺失值！")
```

---

## Series的方法

Series提供了大量方便的方法用于数据分析。这些方法是Series区别于普通数组的重要特性。

---

### 数据查看方法

```python
import pandas as pd
import numpy as np

# 创建示例数据
scores = pd.Series(
    np.random.randint(60, 100, size=20),
    index=[f"学生{i+1}" for i in range(20)]
)
scores.name = "考试成绩"

print("原始数据（太长，不易查看）:")
print(scores)
print()

# head() - 查看前n个元素（默认5个）
print("前5个学生成绩:")
print(scores.head())

# 指定查看个数
print("\n前3个学生成绩:")
print(scores.head(3))

# tail() - 查看后n个元素（默认5个）
print("\n后5个学生成绩:")
print(scores.tail())

# 指定查看个数
print("\n后3个学生成绩:")
print(scores.tail(3))
```

**使用场景**：
- 数据量大时，快速预览数据
- 检查数据加载是否正确
- 查看数据的起始和结尾部分

---

### 统计描述方法

Series提供了丰富的统计方法，这是数据分析的核心功能。

```python
import pandas as pd
import numpy as np

scores = pd.Series([85, 92, 78, 95, 88, 76, 90, 82, 91, 87])

# describe() - 一次性查看所有统计信息
print("完整统计信息:")
print(scores.describe())
print()

# 各种统计方法
print("数量:", scores.count())     # 非NaN元素个数
print("总和:", scores.sum())       # 求和
print("平均值:", scores.mean())     # 平均数
print("中位数:", scores.median())   # 中位数
print("标准差:", scores.std())      # 标准差
print("方差:", scores.var())       # 方差
print("最小值:", scores.min())      # 最小值
print("最大值:", scores.max())      # 最大值
print("范围:", scores.max() - scores.min())  # 极差
```

输出：
```
完整统计信息:
count    10.000000
mean     86.400000
std       6.023452
min      76.000000
25%      82.750000
50%      87.500000
75%      90.750000
max      95.000000
dtype: float64

数量: 10
总和: 864
平均值: 86.4
中位数: 87.5
标准差: 6.023451614797361
方差: 36.28181818181818
最小值: 76
最大值: 95
范围: 19
```

**describe()详解**：

```python
# describe()返回的统计量说明
print("统计量说明:")
print("count: 数据个数")
print("mean:  平均值")
print("std:   标准差")
print("min:   最小值")
print("25%:   第一四分位数（25%的数据小于这个值）")
print("50%:   中位数（50%分位数）")
print("75%:   第三四分位数（75%的数据小于这个值）")
print("max:   最大值")
```

---

### 排序方法

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# sort_values() - 按值排序（默认升序）
print("按成绩升序:")
print(scores.sort_values())

# 降序排序
print("\n按成绩降序:")
print(scores.sort_values(ascending=False))

# sort_index() - 按索引排序
print("\n按姓名排序:")
print(scores.sort_index())
```

输出：
```
按成绩升序:
王五    78
张三    85
孙七    88
李四    92
赵六    95
dtype: int64

按成绩降序:
赵六    95
李四    92
孙七    88
张三    85
王五    78
dtype: int64

按姓名排序:
孙七    88
张三    85
李四    92
王五    78
赵六    95
dtype: int64
```

**注意**：排序方法返回新的Series，不会修改原Series！

```python
# 原Series不变
print("原始数据:")
print(scores)

# 如果要修改原Series，使用inplace参数
scores_copy = scores.copy()
scores_copy.sort_values(inplace=True)
print("\n就地排序后:")
print(scores_copy)
```

---

### 查找方法

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# idxmax() - 找出最大值的索引
print("成绩最高的学生:", scores.idxmax())  # 赵六

# idxmin() - 找出最小值的索引
print("成绩最低的学生:", scores.idxmin())  # 王五

# argmax() - 找出最大值的位置
print("最高分的位置:", scores.argmax())    # 3

# argmin() - 找出最小值的位置
print("最低分的位置:", scores.argmin())    # 2

# nlargest() - 找出最大的n个值
print("\n成绩最高的3名学生:")
print(scores.nlargest(3))

# nsmallest() - 找出最小的n个值
print("\n成绩最低的2名学生:")
print(scores.nsmallest(2))
```

输出：
```
成绩最高的学生: 赵六
成绩最低的学生: 王五
最高分的位置: 3
最低分的位置: 2

成绩最高的3名学生:
赵六    95
李四    92
孙七    88
dtype: int64

成绩最低的2名学生:
王五    78
张三    85
dtype: int64
```

---

### 唯一值和计数方法

```python
import pandas as pd

# 成绩数据（有重复）
grades = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'D', 'B', 'C', 'A'])

# unique() - 获取唯一值
print("所有等级:", grades.unique())

# nunique() - 唯一值个数
print("等级种类数:", grades.nunique())

# value_counts() - 统计每个值的出现次数
print("\n等级分布:")
print(grades.value_counts())

# 按索引排序
print("\n等级分布（按等级排序）:")
print(grades.value_counts().sort_index())

# 显示比例而不是计数
print("\n等级比例:")
print(grades.value_counts(normalize=True))
```

输出：
```
所有等级: ['A' 'B' 'C' 'D']
等级种类数: 4

等级分布:
A    4
B    3
C    2
D    1
dtype: int64

等级分布（按等级排序）:
A    4
B    3
C    2
D    1
dtype: int64

等级比例:
A    0.4
B    0.3
C    0.2
D    0.1
dtype: float64
```

**实际应用**：

```python
# 分析客户订单数据
orders = pd.Series(['北京', '上海', '北京', '广州', '上海', '北京',
                    '深圳', '上海', '北京', '广州', '北京', '上海'])

print("订单城市分布:")
city_counts = orders.value_counts()
print(city_counts)

print(f"\n订单最多的城市: {city_counts.idxmax()}，共{city_counts.max()}单")
print(f"订单最少的城市: {city_counts.idxmin()}，共{city_counts.min()}单")
print(f"总共涉及 {orders.nunique()} 个城市")
```

---

### 应用自定义函数

```python
import pandas as pd
import numpy as np

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# apply() - 对每个元素应用函数
def grade_level(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

grades = scores.apply(grade_level)
print("成绩等级:")
print(grades)

# 使用lambda函数
print("\n加10分后:")
print(scores.apply(lambda x: x + 10))

# map() - 映射（类似apply，但更适合映射字典）
mapping = {85: 'B', 92: 'A', 78: 'C', 95: 'A', 88: 'B'}
letter_grades = scores.map(mapping)
print("\n字母等级:")
print(letter_grades)
```

输出：
```
成绩等级:
张三    良好
李四    优秀
王五    中等
赵六    优秀
孙七    良好
dtype: object

加10分后:
张三    95
李四   102
王五    88
赵六   105
孙七    98
dtype: int64

字母等级:
张三    B
李四    A
王五    C
赵六    A
孙七    B
dtype: object
```

---

## Series的运算

Series支持丰富的运算操作，包括算术运算、比较运算和逻辑运算。这些运算都是**向量化**的，即会自动应用到每个元素。

---

### 算术运算

Series支持所有基本的算术运算，而且运算是基于索引对齐的。

```python
import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

print("s1:\n", s1)
print("\ns2:\n", s2)

# 加法
print("\n加法 (s1 + s2):")
print(s1 + s2)

# 减法
print("\n减法 (s1 - s2):")
print(s1 - s2)

# 乘法
print("\n乘法 (s1 * s2):")
print(s1 * s2)

# 除法
print("\n除法 (s1 / s2):")
print(s1 / s2)

# 幂运算
print("\n幂运算 (s1 ** 2):")
print(s1 ** 2)

# 取模
print("\n取模 (s1 % 7):")
print(s1 % 7)
```

**与标量运算**：

```python
s = pd.Series([10, 20, 30, 40])

print("原始:", s.values)
print("加10:", (s + 10).values)
print("乘2:", (s * 2).values)
print("除5:", (s / 5).values)
print("平方:", (s ** 2).values)
```

**索引对齐**：

这是Series最重要的特性之一！当两个Series进行运算时，会根据索引自动对齐。

```python
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'd', 'e'])

print("s1:\n", s1)
print("\ns2:\n", s2)
print("\ns1 + s2:")
print(s1 + s2)
```

输出：
```
s1:
 a    10
b    20
c    30
dtype: int64

s2:
 a    1
b    2
d    3
e    4
dtype: int64

s1 + s2:
a    11.0
b    22.0
c     NaN
d     NaN
e     NaN
dtype: float64
```

**理解索引对齐**：

- 索引`a`和`b`在两个Series中都存在，所以能正常相加
- 索引`c`只在s1中存在，索引`d`和`e`只在s2中存在，所以结果是NaN（缺失值）

这个特性非常强大！在实际应用中，我们经常需要对不同来源的数据进行合并计算，索引对齐可以自动处理对应关系。

**填充缺失值**：

如果不想要NaN，可以使用`add()、sub()、mul()、div()`等方法，并指定`fill_value`：

```python
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'd', 'e'])

# 用0填充缺失值
print("用0填充缺失值:")
print(s1.add(s2, fill_value=0))
```

输出：
```
用0填充缺失值:
a    11.0
b    22.0
c    30.0
d     3.0
e     4.0
dtype: float64
```

---

### 比较运算

比较运算返回布尔Series，常用于条件筛选。

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])

# 各种比较运算
print("大于90:")
print(scores > 90)

print("\n大于等于88:")
print(scores >= 88)

print("\n等于92:")
print(scores == 92)

print("\n不等于85:")
print(scores != 85)

# 结合布尔索引
print("\n成绩大于90的学生:")
print(scores[scores > 90])

print("\n成绩在80-90之间的学生:")
print(scores[(scores >= 80) & (scores <= 90)])
```

**Series之间的比较**：

```python
s1 = pd.Series([85, 92, 78], index=['a', 'b', 'c'])
s2 = pd.Series([80, 95, 78], index=['a', 'b', 'c'])

print("s1 > s2:")
print(s1 > s2)

print("\ns1 == s2:")
print(s1 == s2)
```

---

### 逻辑运算

逻辑运算用于组合多个条件。

```python
import pandas as pd

scores = pd.Series([85, 92, 78, 95, 88, 76, 90],
                   index=["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九"])

# AND运算：成绩大于80且小于90
condition = (scores > 80) & (scores < 90)
print("80 < 成绩 < 90:")
print(scores[condition])

# OR运算：成绩小于80或大于90
condition = (scores < 80) | (scores > 90)
print("\n成绩<80 或 >90:")
print(scores[condition])

# NOT运算：成绩不在85-90之间
condition = ~((scores >= 85) & (scores <= 90))
print("\n成绩不在85-90之间:")
print(scores[condition])

# 复杂条件：成绩大于85且小于95，或者小于80
condition = ((scores > 85) & (scores < 95)) | (scores < 80)
print("\n(85<成绩<95) 或 (成绩<80):")
print(scores[condition])
```

**注意**：
- 使用`&`（AND）、`|`（OR）、`~`（NOT）
- 不要使用`and`、`or`、`not`（这些是Python的关键字，不适用于Series）
- 每个条件必须用括号包起来

---

### 数学函数

Series可以直接使用NumPy的数学函数。

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 4, 9, 16, 25])

print("原始数据:", s.values)
print("平方根:", np.sqrt(s).values)
print("对数:", np.log(s).values)
print("指数:", np.exp(s).values)
print("正弦:", np.sin(s).values)

# Series自带的数学方法
print("\n绝对值:", s.abs().values)
print("累计和:", s.cumsum().values)
print("累计积:", s.cumprod().values)
print("累计最大值:", s.cummax().values)
print("累计最小值:", s.cummin().values)
```

**实际应用示例**：

```python
# 计算股票收益率
prices = pd.Series([100, 102, 98, 105, 107, 103],
                   index=['周一', '周二', '周三', '周四', '周五', '周六'])

# 计算每日收益率（百分比变化）
returns = prices.pct_change() * 100
print("每日收益率（%）:")
print(returns)

# 累计收益率
cumulative_returns = (1 + prices.pct_change()).cumprod() - 1
print("\n累计收益率:")
print(cumulative_returns * 100)
```

---

## Series的缺失值处理

在实际数据分析中，缺失值（NaN）是常见问题。Pandas提供了完善的缺失值处理机制。

---

### 什么是缺失值？

缺失值（Missing Value）是指数据中不存在的值，在Pandas中用`NaN`（Not a Number）表示。

```python
import pandas as pd
import numpy as np

# 创建包含缺失值的Series
s = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print(s)
```

输出：
```
0    1.0
1    2.0
2    NaN
3    4.0
4    NaN
5    6.0
dtype: float64
```

**缺失值产生的原因**：
1. 数据采集失败
2. 数据传输错误
3. 某些数据本身就不存在
4. Series运算时索引不对齐

```python
# 索引不对齐产生NaN
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'd'])
result = s1 + s2
print("索引不对齐的结果:")
print(result)  # c和d的位置会是NaN
```

---

### 检测缺失值

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, np.nan, 6])

# isna() / isnull() - 检测每个元素是否为NaN（两个方法等价）
print("isna():")
print(s.isna())

print("\nisnull():")
print(s.isnull())

# notna() / notnull() - 检测每个元素是否不为NaN
print("\nnotna():")
print(s.notna())

# 统计缺失值个数
print("\n缺失值个数:", s.isna().sum())
print("非缺失值个数:", s.notna().sum())

# hasnans属性 - 是否包含NaN
print("是否包含NaN:", s.hasnans)
```

输出：
```
isna():
0    False
1    False
2     True
3    False
4     True
5    False
dtype: bool

isnull():
0    False
1    False
2     True
3    False
4     True
5    False
dtype: bool

notna():
0     True
1     True
2    False
3     True
4    False
5     True
dtype: bool

缺失值个数: 2
非缺失值个数: 4
是否包含NaN: True
```

---

### 删除缺失值

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print("原始数据:")
print(s)

# dropna() - 删除所有NaN
print("\n删除NaN后:")
print(s.dropna())

# 注意：原Series不变
print("\n原Series:")
print(s)

# 就地删除
s_copy = s.copy()
s_copy.dropna(inplace=True)
print("\n就地删除后:")
print(s_copy)
```

**实际应用**：

```python
scores = pd.Series([85, 92, np.nan, 95, 88, np.nan],
                   index=["张三", "李四", "王五", "赵六", "孙七", "周八"])

print("原始成绩:")
print(scores)

# 只计算有成绩的学生的平均分
valid_scores = scores.dropna()
print(f"\n有效成绩个数: {len(valid_scores)}")
print(f"平均成绩: {valid_scores.mean():.2f}")
```

---

### 填充缺失值

删除缺失值会丢失数据，有时我们需要用某个值来填充NaN。

```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, np.nan, 6])

# fillna() - 用指定值填充NaN
print("用0填充:")
print(s.fillna(0))

print("\n用-1填充:")
print(s.fillna(-1))

print("\n用平均值填充:")
print(s.fillna(s.mean()))

print("\n用中位数填充:")
print(s.fillna(s.median()))
```

**前向/后向填充**：

```python
s = pd.Series([1, np.nan, np.nan, 4, np.nan, 6])

# 前向填充（用前一个值填充）
print("前向填充 (ffill):")
print(s.ffill())

# 后向填充（用后一个值填充）
print("\n后向填充 (bfill):")
print(s.bfill())
```

输出：
```
前向填充 (ffill):
0    1.0
1    1.0
2    1.0
3    4.0
4    4.0
5    6.0
dtype: float64

后向填充 (bfill):
0    1.0
1    4.0
2    4.0
3    4.0
4    6.0
5    6.0
dtype: float64
```

**限制填充个数**：

```python
s = pd.Series([1, np.nan, np.nan, np.nan, 5])

# 只填充前2个NaN
print("限制填充个数:")
print(s.ffill(limit=2))
```

---

### 插值填充

interpolate()方法可以用插值的方式填充缺失值，更加智能。

```python
import pandas as pd
import numpy as np

# 温度数据，有些天的数据缺失
temps = pd.Series([22.5, np.nan, np.nan, 25.5, np.nan, 27.0],
                  index=['周一', '周二', '周三', '周四', '周五', '周六'])

print("原始数据:")
print(temps)

# 线性插值
print("\n线性插值:")
print(temps.interpolate())

# 多项式插值
print("\n多项式插值:")
print(temps.interpolate(method='polynomial', order=2))
```

输出：
```
原始数据:
周一    22.5
周二     NaN
周三     NaN
周四    25.5
周五     NaN
周六    27.0
dtype: float64

线性插值:
周一    22.5
周二    23.5
周三    24.5
周四    25.5
周五    26.25
周六    27.0
dtype: float64
```

---

### 替换值

replace()方法可以替换指定的值（不限于NaN）。

```python
import pandas as pd

s = pd.Series([1, 2, 3, 1, 2, 3, 1])

# 替换单个值
print("把1替换成10:")
print(s.replace(1, 10))

# 替换多个值
print("\n把1替换成10，把2替换成20:")
print(s.replace({1: 10, 2: 20}))

# 替换列表中的值
print("\n把1和2都替换成0:")
print(s.replace([1, 2], 0))

# 用字典替换
print("\n用字典一对一替换:")
print(s.replace({1: 'A', 2: 'B', 3: 'C'}))
```

**实际应用**：

```python
# 处理特殊标记
data = pd.Series([100, 200, -999, 300, -999, 400])
# -999表示缺失值，替换为NaN
clean_data = data.replace(-999, np.nan)
print("清洗后的数据:")
print(clean_data)

# 替换异常值
scores = pd.Series([85, 92, 999, 95, 88, 0])
# 999和0是异常值，替换为NaN
clean_scores = scores.replace([0, 999], np.nan)
print("\n清洗后的成绩:")
print(clean_scores)
```

---

## Series vs NumPy数组深度对比

让我们深入对比Series和NumPy数组，理解为什么在数据分析中要使用Series。

---

### 创建对比

```python
import pandas as pd
import numpy as np

# NumPy数组
np_arr = np.array([85, 92, 78, 95, 88])
print("NumPy数组:")
print(np_arr)
print("类型:", type(np_arr))

# Pandas Series
pd_series = pd.Series([85, 92, 78, 95, 88])
print("\nPandas Series:")
print(pd_series)
print("类型:", type(pd_series))

# Series with index
pd_series_labeled = pd.Series([85, 92, 78, 95, 88],
                               index=["张三", "李四", "王五", "赵六", "孙七"])
print("\n带标签的Series:")
print(pd_series_labeled)
```

---

### 索引对比

```python
import pandas as pd
import numpy as np

np_arr = np.array([85, 92, 78, 95, 88])
pd_series = pd.Series([85, 92, 78, 95, 88],
                      index=["张三", "李四", "王五", "赵六", "孙七"])

# NumPy：只能用位置索引
print("NumPy访问第一个:", np_arr[0])
# print(np_arr["张三"])  # 报错！

# Series：可以用位置索引，也可以用标签索引
print("\nSeries访问第一个（位置）:", pd_series.iloc[0])
print("Series访问张三（标签）:", pd_series["张三"])
```

---

### 运算对比

```python
import pandas as pd
import numpy as np

# NumPy数组
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

# 必须长度相同
print("NumPy数组运算:")
print(arr1 + arr2)  # [11 22 33]

# Series：自动根据索引对齐
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'd', 'e'])

print("\nSeries运算（自动对齐）:")
print(s1 + s2)
# a    11.0
# b    22.0
# c     NaN
# d     NaN
# e     NaN
```

---

### 缺失值对比

```python
import pandas as pd
import numpy as np

# NumPy：缺失值处理不方便
np_arr = np.array([1.0, 2.0, np.nan, 4.0, np.nan])
print("NumPy数组:")
print(np_arr)
print("平均值（包含NaN）:", np.mean(np_arr))  # NaN
print("平均值（忽略NaN）:", np.nanmean(np_arr))  # 2.33...

# Series：缺失值处理很方便
pd_series = pd.Series([1.0, 2.0, np.nan, 4.0, np.nan])
print("\nSeries:")
print(pd_series)
print("平均值（自动忽略NaN）:", pd_series.mean())  # 2.33...
print("删除NaN:\n", pd_series.dropna())
print("填充NaN:\n", pd_series.fillna(0))
```

---

### 方法对比

```python
import pandas as pd
import numpy as np

np_arr = np.array([85, 92, 78, 95, 88])
pd_series = pd.Series([85, 92, 78, 95, 88],
                      index=["张三", "李四", "王五", "赵六", "孙七"])

# NumPy：需要函数调用
print("NumPy统计:")
print("平均值:", np.mean(np_arr))
print("中位数:", np.median(np_arr))
print("标准差:", np.std(np_arr))
print("最大值:", np.max(np_arr))

# Series：可以用方法
print("\nSeries统计:")
print("平均值:", pd_series.mean())
print("中位数:", pd_series.median())
print("标准差:", pd_series.std())
print("最大值:", pd_series.max())

# Series有更多方法
print("\nSeries独有:")
print("完整统计:\n", pd_series.describe())
print("最大值的索引:", pd_series.idxmax())
print("值计数:\n", pd_series.value_counts())
```

---

### 什么时候用NumPy，什么时候用Series？

**使用NumPy数组的场景**：

1. **纯数值计算**：矩阵运算、线性代数、科学计算
2. **性能极致要求**：NumPy在某些底层计算上比Pandas稍快
3. **多维数组**：处理图像（3维）、视频（4维）等
4. **与其他库交互**：很多科学计算库（如SciPy）基于NumPy

```python
import numpy as np

# 矩阵运算
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)  # 矩阵乘法

# 图像处理
image = np.zeros((1920, 1080, 3))  # 高×宽×颜色通道
```

**使用Pandas Series的场景**：

1. **数据分析**：处理表格数据、统计分析
2. **需要标签**：数据有明确含义（日期、名称等）
3. **缺失值处理**：数据有NaN需要处理
4. **索引对齐**：需要基于标签合并数据
5. **数据清洗**：去重、替换、转换等

```python
import pandas as pd

# 时间序列分析
stock_prices = pd.Series([152.3, 153.1, 151.8],
                         index=['2024-01-15', '2024-01-16', '2024-01-17'])

# 数据清洗
messy_data = pd.Series([100, 200, -999, 300, -999])
clean_data = messy_data.replace(-999, np.nan).fillna(messy_data.mean())

# 统计分析
scores = pd.Series([85, 92, 78, 95, 88],
                   index=["张三", "李四", "王五", "赵六", "孙七"])
print(scores.describe())
```

**总结表**：

| 特性 | NumPy数组 | Pandas Series |
|------|----------|--------------|
| **使用场景** | 科学计算、矩阵运算 | 数据分析、统计 |
| **标签支持** | | |
| **缺失值处理** | 基本 | 完善 |
| **索引对齐** | | |
| **多维支持** | | （仅1维） |
| **性能** | 极快 | 快 |
| **方法丰富度** | 基本 | 丰富 |
| **适合初学者** | 较难 | 容易 |

---

## 实战练习

通过实际练习巩固所学知识。每个练习都有完整的解决方案。

---

### 练习1：学生成绩管理

**题目**：创建一个存储学生成绩的Series，完成以下任务：

1. 创建包含10名学生成绩的Series（自己设定）
2. 找出成绩最高和最低的学生
3. 计算平均分、中位数
4. 找出成绩大于平均分的学生
5. 按成绩降序排列

**解答**：

```python
import pandas as pd

# 1. 创建学生成绩Series
scores = pd.Series(
    [85, 92, 78, 95, 88, 76, 90, 82, 91, 87],
    index=['张三', '李四', '王五', '赵六', '孙七',
           '周八', '吴九', '郑十', '钱一', '孙二']
)
scores.name = '期末成绩'
scores.index.name = '学生姓名'

print("学生成绩:")
print(scores)
print()

# 2. 找出最高分和最低分
highest_student = scores.idxmax()
lowest_student = scores.idxmin()
print(f"成绩最高：{highest_student}，{scores[highest_student]}分")
print(f"成绩最低：{lowest_student}，{scores[lowest_student]}分")
print()

# 3. 计算平均分和中位数
mean_score = scores.mean()
median_score = scores.median()
print(f"平均分：{mean_score:.2f}")
print(f"中位数：{median_score:.2f}")
print()

# 4. 找出成绩大于平均分的学生
above_average = scores[scores > mean_score]
print(f"成绩高于平均分的学生（共{len(above_average)}人）:")
print(above_average)
print()

# 5. 按成绩降序排列
sorted_scores = scores.sort_values(ascending=False)
print("成绩排名:")
for rank, (student, score) in enumerate(sorted_scores.items(), 1):
    print(f"{rank}. {student}: {score}分")
```

---

### 练习2：温度数据分析

**题目**：分析一周的温度数据：

1. 创建一周7天的温度Series（包含2个缺失值）
2. 用线性插值填充缺失值
3. 找出最热和最冷的是星期几
4. 计算温度的标准差
5. 判断哪几天温度高于平均温度

**解答**：

```python
import pandas as pd
import numpy as np

# 1. 创建温度数据（包含缺失值）
temperatures = pd.Series(
    [22.5, 24.1, np.nan, 25.3, 26.0, np.nan, 23.2],
    index=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
)
temperatures.name = '气温(℃)'

print("原始温度数据:")
print(temperatures)
print()

# 2. 用线性插值填充缺失值
temps_filled = temperatures.interpolate()
print("填充后的温度数据:")
print(temps_filled)
print()

# 3. 找出最热和最冷的日子
hottest_day = temps_filled.idxmax()
coldest_day = temps_filled.idxmin()
print(f"最热的日子：{hottest_day}，{temps_filled[hottest_day]:.1f}℃")
print(f"最冷的日子：{coldest_day}，{temps_filled[coldest_day]:.1f}℃")
print()

# 4. 计算标准差
std_temp = temps_filled.std()
print(f"温度标准差：{std_temp:.2f}℃")
print()

# 5. 找出温度高于平均的日子
mean_temp = temps_filled.mean()
above_average_days = temps_filled[temps_filled > mean_temp]
print(f"平均温度：{mean_temp:.2f}℃")
print(f"高于平均温度的日子:")
for day, temp in above_average_days.items():
    print(f"  {day}: {temp:.1f}℃")
```

---

### 练习3：股票价格分析

**题目**：分析一只股票5天的收盘价：

1. 创建股票价格Series（5个交易日）
2. 计算每日涨跌额和涨跌幅
3. 找出涨幅最大的一天
4. 计算5日累计收益率
5. 判断整体趋势（上涨/下跌）

**解答**：

```python
import pandas as pd

# 1. 创建股票价格数据
prices = pd.Series(
    [152.30, 153.10, 151.80, 154.20, 155.60],
    index=['2024-01-15', '2024-01-16', '2024-01-17',
           '2024-01-18', '2024-01-19']
)
prices.name = '收盘价'
prices.index.name = '日期'

print("股票价格:")
print(prices)
print()

# 2. 计算每日涨跌额和涨跌幅
price_change = prices.diff()  # 涨跌额
price_pct_change = prices.pct_change() * 100  # 涨跌幅（百分比）

print("每日涨跌:")
for date in prices.index[1:]:  # 跳过第一天（没有前一日）
    change = price_change[date]
    pct = price_pct_change[date]
    symbol = "📈" if change > 0 else "📉"
    print(f"{date}: {change:+.2f}元 ({pct:+.2f}%) {symbol}")
print()

# 3. 找出涨幅最大的一天
max_gain_date = price_pct_change.idxmax()
max_gain = price_pct_change[max_gain_date]
print(f"涨幅最大：{max_gain_date}，涨幅{max_gain:.2f}%")
print()

# 4. 计算5日累计收益率
total_return = (prices.iloc[-1] / prices.iloc[0] - 1) * 100
print(f"5日累计收益率：{total_return:.2f}%")
print()

# 5. 判断整体趋势
if prices.iloc[-1] > prices.iloc[0]:
    trend = "上涨"
    emoji = "📈"
else:
    trend = "下跌"
    emoji = "📉"
print(f"整体趋势：{trend} {emoji}")
print(f"起始价：{prices.iloc[0]:.2f}元")
print(f"最终价：{prices.iloc[-1]:.2f}元")
```

---

### 练习4：城市人口统计

**题目**：统计多个城市的人口数据：

1. 创建10个城市的人口Series（单位：万人）
2. 找出人口最多和最少的城市
3. 计算人口总和和平均值
4. 找出人口超过2000万的城市
5. 按人口降序排列并显示排名

**解答**：

```python
import pandas as pd

# 1. 创建城市人口数据
population = pd.Series({
    '北京': 2189,
    '上海': 2428,
    '广州': 1868,
    '深圳': 1756,
    '成都': 2094,
    '重庆': 3205,
    '杭州': 1237,
    '武汉': 1364,
    '西安': 1316,
    '苏州': 1275
})
population.name = '人口(万)'
population.index.name = '城市'

print("城市人口数据:")
print(population)
print()

# 2. 找出人口最多和最少的城市
most_populated = population.idxmax()
least_populated = population.idxmin()
print(f"人口最多：{most_populated}，{population[most_populated]}万人")
print(f"人口最少：{least_populated}，{population[least_populated]}万人")
print()

# 3. 计算人口总和和平均值
total_pop = population.sum()
avg_pop = population.mean()
print(f"总人口：{total_pop}万人 ({total_pop/10000:.2f}亿人)")
print(f"平均人口：{avg_pop:.2f}万人")
print()

# 4. 找出人口超过2000万的城市
megacities = population[population > 2000]
print(f"人口超过2000万的超大城市（共{len(megacities)}个）:")
for city, pop in megacities.items():
    print(f"  {city}: {pop}万人")
print()

# 5. 按人口降序排列并显示排名
ranked = population.sort_values(ascending=False)
print("城市人口排名:")
for rank, (city, pop) in enumerate(ranked.items(), 1):
    # 添加徽章
    if rank == 1:
        badge = "🥇"
    elif rank == 2:
        badge = "🥈"
    elif rank == 3:
        badge = "🥉"
    else:
        badge = "  "
    print(f"{badge} {rank:2d}. {city:3s}: {pop:4d}万人")
```

---

### 练习5：商品销售分析

**题目**：分析商品销售数据：

1. 创建不同商品的销售数量Series
2. 创建对应的单价Series
3. 计算每种商品的销售额
4. 找出销售额最高的商品
5. 计算总销售额和平均销售额

**解答**：

```python
import pandas as pd

# 1. 创建销售数量Series
quantities = pd.Series({
    '苹果': 150,
    '香蕉': 200,
    '橙子': 120,
    '葡萄': 80,
    '西瓜': 50,
    '草莓': 100
})
quantities.name = '销售数量(斤)'

# 2. 创建单价Series
prices = pd.Series({
    '苹果': 5.5,
    '香蕉': 3.2,
    '橙子': 4.8,
    '葡萄': 8.9,
    '西瓜': 2.5,
    '草莓': 15.0
})
prices.name = '单价(元/斤)'

print("销售数据:")
print(quantities)
print("\n价格数据:")
print(prices)
print()

# 3. 计算销售额（索引会自动对齐）
revenue = quantities * prices
revenue.name = '销售额(元)'

print("各商品销售额:")
print(revenue)
print()

# 4. 找出销售额最高的商品
best_seller = revenue.idxmax()
print(f"销售额最高商品：{best_seller}")
print(f"  数量：{quantities[best_seller]}斤")
print(f"  单价：{prices[best_seller]}元/斤")
print(f"  销售额：{revenue[best_seller]:.2f}元")
print()

# 5. 计算总销售额和平均销售额
total_revenue = revenue.sum()
avg_revenue = revenue.mean()
print(f"总销售额：{total_revenue:.2f}元")
print(f"平均销售额：{avg_revenue:.2f}元")
print()

# 额外分析：销售额占比
revenue_pct = (revenue / total_revenue * 100).sort_values(ascending=False)
print("销售额占比:")
for product, pct in revenue_pct.items():
    bar = '█' * int(pct / 2)  # 简单的条形图
    print(f"{product:3s}: {pct:5.2f}% {bar}")
```

---

### 练习6：考试成绩等级划分

**题目**：处理学生考试成绩并划分等级：

1. 创建20名学生的成绩Series
2. 根据成绩划分等级（A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60）
3. 统计各等级的人数
4. 计算各等级的平均分
5. 找出需要补考的学生（F等级）

**解答**：

```python
import pandas as pd
import numpy as np

# 1. 创建学生成绩
np.random.seed(42)  # 固定随机种子，保证结果可复现
scores = pd.Series(
    np.random.randint(55, 100, size=20),
    index=[f'学生{i+1:02d}' for i in range(20)]
)
scores.name = '成绩'

print("学生成绩:")
print(scores)
print()

# 2. 划分等级
def grade_level(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grades = scores.apply(grade_level)
grades.name = '等级'

print("成绩等级:")
for student in scores.index:
    print(f"{student}: {scores[student]:3d}分 - {grades[student]}等")
print()

# 3. 统计各等级人数
grade_counts = grades.value_counts().sort_index()
print("各等级人数统计:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    count = grade_counts.get(grade, 0)
    bar = '█' * count
    print(f"{grade}等: {count:2d}人 {bar}")
print()

# 4. 计算各等级平均分
print("各等级平均分:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    students_in_grade = scores[grades == grade]
    if len(students_in_grade) > 0:
        avg = students_in_grade.mean()
        print(f"{grade}等: {avg:.2f}分")
    else:
        print(f"{grade}等: 无")
print()

# 5. 找出需要补考的学生
failed_students = scores[grades == 'F']
if len(failed_students) > 0:
    print(f"需要补考的学生（共{len(failed_students)}人）:")
    for student, score in failed_students.items():
        print(f"  {student}: {score}分")
else:
    print("没有学生需要补考！")
```

---

### 练习7：时间序列数据处理

**题目**：处理网站访问量时间序列数据：

1. 创建连续7天的网站访问量Series
2. 计算每日增长量和增长率
3. 找出访问量最高的一天
4. 计算7日平均访问量
5. 预测第8天的访问量（简单移动平均）

**解答**：

```python
import pandas as pd

# 1. 创建访问量数据
visits = pd.Series(
    [1523, 1687, 1854, 1792, 1956, 2134, 2287],
    index=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
)
visits.name = '访问量'
visits.index.name = '日期'

print("网站访问量:")
print(visits)
print()

# 2. 计算每日增长量和增长率
daily_change = visits.diff()
daily_pct_change = visits.pct_change() * 100

print("每日变化:")
for day in visits.index[1:]:
    change = daily_change[day]
    pct = daily_pct_change[day]
    symbol = "📈" if change > 0 else "📉"
    print(f"{day}: {change:+5.0f} ({pct:+.2f}%) {symbol}")
print()

# 3. 找出访问量最高的一天
peak_day = visits.idxmax()
peak_visits = visits[peak_day]
print(f"访问量最高：{peak_day}，{peak_visits}次")
print()

# 4. 计算7日平均访问量
avg_visits = visits.mean()
print(f"7日平均访问量：{avg_visits:.0f}次")
print()

# 5. 预测第8天访问量（3日移动平均）
last_3_days_avg = visits.tail(3).mean()
print(f"第8天预测访问量（基于最近3天平均）：{last_3_days_avg:.0f}次")

# 可视化趋势
print("\n访问量趋势图（简易版）:")
max_val = visits.max()
for day, count in visits.items():
    bar_length = int(count / max_val * 50)
    bar = '█' * bar_length
    print(f"{day}: {bar} {count}")
```

---

## 总结

恭喜你！你已经完成了Series数据结构的学习。让我们回顾一下学到的核心内容：

### 核心概念回顾

1. **Series是什么？**
   - 带标签的一维数组
   - 结合了Python字典和NumPy数组的优点
   - Pandas的基础数据结构

2. **Series的核心特性**：
   - **标签索引**：每个数据都有有意义的标签
   - **向量化运算**：支持快速的数学运算
   - **索引对齐**：运算时自动根据标签对齐
   - **缺失值处理**：完善的NaN处理机制

3. **创建Series的方法**：
   - 从列表创建：`pd.Series([1, 2, 3])`
   - 从字典创建：`pd.Series({'a': 1, 'b': 2})`
   - 从NumPy数组创建：`pd.Series(np.array([1, 2, 3]))`
   - 从标量创建：`pd.Series(100, index=['a', 'b'])`

4. **索引方法**：
   - 位置索引：`s.iloc[0]`
   - 标签索引：`s.loc['label']` 或 `s['label']`
   - 切片：`s.iloc[1:4]` 或 `s.loc['a':'c']`
   - 布尔索引：`s[s > 10]`
   - 多元素索引：`s[['a', 'b', 'c']]`

5. **常用属性**：
   - `values`: 数据值（NumPy数组）
   - `index`: 索引标签
   - `dtype`: 数据类型
   - `shape`: 形状
   - `size`: 元素个数

6. **常用方法**：
   - 查看：`head()`, `tail()`, `describe()`
   - 统计：`mean()`, `median()`, `std()`, `max()`, `min()`
   - 排序：`sort_values()`, `sort_index()`
   - 查找：`idxmax()`, `idxmin()`, `nlargest()`, `nsmallest()`
   - 唯一值：`unique()`, `nunique()`, `value_counts()`

7. **运算**：
   - 算术运算：`+`, `-`, `*`, `/`, `**`
   - 比较运算：`>`, `<`, `>=`, `<=`, `==`, `!=`
   - 逻辑运算：`&` (AND), `|` (OR), `~` (NOT)

8. **缺失值处理**：
   - 检测：`isna()`, `notna()`, `hasnans`
   - 删除：`dropna()`
   - 填充：`fillna()`, `interpolate()`
   - 替换：`replace()`

### Series vs 其他数据结构

| 特性 | Python列表 | Python字典 | NumPy数组 | Pandas Series |
|------|-----------|-----------|----------|--------------|
| 有标签 | | | | |
| 向量化运算 | | | | |
| 位置索引 | | | | |
| 标签索引 | | | | |
| 索引对齐 | | | | |
| 缺失值处理 | | | 部分 | |
| 数据分析方法 | | | 基本 | 丰富 |
| 适用场景 | 通用 | 键值对 | 科学计算 | 数据分析 |

### 学习建议

1. **多练习**：通过实际数据练习Series的各种操作
2. **理解标签索引**：这是Series最重要的特性
3. **掌握布尔索引**：数据筛选的核心技能
4. **熟悉常用方法**：describe()、value_counts()等
5. **理解索引对齐**：Series运算的关键机制

### 下一步

学完Series后，你可以继续学习：

1. **DataFrame**：Pandas的二维数据结构（多个Series的集合）
2. **数据读写**：CSV、Excel、SQL等格式的读写
3. **数据清洗**：处理重复值、异常值、格式转换
4. **数据分组**：groupby操作和聚合
5. **时间序列**：处理日期时间数据
6. **数据可视化**：用matplotlib和seaborn绘图

Series是Pandas的基础，掌握好Series，学习DataFrame会非常顺利！

---

## 参考资源

- Pandas官方文档：https://pandas.pydata.org/docs/
- Pandas用户指南：https://pandas.pydata.org/docs/user_guide/index.html
- Series API文档：https://pandas.pydata.org/docs/reference/series.html

数据分析之路才刚刚开始！
