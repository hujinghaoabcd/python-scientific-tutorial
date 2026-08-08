# 第02章：NumPy数组基础

在上一章，我们初步认识了NumPy这个强大的科学计算库。这一章，我们要深入学习NumPy的核心——数组（ndarray）。这是NumPy最重要的概念，也是数据分析和科学计算的基础。

学完这一章，你会明白为什么NumPy数组比Python列表快那么多，以及如何正确地使用数组来处理数据。

---

## 什么是ndarray？

### 生活化理解

想象一下你在超市整理货架。Python的列表就像一个购物袋，你可以往里面随便扔东西：苹果、牛奶、洗发水，什么都能装，但找东西很慢。

而NumPy的ndarray（N-dimensional array，N维数组）就像一个**有序的格子柜**：
- 每个格子大小一样
- 所有格子只能装同一类型的东西（比如只能装数字）
- 格子按顺序排列，可以快速找到任何一个格子
- 可以是一排格子（一维）、一个平面的格子（二维）、或者立体的格子（三维）

**为什么要用格子柜而不是购物袋？**

因为整齐排列、类型统一的格子柜，可以让我们：
- 快速找到任何一个格子
- 一次性对所有格子做相同操作
- 节省空间（不需要记录每个东西是什么类型）
- 用硬件加速（CPU/GPU可以并行处理）

### 技术定义

ndarray是NumPy的核心数据结构，它是一个：
- **同质化**的多维数组（所有元素类型相同）
- **固定大小**的数组（创建后大小不可变）
- **高效存储**的数组（内存连续存储）
- **支持向量化**运算的数组（可以批量计算）

### 第一个数组

让我们创建第一个NumPy数组，感受一下它的魅力：

```python
import numpy as np

# 创建一个简单的一维数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# 输出：[1 2 3 4 5]

print(type(arr))
# 输出：<class 'numpy.ndarray'>

# 创建一个二维数组（矩阵）
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix)
# 输出：
# [[1 2 3]
#  [4 5 6]]
```

看到了吗？创建数组就是这么简单！用`np.array()`函数，把Python列表转换成NumPy数组。

---

## 数组 vs 列表：详细对比

很多初学者会问：既然Python已经有列表了，为什么还要用NumPy数组？

让我们从多个角度详细比较一下：

### 速度对比

NumPy数组的速度是Python列表的10-100倍！让我们实际测试一下：

```python
import numpy as np
import time

# 创建大数据
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# 测试Python列表
start = time.time()
result_list = [x * 2 for x in python_list]
list_time = time.time() - start

# 测试NumPy数组
start = time.time()
result_array = numpy_array * 2
array_time = time.time() - start

print(f"Python列表时间：{list_time:.4f}秒")
print(f"NumPy数组时间：{array_time:.4f}秒")
print(f"NumPy快了：{list_time / array_time:.1f}倍")

# 输出示例：
# Python列表时间：0.1234秒
# NumPy数组时间：0.0012秒
# NumPy快了：102.8倍
```

**为什么NumPy这么快？**
1. **内存连续存储**：数组元素在内存中紧密排列，CPU可以快速访问
2. **类型统一**：不需要检查每个元素的类型，减少开销
3. **向量化运算**：底层用C语言实现，利用CPU的SIMD指令并行计算
4. **避免Python循环**：不需要Python的for循环，减少解释开销

### 内存对比

NumPy数组比Python列表更节省内存：

```python
import sys
import numpy as np

# 创建相同的数据
size = 1000
python_list = list(range(size))
numpy_array = np.arange(size)

# 计算内存占用
list_memory = sys.getsizeof(python_list)
array_memory = numpy_array.nbytes

print(f"Python列表内存：{list_memory:,} 字节")
print(f"NumPy数组内存：{array_memory:,} 字节")
print(f"节省了：{(1 - array_memory/list_memory)*100:.1f}%")

# 输出示例：
# Python列表内存：8,056 字节
# NumPy数组内存：8,000 字节
# 节省了：0.7%（对于大数组，差异会更明显）
```

### 功能对比表

| 特性 | Python列表 | NumPy数组 |
|------|-----------|----------|
| **数据类型** | 可以混合类型 | 必须相同类型 |
| **大小** | 可以动态改变 | 创建后固定 |
| **速度** | 较慢（解释执行） | 很快（C语言实现） |
| **内存** | 占用较多 | 占用较少 |
| **运算** | 需要循环 | 支持向量化 |
| **多维** | 需要嵌套列表 | 原生支持 |
| **数学运算** | 不支持 | 丰富的数学函数 |
| **适用场景** | 通用数据存储 | 科学计算、数据分析 |

### 使用场景对比

**什么时候用Python列表？**
- 存储不同类型的数据（如混合字符串和数字）
- 需要频繁添加/删除元素
- 数据量较小
- 不需要复杂的数学运算

```python
# 适合用列表的例子
shopping_cart = ["苹果", 3, "香蕉", 5, "牛奶", 2]  # 混合类型
todo_list = []
todo_list.append("买菜")  # 频繁添加
todo_list.append("洗衣服")
```

**什么时候用NumPy数组？**
- 存储数值数据（整数、浮点数）
- 需要快速的数学运算
- 处理大量数据
- 多维数据（矩阵、张量）
- 科学计算、数据分析、机器学习

```python
import numpy as np

# 适合用数组的例子
temperatures = np.array([25.3, 26.1, 24.8, 27.2, 25.9])  # 温度数据
image = np.zeros((1920, 1080, 3))  # 图像数据（高×宽×颜色通道）
matrix = np.array([[1, 2], [3, 4]])  # 矩阵运算
```

### 代码对比示例

让我们看一个实际的例子，比较两者的写法：

```python
import numpy as np

# 场景：计算一组数的平方，然后求和

# 方法1：Python列表（需要循环）
numbers_list = [1, 2, 3, 4, 5]
squares_list = []
for num in numbers_list:
    squares_list.append(num ** 2)
total = sum(squares_list)
print(f"列表方法结果：{total}")  # 55

# 方法2：NumPy数组（向量化，一行搞定）
numbers_array = np.array([1, 2, 3, 4, 5])
total = (numbers_array ** 2).sum()
print(f"数组方法结果：{total}")  # 55

# 更复杂的例子：计算两组数的欧几里得距离
# 距离 = sqrt((x2-x1)² + (y2-y1)² + ...)

# Python列表方法（繁琐）
point1 = [1, 2, 3]
point2 = [4, 5, 6]
distance = 0
for i in range(len(point1)):
    distance += (point2[i] - point1[i]) ** 2
distance = distance ** 0.5
print(f"距离：{distance:.2f}")  # 5.20

# NumPy数组方法（简洁）
point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
distance = np.sqrt(((point2 - point1) ** 2).sum())
print(f"距离：{distance:.2f}")  # 5.20

# 或者更简洁
distance = np.linalg.norm(point2 - point1)
print(f"距离：{distance:.2f}")  # 5.20
```

