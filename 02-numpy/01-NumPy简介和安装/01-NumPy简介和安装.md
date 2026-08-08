# 第01章：NumPy简介和安装

欢迎来到NumPy的世界！

如果你已经学过 Python 基础，接下来就可以进入 NumPy。它是 Python 数值计算生态中的基础工具，很多数据分析、科学计算和机器学习库都会用到它。可以把 Python 列表看作日常工具，而 NumPy 数组更适合成批处理数值数据。

---

## 什么是NumPy？

### 先来个生活化的比喻

想象一下，你是一家工厂的仓库管理员：

**用Python列表管理货物**：就像用记事本记录，一个个箱子手动搬运、手动清点。你要查找某个货物，得一个个翻；要统计总数，得一个个数。虽然能完成任务，但效率低，累得要死！

**用NumPy数组管理货物**：就像有了现代化的自动化仓库系统！货物整齐排列在货架上，想找什么按个按钮就能定位，想统计数据电脑自动算好，想搬运货物有叉车、有输送带。效率会高很多。

**NumPy 可以理解为面向数值数据的“自动化仓库系统”**：它擅长按统一的数据类型组织数组，并对整批数据进行高效计算。

---

### NumPy的正式定义

**NumPy（Numerical Python）** 是Python的一个开源数值计算扩展库。它提供了：

1. **多维数组对象**（ndarray）：可以存储和处理大型矩阵
2. **高效的数学函数**：对数组进行快速运算
3. **线性代数、随机数生成等工具**：科学计算的瑞士军刀
4. **与C/C++集成的能力**：性能接近底层语言

**核心特点**：
- **快**：比Python列表快10-100倍
- **方便**：一行代码能完成几十行循环的工作
- **专业**：专为科学计算设计
- **通用**：数据分析、机器学习、图像处理都离不开它

---

### NumPy的小故事

NumPy的前身是1995年诞生的Numeric库，后来发展成NumPy（2005年）。它的创始人Travis Oliphant在2005年时，把Numeric和另一个库Numarray合并，创造了NumPy。

有趣的是，Travis当时是在大学当教授，他晚上加班写代码，白天教书，花了好几个月才完成NumPy的第一版。他的初衷很简单：让Python能像MATLAB那样方便地做科学计算，但又是免费开源的！

现在NumPy已经20多岁了，成为了Python数据科学生态的基石。几乎所有数据科学、机器学习的库（Pandas、SciPy、Scikit-learn、TensorFlow等）都依赖NumPy！

---

## 为什么要学NumPy？

### 1. 性能优势 - 速度优势很明显。

让我们看个对比，就知道NumPy有多快了：

**场景**：计算一个包含100万个数字的列表，每个数字乘以2

```python
# 用Python列表（慢）
import time

# 创建100万个数字
python_list = list(range(1000000))

start = time.time()
result = [x * 2 for x in python_list]
python_time = time.time() - start

print(f"Python列表耗时：{python_time:.4f}秒")

# 用NumPy数组（快）
import numpy as np

numpy_array = np.arange(1000000)

start = time.time()
result = numpy_array * 2
numpy_time = time.time() - start

print(f"NumPy数组耗时：{numpy_time:.4f}秒")
print(f"NumPy快了：{python_time / numpy_time:.2f}倍")
```

**运行结果**（大概）：
```
Python列表耗时：0.0856秒
NumPy数组耗时：0.0012秒
NumPy快了：71.33倍
```

**为什么NumPy这么快？**

1. **底层用C语言实现**：NumPy的核心代码用C和Fortran写的，速度接近编译语言
2. **向量化运算**：不用写循环，NumPy自动帮你并行处理
3. **内存连续存储**：数据在内存中紧密排列，读取速度快
4. **类型固定**：NumPy数组元素类型固定（比如都是整数），不像Python列表可以混合类型

**打个比方**：
- Python列表：像小轿车，一次运一个人
- NumPy数组：像高铁，一次运一车厢的人，而且速度还快

---

### 2. 向量化让代码更简洁

**场景**：有两个列表，要对应元素相加

**用Python列表**：
```python
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

# 需要写循环
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)  # [11, 22, 33, 44, 55]
```

**用NumPy数组**：
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# 一行即可完成。
result = a + b

print(result)  # [11 22 33 44 55]
```

可以看到，NumPy 可以直接对整个数组进行运算，不必手写逐元素循环，这就是向量化带来的便利。

---

### 3. 专业工具 - 科学计算必备

NumPy提供了大量数学函数，让你轻松完成复杂计算：

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])

# 常用数学运算
print("求和：", np.sum(arr))          # 15
print("平均值：", np.mean(arr))       # 3.0
print("标准差：", np.std(arr))        # 1.414...
print("最大值：", np.max(arr))        # 5
print("最小值：", np.min(arr))        # 1

# 更高级的运算
print("平方根：", np.sqrt(arr))       # [1. 1.414 1.732 2. 2.236]
print("指数：", np.exp(arr))          # [2.718... 7.389... 20.085...]
print("对数：", np.log(arr))          # [0. 0.693 1.098 1.386 1.609]
print("正弦：", np.sin(arr))          # [0.841 0.909 0.141 -0.756 -0.958]
```

这些函数用纯Python写，可能要几十行代码，用NumPy一个函数搞定！

---

### 4. 生态基石 - 通往数据科学的大门

学会NumPy，你就能学：

- **Pandas**：数据分析利器（处理表格数据）
- **Matplotlib**：数据可视化（画图表）
- **SciPy**：科学计算工具集
- **Scikit-learn**：机器学习库
- **TensorFlow/PyTorch**：深度学习框架

**简单理解**：NumPy 提供了数组和向量化运算基础，理解这些概念后再学习 Pandas、SciPy 等库会更顺畅。

---

### 5. 实际应用场景

NumPy到底能干什么？让我们看看实际场景：

#### 场景1：数据分析
```python
# 分析班级成绩
import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 84, 91])

print(f"平均分：{np.mean(scores):.2f}")
print(f"最高分：{np.max(scores)}")
print(f"最低分：{np.min(scores)}")
print(f"标准差：{np.std(scores):.2f}")
print(f"及格率：{np.sum(scores >= 60) / len(scores) * 100:.2f}%")
```

