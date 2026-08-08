# MATLAB 文件操作详解

MATLAB 文件（.mat）是科学计算中最常用的数据交换格式。

## 保存 MATLAB 文件

### 基本用法

```python
import numpy as np
from scipy.io import savemat

# 准备数据
data_dict = {
    'vector': np.array([1, 2, 3, 4, 5]),
    'matrix': np.array([[1, 2], [3, 4], [5, 6]]),
    'scalar': 42,
    'string': 'Hello MATLAB'
}

# 保存为 .mat 文件
savemat('my_data.mat', data_dict)
print("数据已保存到 my_data.mat")
```

### 保存多种数据类型

```python
# 创建各种类型的数据
data = {
    # 数值数组
    'integers': np.array([1, 2, 3], dtype=np.int32),
    'floats': np.array([1.1, 2.2, 3.3]),
    'complex_numbers': np.array([1+2j, 3+4j]),

    # 多维数组
    'matrix_2d': np.random.rand(3, 4),
    'tensor_3d': np.random.rand(2, 3, 4),

    # 标量
    'scalar_value': 3.14,

    # 逻辑值
    'boolean': np.array([True, False, True]),

    # 字符串
    'text': 'SciPy Tutorial'
}

savemat('various_types.mat', data)
print("多种数据类型已保存")
```

## 读取 MATLAB 文件

### 基本读取

```python
from scipy.io import loadmat

# 读取文件
loaded_data = loadmat('my_data.mat')

# 查看所有变量名
print("文件中的变量:")
print(loaded_data.keys())

# 访问特定变量
vector = loaded_data['vector']
matrix = loaded_data['matrix']

print(f"\nvector: {vector}")
print(f"vector 形状: {vector.shape}")
print(f"\nmatrix:\n{matrix}")
print(f"matrix 形状: {matrix.shape}")
```

**重要说明**：`loadmat` 返回的字典包含一些元数据键，以双下划线开头（如 `__header__`, `__version__`, `__globals__`）。

### 过滤元数据

```python
def load_mat_clean(filename):
    """
    读取 MATLAB 文件，过滤掉元数据
    """
    data = loadmat(filename)
    # 移除以 '__' 开头的键
    return {key: value for key, value in data.items()
            if not key.startswith('__')}

# 使用
clean_data = load_mat_clean('my_data.mat')
print("用户变量:", list(clean_data.keys()))
```

## MATLAB 文件的维度问题

### 重要：MATLAB 的数组是 2D

MATLAB 中所有数组至少是 2D 的，这会导致一些维度上的差异。

```python
# 在 Python 中保存
data = {'vector': np.array([1, 2, 3, 4, 5])}  # 1D 数组
savemat('vector_test.mat', data)

# 读取回来
loaded = loadmat('vector_test.mat')
vector_loaded = loaded['vector']

print(f"原始形状: (5,)")
print(f"加载后形状: {vector_loaded.shape}")  # (1, 5) 或 (5, 1)

# 转换回 1D
vector_1d = vector_loaded.flatten()
print(f"转换后形状: {vector_1d.shape}")  # (5,)
```

### 自动展平的辅助函数

```python
def load_mat_flat(filename):
    """
    读取 MATLAB 文件，自动展平单行/单列向量
    """
    data = loadmat(filename)
    result = {}

    for key, value in data.items():
        if key.startswith('__'):
            continue

        # 如果是单行或单列向量，展平为 1D
        if isinstance(value, np.ndarray):
            if value.shape[0] == 1 or value.shape[1] == 1:
                result[key] = value.flatten()
            else:
                result[key] = value
        else:
            result[key] = value

    return result

# 使用
data = load_mat_flat('vector_test.mat')
print(f"自动展平后: {data['vector'].shape}")
```

## 高级用法

### 追加模式（appendmat 参数）

```python
# appendmat=True（默认）：自动添加 .mat 扩展名
savemat('data', {'x': [1, 2, 3]}, appendmat=True)
# 生成文件：data.mat

# appendmat=False：使用完整文件名
savemat('data.mat', {'x': [1, 2, 3]}, appendmat=False)
# 生成文件：data.mat
```

### 压缩选项

```python
# do_compression=True：启用压缩（默认）
savemat('data_compressed.mat',
        {'large_array': np.random.rand(1000, 1000)},
        do_compression=True)

# 检查文件大小
import os
size = os.path.getsize('data_compressed.mat')
print(f"压缩文件大小: {size / 1024:.2f} KB")
```

### 格式版本

```python
# format='5' : MATLAB 5 (默认，兼容性最好)
# format='4' : MATLAB 4 (旧版本)

savemat('data_v5.mat', {'x': [1, 2, 3]}, format='5')
savemat('data_v4.mat', {'x': [1, 2, 3]}, format='4')
```

**注意**：MATLAB v7.3+ 文件使用 HDF5 格式，需要用 `h5py` 库读取。

## 实际应用案例

### 案例1：实验数据保存

```python
"""
场景：保存实验结果供 MATLAB 分析
"""

# 实验数据
experiment_data = {
    # 元信息
    'experiment_name': 'Temperature Test',
    'date': '2026-01-16',
    'researcher': 'Zhang San',

    # 测量数据
    'time': np.arange(0, 10, 0.1),  # 时间序列
    'temperature': 20 + 5 * np.sin(np.arange(0, 10, 0.1)) +
                   np.random.randn(100) * 0.5,  # 温度数据

    # 实验参数
    'sampling_rate': 10,  # Hz
    'duration': 10,  # 秒
    'sensor_id': 'TC-001',

    # 统计结果
    'mean_temp': 0,  # 稍后计算
    'std_temp': 0,
}

# 计算统计量
experiment_data['mean_temp'] = np.mean(experiment_data['temperature'])
experiment_data['std_temp'] = np.std(experiment_data['temperature'])

# 保存
savemat('experiment_results.mat', experiment_data)
print("实验数据已保存")

# 验证
loaded = load_mat_clean('experiment_results.mat')
print(f"\n保存的变量: {list(loaded.keys())}")
print(f"平均温度: {loaded['mean_temp']:.2f}°C")
```