---

## 一维数组：最简单的数组

一维数组就像一条项链，珠子一个接一个排列。这是最简单、最基础的数组形式。

### 创建一维数组

有很多种方式可以创建一维数组：

```python
import numpy as np

# 方法1：从Python列表创建
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 方法2：用arange创建（类似Python的range）
arr2 = np.arange(10)  # 0到9
print(arr2)  # [0 1 2 3 4 5 6 7 8 9]

arr3 = np.arange(5, 15)  # 5到14
print(arr3)  # [ 5  6  7  8  9 10 11 12 13 14]

arr4 = np.arange(0, 10, 2)  # 0到10，步长为2
print(arr4)  # [0 2 4 6 8]

# 方法3：用linspace创建（指定数量）
arr5 = np.linspace(0, 10, 5)  # 0到10，均匀分成5个数
print(arr5)  # [ 0.   2.5  5.   7.5 10. ]

# 方法4：创建全0或全1数组
zeros = np.zeros(5)
print(zeros)  # [0. 0. 0. 0. 0.]

ones = np.ones(5)
print(ones)  # [1. 1. 1. 1. 1.]

# 方法5：创建指定值的数组
fives = np.full(5, 5.0)
print(fives)  # [5. 5. 5. 5. 5.]

# 方法6：创建随机数组
random_arr = np.random.random(5)  # 0-1之间的随机数
print(random_arr)  # [0.123 0.456 0.789 0.234 0.567]（每次不同）

random_int = np.random.randint(0, 100, 5)  # 0-100之间的随机整数
print(random_int)  # [23 67 89 12 45]（每次不同）
```

### 一维数组的属性

每个数组都有一些属性，告诉我们数组的信息：

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 维度数（几维数组）
print(arr.ndim)  # 1（一维）

# 形状（每个维度的大小）
print(arr.shape)  # (5,)（有5个元素）

# 元素总数
print(arr.size)  # 5

# 数据类型
print(arr.dtype)  # int64（64位整数）

# 每个元素的字节数
print(arr.itemsize)  # 8（8字节 = 64位）

# 总字节数
print(arr.nbytes)  # 40（5个元素 × 8字节）
```

### 一维数组的索引和切片

和Python列表一样，数组也可以用索引访问元素：

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 正向索引（从0开始）
print(arr[0])  # 10（第一个元素）
print(arr[2])  # 30（第三个元素）

# 反向索引（从-1开始）
print(arr[-1])  # 50（最后一个元素）
print(arr[-2])  # 40（倒数第二个元素）

# 切片（和列表一样）
print(arr[1:4])  # [20 30 40]（索引1到3）
print(arr[:3])   # [10 20 30]（前3个）
print(arr[2:])   # [30 40 50]（从索引2到末尾）
print(arr[::2])  # [10 30 50]（每隔2个）
print(arr[::-1]) # [50 40 30 20 10]（反转）

# 修改元素
arr[0] = 100
print(arr)  # [100  20  30  40  50]

# 修改切片
arr[1:3] = [200, 300]
print(arr)  # [100 200 300  40  50]
```

### 一维数组的基本运算

数组可以直接进行数学运算，这叫**向量化运算**：

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 数组和标量运算（每个元素都参与运算）
print(arr + 10)  # [11 12 13 14 15]
print(arr - 5)   # [-4 -3 -2 -1  0]
print(arr * 2)   # [ 2  4  6  8 10]
print(arr / 2)   # [0.5 1.  1.5 2.  2.5]
print(arr ** 2)  # [ 1  4  9 16 25]

# 数组和数组运算（对应元素相运算）
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(arr1 + arr2)  # [11 22 33 44 55]
print(arr1 * arr2)  # [ 10  40  90 160 250]

# 数学函数
print(np.sqrt(arr))  # [1.         1.41421356 1.73205081 2.         2.23606798]
print(np.exp(arr))   # [ 2.71828183  7.3890561  20.08553692 54.59815003 148.4131591 ]
print(np.sin(arr))   # [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]

# 统计函数
print(arr.sum())   # 15（求和）
print(arr.mean())  # 3.0（平均值）
print(arr.max())   # 5（最大值）
print(arr.min())   # 1（最小值）
print(arr.std())   # 1.414...（标准差）
```

### 一维数组的实际应用

让我们看一些实际的例子：

```python
import numpy as np

# 例子1：计算学生成绩统计
scores = np.array([85, 92, 78, 90, 88, 95, 82, 89])

print(f"最高分：{scores.max()}")
print(f"最低分：{scores.min()}")
print(f"平均分：{scores.mean():.2f}")
print(f"中位数：{np.median(scores):.2f}")
print(f"标准差：{scores.std():.2f}")

# 找出高于平均分的成绩
above_avg = scores[scores > scores.mean()]
print(f"高于平均分的成绩：{above_avg}")

# 例子2：温度数据处理
temperatures = np.array([25.3, 26.1, 24.8, 27.2, 25.9, 26.5, 25.1])

# 摄氏度转华氏度：F = C * 9/5 + 32
fahrenheit = temperatures * 9/5 + 32
print(f"华氏温度：{fahrenheit}")

# 找出高温天数
hot_days = (temperatures > 26).sum()
print(f"超过26度的天数：{hot_days}天")

# 例子3：股票价格分析
prices = np.array([100, 102, 98, 105, 110, 108, 112])

# 计算每日涨跌幅
daily_returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100
print(f"每日涨跌幅：{daily_returns}")
print(f"平均涨跌幅：{daily_returns.mean():.2f}%")
```

---

## 二维数组：像电子表格一样

二维数组就像一个表格或矩阵，有行和列。想象成Excel电子表格就对了！

### 理解二维数组

```
     列0  列1  列2
行0  [ 1   2   3 ]
行1  [ 4   5   6 ]
行2  [ 7   8   9 ]
```

这就是一个3×3的二维数组，有3行3列，共9个元素。

### 创建二维数组

```python
import numpy as np

# 方法1：从嵌套列表创建
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 方法2：创建全0或全1矩阵
zeros = np.zeros((3, 4))  # 3行4列的全0矩阵
print(zeros)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

ones = np.ones((2, 5))  # 2行5列的全1矩阵
print(ones)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# 方法3：创建单位矩阵（对角线为1，其他为0）
identity = np.eye(3)
print(identity)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 方法4：创建对角矩阵
diag = np.diag([1, 2, 3, 4])
print(diag)
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

