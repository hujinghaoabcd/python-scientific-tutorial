# 第16章：Lambda和高阶函数

Lambda表达式和高阶函数是函数式编程的核心，让代码更简洁优雅。

## 什么是Lambda和高阶函数？

### 从生活中理解Lambda

**Lambda = 一次性工具**

想象你在做饭：

**场景1：需要重复用的工具（普通函数）**
```python
# 炒菜锅：经常用，专门买一个，放在厨房
def stir_fry(ingredients):
    """炒菜"""
    print(f"炒{ingredients}")
    return f"炒好的{ingredients}"

# 用很多次
stir_fry("鸡蛋")
stir_fry("青菜")
stir_fry("牛肉")
```

**场景2：只用一次的工具（Lambda）**
```python
# 一次性筷子：用完就扔，不需要专门买
# Lambda就是"一次性函数"

# 普通函数：写个函数，起个名字
def double(x):
    return x * 2

result = double(5)  # 10

# Lambda：不起名字，写完就用，用完就忘
result = (lambda x: x * 2)(5)  # 10

# 就像一次性筷子，用完不需要洗不需要收！
```

**什么时候用Lambda？**
- 函数很简单（1行就能写完）
- 只用一次，不需要重复调用
- 作为参数传给其他函数

**什么时候不用Lambda？**
- 逻辑复杂（多行代码）
- 需要多次调用（起个名字更好）
- 需要文档说明（Lambda没法写文档）

### 从生活中理解高阶函数

**高阶函数 = 函数的函数**

想象你是老板，员工就是"函数"：

**场景1：map() = 流水线工人**
```python
# 你有一批原材料（数据）
numbers = [1, 2, 3, 4, 5]

# 你需要每个都加工一遍（平方）
# 不用高阶函数：一个个处理
results = []
for num in numbers:
    results.append(num ** 2)
# [1, 4, 9, 16, 25]

# 用map（高阶函数）：告诉流水线工人"把每个都平方"
results = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# map就像流水线：每个数字都经过"平方"这道工序
```

**场景2：filter() = 质检员**
```python
# 你有一批产品（数据）
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 你只要合格的（偶数）
# 不用高阶函数：一个个检查
results = []
for num in numbers:
    if num % 2 == 0:  # 检查是否偶数
        results.append(num)
# [2, 4, 6, 8, 10]

# 用filter（高阶函数）：告诉质检员"只留偶数"
results = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# filter就像质检员：把不合格的去掉
```

**场景3：reduce() = 会计**
```python
from functools import reduce

# 你有一堆账单（数据）
expenses = [100, 200, 150, 300, 50]

# 你要算总共花了多少钱（累加）
# 不用高阶函数：一个个加
total = 0
for expense in expenses:
    total = total + expense
# 800

# 用reduce（高阶函数）：告诉会计"把这些都加起来"
total = reduce(lambda x, y: x + y, expenses)
# 800

# reduce就像会计：把多个数字合并成一个结果
```

### 为什么要学Lambda和高阶函数？

**1. 代码更简洁**
```python
# ❌ 不用Lambda和高阶函数：啰嗦
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)

# ✅ 用Lambda和map：一行搞定！
squared = list(map(lambda x: x ** 2, numbers))
```

**2. 函数式编程风格**
```python
# 函数式编程：像搭积木一样组合函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 找出偶数，平方，求和
result = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
# 2² + 4² + 6² + 8² + 10² = 220

# 读法：从里到外
# 1. filter找出偶数：[2, 4, 6, 8, 10]
# 2. map平方：[4, 16, 36, 64, 100]
# 3. sum求和：220
```

**3. 作为参数传递很方便**
```python
# 按不同规则排序
students = [
    ("张三", 85),
    ("李四", 92),
    ("王五", 78)
]

# 按分数排序：用Lambda作为key
students.sort(key=lambda s: s[1])  # [(王五, 78), (张三, 85), (李四, 92)]

# 如果用普通函数，还要专门定义一个：
def get_score(student):
    return student[1]

students.sort(key=get_score)  # 麻烦！
```

### 本章要学什么？

1. **Lambda表达式** - 匿名函数，一行代码定义函数
2. **map()** - 对每个元素应用函数
3. **filter()** - 过滤出符合条件的元素
4. **reduce()** - 把多个值合并成一个
5. **其他高阶函数** - sorted(), zip(), all(), any()
6. **实战应用** - 数据处理、排序、过滤