#### 场景2：图像处理
```python
# 图像本质上就是数字矩阵！
import numpy as np

# 一张100x100的黑白图片就是100x100的数组
image = np.zeros((100, 100))  # 黑色背景

# 画一个白色的正方形
image[25:75, 25:75] = 255  # 白色

# 调整亮度（所有像素值乘以0.5）
darker_image = image * 0.5

# 反转颜色
inverted_image = 255 - image
```

#### 场景3：金融分析
```python
# 计算股票收益率
import numpy as np

# 某股票每天的收盘价
prices = np.array([100, 102, 101, 105, 103, 107, 110])

# 计算每日涨跌幅
daily_returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100

print("每日涨跌幅：", daily_returns)
print(f"平均涨幅：{np.mean(daily_returns):.2f}%")
print(f"波动率（标准差）：{np.std(daily_returns):.2f}%")
```

#### 场景4：科学计算
```python
# 计算物理实验数据
import numpy as np

# 测量数据（可能有误差）
measurements = np.array([9.8, 9.9, 9.7, 9.8, 9.9, 9.6, 9.8])

# 计算平均值和误差
mean_value = np.mean(measurements)
std_error = np.std(measurements)

print(f"重力加速度：{mean_value:.2f} ± {std_error:.2f} m/s²")
```

---

## NumPy vs Python列表 - 详细对比

让我们深入对比一下NumPy数组和Python列表的区别：

### 对比表格

| 特性 | Python列表 | NumPy数组 |
|------|-----------|----------|
| **存储类型** | 可以混合类型 | 必须相同类型 |
| **速度** | 慢 | 快（10-100倍） |
| **内存占用** | 大 | 小（节省内存） |
| **数学运算** | 需要写循环 | 直接向量化运算 |
| **维度** | 一维（列表的列表除外） | 多维（1D, 2D, 3D...） |
| **功能** | 通用容器 | 专门做数值计算 |

### 详细对比示例

#### 1. 类型限制

```python
# Python列表：可以混合类型
python_list = [1, "hello", 3.14, True, [1, 2]]  # 完全OK
print(python_list)

# NumPy数组：类型必须统一
import numpy as np
numpy_array = np.array([1, 2, 3, 4])  # 都是整数，OK
print(numpy_array)
print(numpy_array.dtype)  # int64（整数类型）

# 如果混合类型，NumPy会自动转换为相同类型
mixed = np.array([1, 2.5, 3])  # 有整数和浮点数
print(mixed)  # [1.  2.5 3. ]（全部变成浮点数）
print(mixed.dtype)  # float64
```

#### 2. 数学运算对比

```python
# Python列表：需要循环
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# 相加（错误示例）
# result = list1 + list2  # 这会把列表拼接，不是对应元素相加
# print(result)  # [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]

# 正确做法：需要循环
result = [a + b for a, b in zip(list1, list2)]
print("Python列表相加：", result)

# NumPy数组：直接运算
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# 一行即可完成。
result = arr1 + arr2
print("NumPy数组相加：", result)

# 其他运算也一样简单
print("相减：", arr1 - arr2)
print("相乘：", arr1 * arr2)
print("相除：", arr1 / arr2)
print("平方：", arr1 ** 2)
```

#### 3. 多维数据对比

```python
# Python列表：表示矩阵很麻烦
matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 访问元素：需要两层索引
print("列表访问元素：", matrix_list[1][2])  # 6

# NumPy数组：原生支持多维
import numpy as np
matrix_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 访问元素：更直观
print("NumPy访问元素：", matrix_np[1, 2])  # 6

# NumPy提供丰富的操作
print("形状：", matrix_np.shape)  # (3, 3)
print("转置：\n", matrix_np.T)  # 矩阵转置
print("每列求和：", np.sum(matrix_np, axis=0))  # [12 15 18]
print("每行求和：", np.sum(matrix_np, axis=1))  # [6 15 24]
```

#### 4. 内存占用对比

```python
import sys
import numpy as np

# 创建包含1000个整数的列表和数组
python_list = list(range(1000))
numpy_array = np.arange(1000)

# 查看内存占用
list_size = sys.getsizeof(python_list)
array_size = numpy_array.nbytes

print(f"Python列表内存：{list_size} 字节")
print(f"NumPy数组内存：{array_size} 字节")
print(f"列表是数组的：{list_size / array_size:.2f} 倍")
```

**运行结果**（大概）：
```
Python列表内存：9016 字节
NumPy数组内存：8000 字节
列表是数组的：1.13 倍
```

#### 5. 功能丰富度对比

```python
import numpy as np

# NumPy提供的功能，Python列表要写很多代码才能实现
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 统计功能
print("求和：", np.sum(arr))
print("平均值：", np.mean(arr))
print("中位数：", np.median(arr))
print("标准差：", np.std(arr))
print("方差：", np.var(arr))
print("最大值：", np.max(arr))
print("最小值：", np.min(arr))
print("最大值索引：", np.argmax(arr))
print("最小值索引：", np.argmin(arr))

# 数学函数
print("平方根：", np.sqrt(arr))
print("绝对值：", np.abs(arr))
print("四舍五入：", np.round(arr / 3, 2))

# 条件筛选
print("大于5的元素：", arr[arr > 5])
print("偶数：", arr[arr % 2 == 0])

# 形状操作
print("重塑为2x5矩阵：\n", arr.reshape(2, 5))

# 这些功能用Python列表实现，每个都要写好几行代码！
```

### 什么时候用列表，什么时候用NumPy？

**用Python列表**：
- 存储不同类型的数据（混合存储）
- 数据量小，不需要数学运算
- 需要灵活的插入、删除操作
- 作为通用容器使用

**用NumPy数组**：
- 数值计算（数学、统计、科学计算）
- 数据量大，需要高性能
- 需要矩阵运算、线性代数
- 数据分析、机器学习、图像处理

**记住**：NumPy不是要替代列表，而是在特定场景（数值计算）下提供更好的工具！

---

## NumPy与其他库的关系

NumPy是Python数据科学生态的基石，几乎所有相关库都依赖它。让我们看看NumPy在整个生态中的位置：