# 方法5：创建随机矩阵
random_matrix = np.random.randint(0, 10, (3, 3))  # 3×3随机整数矩阵
print(random_matrix)

# 方法6：用arange + reshape创建
arr = np.arange(12).reshape(3, 4)  # 0-11重塑成3×4
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

### 二维数组的属性

```python
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 维度数
print(arr.ndim)  # 2（二维）

# 形状（行数，列数）
print(arr.shape)  # (3, 4)（3行4列）

# 元素总数
print(arr.size)  # 12（3×4=12个元素）

# 数据类型
print(arr.dtype)  # int64

# 查看每个维度的大小
rows, cols = arr.shape
print(f"行数：{rows}，列数：{cols}")  # 行数：3，列数：4
```

### 二维数组的索引

二维数组的索引需要两个数字：`[行索引, 列索引]`

```python
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 访问单个元素（行，列）
print(arr[0, 0])  # 1（第1行第1列）
print(arr[0, 2])  # 3（第1行第3列）
print(arr[1, 3])  # 8（第2行第4列）
print(arr[-1, -1])  # 12（最后一行最后一列）

# 访问整行
print(arr[0])  # [1 2 3 4]（第1行）
print(arr[1])  # [5 6 7 8]（第2行）
print(arr[0, :])  # [1 2 3 4]（第1行，更明确的写法）

# 访问整列
print(arr[:, 0])  # [1 5 9]（第1列）
print(arr[:, 2])  # [ 3  7 11]（第3列）

# 访问子矩阵（切片）
print(arr[0:2, 1:3])
# [[2 3]
#  [6 7]]（前2行，第2-3列）

print(arr[:2, :2])
# [[1 2]
#  [5 6]]（左上角2×2子矩阵）

# 修改元素
arr[0, 0] = 100
print(arr)
# [[100   2   3   4]
#  [  5   6   7   8]
#  [  9  10  11  12]]

# 修改整行
arr[1] = [50, 60, 70, 80]
print(arr)

# 修改整列
arr[:, 0] = [1, 2, 3]
print(arr)
```

### 二维数组的运算

```python
import numpy as np

# 创建两个矩阵
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 元素级运算（对应元素相运算）
print("A + B：")
print(A + B)
# [[ 6  8]
#  [10 12]]

print("A * B：")
print(A * B)
# [[ 5 12]
#  [21 32]]

# 矩阵乘法（线性代数中的矩阵乘法）
print("A @ B：")
print(A @ B)  # 或 np.dot(A, B)
# [[19 22]
#  [43 50]]

# 转置（行列互换）
print("A的转置：")
print(A.T)
# [[1 3]
#  [2 4]]

# 统计函数
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.sum())  # 21（所有元素之和）
print(arr.sum(axis=0))  # [5 7 9]（每列的和）
print(arr.sum(axis=1))  # [ 6 15]（每行的和）

print(arr.mean())  # 3.5（所有元素的平均值）
print(arr.mean(axis=0))  # [2.5 3.5 4.5]（每列的平均值）
print(arr.mean(axis=1))  # [2. 5.]（每行的平均值）
```

### 理解axis参数

`axis`参数很重要但容易混淆，让我们详细理解一下：

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("原数组：")
print(arr)
# [[1 2 3]
#  [4 5 6]]

# axis=0：沿着第0维（行方向）操作，结果是每列的统计
print("\naxis=0（按列统计）：")
print(arr.sum(axis=0))  # [5 7 9]
# 相当于：[1+4, 2+5, 3+6]

# axis=1：沿着第1维（列方向）操作，结果是每行的统计
print("\naxis=1（按行统计）：")
print(arr.sum(axis=1))  # [ 6 15]
# 相当于：[1+2+3, 4+5+6]
```

**记忆技巧**：
- `axis=0`：想象数组沿着行方向"压扁"，得到每列的结果
- `axis=1`：想象数组沿着列方向"压扁"，得到每行的结果

用图形理解：
```
原数组（2行3列）：
[[1 2 3]
 [4 5 6]]

axis=0（按列）：     axis=1（按行）：
↓  ↓  ↓            →
[5 7 9]            [ 6]
                   [15]
```

### 二维数组的实际应用

```python
import numpy as np

# 例子1：学生成绩表（行=学生，列=科目）
scores = np.array([[85, 92, 78],  # 学生1：语文、数学、英语
                   [90, 88, 95],  # 学生2
                   [82, 89, 91],  # 学生3
                   [95, 85, 88]]) # 学生4

print("成绩表：")
print(scores)

# 每个学生的总分
total_scores = scores.sum(axis=1)
print(f"\n每个学生的总分：{total_scores}")

# 每个学生的平均分
avg_scores = scores.mean(axis=1)
print(f"每个学生的平均分：{avg_scores}")

# 每个科目的平均分
subject_avg = scores.mean(axis=0)
print(f"各科平均分：{subject_avg}")

# 找出最高分和最低分
print(f"最高分：{scores.max()}")
print(f"最低分：{scores.min()}")

# 例子2：图像处理（灰度图）
# 假设这是一个5×5的灰度图像（0-255）
image = np.array([[100, 120, 130, 140, 150],
                  [110, 125, 135, 145, 155],
                  [115, 130, 140, 150, 160],
                  [120, 135, 145, 155, 165],
                  [125, 140, 150, 160, 170]])

print("\n原始图像：")
print(image)

# 增加亮度（每个像素+50）
brighter = image + 50
print("\n增加亮度后：")
print(brighter)

# 降低对比度（乘以0.5）
lower_contrast = image * 0.5
print("\n降低对比度后：")
print(lower_contrast)

# 例子3：销售数据分析（行=月份，列=产品）
sales = np.array([[100, 120, 80, 90],   # 1月
                  [110, 130, 85, 95],   # 2月
                  [120, 125, 90, 100],  # 3月
                  [130, 140, 95, 105]]) # 4月

print("\n销售数据（行=月份，列=产品）：")
print(sales)

# 每个月的总销量
monthly_total = sales.sum(axis=1)
print(f"每月总销量：{monthly_total}")

# 每个产品的总销量
product_total = sales.sum(axis=0)
print(f"各产品总销量：{product_total}")