### 案例2：与 MATLAB 脚本协同

```python
"""
场景：Python 处理数据 → MATLAB 可视化
"""

# Python 中的数据处理
from scipy import signal

# 生成信号
t = np.linspace(0, 1, 1000)
signal_data = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 12 * t)
noisy_signal = signal_data + np.random.randn(len(t)) * 0.1

# 滤波
b, a = signal.butter(4, 0.1)
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# 保存供 MATLAB 使用
matlab_data = {
    't': t,
    'original': signal_data,
    'noisy': noisy_signal,
    'filtered': filtered_signal,
    'filter_order': 4,
    'cutoff_freq': 0.1
}

savemat('signal_for_matlab.mat', matlab_data)
print("信号数据已导出到 MATLAB")
```

对应的 MATLAB 代码（`plot_signals.m`）：
```matlab
% MATLAB 脚本：可视化 Python 处理的信号
load('signal_for_matlab.mat');

figure;
subplot(3,1,1);
plot(t, original);
title('Original Signal');

subplot(3,1,2);
plot(t, noisy);
title('Noisy Signal');

subplot(3,1,3);
plot(t, filtered);
title('Filtered Signal');
```

### 案例3：批量数据转换

```python
"""
场景：批量将 NumPy 文件转换为 MATLAB 格式
"""

import glob

def convert_npy_to_mat(npy_file):
    """将 .npy 文件转换为 .mat 文件"""
    # 读取 NumPy 文件
    data = np.load(npy_file)

    # 构造 MATLAB 文件名
    mat_file = npy_file.replace('.npy', '.mat')

    # 保存为 MATLAB 格式
    # 使用文件名（不带扩展名）作为变量名
    var_name = os.path.basename(npy_file).replace('.npy', '')
    savemat(mat_file, {var_name: data})

    print(f"转换: {npy_file} -> {mat_file}")

# 批量转换
# npy_files = glob.glob('*.npy')
# for npy_file in npy_files:
#     convert_npy_to_mat(npy_file)
```

## 与 MATLAB 交互的最佳实践

### 1. 变量命名
```python
# ✓ 好的命名（MATLAB 兼容）
data = {
    'time_series': array1,
    'measurement_data': array2,
    'sensor_01': array3
}

# ✗ 避免的命名
data = {
    'time-series': array1,  # 连字符会导致问题
    '1st_sensor': array2,   # 不能以数字开头
    'class': array3,        # 避免 MATLAB 关键字
}
```

### 2. 添加元数据
```python
data = {
    # 数据
    'measurements': np.random.rand(100, 3),

    # 元数据
    'description': 'Sensor measurements',
    'units': 'meters',
    'sampling_rate': 100,
    'date': '2026-01-16',

    # 数据说明
    'column_names': ['x', 'y', 'z']
}
```

### 3. 文档化
```python
# 在同目录创建 README.txt
readme_content = """
Data file: experiment_data.mat

Variables:
- time: Time vector (seconds)
- temperature: Temperature measurements (Celsius)
- pressure: Pressure measurements (Pa)

Date: 2026-01-16
Author: Your Name
"""

with open('README.txt', 'w') as f:
    f.write(readme_content)
```

## 常见问题

### 问题1：读取 MATLAB v7.3 文件失败

```python
# 错误：Cannot read MATLAB file version > 7.2

# 解决方案：使用 h5py
import h5py

def load_mat_v73(filename):
    """读取 MATLAB v7.3 (HDF5) 文件"""
    with h5py.File(filename, 'r') as f:
        data = {}
        for key in f.keys():
            data[key] = np.array(f[key])
        return data

# 使用
# data = load_mat_v73('modern_matlab_file.mat')
```

### 问题2：字符串编码问题

```python
# MATLAB 和 Python 的字符串编码可能不同
data = loadmat('data.mat')
string_value = data['text']

# 转换为 Python 字符串
if isinstance(string_value, np.ndarray):
    string_value = str(string_value[0])

print(string_value)
```

### 问题3：大文件内存溢出

```python
# 对于非常大的文件，考虑：
# 1. 使用 h5py 和 HDF5 格式（支持部分读取）
# 2. 分块保存数据
# 3. 使用内存映射

# 示例：分块保存
def save_large_data_chunked(filename, large_array, chunk_size=1000):
    """分块保存大数组"""
    n_chunks = len(large_array) // chunk_size + 1

    for i in range(n_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(large_array))
        chunk = large_array[start:end]

        savemat(f'{filename}_chunk_{i}.mat',
                {f'data_chunk_{i}': chunk})
```

## 小结

- `savemat` 保存数据到 MATLAB 格式
- `loadmat` 读取 MATLAB 文件
- 注意维度差异（MATLAB 至少 2D）
- MATLAB v7.3+ 需要 h5py
- 使用有意义的变量名
- 添加元数据和文档

## 下一步

学习 WAV 音频文件的读写操作。

→ 继续学习：`03-WAV音频文件.md`