### NumPy生态系统

```
                    Python基础
                        ↓
                     NumPy（核心）
                        ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
     Pandas          SciPy         Matplotlib
   （数据分析）     （科学计算）    （数据可视化）
        ↓               ↓               ↓
        └───────────────┼───────────────┘
                        ↓
                  Scikit-learn
                 （机器学习）
                        ↓
            TensorFlow / PyTorch
              （深度学习）
```

### 1. NumPy + Pandas = 数据分析利器

**Pandas是什么？**
- 建立在NumPy之上的数据分析库
- 提供DataFrame（类似Excel表格）和Series（类似单列数据）
- 专门处理表格数据、时间序列数据

**关系**：
- Pandas的底层就是NumPy数组
- DataFrame的每一列都是一个NumPy数组
- 可以互相转换

```python
import numpy as np
import pandas as pd

# NumPy数组
np_array = np.array([
    [1, 'Alice', 85],
    [2, 'Bob', 92],
    [3, 'Charlie', 78]
])

# 转换为Pandas DataFrame
df = pd.DataFrame(np_array, columns=['ID', 'Name', 'Score'])
print(df)

# DataFrame也可以转回NumPy数组
back_to_numpy = df.values
print(type(back_to_numpy))  # <class 'numpy.ndarray'>
```

**什么时候用谁？**
- **NumPy**：纯数值计算，矩阵运算，科学计算
- **Pandas**：处理表格数据，数据清洗，统计分析

---

### 2. NumPy + SciPy = 科学计算组合

**SciPy是什么？**
- 建立在NumPy之上的科学计算库
- 提供更高级的数学、科学、工程函数
- 包括优化、积分、插值、信号处理等

**关系**：
- SciPy扩展了NumPy的功能
- NumPy提供基础（数组、基本运算）
- SciPy提供高级功能（优化算法、信号处理等）

```python
import numpy as np
from scipy import optimize, integrate

# NumPy提供基础数组
x = np.linspace(0, 10, 100)
y = np.sin(x)

# SciPy提供高级功能
# 优化：找到函数最小值
result = optimize.minimize(lambda x: (x - 5)**2, x0=0)
print("最小值点：", result.x)

# 积分：计算函数积分
result, error = integrate.quad(lambda x: x**2, 0, 1)
print("积分结果：", result)
```

---

### 3. NumPy + Matplotlib = 数据可视化

**Matplotlib是什么？**
- Python的数据可视化库
- 可以画各种图表：线图、柱状图、散点图、热力图等

**关系**：
- Matplotlib直接支持NumPy数组
- NumPy处理数据，Matplotlib画图

```python
import numpy as np
import matplotlib.pyplot as plt

# NumPy生成数据
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Matplotlib画图
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('三角函数图')
plt.legend()
plt.grid(True)
plt.show()
```

---

### 4. NumPy + Scikit-learn = 机器学习

**Scikit-learn是什么？**
- Python最流行的机器学习库
- 提供各种机器学习算法：分类、回归、聚类等

**关系**：
- 输入数据必须是NumPy数组
- 模型训练和预测都用NumPy数组

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# NumPy准备数据
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Scikit-learn训练模型
model = LinearRegression()
model.fit(X, y)

# 预测
prediction = model.predict(np.array([[6]]))
print("预测值：", prediction)  # [12]
```

---

### 5. NumPy + TensorFlow/PyTorch = 深度学习

**TensorFlow/PyTorch是什么？**
- 深度学习框架
- 用于构建和训练神经网络

**关系**：
- 可以将NumPy数组转换为张量（Tensor）
- 张量运算和NumPy数组运算很相似

```python
import numpy as np
import torch  # PyTorch

# NumPy数组
np_array = np.array([[1, 2], [3, 4]])

# 转换为PyTorch张量
torch_tensor = torch.from_numpy(np_array)
print("PyTorch张量：\n", torch_tensor)

# 张量转回NumPy
back_to_numpy = torch_tensor.numpy()
print("转回NumPy：\n", back_to_numpy)
```

---

### 库依赖关系图

```
┌─────────────────────────────────────────┐
│                 Python                  │
│            （编程语言基础）              │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│                NumPy                    │
│      （数组、数值计算、线性代数）        │
└──┬────────┬────────┬────────┬──────────┘
   ↓        ↓        ↓        ↓
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Pandas│ │SciPy │ │Matpl.│ │PIL/  │
│表格  │ │科学  │ │可视化│ │图像  │
└──┬───┘ └──┬───┘ └──────┘ └──────┘
   ↓        ↓
┌──────────────────┐
│  Scikit-learn    │
│   （机器学习）    │
└────────┬─────────┘
         ↓
┌──────────────────┐
│TensorFlow/PyTorch│
│  （深度学习）     │
└──────────────────┘
```

**总结**：学会NumPy，你就拿到了数据科学世界的钥匙！

---

## 安装NumPy

说了这么多NumPy的好处，现在让我们把它装到你的电脑上！安装过程超级简单。

### 前提条件

在安装NumPy之前，确保你已经：
- ✅ 安装了Python 3（建议Python 3.8或更高版本）
- ✅ 知道如何打开命令行（Windows的cmd或PowerShell，macOS/Linux的Terminal）

**检查Python版本**：
```bash
python --version
# 或者（macOS/Linux）
python3 --version
```

如果显示Python版本号，说明Python已安装，可以继续！

---

### 方法一：使用pip安装（推荐，最简单）

pip是Python的包管理工具，安装Python时已经自动安装了pip。

#### 步骤1：打开命令行

- **Windows**：按`Win + R`，输入`cmd`，回车
- **macOS**：打开"终端"（Terminal）
- **Linux**：打开终端

#### 步骤2：运行安装命令

```bash
# Windows
pip install numpy