# 增长率（月度环比）
growth_rate = (sales[1:] - sales[:-1]) / sales[:-1] * 100
print(f"\n月度增长率（%）：")
print(growth_rate)
```

---

## 三维数组：立体的数据结构

如果说一维数组是一条线，二维数组是一个平面，那么三维数组就是一个立方体！

### 理解三维数组

想象一本书：
- 一维数组：一行字
- 二维数组：一页纸（有行有列）
- 三维数组：一本书（有很多页，每页都是一个二维数组）

或者想象一个彩色图片：
- 高度（行数）
- 宽度（列数）
- 颜色通道（红、绿、蓝）

```python
# 一个2×3×4的三维数组
# 可以理解为：2页，每页是3×4的表格

       第0页            第1页
    [[ 1  2  3  4]   [[13 14 15 16]
     [ 5  6  7  8]    [17 18 19 20]
     [ 9 10 11 12]]   [21 22 23 24]]
```

### 创建三维数组

```python
import numpy as np

# 方法1：从嵌套列表创建
arr3d = np.array([[[1, 2, 3],
                   [4, 5, 6]],

                  [[7, 8, 9],
                   [10, 11, 12]]])

print("三维数组形状：", arr3d.shape)  # (2, 2, 3)
print(arr3d)

# 方法2：用zeros或ones创建
zeros3d = np.zeros((2, 3, 4))  # 2页，每页3×4
print("三维全0数组：")
print(zeros3d.shape)  # (2, 3, 4)

# 方法3：用arange + reshape创建
arr = np.arange(24).reshape(2, 3, 4)  # 24个数重塑成2×3×4
print("用reshape创建：")
print(arr)
print("形状：", arr.shape)  # (2, 3, 4)

# 方法4：随机数组
random3d = np.random.randint(0, 100, (2, 3, 4))
print("随机三维数组：")
print(random3d)
```

### 三维数组的索引

三维数组需要三个索引：`[页/深度, 行, 列]`

```python
import numpy as np

arr = np.arange(24).reshape(2, 3, 4)
print("原数组：")
print(arr)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# 访问单个元素
print(arr[0, 0, 0])  # 0（第1页，第1行，第1列）
print(arr[1, 2, 3])  # 23（第2页，第3行，第4列）

# 访问一页（一个二维数组）
print("第1页：")
print(arr[0])
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 访问某一页的某一行
print("第2页第1行：")
print(arr[1, 0])  # [12 13 14 15]

# 访问所有页的同一位置
print("所有页的第1行第1列：")
print(arr[:, 0, 0])  # [ 0 12]

# 切片
print("前1页，前2行，前3列：")
print(arr[:1, :2, :3])
```

### 三维数组的实际应用

```python
import numpy as np

# 例子1：彩色图像（最常见的三维数组应用）
# 形状：(高度, 宽度, 颜色通道)
# 颜色通道：0=红色，1=绿色，2=蓝色

# 创建一个5×5的彩色图像
image = np.zeros((5, 5, 3), dtype=np.uint8)

# 把左上角设为红色
image[0:2, 0:2, 0] = 255  # 红色通道设为最大值

# 把右上角设为绿色
image[0:2, 3:5, 1] = 255  # 绿色通道设为最大值

# 把左下角设为蓝色
image[3:5, 0:2, 2] = 255  # 蓝色通道设为最大值

print("图像形状：", image.shape)  # (5, 5, 3)
print("图像大小：", image.size, "个像素点")  # 75（5×5×3）

# 提取红色通道
red_channel = image[:, :, 0]
print("红色通道：")
print(red_channel)

# 例子2：视频数据（帧×高度×宽度×颜色）
# 10帧，每帧100×100×3
video = np.random.randint(0, 256, (10, 100, 100, 3), dtype=np.uint8)
print("视频形状：", video.shape)  # (10, 100, 100, 3)
print("第一帧的形状：", video[0].shape)  # (100, 100, 3)

# 例子3：时间序列数据
# 形状：(天数, 小时, 传感器数量)
# 7天，每天24小时，3个传感器
sensor_data = np.random.randn(7, 24, 3)
print("传感器数据形状：", sensor_data.shape)  # (7, 24, 3)

# 计算每天每个传感器的平均值
daily_avg = sensor_data.mean(axis=1)  # 在小时维度上求平均
print("每天平均值形状：", daily_avg.shape)  # (7, 3)
```

### 维度变换

三维数组经常需要改变维度顺序或形状：

```python
import numpy as np

# 创建一个3×4×5的数组
arr = np.arange(60).reshape(3, 4, 5)
print("原形状：", arr.shape)  # (3, 4, 5)

# reshape：改变形状（元素总数不变）
reshaped = arr.reshape(4, 5, 3)
print("reshape后：", reshaped.shape)  # (4, 5, 3)

# transpose：转置（交换维度）
transposed = arr.transpose(2, 1, 0)  # 第2维变第0维，第1维不变，第0维变第2维
print("transpose后：", transposed.shape)  # (5, 4, 3)

# 对于图像数据，经常需要调整通道顺序
# (高度, 宽度, 通道) -> (通道, 高度, 宽度)
image = np.random.rand(224, 224, 3)
image_transposed = image.transpose(2, 0, 1)
print("图像原形状：", image.shape)  # (224, 224, 3)
print("转置后形状：", image_transposed.shape)  # (3, 224, 224)
```

---

## 数组的数据类型（dtype详解）

数据类型（dtype）决定了数组中存储的是什么类型的数据，以及每个元素占用多少内存。

### 为什么数据类型很重要？

1. **内存占用**：不同类型占用不同内存
2. **计算精度**：浮点数有不同的精度
3. **运算速度**：整数运算比浮点数快
4. **数据范围**：不同类型能表示的数据范围不同

### 常用数据类型

```python
import numpy as np

# 整数类型
int8 = np.array([1, 2, 3], dtype=np.int8)    # 8位整数（-128到127）
int16 = np.array([1, 2, 3], dtype=np.int16)  # 16位整数（-32768到32767）
int32 = np.array([1, 2, 3], dtype=np.int32)  # 32位整数
int64 = np.array([1, 2, 3], dtype=np.int64)  # 64位整数（默认）

# 无符号整数（只能表示非负数）
uint8 = np.array([1, 2, 3], dtype=np.uint8)   # 0到255（常用于图像）
uint16 = np.array([1, 2, 3], dtype=np.uint16) # 0到65535
uint32 = np.array([1, 2, 3], dtype=np.uint32)
uint64 = np.array([1, 2, 3], dtype=np.uint64)

# 浮点数类型
float16 = np.array([1.0, 2.0, 3.0], dtype=np.float16)  # 半精度（很少用）
float32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)  # 单精度
float64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)  # 双精度（默认）

# 布尔类型
bool_arr = np.array([True, False, True], dtype=np.bool_)

# 复数类型
complex64 = np.array([1+2j, 3+4j], dtype=np.complex64)
complex128 = np.array([1+2j, 3+4j], dtype=np.complex128)