**核心思想**：
- Lambda：小巧轻便的一次性函数
- 高阶函数：把函数当作"工具"来使用
- 组合使用：像搭积木一样组合功能

让我们开始吧！

```python
# 普通函数
def add(x, y):
    return x + y

# Lambda表达式（匿名函数）
add = lambda x, y: x + y

print(add(3, 5))  # 8
```

**Lambda的特点**：
- 没有名字（匿名）
- 只能写一行表达式
- 自动返回结果
- 适合简单的函数

### 为什么叫Lambda？

Lambda（λ）来自数学中的λ演算，是函数式编程的基础。别被名字吓到，它就是"小函数"的意思！

## Lambda基础语法

### 格式

```python
lambda 参数1, 参数2, ... : 表达式
```

### 单个参数

```python
# 平方函数
square = lambda x: x ** 2
print(square(5))  # 25

# 判断偶数
is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(5))  # False
```

### 多个参数

```python
# 两个参数
add = lambda x, y: x + y
print(add(10, 20))  # 30

# 三个参数
volume = lambda l, w, h: l * w * h
print(volume(2, 3, 4))  # 24
```

### 无参数

```python
# 无参数
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!
```

### 带条件的Lambda

```python
# 三元表达式
max_num = lambda x, y: x if x > y else y
print(max_num(10, 20))  # 20

# 判断正负
sign = lambda x: "正数" if x > 0 else ("负数" if x < 0 else "零")
print(sign(5))   # 正数
print(sign(-3))  # 负数
print(sign(0))   # 零
```

## Lambda的使用场景

### 场景1：作为参数传递

```python
# 排序时使用
students = [
    ("张三", 85),
    ("李四", 92),
    ("王五", 78),
    ("赵六", 95)
]

# 按分数排序
students.sort(key=lambda s: s[1])
print(students)  # 按分数升序

# 按分数降序
students.sort(key=lambda s: s[1], reverse=True)
print(students)

# 按名字长度排序
words = ["apple", "pie", "banana", "cherry"]
words.sort(key=lambda w: len(w))
print(words)  # ['pie', 'apple', 'banana', 'cherry']
```

### 场景2：在列表方法中

```python
# max/min的key参数
points = [(1, 5), (3, 2), (5, 8), (2, 9)]

# 找y坐标最大的点
max_point = max(points, key=lambda p: p[1])
print(max_point)  # (2, 9)

# 找x坐标最小的点
min_point = min(points, key=lambda p: p[0])
print(min_point)  # (1, 5)
```

### 场景3：字典排序

```python
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 95}

# 按分数排序
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)
# {'赵六': 95, '李四': 92, '张三': 85, '王五': 78}
```

### 场景4：立即执行

```python
# 定义并立即执行
result = (lambda x, y: x * y)(5, 3)
print(result)  # 15

# 实用例子：配置初始化
config = (lambda: {
    "host": "localhost",
    "port": 8000,
    "debug": True
})()
print(config)
```

## 高阶函数

高阶函数是接受函数作为参数，或返回函数的函数。

### map() - 映射

对序列中的每个元素应用函数。

```python
# 基本用法
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# 字符串转大写
words = ["hello", "world", "python"]
upper = map(lambda w: w.upper(), words)
print(list(upper))  # ['HELLO', 'WORLD', 'PYTHON']

# 或者直接传函数名
upper = map(str.upper, words)
print(list(upper))  # ['HELLO', 'WORLD', 'PYTHON']
```

### map()的高级用法

```python
# 多个序列
a = [1, 2, 3]
b = [10, 20, 30]
result = map(lambda x, y: x + y, a, b)
print(list(result))  # [11, 22, 33]

# 提取属性
students = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 19},
    {"name": "王五", "age": 20}
]
names = map(lambda s: s["name"], students)
print(list(names))  # ['张三', '李四', '王五']

# 格式化
prices = [10.5, 20.3, 30.9]
formatted = map(lambda p: f"¥{p:.2f}", prices)
print(list(formatted))  # ['¥10.50', '¥20.30', '¥30.90']
```

### filter() - 过滤

保留满足条件的元素。

```python
# 基本用法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤偶数
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # [2, 4, 6, 8, 10]

# 过滤奇数
odd = filter(lambda x: x % 2 != 0, numbers)
print(list(odd))  # [1, 3, 5, 7, 9]

# 过滤大于5的数
greater = filter(lambda x: x > 5, numbers)
print(list(greater))  # [6, 7, 8, 9, 10]
```

