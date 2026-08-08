# 第12章：while循环

while循环在条件为True时重复执行，适合不知道循环次数的情况。

## 基本while循环

```python
# 基本格式
count = 0
while count < 5:
    print(f"第{count}次")
    count += 1

# 输出：
# 第0次
# 第1次
# 第2次
# 第3次
# 第4次
```

**特点**：
- 先判断条件，条件为True才执行
- 每次执行完检查条件
- 如果条件一直为True，会无限循环

## while vs for

### 什么时候用while？

```python
# 1. 不知道循环次数
password = ""
while password != "123456":
    password = input("请输入密码：")
print("密码正确！")

# 2. 需要更灵活的控制
balance = 100
while balance > 0:
    cost = float(input("消费金额："))
    if cost > balance:
        print("余额不足")
        break
    balance -= cost
    print(f"剩余：¥{balance}")
```

### 什么时候用for？

```python
# 1. 已知循环次数
for i in range(10):
    print(i)

# 2. 遍历序列
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

## break语句

跳出循环。

```python
# 猜数字（无限机会）
import random
secret = random.randint(1, 100)

while True:
    guess = int(input("猜一个数字："))
    if guess == secret:
        print("猜对了！")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")
```

## continue语句

跳过本次循环。

```python
# 只打印奇数
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)  # 1, 3, 5, 7, 9
```

## else子句

循环正常结束时执行。

```python
# 找质数
num = 17
i = 2
while i < num:
    if num % i == 0:
        print(f"{num}不是质数")
        break
    i += 1
else:
    print(f"{num}是质数")
```

## 无限循环

### 故意的无限循环

```python
# 服务器主循环
while True:
    command = input("输入命令（quit退出）：")
    if command == "quit":
        break
    print(f"执行命令：{command}")
```

### 意外的无限循环（bug）

```python
# 错误：忘记更新条件
count = 0
while count < 5:
    print("循环")
    # 忘记 count += 1，永远循环！

# 错误：条件永远为True
while True:
    print("无限循环")
    # 没有break语句！
```

**如何停止无限循环**：
- 按`Ctrl + C`强制停止

## 嵌套while循环

```python
# 打印乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}×{i}={i*j}", end="\t")
        j += 1
    print()
    i += 1
```

## 实战例子

### 例子1：登录系统（3次机会）

```python
username = "admin"
password = "123456"
attempts = 3

while attempts > 0:
    input_user = input("用户名：")
    input_pass = input("密码：")

    if input_user == username and input_pass == password:
        print("登录成功！")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"用户名或密码错误，还有{attempts}次机会")
        else:
            print("登录失败，账号已锁定")
```

### 例子2：ATM取款机

```python
balance = 1000.0

while True:
    print("\n=== ATM取款机 ===")
    print("1. 查询余额")
    print("2. 取款")
    print("3. 存款")
    print("4. 退出")

    choice = input("请选择：")

    if choice == "1":
        print(f"当前余额：¥{balance:.2f}")
    elif choice == "2":
        amount = float(input("取款金额："))
        if amount > balance:
            print("余额不足")
        elif amount <= 0:
            print("金额无效")
        else:
            balance -= amount
            print(f"取款成功，余额：¥{balance:.2f}")
    elif choice == "3":
        amount = float(input("存款金额："))
        if amount <= 0:
            print("金额无效")
        else:
            balance += amount
            print(f"存款成功，余额：¥{balance:.2f}")
    elif choice == "4":
        print("感谢使用，再见！")
        break
    else:
        print("无效选择")
```

### 例子3：求最大公约数（辗转相除法）

```python
a = int(input("第一个数："))
b = int(input("第二个数："))

# 辗转相除法
original_a, original_b = a, b
while b != 0:
    a, b = b, a % b

print(f"{original_a}和{original_b}的最大公约数是{a}")
```

### 例子4：计算器

```python
print("简单计算器（输入'quit'退出）")

while True:
    expression = input("\n输入表达式（如：5 + 3）：")

    if expression.lower() == "quit":
        print("再见！")
        break

    try:
        result = eval(expression)
        print(f"结果：{result}")
    except:
        print("表达式无效")
```

### 例子5：猜数字游戏（完整版）

```python
import random

print("=== 猜数字游戏 ===")
print("我想了一个1-100的数字")

secret = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"第{attempts+1}次猜测："))
        attempts += 1

        if guess < 1 or guess > 100:
            print("请输入1-100的数字")
            continue

        if guess == secret:
            print(f"恭喜！你用{attempts}次猜对了！")
            break
        elif guess < secret:
            print("太小了")
        else:
            print("太大了")

        # 提示剩余次数
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"还有{remaining}次机会")
    except ValueError:
        print("请输入有效的数字")

if guess != secret:
    print(f"游戏结束，正确答案是{secret}")
```

### 例子6：斐波那契数列（输入最大值）

```python
max_value = int(input("输入最大值："))

a, b = 0, 1
print("斐波那契数列：", end="")

while a <= max_value:
    print(a, end=" ")
    a, b = b, a + b
