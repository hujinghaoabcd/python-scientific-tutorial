# 第24章：JSON和CSV处理

掌握常见数据格式的读写,实现数据交换和存储。

## 什么是JSON和CSV?

### JSON - JavaScript Object Notation

**JSON**是一种轻量级的数据交换格式,人类易读,机器易解析。

```python
# JSON示例
{
  "name": "张三",
  "age": 25,
  "skills": ["Python", "Java"],
  "address": {
    "city": "北京",
    "street": "长安街1号"
  }
}
```

**特点**:
- 结构化数据
- 支持嵌套
- 数据类型丰富
- 跨语言通用
- API常用格式

### CSV - Comma Separated Values

**CSV**是一种简单的表格数据格式,用逗号分隔值。

```csv
姓名,年龄,城市
张三,25,北京
李四,30,上海
王五,28,广州
```

**特点**:
- 简单易懂
- Excel可直接打开
- 文件小巧
- 适合表格数据
- 数据分析常用

## JSON处理

### 基本操作

```python
import json

# Python对象 → JSON字符串
data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "Java"],
    "is_student": True,
    "score": 85.5,
    "address": None
}

# dumps - 序列化为字符串
json_str = json.dumps(data)
print(json_str)
# {"name": "\u5f20\u4e09", "age": 25, ...}

# 中文不转义 + 格式化
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
"""
{
  "name": "张三",
  "age": 25,
  ...
}
"""

# JSON字符串 → Python对象
obj = json.loads(json_str)
print(obj["name"])  # 张三
print(type(obj))    # <class 'dict'>
```

### 类型映射

```python
import json

# Python → JSON
"""
dict    → object {}
list    → array []
tuple   → array []
str     → string ""
int     → number
float   → number
True    → true
False   → false
None    → null
"""

# JSON → Python
"""
object  → dict
array   → list
string  → str
number  → int/float
true    → True
false   → False
null    → None
"""
```

### 文件操作

```python
import json

data = {
    "users": [
        {"name": "张三", "age": 25},
        {"name": "李四", "age": 30}
    ],
    "count": 2
}

# 写入文件 - dump
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# 自动序列化并写入

# 读取文件 - load
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
# 自动读取并反序列化

print(loaded["users"][0]["name"])  # 张三
```