### filter()的高级用法

```python
# 过滤非空字符串
texts = ["hello", "", "world", "", "python"]
non_empty = filter(lambda t: len(t) > 0, texts)
print(list(non_empty))  # ['hello', 'world', 'python']

# 或者更简洁（空字符串是False）
non_empty = filter(None, texts)
print(list(non_empty))  # ['hello', 'world', 'python']

# 过滤及格学生
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 55},
    {"name": "王五", "score": 92},
    {"name": "赵六", "score": 48}
]
passed = filter(lambda s: s["score"] >= 60, students)
print(list(passed))
# [{'name': '张三', 'score': 85}, {'name': '王五', 'score': 92}]
```

### reduce() - 归约

累积计算，把序列归约成单个值。

```python
from functools import reduce

# 求和
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# 等价于
total = 0
for num in numbers:
    total = total + num
print(total)  # 15

# 求积
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# 找最大值
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # 5
```

### reduce()的高级用法

```python
from functools import reduce

# 字符串连接
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Hello World!

# 计算阶乘
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"{n}! = {factorial}")  # 5! = 120

# 展平嵌套列表
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda x, y: x + y, nested)
print(flat)  # [1, 2, 3, 4, 5, 6]
```

## 组合使用map、filter、reduce

```python
from functools import reduce

# 找出偶数，平方后求和
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法1：链式调用
result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print(result)  # 2²+4²+6²+8²+10² = 220

# 方法2：分步骤（更清晰）
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, even_numbers)
total = reduce(lambda x, y: x + y, squared)
print(total)  # 220

# 方法3：列表推导式（最Pythonic）
result = sum(x ** 2 for x in numbers if x % 2 == 0)
print(result)  # 220
```

## 其他高阶函数

### sorted() - 排序

```python
# 按绝对值排序
numbers = [-5, 3, -8, 1, 9, -2]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)  # [1, -2, 3, -5, -8, 9]

# 按字符串长度排序
words = ["python", "is", "awesome", "!"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)  # ['!', 'is', 'python', 'awesome']

# 多条件排序
students = [
    ("张三", 85, 18),
    ("李四", 92, 19),
    ("王五", 85, 17),
    ("赵六", 92, 18)
]
# 先按分数降序，再按年龄升序
sorted_students = sorted(students, key=lambda s: (-s[1], s[2]))
print(sorted_students)
```

### zip() - 打包

```python
# 基本用法
names = ["张三", "李四", "王五"]
ages = [18, 19, 20]
cities = ["北京", "上海", "广州"]

# 打包成元组
combined = list(zip(names, ages, cities))
print(combined)
# [('张三', 18, '北京'), ('李四', 19, '上海'), ('王五', 20, '广州')]

# 创建字典
person_dict = dict(zip(names, ages))
print(person_dict)  # {'张三': 18, '李四': 19, '王五': 20}

# 解包
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*zipped)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

### all() 和 any()

```python
# all() - 所有元素都为True
numbers = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers))  # True（都是偶数）

numbers = [2, 4, 5, 8]
print(all(x % 2 == 0 for x in numbers))  # False（5是奇数）

# any() - 至少一个元素为True
numbers = [1, 3, 5, 6]
print(any(x % 2 == 0 for x in numbers))  # True（6是偶数）

numbers = [1, 3, 5, 7]
print(any(x % 2 == 0 for x in numbers))  # False（都是奇数）
```

## 实战例子

### 例子1：数据处理管道

```python
# 处理学生数据
students = [
    {"name": "张三", "score": 85, "age": 18},
    {"name": "李四", "score": 92, "age": 19},
    {"name": "王五", "score": 78, "age": 18},
    {"name": "赵六", "score": 95, "age": 20},
    {"name": "孙七", "score": 55, "age": 19}
]

# 找出18岁以上且分数>=80的学生姓名
result = list(map(
    lambda s: s["name"],
    filter(
        lambda s: s["age"] > 18 and s["score"] >= 80,
        students
    )
))
print(result)  # ['李四', '赵六']

