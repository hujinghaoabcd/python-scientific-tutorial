# 第11章：for循环

循环让代码重复执行，for循环是Python中最常用的循环。

## 什么是循环？

循环就像跑圈，重复做同一件事。

```python
# 打印5遍
for i in range(5):
    print("Hello")

# 输出：
# Hello
# Hello
# Hello
# Hello
# Hello
```

## 基本for循环

### 遍历range

```python
# range(n)：0到n-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)：start到stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)：步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 倒数
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

### 遍历列表

```python
fruits = ["apple", "banana", "orange"]

# 直接遍历元素
for fruit in fruits:
    print(fruit)

# 遍历索引
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# enumerate()：同时获取索引和元素（推荐！）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 从1开始编号
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### 遍历字符串

```python
text = "Python"

# 遍历每个字符
for char in text:
    print(char)

# 带索引
for i, char in enumerate(text):
    print(f"{i}: {char}")
```

### 遍历字典

```python
student = {"name": "小明", "age": 18, "score": 95}

# 遍历keys
for key in student:
    print(key)

# 遍历values
for value in student.values():
    print(value)

# 遍历items（最常用）
for key, value in student.items():
    print(f"{key}: {value}")
```

### 遍历集合

```python
numbers = {1, 2, 3, 4, 5}

for num in numbers:
    print(num)
```

## 嵌套循环

循环里面还有循环。

### 二重循环

```python
# 打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行
```

### 遍历二维列表

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 遍历每个元素
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# 带索引
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

## break语句

跳出整个循环。

```python
# 找到第一个偶数就停止
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"找到偶数：{num}")
        break
    print(f"检查：{num}")

# 输出：
# 检查：1
# 检查：3
# 检查：5
# 找到偶数：8
```

### 嵌套循环中的break

```python
# break只跳出当前循环
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"i={i}, j={j}")
    print(f"外层循环 i={i}")
```

## continue语句

跳过本次循环，继续下一次。

```python
# 跳过偶数
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 只打印奇数：1, 3, 5, 7, 9
```

## else子句

循环正常结束（没有break）时执行。

```python
# 查找质数
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num}不是质数")
        break
else:
    print(f"{num}是质数")
```

## zip()函数

同时遍历多个序列。

```python
names = ["张三", "李四", "王五"]
ages = [18, 19, 20]
scores = [90, 85, 92]

# 同时遍历
for name, age, score in zip(names, ages, scores):
    print(f"{name}, {age}岁, {score}分")

# 长度不同时，以最短的为准
list1 = [1, 2, 3]
list2 = ['a', 'b']
for x, y in zip(list1, list2):
    print(x, y)  # 只打印2对
```

## reversed()函数

反向遍历。

```python
fruits = ["apple", "banana", "orange"]

# 反向遍历
for fruit in reversed(fruits):
    print(fruit)  # orange, banana, apple

# 倒数
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0
```

## sorted()函数

排序后遍历（不改变原序列）。

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# 升序
for num in sorted(numbers):
    print(num)  # 1, 1, 2, 3, 4, 5, 9

# 降序
for num in sorted(numbers, reverse=True):
    print(num)  # 9, 5, 4, 3, 2, 1, 1

# 按长度排序字符串
words = ["apple", "pie", "banana"]
for word in sorted(words, key=len):
    print(word)  # pie, apple, banana
```

## 实战例子

### 例子1：计算总和和平均值

```python
numbers = [85, 92, 78, 90, 88]

total = 0
for num in numbers:
    total += num

average = total / len(numbers)
print(f"总和：{total}")
print(f"平均值：{average:.2f}")

# 或者用内置函数
print(f"总和：{sum(numbers)}")
print(f"平均值：{sum(numbers) / len(numbers):.2f}")
```

### 例子2：找出最大值和最小值

```python
numbers = [3, 7, 2, 9, 1, 5]

# 不用max()和min()
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"最大值：{max_num}")
print(f"最小值：{min_num}")
```

### 例子3：倒计时

```python
import time

print("倒计时开始！")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # 暂停1秒
print("时间到！")
```

### 例子4：打印图案

```python
# 直角三角形
for i in range(1, 6):
    print("*" * i)

# 输出：
# *
# **
# ***
# ****
# *****

# 等腰三角形
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# 输出：
#     *
#    ***
#   *****
#  *******
# *********
```

### 例子5：九九乘法表

```python
# 完整版
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}×{i}={i*j:2}", end=" ")
    print()

# 三角形版
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
```

### 例子6：斐波那契数列

```python
# 前10项
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 输出：0 1 1 2 3 5 8 13 21 34
```

### 例子7：猜数字游戏（多次机会）

```python
import random