### 自定义JSON编码

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    """自定义datetime编码器"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(obj)

data = {
    "event": "会议",
    "time": datetime.now()
}

# 使用自定义编码器
json_str = json.dumps(data, cls=DateTimeEncoder, ensure_ascii=False)
print(json_str)
# {"event": "会议", "time": "2024-01-15 14:30:45"}
```

### 处理复杂对象

```python
import json

class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def to_dict(self):
        """转为字典"""
        return {
            "name": self.name,
            "age": self.age,
            "courses": self.courses
        }

    @classmethod
    def from_dict(cls, data):
        """从字典创建"""
        return cls(data["name"], data["age"], data["courses"])

# 序列化
student = Student("张三", 18, ["Math", "English"])
json_str = json.dumps(student.to_dict(), ensure_ascii=False)
print(json_str)

# 反序列化
data = json.loads(json_str)
student2 = Student.from_dict(data)
print(student2.name)  # 张三
```

## CSV处理

### 基本读取

```python
import csv

# 方式1: csv.reader
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    # 读取表头
    headers = next(reader)
    print(headers)  # ['姓名', '年龄', '城市']

    # 读取数据
    for row in reader:
        print(row)  # ['张三', '25', '北京']

# 方式2: csv.DictReader (推荐)
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["姓名"], row["年龄"])
        # 张三 25
```

### 基本写入

```python
import csv

# 方式1: csv.writer
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    # 或逐行写入
    # for row in data:
    #     writer.writerow(row)

# 方式2: csv.DictWriter (推荐)
students = [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"}
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()  # 写入表头
    writer.writerows(students)
```

### 处理不同分隔符

```python
import csv

# 自定义分隔符
with open("data.tsv", "r") as f:
    reader = csv.reader(f, delimiter="\t")  # Tab分隔
    for row in reader:
        print(row)

# 自定义引号字符
with open("data.csv", "r") as f:
    reader = csv.reader(f, quotechar="'")
    for row in reader:
        print(row)
```

## 实战例子

### 例子1：数据格式转换

```python
import json
import csv

def json_to_csv(json_file, csv_file):
    """JSON转CSV"""
    # 读取JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        print("JSON文件为空")
        return

    # 写入CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        # 使用第一条记录的键作为表头
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    print(f"转换完成: {csv_file}")

def csv_to_json(csv_file, json_file):
    """CSV转JSON"""
    data = []

    # 读取CSV
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    # 写入JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"转换完成: {json_file}")

# 使用
# json_to_csv("students.json", "students.csv")
# csv_to_json("students.csv", "students.json")
```

### 例子2：配置管理器

```python
import json
from pathlib import Path

class ConfigManager:
    """配置管理器"""

    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self._load()

    def _load(self):
        """加载配置"""
        if self.config_file.exists():
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return self._default_config()

    def _default_config(self):
        """默认配置"""
        return {
            "theme": "light",
            "language": "zh-CN",
            "auto_save": True,
            "max_history": 50
        }

    def save(self):
        """保存配置"""
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def get(self, key, default=None):
        """获取配置"""
        return self.config.get(key, default)

    def set(self, key, value):
        """设置配置"""
        self.config[key] = value
        self.save()

    def reset(self):
        """重置为默认"""
        self.config = self._default_config()
        self.save()

# 使用
config = ConfigManager()
config.set("theme", "dark")
print(config.get("theme"))  # dark
```

### 例子3：数据统计分析

```python
import csv
from collections import defaultdict, Counter

class SalesAnalyzer:
    """销售数据分析器"""

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        """加载数据"""
        data = []
        with open(self.csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 转换数据类型
                row["amount"] = float(row["amount"])
                row["quantity"] = int(row["quantity"])
                data.append(row)
        return data

    def total_sales(self):
        """总销售额"""
        return sum(item["amount"] for item in self.data)

    def sales_by_product(self):
        """按产品统计"""
        product_sales = defaultdict(float)
        for item in self.data:
            product_sales[item["product"]] += item["amount"]
        return dict(sorted(product_sales.items(), key=lambda x: x[1], reverse=True))

    def top_products(self, n=5):
        """销售前N的产品"""
        sales = self.sales_by_product()
        return list(sales.items())[:n]

    def average_order(self):
        """平均订单金额"""
        return self.total_sales() / len(self.data) if self.data else 0

    def report(self):
        """生成报告"""
        print("=== 销售分析报告 ===")
        print(f"总销售额: ¥{self.total_sales():.2f}")
        print(f"订单数量: {len(self.data)}")
        print(f"平均订单: ¥{self.average_order():.2f}")

        print("\nTop 5 产品:")
        for product, amount in self.top_products(5):
            print(f"  {product}: ¥{amount:.2f}")

# 使用
# analyzer = SalesAnalyzer("sales.csv")
# analyzer.report()
```

### 例子4：数据导出工具

```python
import json
import csv
from datetime import datetime

class DataExporter:
    """数据导出工具"""

    @staticmethod
    def export_json(data, filename, pretty=True):
        """导出为JSON"""
        with open(filename, "w", encoding="utf-8") as f:
            if pretty:
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                json.dump(data, f, ensure_ascii=False)

        print(f"已导出: {filename}")

    @staticmethod
    def export_csv(data, filename, fieldnames=None):
        """导出为CSV"""
        if not data:
            print("数据为空")
            return

        # 自动推断表头
        if fieldnames is None:
            if isinstance(data[0], dict):
                fieldnames = data[0].keys()
            else:
                fieldnames = [f"col{i}" for i in range(len(data[0]))]

        with open(filename, "w", newline="", encoding="utf-8") as f:
            if isinstance(data[0], dict):
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            else:
                writer = csv.writer(f)
                writer.writerow(fieldnames)
                writer.writerows(data)

        print(f"已导出: {filename}")

    @staticmethod
    def export_report(data, title, filename):
        """导出为文本报告"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{'='*50}\n")
            f.write(f"{title:^50}\n")
            f.write(f"{'='*50}\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for key, value in data.items():
                f.write(f"{key}: {value}\n")

        print(f"已导出: {filename}")

# 使用
data = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92}
]