# 更Pythonic的写法
result = [s["name"] for s in students if s["age"] > 18 and s["score"] >= 80]
print(result)
```

### 例子2：价格计算

```python
# 商品价格计算
products = [
    {"name": "苹果", "price": 5.0, "quantity": 3},
    {"name": "香蕉", "price": 3.0, "quantity": 5},
    {"name": "橙子", "price": 4.0, "quantity": 2}
]

# 计算每个商品小计
subtotals = list(map(lambda p: p["price"] * p["quantity"], products))
print(subtotals)  # [15.0, 15.0, 8.0]

# 计算总价
from functools import reduce
total = reduce(lambda x, y: x + y, subtotals)
print(f"总价：¥{total}")  # 总价：¥38.0

# 或者一步到位
total = sum(map(lambda p: p["price"] * p["quantity"], products))
print(f"总价：¥{total}")
```

### 例子3：文本处理

```python
# 处理文本数据
texts = [
    "  Hello World  ",
    "PYTHON IS AWESOME",
    "  learn programming  ",
    ""
]

# 清理：去空格、转小写、过滤空字符串
cleaned = list(filter(
    lambda t: len(t) > 0,
    map(
        lambda t: t.strip().lower(),
        texts
    )
))
print(cleaned)
# ['hello world', 'python is awesome', 'learn programming']
```

### 例子4：数学运算

```python
# 计算平方和
numbers = [1, 2, 3, 4, 5]

# 方法1：reduce
from functools import reduce
sum_of_squares = reduce(lambda x, y: x + y, map(lambda n: n ** 2, numbers))
print(sum_of_squares)  # 55

# 方法2：内置函数（更简洁）
sum_of_squares = sum(map(lambda n: n ** 2, numbers))
print(sum_of_squares)  # 55

# 方法3：生成器表达式（最Pythonic）
sum_of_squares = sum(n ** 2 for n in numbers)
print(sum_of_squares)  # 55
```

### 例子5：分组统计

```python
# 按条件分组
numbers = list(range(1, 21))

# 分成偶数和奇数
even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print(f"偶数: {even}")
print(f"奇数: {odd}")

# 按范围分组
small = list(filter(lambda x: x < 10, numbers))
large = list(filter(lambda x: x >= 10, numbers))

print(f"小于10: {small}")
print(f"大于等于10: {large}")
```

### 例子6：坐标变换

```python
# 2D坐标变换
points = [(1, 2), (3, 4), (5, 6)]

# 所有坐标+10
shifted = list(map(lambda p: (p[0] + 10, p[1] + 10), points))
print(shifted)  # [(11, 12), (13, 14), (15, 16)]

# 缩放2倍
scaled = list(map(lambda p: (p[0] * 2, p[1] * 2), points))
print(scaled)  # [(2, 4), (6, 8), (10, 12)]

# 计算距离
import math
distances = list(map(lambda p: math.sqrt(p[0]**2 + p[1]**2), points))
print(distances)
```

### 例子7：数据验证

```python
# 验证邮箱列表
emails = [
    "user@example.com",
    "invalid@",
    "test@domain.co.uk",
    "bad email",
    "admin@site.com"
]

# 简单验证：包含@和.
valid_emails = list(filter(lambda e: '@' in e and '.' in e, emails))
print(valid_emails)
# ['user@example.com', 'test@domain.co.uk', 'admin@site.com']
```

### 例子8：成绩统计

```python
# 成绩统计
scores = [85, 92, 78, 95, 88, 76, 90, 82]

# 统计信息
stats = {
    "总分": sum(scores),
    "平均分": sum(scores) / len(scores),
    "最高分": max(scores),
    "最低分": min(scores),
    "及格人数": len(list(filter(lambda s: s >= 60, scores))),
    "优秀人数": len(list(filter(lambda s: s >= 90, scores)))
}

for key, value in stats.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
```

### 例子9：购物车折扣

```python
# 购物车折扣计算
cart = [
    {"name": "T恤", "price": 99, "quantity": 2},
    {"name": "裤子", "price": 199, "quantity": 1},
    {"name": "鞋子", "price": 299, "quantity": 1}
]

# 满100打9折
discount_rate = lambda total: 0.9 if total >= 100 else 1.0

# 计算每项小计
cart_with_subtotal = list(map(
    lambda item: {
        **item,
        "subtotal": item["price"] * item["quantity"]
    },
    cart
))

# 计算总价
total = sum(map(lambda item: item["subtotal"], cart_with_subtotal))
final_price = total * discount_rate(total)