# 字符串类型
str_arr = np.array(['hello', 'world'], dtype='U10')  # Unicode字符串，最长10个字符
```

### 数据类型对比表

| 类型 | 说明 | 字节数 | 范围 | 适用场景 |
|------|------|--------|------|---------|
| `int8` | 8位整数 | 1 | -128 到 127 | 很小的整数 |
| `int16` | 16位整数 | 2 | -32768 到 32767 | 小整数 |
| `int32` | 32位整数 | 4 | -2^31 到 2^31-1 | 一般整数 |
| `int64` | 64位整数 | 8 | -2^63 到 2^63-1 | 大整数（默认） |
| `uint8` | 无符号8位 | 1 | 0 到 255 | 图像像素值 |
| `float32` | 单精度浮点 | 4 | ±1.4E-45 到 ±3.4E38 | 深度学习 |
| `float64` | 双精度浮点 | 8 | ±5.0E-324 到 ±1.7E308 | 科学计算（默认） |
| `bool_` | 布尔值 | 1 | True/False | 逻辑运算 |
| `complex128` | 复数 | 16 | - | 科学计算 |

### 查看和修改数据类型

```python
import numpy as np

# 创建数组时自动推断类型
arr1 = np.array([1, 2, 3])
print(arr1.dtype)  # int64

arr2 = np.array([1.0, 2.0, 3.0])
print(arr2.dtype)  # float64

arr3 = np.array([True, False])
print(arr3.dtype)  # bool

# 显式指定类型
arr4 = np.array([1, 2, 3], dtype=np.float32)
print(arr4.dtype)  # float32
print(arr4)  # [1. 2. 3.]

# 转换类型
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.dtype)  # int32

# astype：创建新数组并转换类型
arr_float = arr.astype(np.float64)
print(arr_float.dtype)  # float64
print(arr_float)  # [1. 2. 3.]

# 浮点转整数（会截断小数）
arr_float = np.array([1.9, 2.5, 3.1])
arr_int = arr_float.astype(np.int32)
print(arr_int)  # [1 2 3]（小数被截断）
```

### 数据类型的选择

**什么时候用整数？**
- 计数、索引
- 不需要小数的数据
- 内存有限时（整数比浮点数省内存）

```python
# 计数
counts = np.array([10, 20, 30], dtype=np.int32)

# 图像像素（0-255）
image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
```

**什么时候用float32？**
- 深度学习（GPU计算更快）
- 内存有限但需要小数
- 精度要求不高的场景

```python
# 深度学习权重
weights = np.random.randn(1000, 1000).astype(np.float32)
```

**什么时候用float64？**
- 科学计算（需要高精度）
- 金融计算
- 默认选择

```python
# 科学计算
import numpy as np
x = np.linspace(0, 2*np.pi, 1000)  # 默认float64
y = np.sin(x)  # 高精度
```

**什么时候用uint8？**
- 图像处理（像素值0-255）
- 需要节省内存
- 只存储非负小整数

```python
# 图像数据
image = np.zeros((1920, 1080, 3), dtype=np.uint8)  # RGB图像
```

### 内存和性能对比

```python
import numpy as np
import sys

# 创建相同数据，不同类型
size = 1000000

arr_int64 = np.arange(size, dtype=np.int64)
arr_int32 = np.arange(size, dtype=np.int32)
arr_int8 = np.arange(size, dtype=np.int8)

print("int64内存：", arr_int64.nbytes / 1024 / 1024, "MB")  # ~7.6 MB
print("int32内存：", arr_int32.nbytes / 1024 / 1024, "MB")  # ~3.8 MB
print("int8内存：", arr_int8.nbytes / 1024 / 1024, "MB")    # ~1 MB

# 浮点数对比
arr_float64 = np.random.random(size)
arr_float32 = np.random.random(size).astype(np.float32)

print("float64内存：", arr_float64.nbytes / 1024 / 1024, "MB")  # ~7.6 MB
print("float32内存：", arr_float32.nbytes / 1024 / 1024, "MB")  # ~3.8 MB

# 性能测试
import time

def time_operation(arr, operation):
    start = time.time()
    for _ in range(100):
        result = operation(arr)
    return time.time() - start

arr64 = np.random.random(1000000)
arr32 = arr64.astype(np.float32)

time64 = time_operation(arr64, lambda x: x * 2 + 1)
time32 = time_operation(arr32, lambda x: x * 2 + 1)

print(f"float64时间：{time64:.4f}秒")
print(f"float32时间：{time32:.4f}秒")
print(f"float32快了：{time64/time32:.2f}倍")
```

### 类型转换的注意事项

```python
import numpy as np

# 1. 浮点转整数会丢失精度
arr_float = np.array([1.1, 2.9, 3.5, 4.8])
arr_int = arr_float.astype(np.int32)
print(arr_int)  # [1 2 3 4]（小数部分丢失）

# 2. 整数溢出
arr = np.array([200], dtype=np.int8)  # int8最大127
arr = arr + 100  # 溢出！
print(arr)  # [-56]（发生了溢出）

# 正确做法：用更大的类型
arr = np.array([200], dtype=np.int16)
arr = arr + 100
print(arr)  # [300]

# 3. 精度损失
arr = np.array([1.123456789012345], dtype=np.float64)
print(arr)  # [1.12345679]（float64精度）

arr32 = arr.astype(np.float32)
print(arr32)  # [1.1234568]（float32精度更低）

# 4. 布尔转数字
bool_arr = np.array([True, False, True])
num_arr = bool_arr.astype(np.int32)
print(num_arr)  # [1 0 1]（True变1，False变0）

# 5. 字符串转数字
str_arr = np.array(['1', '2', '3'])
num_arr = str_arr.astype(np.int32)
print(num_arr)  # [1 2 3]
```

---

## 数组的维度理解（axis概念详解）

`axis`是NumPy中最重要但最容易混淆的概念之一。很多初学者在这里卡住了，让我们用最通俗的方式理解它！

### axis的本质

**axis就是"沿着哪个方向操作"的意思。**

想象你在看一个表格：
- `axis=0`：沿着行的方向（垂直方向，从上到下）
- `axis=1`：沿着列的方向（水平方向，从左到右）

### 一维数组的axis

一维数组只有一个轴（axis=0）：

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 一维数组只有axis=0
print(arr.sum(axis=0))  # 15（等同于arr.sum()）
print(arr.mean(axis=0))  # 3.0
```

### 二维数组的axis

二维数组有两个轴：axis=0（行）和axis=1（列）

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("原数组：")
print(arr)
# [[1 2 3]
#  [4 5 6]]

# 不指定axis：对所有元素操作
print("所有元素之和：", arr.sum())  # 21