exporter = DataExporter()
exporter.export_json(data, "output.json")
exporter.export_csv(data, "output.csv")
```

### 例子5：合并多个文件

```python
import json
import csv
from pathlib import Path

def merge_json_files(input_dir, output_file):
    """合并多个JSON文件"""
    merged_data = []

    # 遍历目录中的JSON文件
    for json_file in Path(input_dir).glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 如果是列表,扩展;如果是字典,添加
            if isinstance(data, list):
                merged_data.extend(data)
            else:
                merged_data.append(data)

    # 写入合并后的文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"已合并 {len(merged_data)} 条记录到 {output_file}")

def merge_csv_files(input_files, output_file):
    """合并多个CSV文件"""
    all_rows = []
    headers = None

    for csv_file in input_files:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # 使用第一个文件的表头
            if headers is None:
                headers = reader.fieldnames

            for row in reader:
                all_rows.append(row)

    # 写入合并后的文件
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"已合并 {len(all_rows)} 行到 {output_file}")
```

## 常见陷阱

### 陷阱1：JSON中的中文问题

```python
import json

data = {"name": "张三"}

# ❌ 错误 - 中文变成Unicode转义
json_str = json.dumps(data)
print(json_str)  # {"name": "\u5f20\u4e09"}

# ✅ 正确 - 保持中文
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)  # {"name": "张三"}
```

### 陷阱2：CSV忘记newline参数

```python
import csv

# ❌ 错误 - Windows上会出现空行
with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# ✅ 正确
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### 陷阱3：JSON不支持某些类型

```python
import json
from datetime import datetime

data = {
    "time": datetime.now(),
    "tuple": (1, 2, 3)
}

# ❌ 错误 - TypeError
# json.dumps(data)

# ✅ 正确 - 转换为支持的类型
data = {
    "time": datetime.now().isoformat(),
    "tuple": list((1, 2, 3))
}
json.dumps(data)
```

## 最佳实践

### 1. 始终指定编码

```python
# ✅ 推荐
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
```

### 2. 使用DictReader/DictWriter

```python
# ✅ 推荐 - 更清晰
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

# ❌ 不推荐 - 需要手动处理索引
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])  # 哪一列?
```

### 3. 处理大文件时逐行读取

```python
# ✅ 推荐 - 内存友好
with open("large.json", "r") as f:
    for line in f:
        item = json.loads(line)
        process(item)
```

## 练习题

### 练习1：学生成绩管理

读取学生成绩CSV文件:
- 计算每个学生的平均分
- 找出最高分和最低分
- 统计各分数段人数
- 导出为JSON格式

### 练习2：API数据处理

从API获取JSON数据:
- 解析JSON响应
- 提取所需字段
- 保存为CSV文件
- 生成统计报告

### 练习3：数据清洗工具

实现数据清洗功能:
- 读取CSV/JSON数据
- 去除空值和重复数据
- 标准化数据格式
- 导出清洗后的数据

### 练习4：日志分析

分析JSON格式的日志:
- 统计各类型日志数量
- 提取错误信息
- 按时间分组统计
- 生成分析报告

### 练习5：数据合并工具

实现数据合并:
- 合并多个CSV文件
- 合并多个JSON文件
- 按条件筛选数据
- 导出合并结果

## 下一步

掌握了数据处理,最后一章我们通过实战项目综合运用所学知识!

[上一章:第23章 - 正则表达式 ←](../23-正则表达式/23-正则表达式.md)

[下一章:第25章 - 实战项目 →](../25-实战项目/25-实战项目.md)

---

**本章重点**
- ✅ 掌握JSON序列化和反序列化
- ✅ 掌握CSV读写操作
- ✅ 理解数据类型映射
- ✅ 处理复杂数据结构
- ✅ 实现数据格式转换
- ✅ 避免常见陷阱

**记住**
- JSON中文要ensure_ascii=False
- CSV写入要newline=""
- 优先使用DictReader/DictWriter
- 大文件逐行处理
- 始终指定encoding="utf-8"
- 处理不支持的类型要转换