# macOS/Linux（如果上面的不行，用这个）
pip3 install numpy
```

#### 步骤3：等待安装

你会看到类似这样的输出：
```
Collecting numpy
  Downloading numpy-1.26.0-cp312-cp312-win_amd64.whl (15.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 5.2 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.0
```

#### 步骤4：验证安装

```bash
# 在命令行输入
python -c "import numpy; print(numpy.__version__)"
```

如果显示版本号（比如`1.26.0`），恭喜你安装成功！

---

### 方法二：使用Anaconda安装（推荐数据科学方向）

如果你安装了Anaconda，NumPy已经自动包含在里面了，不需要单独安装！

#### 验证NumPy是否已安装

```bash
# 打开Anaconda Prompt或普通命令行
conda list numpy
```

如果看到NumPy的信息，说明已经安装了！

#### 如果没有，手动安装

```bash
conda install numpy
```

#### 使用conda的好处

- 自动处理依赖关系
- 可以创建独立的环境
- 避免版本冲突

---

### 方法三：从源代码编译（高级用户，不推荐新手）

这种方法适合需要最新开发版或想定制编译的高级用户。

```bash
# 克隆NumPy仓库
git clone https://github.com/numpy/numpy.git
cd numpy

# 安装
pip install .
```

**注意**：这种方法需要编译环境（C编译器等），比较复杂，新手不推荐！

---

### 方法四：升级已安装的NumPy

如果你已经安装了NumPy，想升级到最新版：

```bash
# 升级到最新版
pip install --upgrade numpy

# 或者用conda
conda update numpy
```

---

### 方法五：安装特定版本

有时候某些项目需要特定版本的NumPy：

```bash
# 安装特定版本
pip install numpy==1.24.0

# 安装大于某版本
pip install "numpy>=1.24.0"

# 安装小于某版本
pip install "numpy<1.26.0"
```

---

### 国内镜像加速（强烈推荐！）

如果你在国内，pip下载可能会很慢，可以使用国内镜像：

#### 临时使用镜像

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
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

---

### 验证安装是否成功

安装完成后，让我们验证NumPy是否正常工作：

#### 方法1：命令行快速验证

```bash
python -c "import numpy as np; print('NumPy版本:', np.__version__); print('测试:', np.array([1,2,3]))"
```

#### 方法2：进入Python交互模式验证

```bash
# 打开Python
python

# 然后输入
>>> import numpy as np
>>> np.__version__
'1.26.0'
>>> np.array([1, 2, 3])
array([1, 2, 3])
>>> exit()
```

#### 方法3：创建测试脚本

创建一个`test_numpy.py`文件：

```python
import numpy as np

print("=" * 50)
print("NumPy安装验证")
print("=" * 50)

# 显示版本
print(f"\nNumPy版本：{np.__version__}")

# 测试基本功能
arr = np.array([1, 2, 3, 4, 5])
print(f"\n创建数组：{arr}")
print(f"数组类型：{type(arr)}")
print(f"元素类型：{arr.dtype}")
print(f"数组形状：{arr.shape}")

# 测试数学运算
print(f"\n数组 * 2：{arr * 2}")
print(f"数组求和：{np.sum(arr)}")
print(f"数组平均值：{np.mean(arr)}")

# 测试多维数组
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D数组：\n{matrix}")
print(f"数组形状：{matrix.shape}")

print("\n" + "=" * 50)
print("恭喜！NumPy安装成功，运行正常！")
print("=" * 50)
```

运行：
```bash
python test_numpy.py
```

如果看到输出，说明NumPy安装成功！

---

### 安装常见问题及解决方案

#### 问题1：提示"pip不是内部或外部命令"

**原因**：pip没有添加到系统PATH

**解决**：
```bash
# 用python -m pip代替pip
python -m pip install numpy
```

#### 问题2：提示"Permission denied"（权限不足）

**原因**：没有管理员权限

**解决（Windows）**：
```bash
# 以管理员身份运行命令行
# 或者安装到用户目录
pip install --user numpy
```

**解决（macOS/Linux）**：
```bash
# 方法1：加sudo
sudo pip3 install numpy

# 方法2：安装到用户目录（推荐）
pip3 install --user numpy
```

#### 问题3：下载速度慢或超时

**原因**：网络问题

**解决**：使用国内镜像（见上面的"国内镜像加速"部分）

#### 问题4：提示版本冲突

**原因**：与其他包版本不兼容

**解决**：
```bash
# 卸载重装
pip uninstall numpy
pip install numpy

# 或者指定兼容版本
pip install numpy==1.24.0
```

#### 问题5：Import numpy成功，但某些功能报错

**原因**：安装不完整或损坏

**解决**：
```bash
# 重新安装
pip install --force-reinstall numpy
```

#### 问题6：在Jupyter Notebook中import失败

**原因**：Jupyter的Python环境和命令行的不同

**解决**：
```bash
# 在Jupyter的单元格中运行
!pip install numpy

# 或者在命令行中指定Jupyter的Python
python -m pip install numpy
```

---

## 第一个NumPy程序

NumPy安装好了，现在让我们写第一个真正的NumPy程序！

### Hello NumPy！

创建一个文件`hello_numpy.py`：

```python
# 导入NumPy库，通常简称为np
import numpy as np

# 打印欢迎信息
print("=" * 50)
print("欢迎来到NumPy的世界！")
print("=" * 50)

# 创建第一个NumPy数组
my_first_array = np.array([1, 2, 3, 4, 5])

print("\n我的第一个NumPy数组：")
print(my_first_array)

# 查看数组信息
print(f"\n数组类型：{type(my_first_array)}")
print(f"元素类型：{my_first_array.dtype}")
print(f"数组形状：{my_first_array.shape}")
print(f"数组维度：{my_first_array.ndim}")
print(f"数组大小：{my_first_array.size}")

# 做些简单运算
print("\n让我们做些运算：")
print(f"数组 + 10：{my_first_array + 10}")
print(f"数组 * 2：{my_first_array * 2}")
print(f"数组平方：{my_first_array ** 2}")

# 使用NumPy函数
print("\n使用NumPy函数：")
print(f"求和：{np.sum(my_first_array)}")
print(f"平均值：{np.mean(my_first_array)}")
print(f"最大值：{np.max(my_first_array)}")
print(f"最小值：{np.min(my_first_array)}")

print("\n" + "=" * 50)
print("恭喜！你的第一个NumPy程序运行成功！")
print("=" * 50)
```

运行：
```bash
python hello_numpy.py
```

**预期输出**：
```
==================================================
欢迎来到NumPy的世界！
==================================================

我的第一个NumPy数组：
[1 2 3 4 5]

数组类型：<class 'numpy.ndarray'>
元素类型：int64
数组形状：(5,)
数组维度：1
数组大小：5

让我们做些运算：
数组 + 10：[11 12 13 14 15]
数组 * 2：[ 2  4  6  8 10]
数组平方：[ 1  4  9 16 25]

使用NumPy函数：
求和：15
平均值：3.0
最大值：5
最小值：1

==================================================
恭喜！你的第一个NumPy程序运行成功！
==================================================
```

---

### 稍微复杂一点的例子

让我们写个更实用的程序，计算班级成绩统计：

```python
import numpy as np

print("=" * 60)
print("班级成绩统计系统")
print("=" * 60)

# 创建学生成绩数组（假设有10个学生）
scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 84, 91])