print(f"原价：¥{total}")
print(f"折后：¥{final_price:.2f}")
```

### 例子10：数据转换

```python
# CSV数据转换
csv_data = [
    "张三,18,北京",
    "李四,19,上海",
    "王五,20,广州"
]

# 转换成字典列表
students = list(map(
    lambda line: dict(zip(
        ["name", "age", "city"],
        line.split(",")
    )),
    csv_data
))

print(students)
# [{'name': '张三', 'age': '18', 'city': '北京'}, ...]

# 转换年龄为整数
students = list(map(
    lambda s: {**s, "age": int(s["age"])},
    students
))
print(students)
```

## Lambda vs 普通函数

### 什么时候用Lambda？

```python
# ✅ 适合用Lambda
# 1. 简单的单行函数
numbers.sort(key=lambda x: x % 10)

# 2. 作为参数传递
squared = map(lambda x: x ** 2, numbers)

# 3. 临时使用，不需要复用
result = filter(lambda x: x > 0, values)
```

### 什么时候用普通函数？

```python
# ✅ 应该用普通函数
# 1. 复杂逻辑
def process_data(data):
    if not data:
        return None
    cleaned = [x.strip() for x in data]
    filtered = [x for x in cleaned if x]
    return filtered

# 2. 需要文档说明
def calculate_tax(income):
    """
    计算个人所得税

    参数:
        income: 收入金额
    返回:
        应纳税额
    """
    # 复杂的计算逻辑...
    return tax

# 3. 需要多处复用
def validate_email(email):
    """验证邮箱格式"""
    return '@' in email and '.' in email
```

## 常见陷阱

### 陷阱1：Lambda中的循环变量

```python
# 错误
functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())  # 2, 2, 2（都是2！）

# 正确：使用默认参数
functions = []
for i in range(3):
    functions.append(lambda x=i: x)

for f in functions:
    print(f())  # 0, 1, 2
```

### 陷阱2：Lambda不能包含语句

```python
# 错误
# func = lambda x: print(x)  # SyntaxError

# 正确：使用普通函数
def func(x):
    print(x)
```

### 陷阱3：过度使用Lambda

```python
# 不好：难以理解
result = list(filter(lambda x: x > 0, map(lambda x: x ** 2 - 10, range(10))))

# 好：分步骤或用函数
def process(x):
    return x ** 2 - 10

def is_positive(x):
    return x > 0

result = list(filter(is_positive, map(process, range(10))))

# 或者用列表推导式
result = [x ** 2 - 10 for x in range(10) if x ** 2 - 10 > 0]
```

## 练习题

### 练习1：过滤质数

用filter和lambda找出列表中的所有质数。

```python
numbers = list(range(2, 50))
# 提示：先写判断质数的函数
```

### 练习2：单词统计

用map统计每个单词的长度。

```python
words = ["python", "is", "awesome"]
# 结果：[(6, 'python'), (2, 'is'), (7, 'awesome')]
```

### 练习3：数据清洗

用map和filter清洗数据：去空格、转小写、过滤空字符串。

```python
data = ["  Hello  ", "", "  WORLD  ", "python", "  "]
```

### 练习4：嵌套列表展平

用reduce展平嵌套列表。

```python
nested = [[1, 2], [3, 4, 5], [6]]
# 结果：[1, 2, 3, 4, 5, 6]
```

### 练习5：复杂排序

按多个条件排序学生列表。

```python
students = [
    ("张三", 85, "male"),
    ("李四", 92, "female"),
    ("王五", 85, "male"),
    ("赵六", 92, "male")
]
# 先按分数降序，再按性别，再按姓名
```

## 下一步

学会了Lambda和高阶函数，下一章我们学习模块和包，学会组织大型项目！

[上一章：第15章 - 函数进阶 ←](../15-函数进阶/15-函数进阶.md)

[下一章：第17章 - 模块和包 →](../17-模块和包/17-模块和包.md)

---

**本章重点**
- ✅ Lambda表达式语法
- ✅ map()、filter()、reduce()
- ✅ 高阶函数的使用
- ✅ 函数式编程思想
- ✅ Lambda vs 普通函数
- ✅ 避免常见陷阱

**记住**
- Lambda适合简单函数
- 复杂逻辑用普通函数
- map/filter/reduce很强大
- 不要过度使用Lambda
- 可读性比简洁性更重要