```

### 例子7：数字反转

```python
num = int(input("输入一个整数："))
reversed_num = 0

original = num
while num > 0:
    digit = num % 10  # 取最后一位
    reversed_num = reversed_num * 10 + digit
    num = num // 10   # 去掉最后一位

print(f"{original}反转后是{reversed_num}")
```

### 例子8：回文数判断

```python
num = int(input("输入一个整数："))

# 反转数字
original = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10

# 判断
if original == reversed_num:
    print(f"{original}是回文数")
else:
    print(f"{original}不是回文数")
```

### 例子9：菜单系统

```python
shopping_list = []

while True:
    print("\n=== 购物清单 ===")
    print("1. 添加商品")
    print("2. 删除商品")
    print("3. 查看清单")
    print("4. 清空清单")
    print("5. 退出")

    choice = input("选择操作：")

    if choice == "1":
        item = input("商品名称：")
        shopping_list.append(item)
        print(f"已添加：{item}")
    elif choice == "2":
        if shopping_list:
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            try:
                index = int(input("删除第几个？")) - 1
                removed = shopping_list.pop(index)
                print(f"已删除：{removed}")
            except:
                print("无效的选择")
        else:
            print("清单为空")
    elif choice == "3":
        if shopping_list:
            print("\n当前清单：")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("清单为空")
    elif choice == "4":
        shopping_list.clear()
        print("清单已清空")
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效选择")
```

### 例子10：简单的聊天机器人

```python
print("聊天机器人：你好！我是机器人，输入'bye'退出")

while True:
    user_input = input("你：").lower()

    if user_input == "bye":
        print("机器人：再见！")
        break
    elif "你好" in user_input or "hello" in user_input:
        print("机器人：你好！很高兴见到你")
    elif "名字" in user_input or "name" in user_input:
        print("机器人：我叫小智")
    elif "天气" in user_input:
        print("机器人：今天天气不错呢")
    elif "谢谢" in user_input:
        print("机器人：不客气")
    else:
        print("机器人：我不太明白你的意思")
```

## while True的常见模式

### 模式1：直到满足条件

```python
while True:
    user_input = input("输入'yes'继续：")
    if user_input == "yes":
        break
```

### 模式2：菜单循环

```python
while True:
    print("菜单...")
    choice = input("选择：")
    if choice == "quit":
        break
    # 处理选择
```

### 模式3：重试机制

```python
max_retries = 3
retry = 0

while retry < max_retries:
    try:
        # 尝试操作
        result = risky_operation()
        break
    except:
        retry += 1
        print(f"失败，重试{retry}/{max_retries}")
```

## 常见错误

### 错误1：忘记更新条件

```python
# 错误
i = 0
while i < 5:
    print(i)
    # 忘记 i += 1，无限循环！

# 正确
i = 0
while i < 5:
    print(i)
    i += 1
```

### 错误2：条件永远为True

```python
# 错误
x = 10
while x > 0:
    print(x)
    x += 1  # x越来越大，永远>0

# 正确
x = 10
while x > 0:
    print(x)
    x -= 1
```

### 错误3：死循环没有退出条件

```python
# 错误
while True:
    print("循环")
    # 没有break

# 正确
while True:
    print("循环")
    if some_condition:
        break
```

## for vs while 对比

```python
# 已知次数：用for
for i in range(10):
    print(i)

# 相同功能的while（但for更简洁）
i = 0
while i < 10:
    print(i)
    i += 1

# 未知次数：用while
password = ""
while password != "correct":
    password = input("密码：")

# 无限循环：用while True
while True:
    command = input("命令：")
    if command == "quit":
        break
```

## 练习题

### 练习1：累加到100

从1加到100，使用while循环。

### 练习2：数字游戏

用户输入数字，累加，输入0时停止并显示总和。

### 练习3：密码强度检查

要求用户输入密码，直到密码长度>=8且包含数字和字母。

### 练习4：倒序打印

输入一个正整数，倒序打印每一位数字。

### 练习5：求平方根

用牛顿迭代法求平方根（不用math.sqrt）。

### 练习6：完美数

找出1-10000中的所有完美数。

### 练习7：输入验证

要求用户输入1-100的数字，无效输入时重新提示。

### 练习8：简单游戏

实现一个"石头剪刀布"游戏，记录胜负次数。

## 下一步

学会了两种循环，下一章我们学习推导式，一种优雅的循环写法！

[上一章：第11章 - for循环 ←](../11-for循环/11-for循环.md)

[下一章：第13章 - 推导式 →](../13-推导式/13-推导式.md)

---

**本章重点**
- ✅ while循环在条件为True时执行
- ✅ 适合不知道循环次数的情况
- ✅ while True创建无限循环
- ✅ 必须有更新条件的语句，否则死循环
- ✅ break跳出循环，continue跳过本次
- ✅ else在正常结束时执行

**记住**
- while循环要小心无限循环
- 一定要有更新条件的代码
- while True + break是常见模式
- 按Ctrl+C停止无限循环
- 已知次数用for，未知次数用while