print(f"\n学生成绩：{scores}")
print(f"学生人数：{len(scores)}")

# 基本统计
print("\n" + "-" * 60)
print("基本统计信息")
print("-" * 60)
print(f"平均分：{np.mean(scores):.2f}")
print(f"最高分：{np.max(scores)}")
print(f"最低分：{np.min(scores)}")
print(f"中位数：{np.median(scores):.2f}")
print(f"标准差：{np.std(scores):.2f}")
print(f"总分：{np.sum(scores)}")

# 成绩分析
print("\n" + "-" * 60)
print("成绩分析")
print("-" * 60)

# 及格人数（>=60）
passed = np.sum(scores >= 60)
print(f"及格人数：{passed}（及格率：{passed/len(scores)*100:.1f}%）")

# 优秀人数（>=90）
excellent = np.sum(scores >= 90)
print(f"优秀人数：{excellent}（优秀率：{excellent/len(scores)*100:.1f}%）")

# 良好人数（80-89）
good = np.sum((scores >= 80) & (scores < 90))
print(f"良好人数：{good}（良好率：{good/len(scores)*100:.1f}%）")

# 中等人数（70-79）
medium = np.sum((scores >= 70) & (scores < 80))
print(f"中等人数：{medium}（中等率：{medium/len(scores)*100:.1f}%）")

# 找出最高分和最低分的位置
print("\n" + "-" * 60)
print("排名信息")
print("-" * 60)
max_idx = np.argmax(scores)
min_idx = np.argmin(scores)
print(f"最高分学生：第{max_idx + 1}号，成绩：{scores[max_idx]}")
print(f"最低分学生：第{min_idx + 1}号，成绩：{scores[min_idx]}")

# 排序
sorted_scores = np.sort(scores)[::-1]  # 降序排列
print(f"\n成绩降序排列：{sorted_scores}")

# 高于平均分的学生
mean_score = np.mean(scores)
above_average = scores[scores > mean_score]
print(f"\n高于平均分的成绩：{above_average}")
print(f"高于平均分的人数：{len(above_average)}")

print("\n" + "=" * 60)
```

---

### 在Jupyter Notebook中体验NumPy

Jupyter Notebook是学习NumPy的绝佳工具！让我们看看如何使用：

#### 1. 启动Jupyter Notebook

```bash
jupyter notebook
```

浏览器会自动打开，点击"New" → "Python 3"创建新的notebook。

#### 2. 在Notebook中体验NumPy

**单元格1：导入库**
```python
import numpy as np
print("NumPy版本：", np.__version__)
```

**单元格2：创建数组**
```python
# 创建一维数组
arr1d = np.array([1, 2, 3, 4, 5])
print("一维数组：", arr1d)

# 创建二维数组（矩阵）
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组：\n", arr2d)
```

**单元格3：数组运算**
```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("a + b =", a + b)
print("a * b =", a * b)
print("a ** 2 =", a ** 2)
```

**单元格4：可视化**
```python
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 画图
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('正弦函数')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
```

**Jupyter的优势**：
- 可以边写边运行，立刻看结果
- 可以可视化数据
- 可以写文档说明
- 适合做实验和学习

---

## NumPy核心概念快速预览

在正式学习之前，让我们快速预览一下NumPy的核心概念：

### 1. ndarray（N维数组）

NumPy的核心数据结构：

```python
import numpy as np

# 一维数组（向量）
arr_1d = np.array([1, 2, 3])
print("1D数组：", arr_1d)
print("形状：", arr_1d.shape)  # (3,)

# 二维数组（矩阵）
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D数组：\n", arr_2d)
print("形状：", arr_2d.shape)  # (2, 3)

# 三维数组（张量）
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D数组：\n", arr_3d)
print("形状：", arr_3d.shape)  # (2, 2, 2)
```

### 2. 数据类型（dtype）

```python
import numpy as np

# 整数
int_arr = np.array([1, 2, 3])
print("整数数组：", int_arr.dtype)  # int64

# 浮点数
float_arr = np.array([1.0, 2.0, 3.0])
print("浮点数数组：", float_arr.dtype)  # float64

# 指定数据类型
specific_arr = np.array([1, 2, 3], dtype=np.float32)
print("指定类型：", specific_arr.dtype)  # float32
```

### 3. 数组创建方法

```python
import numpy as np

# 从列表创建
arr = np.array([1, 2, 3])

# 全零数组
zeros = np.zeros(5)
print("全零：", zeros)

# 全一数组
ones = np.ones((2, 3))
print("全一：\n", ones)

# 等差数列
arange = np.arange(0, 10, 2)
print("等差数列：", arange)  # [0 2 4 6 8]

# 等分数列
linspace = np.linspace(0, 1, 5)
print("等分数列：", linspace)  # [0.   0.25 0.5  0.75 1.  ]

# 随机数组
random = np.random.rand(3, 3)
print("随机数组：\n", random)
```

### 4. 数组运算

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 算术运算
print("加法：", a + b)
print("减法：", a - b)
print("乘法：", a * b)
print("除法：", a / b)

# 数学函数
print("平方根：", np.sqrt(a))
print("指数：", np.exp(a))
print("对数：", np.log(a))
print("正弦：", np.sin(a))
```