secret = random.randint(1, 100)
attempts = 5

print("我想了一个1-100的数字，你有5次机会猜")

for i in range(attempts):
    guess = int(input(f"第{i+1}次猜测："))

    if guess == secret:
        print("恭喜你猜对了！")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"很遗憾，正确答案是{secret}")
```

### 例子8：成绩统计

```python
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 95},
    {"name": "孙七", "score": 88}
]

# 统计
total = 0
max_score = 0
max_student = ""
pass_count = 0

for student in students:
    name = student["name"]
    score = student["score"]

    total += score

    if score > max_score:
        max_score = score
        max_student = name

    if score >= 60:
        pass_count += 1

average = total / len(students)

print(f"平均分：{average:.2f}")
print(f"最高分：{max_student} {max_score}分")
print(f"及格人数：{pass_count}/{len(students)}")
```

### 例子9：字符统计

```python
text = "Hello, World!"

# 统计每个字符出现的次数
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 打印结果
for char, count in sorted(char_count.items()):
    print(f"'{char}': {count}次")
```

### 例子10：购物车结算

```python
cart = [
    {"name": "苹果", "price": 5.0, "quantity": 3},
    {"name": "香蕉", "price": 3.0, "quantity": 5},
    {"name": "橙子", "price": 4.0, "quantity": 2}
]

print("=== 购物清单 ===")
print("商品\t单价\t数量\t小计")
print("-" * 40)

total = 0
for item in cart:
    name = item["name"]
    price = item["price"]
    quantity = item["quantity"]
    subtotal = price * quantity

    print(f"{name}\t¥{price}\t{quantity}\t¥{subtotal}")
    total += subtotal

print("-" * 40)
print(f"总计：¥{total:.2f}")

# 打折
if total >= 100:
    discount = total * 0.1
    final = total - discount
    print(f"满100减10: -¥{discount:.2f}")
    print(f"实付：¥{final:.2f}")
```

## 性能优化技巧

### 避免在循环中重复计算

```python
# 不好
for i in range(len(my_list)):
    print(my_list[i])

# 好
length = len(my_list)
for i in range(length):
    print(my_list[i])

# 更好
for item in my_list:
    print(item)
```

### 列表推导式（后面会讲）

```python
# 传统方式
squares = []
for x in range(10):
    squares.append(x ** 2)

# 列表推导式（更快）
squares = [x ** 2 for x in range(10)]
```

## 常见错误

### 错误1：修改循环中的列表

```python
# 错误：边遍历边删除
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 危险！

# 正确：用列表推导式
numbers = [num for num in numbers if num % 2 != 0]

# 或者：复制一份
numbers = [1, 2, 3, 4, 5]
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)
```

### 错误2：range参数理解错误

```python
# 错误理解
for i in range(5, 1):  # 空循环，不会执行
    print(i)

# 正确：降序要指定步长
for i in range(5, 1, -1):
    print(i)  # 5, 4, 3, 2
```

### 错误3：循环变量作用域

```python
# i在循环结束后仍然存在
for i in range(5):
    pass
print(i)  # 4，i还在

# 这可能导致意外错误
for i in range(3):
    for i in range(2):  # 内层循环覆盖了i
        pass
```

## 练习题

### 练习1：阶乘计算

计算n的阶乘（n! = 1×2×3×...×n）。

### 练习2：质数判断

判断1-100中有多少个质数。

### 练习3：找出完数

找出1-1000中的所有完数（完数=所有因子之和，如6=1+2+3）。

### 练习4：打印菱形

```python
# 输入n=5，输出：
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
```

### 练习5：数字金字塔

```python
# 输出：
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

### 练习6：反转列表

不使用reverse()方法，反转一个列表。

### 练习7：寻找重复元素

找出列表中第一个重复的元素。

### 练习8：矩阵转置

将二维列表转置。

## 下一步

学会了for循环，下一章我们学习while循环，另一种循环方式！

[上一章：第10章 - 条件判断 ←](../10-条件判断/10-条件判断.md)

[下一章：第12章 - while循环 →](../12-while循环/12-while循环.md)

---

**本章重点**
- ✅ for循环遍历序列
- ✅ range()生成数字序列
- ✅ enumerate()同时获取索引和元素
- ✅ break跳出循环
- ✅ continue跳过本次循环
- ✅ else在循环正常结束时执行
- ✅ zip()同时遍历多个序列

**记住**
- for循环用于遍历已知次数的情况
- 不要在循环中修改正在遍历的列表
- enumerate()从0开始，可以用start参数改变
- break和continue只影响当前循环
- 嵌套循环要注意性能