# axis=0：沿着行方向（垂直），对每列操作
print("axis=0（每列的和）：", arr.sum(axis=0))  # [5 7 9]
# 解释：第1列=1+4=5，第2列=2+5=7，第3列=3+6=9

# axis=1：沿着列方向（水平），对每行操作
print("axis=1（每行的和）：", arr.sum(axis=1))  # [ 6 15]
# 解释：第1行=1+2+3=6，第2行=4+5+6=15
```

### 记忆技巧：折叠法

想象把数组沿着某个轴"折叠"起来：

```python
原数组：
[[1 2 3]
 [4 5 6]]

axis=0（沿着行折叠，压扁成一行）：
  ↓ ↓ ↓
[5 7 9]

axis=1（沿着列折叠，压扁成一列）：
→ [ 6]
→ [15]
```

### 三维数组的axis

三维数组有三个轴：axis=0、axis=1、axis=2

```python
import numpy as np

# 创建一个2×3×4的数组
arr = np.arange(24).reshape(2, 3, 4)
print("形状：", arr.shape)  # (2, 3, 4)
print(arr)

# axis=0：沿着"页"方向（深度）
result0 = arr.sum(axis=0)
print("axis=0结果形状：", result0.shape)  # (3, 4)
# 把2页叠在一起，剩下3×4

# axis=1：沿着"行"方向
result1 = arr.sum(axis=1)
print("axis=1结果形状：", result1.shape)  # (2, 4)
# 每页的3行压扁，剩下2页×4列

# axis=2：沿着"列"方向
result2 = arr.sum(axis=2)
print("axis=2结果形状：", result2.shape)  # (2, 3)
# 每行的4列压扁，剩下2页×3行
```

### axis=-1的含义

`axis=-1`表示最后一个轴：

```python
import numpy as np

# 二维数组
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d.sum(axis=-1))  # 等同于axis=1

# 三维数组
arr3d = np.arange(24).reshape(2, 3, 4)
print(arr3d.sum(axis=-1).shape)  # 等同于axis=2
```

### 实际应用：理解axis的重要性

```python
import numpy as np

# 例子1：计算每个学生的平均分
scores = np.array([[85, 92, 78],  # 学生1
                   [90, 88, 95],  # 学生2
                   [82, 89, 91]]) # 学生3

# 每个学生的平均分（每行的平均）
student_avg = scores.mean(axis=1)
print("每个学生的平均分：", student_avg)
# [85.  91.  87.33]

# 每个科目的平均分（每列的平均）
subject_avg = scores.mean(axis=0)
print("每个科目的平均分：", subject_avg)
# [85.67 89.67 88.  ]

# 例子2：图像处理
# 假设image形状是(高度, 宽度, 通道)
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# 转成灰度图（对通道求平均）
gray = image.mean(axis=2)  # 沿着通道方向求平均
print("灰度图形状：", gray.shape)  # (100, 100)

# 例子3：时间序列数据
# 形状：(天数, 小时, 传感器)
data = np.random.randn(7, 24, 3)

# 每天的平均值（对小时求平均）
daily_avg = data.mean(axis=1)
print("每天平均值形状：", daily_avg.shape)  # (7, 3)

# 每个传感器的总体平均值（对天数和小时求平均）
sensor_avg = data.mean(axis=(0, 1))
print("传感器平均值形状：", sensor_avg.shape)  # (3,)
```

### axis常见错误

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 错误1：axis超出范围
# print(arr.sum(axis=2))  # AxisError: axis 2 is out of bounds

# 错误2：混淆axis的方向
# 想要每行的和，却用了axis=0
print("错误用法：", arr.sum(axis=0))  # [5 7 9]（每列的和）
print("正确用法：", arr.sum(axis=1))  # [ 6 15]（每行的和）

# 错误3：忘记axis的默认行为
print("不指定axis：", arr.sum())  # 21（所有元素的和）
```

### axis记忆口诀

**"axis=0往下走，axis=1往右走，结果是剩下的"**

或者记住：
- axis=0：行方向，结果按列排列
- axis=1：列方向，结果按行排列
- axis=-1：最后一个维度

---

## 向量化运算入门

向量化运算是NumPy最强大的特性之一，它让我们能够用简洁的代码完成复杂的数学运算。

### 什么是向量化运算？

**传统方式（用循环）：**
```python
# 计算两个列表对应元素的和
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)  # [11, 22, 33, 44, 55]
```

**向量化方式（NumPy）：**
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

result = a + b  # 一行搞定！
print(result)  # [11 22 33 44 55]
```

### 为什么向量化更快？

1. **底层用C实现**：不需要Python循环的开销
2. **SIMD指令**：CPU可以一次处理多个数据
3. **缓存友好**：内存连续访问更快
4. **并行计算**：可以利用多核CPU

### 基本向量化运算

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 数组和标量运算
print(arr + 10)   # [11 12 13 14 15]（每个元素+10）
print(arr - 3)    # [-2 -1  0  1  2]
print(arr * 2)    # [ 2  4  6  8 10]
print(arr / 2)    # [0.5 1.  1.5 2.  2.5]
print(arr ** 2)   # [ 1  4  9 16 25]
print(arr % 2)    # [1 0 1 0 1]（奇偶判断）

# 数组和数组运算（元素对应运算）
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)  # [11 22 33 44 55]
print(a * b)  # [ 10  40  90 160 250]
print(b / a)  # [10. 10. 10. 10. 10.]
```

### 比较运算

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 比较运算返回布尔数组
print(arr > 3)   # [False False False  True  True]
print(arr == 3)  # [False False  True False False]
print(arr <= 2)  # [ True  True False False False]

# 组合条件
print((arr > 2) & (arr < 5))  # [False False  True  True False]
print((arr < 2) | (arr > 4))  # [ True False False False  True]

# 布尔索引（选择满足条件的元素）
print(arr[arr > 3])  # [4 5]（选择大于3的元素）

# 实际应用：筛选数据
scores = np.array([85, 92, 78, 90, 88, 95, 82, 89])
high_scores = scores[scores >= 90]
print("高分（>=90）：", high_scores)  # [92 90 95]