### 5. 数组索引和切片

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 索引
print("第一个元素：", arr[0])  # 10
print("最后一个元素：", arr[-1])  # 50

# 切片
print("前3个元素：", arr[:3])  # [10 20 30]
print("从第2个开始：", arr[2:])  # [30 40 50]

# 条件索引
print("大于25的元素：", arr[arr > 25])  # [30 40 50]
```

### 6. 数组形状操作

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# 重塑形状
reshaped = arr.reshape(2, 3)
print("重塑为2x3：\n", reshaped)

# 转置
transposed = reshaped.T
print("转置：\n", transposed)

# 展平
flattened = reshaped.flatten()
print("展平：", flattened)
```

### 7. 聚合操作

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 全局聚合
print("总和：", np.sum(arr))  # 21
print("平均值：", np.mean(arr))  # 3.5

# 按轴聚合
print("按列求和：", np.sum(arr, axis=0))  # [5 7 9]
print("按行求和：", np.sum(arr, axis=1))  # [6 15]
```

**别担心**！这些概念看起来多，但我们会在后续章节一个个详细讲解。现在只是快速预览，让你有个整体印象！

---

## 实战练习

学习最好的方式就是动手！让我们做几个练习巩固一下：

### 练习1：温度转换器

**任务**：创建一个程序，将摄氏温度转换为华氏温度。

**提示**：华氏度 = 摄氏度 × 9/5 + 32

```python
import numpy as np

# 一周的温度（摄氏度）
celsius = np.array([20, 22, 19, 25, 23, 21, 24])

# TODO: 转换为华氏度
fahrenheit = celsius * 9/5 + 32

print("摄氏温度：", celsius)
print("华氏温度：", fahrenheit)
print(f"平均温度：{np.mean(celsius):.1f}°C / {np.mean(fahrenheit):.1f}°F")
```

**参考答案**：
```python
import numpy as np

# 一周的温度（摄氏度）
celsius = np.array([20, 22, 19, 25, 23, 21, 24])

# 转换为华氏度
fahrenheit = celsius * 9/5 + 32

print("=" * 50)
print("温度转换器")
print("=" * 50)
print(f"摄氏温度：{celsius}")
print(f"华氏温度：{fahrenheit}")
print(f"\n平均温度：{np.mean(celsius):.1f}°C / {np.mean(fahrenheit):.1f}°F")
print(f"最高温度：{np.max(celsius)}°C / {np.max(fahrenheit)}°F")
print(f"最低温度：{np.min(celsius)}°C / {np.min(fahrenheit)}°F")
```

---

### 练习2：购物车价格计算

**任务**：计算购物车的总价、打折后价格。

```python
import numpy as np

# 商品价格
prices = np.array([29.9, 199.0, 89.5, 15.8, 299.0])

# 商品数量
quantities = np.array([2, 1, 3, 5, 1])

# TODO:
# 1. 计算每个商品的小计
# 2. 计算总价
# 3. 如果总价超过500，打9折
# 4. 显示结果

# 参考答案在下面...
```

**参考答案**：
```python
import numpy as np

# 商品价格
prices = np.array([29.9, 199.0, 89.5, 15.8, 299.0])

# 商品数量
quantities = np.array([2, 1, 3, 5, 1])

print("=" * 50)
print("购物车价格计算")
print("=" * 50)

# 计算每个商品的小计
subtotals = prices * quantities
print("\n商品小计：")
for i, subtotal in enumerate(subtotals):
    print(f"商品{i+1}：单价 {prices[i]:.2f} × 数量 {quantities[i]} = {subtotal:.2f}元")

# 计算总价
total = np.sum(subtotals)
print(f"\n原始总价：{total:.2f}元")

# 打折
if total > 500:
    discount_rate = 0.9
    final_price = total * discount_rate
    saved = total - final_price
    print(f"满500打9折！")
    print(f"折后价格：{final_price:.2f}元")
    print(f"节省：{saved:.2f}元")
else:
    final_price = total
    print(f"实付金额：{final_price:.2f}元")
```

---

### 练习3：成绩等级划分

**任务**：根据分数划分等级（A/B/C/D/F）。

```python
import numpy as np

# 学生成绩
scores = np.array([95, 87, 76, 92, 68, 54, 88, 91, 73, 85])

# TODO:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# 统计各等级人数

# 参考答案在下面...
```

**参考答案**：
```python
import numpy as np

# 学生成绩
scores = np.array([95, 87, 76, 92, 68, 54, 88, 91, 73, 85])

print("=" * 50)
print("成绩等级统计")
print("=" * 50)

print(f"\n学生成绩：{scores}")
print(f"学生人数：{len(scores)}")
print(f"平均分：{np.mean(scores):.2f}")

# 统计各等级人数
grade_a = np.sum(scores >= 90)
grade_b = np.sum((scores >= 80) & (scores < 90))
grade_c = np.sum((scores >= 70) & (scores < 80))
grade_d = np.sum((scores >= 60) & (scores < 70))
grade_f = np.sum(scores < 60)

print("\n" + "-" * 50)
print("等级分布")
print("-" * 50)
print(f"A等级 (90-100): {grade_a}人 ({grade_a/len(scores)*100:.1f}%)")
print(f"B等级 (80-89):  {grade_b}人 ({grade_b/len(scores)*100:.1f}%)")
print(f"C等级 (70-79):  {grade_c}人 ({grade_c/len(scores)*100:.1f}%)")
print(f"D等级 (60-69):  {grade_d}人 ({grade_d/len(scores)*100:.1f}%)")
print(f"F等级 (0-59):   {grade_f}人 ({grade_f/len(scores)*100:.1f}%)")

# 找出各等级的具体分数
print("\n" + "-" * 50)
print("各等级分数")
print("-" * 50)
print(f"A等级分数：{scores[scores >= 90]}")
print(f"B等级分数：{scores[(scores >= 80) & (scores < 90)]}")
print(f"C等级分数：{scores[(scores >= 70) & (scores < 80)]}")
print(f"D等级分数：{scores[(scores >= 60) & (scores < 70)]}")
print(f"F等级分数：{scores[scores < 60]}")
```

---

### 练习4：简单数据分析

**任务**：分析一周的步数数据。

```python
import numpy as np

# 一周的步数
steps = np.array([8234, 10532, 6891, 9234, 11023, 5432, 7865])
days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

# TODO:
# 1. 计算平均步数
# 2. 找出步数最多和最少的一天
# 3. 计算达到目标（8000步）的天数
# 4. 计算总步数

# 参考答案在下面...
```

**参考答案**：
```python
import numpy as np

# 一周的步数
steps = np.array([8234, 10532, 6891, 9234, 11023, 5432, 7865])
days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
goal = 8000

print("=" * 60)
print("一周步数统计")
print("=" * 60)

# 显示每天数据
print("\n每日步数：")
for day, step in zip(days, steps):
    status = "✓ 达标" if step >= goal else "✗ 未达标"
    print(f"{day}：{step:5d} 步  {status}")

# 基本统计
print("\n" + "-" * 60)
print("统计信息")
print("-" * 60)
print(f"总步数：{np.sum(steps):,} 步")
print(f"平均步数：{np.mean(steps):.0f} 步")
print(f"最多步数：{np.max(steps)} 步")
print(f"最少步数：{np.min(steps)} 步")
print(f"中位数：{np.median(steps):.0f} 步")

# 目标达成情况
achieved_days = np.sum(steps >= goal)
achievement_rate = achieved_days / len(steps) * 100
print(f"\n达标天数：{achieved_days} 天")
print(f"达标率：{achievement_rate:.1f}%")

# 找出最多和最少的一天
max_idx = np.argmax(steps)
min_idx = np.argmin(steps)
print(f"\n步数最多：{days[max_idx]}（{steps[max_idx]} 步）")
print(f"步数最少：{days[min_idx]}（{steps[min_idx]} 步）")

# 周末 vs 工作日
weekday_steps = steps[:5]  # 周一到周五
weekend_steps = steps[5:]  # 周六周日
print(f"\n工作日平均：{np.mean(weekday_steps):.0f} 步")
print(f"周末平均：{np.mean(weekend_steps):.0f} 步")
```

---

### 练习5：矩阵运算初体验

**任务**：计算两个班级的成绩统计。

```python
import numpy as np

# 两个班级的成绩（行=学生，列=科目：语文、数学、英语）
class1 = np.array([
    [85, 92, 88],
    [78, 85, 90],
    [92, 88, 85],
    [88, 90, 92],
    [90, 87, 89]
])

class2 = np.array([
    [87, 89, 91],
    [82, 88, 85],
    [90, 92, 88],
    [85, 87, 90],
    [89, 91, 87]
])

# TODO:
# 1. 计算每个班级每科的平均分
# 2. 计算每个学生的总分
# 3. 找出每个班级的最高分学生
# 4. 比较两个班级的整体表现

# 参考答案在下面...
```

**参考答案**：
```python
import numpy as np

# 两个班级的成绩（行=学生，列=科目：语文、数学、英语）
class1 = np.array([
    [85, 92, 88],
    [78, 85, 90],
    [92, 88, 85],
    [88, 90, 92],
    [90, 87, 89]
])

class2 = np.array([
    [87, 89, 91],
    [82, 88, 85],
    [90, 92, 88],
    [85, 87, 90],
    [89, 91, 87]
])

subjects = ['语文', '数学', '英语']

print("=" * 70)
print("两班成绩对比分析")
print("=" * 70)

# 班级1分析
print("\n【一班成绩】")
print("-" * 70)
for i, student in enumerate(class1):
    total = np.sum(student)
    avg = np.mean(student)
    print(f"学生{i+1}：语文 {student[0]}, 数学 {student[1]}, 英语 {student[2]} "
          f"| 总分：{total}, 平均：{avg:.1f}")

print("\n一班各科平均分：")
for i, subject in enumerate(subjects):
    avg = np.mean(class1[:, i])
    print(f"  {subject}：{avg:.2f}")

class1_total = np.sum(class1, axis=1)
best_student1 = np.argmax(class1_total)
print(f"\n一班最高分：学生{best_student1+1}（总分：{class1_total[best_student1]}）")

# 班级2分析
print("\n" + "=" * 70)
print("【二班成绩】")
print("-" * 70)
for i, student in enumerate(class2):
    total = np.sum(student)
    avg = np.mean(student)
    print(f"学生{i+1}：语文 {student[0]}, 数学 {student[1]}, 英语 {student[2]} "
          f"| 总分：{total}, 平均：{avg:.1f}")

print("\n二班各科平均分：")
for i, subject in enumerate(subjects):
    avg = np.mean(class2[:, i])
    print(f"  {subject}：{avg:.2f}")

class2_total = np.sum(class2, axis=1)
best_student2 = np.argmax(class2_total)
print(f"\n二班最高分：学生{best_student2+1}（总分：{class2_total[best_student2]}）")

# 对比分析
print("\n" + "=" * 70)
print("【对比分析】")
print("-" * 70)
print(f"一班平均分：{np.mean(class1):.2f}")
print(f"二班平均分：{np.mean(class2):.2f}")

print("\n各科对比：")
for i, subject in enumerate(subjects):
    avg1 = np.mean(class1[:, i])
    avg2 = np.mean(class2[:, i])
    diff = avg2 - avg1
    if diff > 0:
        print(f"  {subject}：二班领先 {diff:.2f} 分")
    elif diff < 0:
        print(f"  {subject}：一班领先 {-diff:.2f} 分")
    else:
        print(f"  {subject}：两班持平")
```

---

### 挑战练习：简易数据可视化

**任务**：画出一周步数的柱状图。

```python
import numpy as np
import matplotlib.pyplot as plt

# 一周的步数
steps = np.array([8234, 10532, 6891, 9234, 11023, 5432, 7865])
days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
goal = 8000

# 创建柱状图
plt.figure(figsize=(12, 6))

# 根据是否达标设置颜色
colors = ['green' if step >= goal else 'red' for step in steps]