low_scores = scores[scores < 80]
print("低分（<80）：", low_scores)  # [78]
```

### 数学函数

NumPy提供了大量的数学函数，都支持向量化：

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

# 基本数学函数
print(np.sqrt(arr))  # [ 1.  2.  3.  4.  5.]（平方根）
print(np.square(arr))  # [  1  16  81 256 625]（平方）
print(np.abs([-1, -2, 3]))  # [1 2 3]（绝对值）

# 指数和对数
print(np.exp([1, 2, 3]))  # [ 2.71828183  7.3890561  20.08553692]
print(np.log([1, 10, 100]))  # [0.         2.30258509 4.60517019]（自然对数）
print(np.log10([1, 10, 100]))  # [0. 1. 2.]（以10为底）

# 三角函数
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(angles))  # [0.         0.5        0.70710678 0.8660254  1.        ]
print(np.cos(angles))  # [1.         0.8660254  0.70710678 0.5        0.        ]

# 舍入函数
arr = np.array([1.1, 2.5, 3.9, 4.5, 5.1])
print(np.round(arr))  # [1. 2. 4. 4. 5.]（四舍五入）
print(np.floor(arr))  # [1. 2. 3. 4. 5.]（向下取整）
print(np.ceil(arr))   # [2. 3. 4. 5. 6.]（向上取整）

# 限制范围
arr = np.array([-5, 10, 15, 20, 25])
print(np.clip(arr, 0, 20))  # [ 0 10 15 20 20]（限制在0-20之间）
```

### 统计函数

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 基本统计
print(arr.sum())   # 55（求和）
print(arr.mean())  # 5.5（平均值）
print(arr.std())   # 2.87...（标准差）
print(arr.var())   # 8.25（方差）
print(arr.max())   # 10（最大值）
print(arr.min())   # 1（最小值）

# 累积运算
print(arr.cumsum())  # [ 1  3  6 10 15 21 28 36 45 55]（累积和）
print(arr.cumprod())  # [1 2 6 24 120 ...]（累积乘积）

# 排序
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.sort(arr))  # [1 1 2 3 4 5 6 9]

# 唯一值
print(np.unique(arr))  # [1 2 3 4 5 6 9]

# 二维数组统计
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2d.sum())  # 21（所有元素和）
print(arr2d.sum(axis=0))  # [5 7 9]（每列的和）
print(arr2d.sum(axis=1))  # [ 6 15]（每行的和）
```

### 广播（Broadcasting）

广播是NumPy的高级特性，允许不同形状的数组进行运算：

```python
import numpy as np

# 一维数组和标量
arr = np.array([1, 2, 3])
print(arr + 10)  # [11 12 13]（10被"广播"到每个元素）

# 二维数组和一维数组
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

arr1d = np.array([10, 20, 30])

print(arr2d + arr1d)
# [[11 22 33]
#  [14 25 36]]
# arr1d被广播到每一行

# 二维数组和列向量
col = np.array([[10],
                [20]])

print(arr2d + col)
# [[11 12 13]
#  [24 25 26]]
# col被广播到每一列
```

### 向量化实战案例

```python
import numpy as np

# 案例1：批量计算折扣价格
prices = np.array([99, 199, 299, 399, 499])
discount = 0.8  # 8折

sale_prices = prices * discount
print("原价：", prices)
print("折后价：", sale_prices)

# 案例2：温度转换（摄氏度转华氏度）
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9/5 + 32
print(f"摄氏度：{celsius}")
print(f"华氏度：{fahrenheit}")

# 案例3：计算距离
# 两点之间的欧几里得距离
points1 = np.array([[0, 0],
                    [1, 1],
                    [2, 2]])

points2 = np.array([[3, 4],
                    [4, 5],
                    [5, 6]])

# 向量化计算距离
distances = np.sqrt(((points2 - points1) ** 2).sum(axis=1))
print("距离：", distances)

# 案例4：标准化数据（常用于机器学习）
data = np.array([10, 20, 30, 40, 50])

# Z-score标准化：(x - mean) / std
mean = data.mean()
std = data.std()
normalized = (data - mean) / std
print("原始数据：", data)
print("标准化后：", normalized)
print("均值：", normalized.mean())  # 接近0
print("标准差：", normalized.std())  # 接近1

# 案例5：批量评分
# 计算多个学生的加权平均分
scores = np.array([[85, 92, 78],  # 学生1：语文、数学、英语
                   [90, 88, 95],  # 学生2
                   [82, 89, 91]]) # 学生3

weights = np.array([0.3, 0.4, 0.3])  # 权重：语文30%，数学40%，英语30%

# 向量化计算加权平均
weighted_avg = (scores * weights).sum(axis=1)
print("加权平均分：", weighted_avg)
```

---

## 实战练习题

理论学完了，通过练习来巩固所学的知识吧！

### 练习1：数组基础操作

创建一个1-100的数组，完成以下任务：
1. 找出所有能被3整除的数
2. 计算这些数的平均值
3. 找出大于50的数有多少个

```python
import numpy as np

# 你的代码

# 参考答案
arr = np.arange(1, 101)

# 1. 能被3整除的数
divisible_by_3 = arr[arr % 3 == 0]
print("能被3整除的数：", divisible_by_3)

# 2. 平均值
avg = divisible_by_3.mean()
print("平均值：", avg)

# 3. 大于50的个数
count = (arr > 50).sum()
print("大于50的个数：", count)
```

### 练习2：成绩分析

有一个班级的成绩表（5个学生，3个科目）：
```python
scores = np.array([[85, 92, 78],
                   [90, 88, 95],
                   [82, 89, 91],
                   [95, 85, 88],
                   [78, 91, 87]])
```

任务：
1. 计算每个学生的总分和平均分
2. 找出每个科目的最高分和最低分
3. 找出总分最高的学生
4. 统计多少人的平均分超过85

```python
import numpy as np

scores = np.array([[85, 92, 78],
                   [90, 88, 95],
                   [82, 89, 91],
                   [95, 85, 88],
                   [78, 91, 87]])

# 你的代码

# 参考答案
# 1. 每个学生的总分和平均分
total_scores = scores.sum(axis=1)
avg_scores = scores.mean(axis=1)
print("总分：", total_scores)
print("平均分：", avg_scores)

# 2. 每个科目的最高分和最低分
max_scores = scores.max(axis=0)
min_scores = scores.min(axis=0)
print("各科最高分：", max_scores)
print("各科最低分：", min_scores)

# 3. 总分最高的学生
best_student = total_scores.argmax()
print(f"总分最高的是学生{best_student + 1}，总分{total_scores[best_student]}")

# 4. 平均分超过85的人数
count = (avg_scores > 85).sum()
print(f"平均分超过85的有{count}人")
```

### 练习3：图像处理基础

创建一个10×10的"图像"（随机整数0-255），完成：
1. 将图像二值化（>128的设为255，其他设为0）
2. 反转图像（255-原值）
3. 提取图像的中心4×4区域

```python
import numpy as np

# 你的代码

# 参考答案
# 创建图像
image = np.random.randint(0, 256, (10, 10))
print("原始图像：")
print(image)

# 1. 二值化
binary = np.where(image > 128, 255, 0)
print("\n二值化：")
print(binary)

# 2. 反转
inverted = 255 - image
print("\n反转：")
print(inverted)