plt.bar(days, steps, color=colors, alpha=0.7, edgecolor='black')
plt.axhline(y=goal, color='blue', linestyle='--', linewidth=2, label=f'目标：{goal}步')
plt.xlabel('日期', fontsize=12)
plt.ylabel('步数', fontsize=12)
plt.title('一周步数统计', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# 在柱子上显示数值
for i, (day, step) in enumerate(zip(days, steps)):
    plt.text(i, step + 200, str(step), ha='center', fontsize=10)

plt.tight_layout()
plt.show()

print("绿色：达标  红色：未达标")
```

**注意**：这个练习需要安装matplotlib：
```bash
pip install matplotlib
```

---

## 学习资源推荐

学完这一章，如果你想深入学习NumPy，这里有一些推荐资源：

### 官方资源

1. **NumPy官方文档**
   - 网址：https://numpy.org/doc/
   - 特点：最权威、最全面
   - 适合：查API、看示例

2. **NumPy官方教程**
   - 网址：https://numpy.org/doc/stable/user/quickstart.html
   - 特点：从入门到进阶
   - 适合：系统学习

### 在线教程

3. **NumPy中文文档**
   - 网址：https://www.numpy.org.cn/
   - 特点：中文版，方便阅读
   - 适合：中文母语者

4. **菜鸟教程 - NumPy**
   - 网址：https://www.runoob.com/numpy/numpy-tutorial.html
   - 特点：通俗易懂，例子丰富
   - 适合：快速入门

### 书籍推荐

5. **《Python数据分析基础教程：NumPy学习指南》**
   - 作者：Ivan Idris
   - 特点：全面系统，循序渐进
   - 适合：想深入学习的人

6. **《利用Python进行数据分析》**
   - 作者：Wes McKinney（Pandas创始人）
   - 特点：实战导向，讲NumPy和Pandas
   - 适合：想做数据分析的人

### 视频课程

7. **B站**
   - 搜索"NumPy教程"
   - 特点：免费，选择多
   - 适合：喜欢看视频学习的人

### 练习网站

8. **LeetCode**
   - 网址：https://leetcode.com/
   - 特点：算法题，可以用NumPy解
   - 适合：提高编程能力

9. **Kaggle**
   - 网址：https://www.kaggle.com/
   - 特点：真实数据集，实战项目
   - 适合：想做数据科学的人

### 社区

10. **Stack Overflow**
    - 网址：https://stackoverflow.com/
    - 特点：遇到问题可以搜索或提问
    - 适合：解决实际问题

11. **GitHub**
    - 搜索NumPy相关项目
    - 特点：看别人的代码，学习经验
    - 适合：提高代码质量

---

## 学习建议

### 学习路线

```
第1周：基础篇
  ├─ 数组创建和基本操作
  ├─ 数组索引和切片
  └─ 数组形状操作

第2周：运算篇
  ├─ 数学运算
  ├─ 统计函数
  └─ 线性代数基础

第3周：进阶篇
  ├─ 广播机制
  ├─ 数组拼接和分割
  └─ 文件读写

第4周：实战篇
  ├─ 数据分析项目
  ├─ 图像处理
  └─ 综合应用
```

### 学习方法

1. **边学边练**：看完一个知识点，马上写代码试试
2. **做笔记**：记录重要概念和常用方法
3. **写注释**：给自己的代码写注释，加深理解
4. **做项目**：学完基础后，找个小项目练手
5. **查文档**：养成查官方文档的习惯
6. **多思考**：遇到问题先自己想，再查资料

### 常见误区

1. **误区1**：只看不练
   - **正确做法**：每个例子都亲手敲一遍

2. **误区2**：急于求成
   - **正确做法**：扎实学好基础，循序渐进

3. **误区3**：死记硬背
   - **正确做法**：理解原理，需要时查文档

4. **误区4**：只学语法不做项目
   - **正确做法**：学完基础就开始做小项目

5. **误区5**：遇到问题就放弃
   - **正确做法**：报错是正常的，学会调试和查资料

---

## 下一步

太棒了！现在你已经：
- ✅ 了解了NumPy是什么，为什么要学它
- ✅ 知道了NumPy的优势和应用场景
- ✅ 成功安装了NumPy
- ✅ 运行了第一个NumPy程序
- ✅ 了解了NumPy的核心概念
- ✅ 完成了几个实战练习

**你已经迈出了数据科学的第一步！**

NumPy的大门已经为你敞开，接下来我们将深入学习：
- NumPy数组的创建方法
- 数组的索引和切片
- 数组的形状操作
- 数学运算和统计函数
- 线性代数
- 实战项目

准备好了吗？让我们继续NumPy的学习之旅！

[下一章：第02章 - NumPy数组基础 →](../02-NumPy数组基础/02-NumPy数组基础.md)

---

## 本章重点总结

### 核心概念

1. **NumPy是什么**
   - Python的数值计算库
   - 提供高效的多维数组对象（ndarray）
   - 数据科学生态的基石

2. **为什么学NumPy**
   - 速度快（比列表快10-100倍）
   - 代码简洁（向量化运算）
   - 功能强大（丰富的数学函数）
   - 生态基础（其他库都依赖它）

3. **NumPy vs Python列表**
   - 类型：NumPy必须统一，列表可以混合
   - 速度：NumPy快得多
   - 功能：NumPy专为数值计算设计
   - 内存：NumPy更节省

4. **NumPy生态**
   - Pandas：数据分析
   - SciPy：科学计算
   - Matplotlib：数据可视化
   - Scikit-learn：机器学习
   - TensorFlow/PyTorch：深度学习

### 技能清单

- ✅ 能够安装NumPy
- ✅ 能够导入NumPy并创建数组
- ✅ 了解NumPy的基本概念
- ✅ 能够做简单的数组运算
- ✅ 知道如何查文档和找资源

### 常用命令

```python
# 导入NumPy
import numpy as np

# 创建数组
arr = np.array([1, 2, 3])

# 查看版本
print(np.__version__)

# 基本运算
arr + 10
arr * 2
np.sum(arr)
np.mean(arr)
```

### 记住这些

1. **NumPy快但类型要统一**
2. **向量化运算是NumPy的精髓**
3. **NumPy是数据科学的基础，必须学好**
4. **遇到问题先查官方文档**
5. **多练习，多写代码**

---

**准备好了吗？下一章我们将深入学习NumPy数组！**