# 3. 提取中心4×4
center = image[3:7, 3:7]
print("\n中心4×4：")
print(center)
```

### 练习4：数据标准化

编写函数实现以下标准化方法：
1. Min-Max标准化：(x - min) / (max - min)，结果在0-1之间
2. Z-score标准化：(x - mean) / std，结果均值0、标准差1

测试数据：`data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])`

```python
import numpy as np

def min_max_normalize(arr):
    """Min-Max标准化"""
    # 你的代码
    pass

def z_score_normalize(arr):
    """Z-score标准化"""
    # 你的代码
    pass

# 测试
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# 参考答案
def min_max_normalize(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

def z_score_normalize(arr):
    return (arr - arr.mean()) / arr.std()

# 测试
print("原始数据：", data)
print("Min-Max标准化：", min_max_normalize(data))
print("Z-score标准化：", z_score_normalize(data))
```

### 练习5：矩阵运算

创建两个3×3矩阵：
```python
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
```

完成：
1. 元素级乘法（A * B）
2. 矩阵乘法（A @ B）
3. 计算A的转置
4. 找出A中大于5的元素，并用0替换

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# 你的代码

# 参考答案
# 1. 元素级乘法
element_wise = A * B
print("元素级乘法：")
print(element_wise)

# 2. 矩阵乘法
matrix_mult = A @ B
print("\n矩阵乘法：")
print(matrix_mult)

# 3. 转置
transpose = A.T
print("\nA的转置：")
print(transpose)

# 4. 替换
A_modified = A.copy()
A_modified[A_modified > 5] = 0
print("\n替换后的A：")
print(A_modified)
```

### 练习6：实战综合题

某公司记录了一周的销售数据（7天，4个产品）：
```python
sales = np.array([[100, 120, 80, 90],   # 周一
                  [110, 130, 85, 95],   # 周二
                  [120, 125, 90, 100],  # 周三
                  [130, 140, 95, 105],  # 周四
                  [125, 135, 92, 102],  # 周五
                  [140, 150, 100, 110], # 周六
                  [150, 160, 105, 115]])# 周日
```

任务：
1. 计算每天的总销量
2. 计算每个产品的周销量
3. 找出销量最好的一天和产品
4. 计算每天销量相比前一天的增长率
5. 找出哪些天所有产品销量都超过100

```python
import numpy as np

sales = np.array([[100, 120, 80, 90],
                  [110, 130, 85, 95],
                  [120, 125, 90, 100],
                  [130, 140, 95, 105],
                  [125, 135, 92, 102],
                  [140, 150, 100, 110],
                  [150, 160, 105, 115]])

# 你的代码

# 参考答案
# 1. 每天总销量
daily_total = sales.sum(axis=1)
print("每天总销量：", daily_total)

# 2. 每个产品周销量
product_total = sales.sum(axis=0)
print("各产品周销量：", product_total)

# 3. 最好的一天和产品
best_day = daily_total.argmax()
best_product = product_total.argmax()
print(f"销量最好的是第{best_day+1}天，总销量{daily_total[best_day]}")
print(f"销量最好的产品是产品{best_product+1}，周销量{product_total[best_product]}")

# 4. 增长率
growth_rate = (daily_total[1:] - daily_total[:-1]) / daily_total[:-1] * 100
print("每日增长率（%）：", growth_rate)

# 5. 所有产品都超过100的天数
all_above_100 = (sales > 100).all(axis=1)
print("所有产品都超过100的天：", np.where(all_above_100)[0] + 1)
```

---

## 常见问题和易错点

### 问题1：数组不可变大小

```python
import numpy as np

arr = np.array([1, 2, 3])

# 错误：不能像列表一样append
# arr.append(4)  # AttributeError

# 正确：创建新数组
arr = np.append(arr, 4)
print(arr)  # [1 2 3 4]

# 或者用concatenate
arr = np.concatenate([arr, [5, 6]])
print(arr)  # [1 2 3 4 5 6]
```

**建议**：如果需要频繁添加元素，先用列表，最后转成数组。

### 问题2：视图vs复制

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 切片是视图（共享内存）
view = arr[1:4]
view[0] = 100
print(arr)  # [  1 100   3   4   5]（原数组也变了！）

# 要创建独立副本，用copy()
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 100
print(arr)  # [1 2 3 4 5]（原数组没变）
```

### 问题3：整数除法类型变化

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 除法会自动转成浮点数
result = arr / 2
print(result.dtype)  # float64

# 如果想保持整数
result = arr // 2
print(result.dtype)  # int64
```

### 问题4：维度不匹配

```python
import numpy as np

a = np.array([[1, 2, 3]])  # 形状(1, 3)
b = np.array([[1], [2], [3]])  # 形状(3, 1)

# 错误：维度不匹配
# result = a + np.array([1, 2])  # ValueError

# 正确：确保形状兼容
result = a + np.array([1, 2, 3])  # OK
```

### 问题5：数组比较

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([1, 2, 3])

# 错误：不能直接用==判断两个数组是否相等
# if a == b:  # ValueError: ambiguous
#     print("相等")

# 正确：用array_equal
if np.array_equal(a, b):
    print("相等")

# 或者用all()
if (a == b).all():
    print("相等")
```

---

## 下一步

恭喜你完成了NumPy数组基础的学习！你已经掌握了：
- ndarray的概念和创建
- 一维、二维、三维数组的使用
- 数据类型（dtype）的选择
- axis的理解和应用
- 向量化运算的威力

下一章，我们将学习**数组的高级索引和切片**，包括：
- 花式索引
- 布尔索引
- 多维索引技巧
- 索引的实际应用

继续加油！NumPy的世界才刚刚开始！

---

## 本章要点总结

**核心概念**：
- ndarray是NumPy的核心数据结构
- 数组比列表快10-100倍
- 数组是同质化、固定大小的
- 支持向量化运算

**数组维度**：
- 一维：像一条线
- 二维：像表格（行和列）
- 三维：像立方体（页、行、列）

**数据类型**：
- int8/16/32/64：整数
- uint8：0-255（图像）
- float32/64：浮点数
- bool：布尔值

**axis理解**：
- axis=0：沿行方向（垂直），结果是列
- axis=1：沿列方向（水平），结果是行
- 记住"折叠法"

**向量化运算**：
- 避免Python循环
- 用数组运算符直接计算
- 速度快、代码简洁

**记住**：
- 数组创建后大小不可变
- 切片是视图，要复制用copy()
- 除法自动转浮点数
- 用array_equal比较数组

现在你已经具备了使用NumPy进行数据分析的基础能力！继续练习，多写代码，很快你就能熟练运用NumPy处理各种数据了！
