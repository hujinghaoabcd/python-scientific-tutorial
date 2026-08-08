# WAV 音频文件操作

WAV 是一种无损音频格式，广泛用于音频处理和分析。

## 音频基础知识

### 关键概念

**采样率 (Sample Rate)**
- 每秒采样的次数，单位 Hz
- 常见值：44100 Hz (CD质量), 48000 Hz (专业音频), 16000 Hz (语音)
- 越高越精确，但文件越大

**位深度 (Bit Depth)**
- 每个样本的比特数
- 常见值：16 位, 24 位, 32 位
- 越高动态范围越大

**声道 (Channels)**
- 单声道 (Mono): 1 个声道
- 立体声 (Stereo): 2 个声道（左、右）

## 读取 WAV 文件

### 基本读取

```python
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# 读取 WAV 文件
sample_rate, audio_data = wavfile.read('audio.wav')

print(f"采样率: {sample_rate} Hz")
print(f"数据形状: {audio_data.shape}")
print(f"数据类型: {audio_data.dtype}")
print(f"时长: {len(audio_data) / sample_rate:.2f} 秒")

# 单声道：audio_data.shape = (N,)
# 立体声：audio_data.shape = (N, 2)
```

### 可视化音频

```python
def plot_audio(sample_rate, audio_data):
    """可视化音频波形"""
    # 计算时间轴
    duration = len(audio_data) / sample_rate
    time = np.linspace(0, duration, len(audio_data))

    plt.figure(figsize=(14, 6))

    # 单声道
    if len(audio_data.shape) == 1:
        plt.plot(time, audio_data)
        plt.xlabel('时间 (秒)')
        plt.ylabel('振幅')
        plt.title(f'音频波形 (采样率: {sample_rate} Hz)')

    # 立体声
    else:
        plt.subplot(2, 1, 1)
        plt.plot(time, audio_data[:, 0])
        plt.ylabel('左声道振幅')
        plt.title(f'音频波形 (采样率: {sample_rate} Hz)')

        plt.subplot(2, 1, 2)
        plt.plot(time, audio_data[:, 1])
        plt.xlabel('时间 (秒)')
        plt.ylabel('右声道振幅')

    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# 使用
# plot_audio(sample_rate, audio_data)
```

## 创建和保存 WAV 文件

### 生成简单音调

```python
def generate_tone(frequency, duration, sample_rate=44100, amplitude=0.5):
    """
    生成正弦波音调

    参数:
        frequency: 频率 (Hz)
        duration: 时长 (秒)
        sample_rate: 采样率 (Hz)
        amplitude: 振幅 (0-1)

    返回:
        audio_data: 音频数据数组
    """
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = amplitude * np.sin(2 * np.pi * frequency * t)

    # 转换为 16 位整数格式
    audio_int = (audio * 32767).astype(np.int16)

    return audio_int

# 生成 A4 音（440 Hz），持续 2 秒
audio = generate_tone(440, 2)

# 保存为 WAV 文件
wavfile.write('tone_440hz.wav', 44100, audio)
print("音频已保存")
```

### 生成和弦

```python
def generate_chord(frequencies, duration, sample_rate=44100):
    """生成多个频率的和弦"""
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio = np.zeros_like(t)

    # 叠加多个频率
    for freq in frequencies:
        audio += np.sin(2 * np.pi * freq * t)

    # 归一化
    audio = audio / len(frequencies)

    # 转换为 16 位整数
    audio_int = (audio * 32767).astype(np.int16)

    return audio_int

# 生成 C 大三和弦 (C-E-G: 261.63, 329.63, 392.00 Hz)
chord = generate_chord([261.63, 329.63, 392.00], duration=2)
wavfile.write('chord_c_major.wav', 44100, chord)
print("和弦已保存")
```

### 生成立体声

```python
def generate_stereo(freq_left, freq_right, duration, sample_rate=44100):
    """生成立体声音频"""
    t = np.linspace(0, duration, int(sample_rate * duration))

    # 左右声道不同频率
    left = np.sin(2 * np.pi * freq_left * t)
    right = np.sin(2 * np.pi * freq_right * t)

    # 合并为立体声 (N, 2)
    stereo = np.column_stack([left, right])

    # 转换为 16 位整数
    stereo_int = (stereo * 32767).astype(np.int16)

    return stereo_int

# 左声道 440 Hz，右声道 880 Hz
stereo = generate_stereo(440, 880, 2)
wavfile.write('stereo_tone.wav', 44100, stereo)
print("立体声已保存")
```

## 音频处理示例

### 案例1：音量调节

```python
def adjust_volume(audio_data, factor):
    """
    调节音量

    参数:
        audio_data: 音频数据
        factor: 音量因子（0.5=减半, 2.0=加倍）
    """
    # 转换为浮点数进行计算
    audio_float = audio_data.astype(np.float32)

    # 调节音量
    adjusted = audio_float * factor

    # 防止溢出（剪裁）
    adjusted = np.clip(adjusted, -32768, 32767)

    return adjusted.astype(np.int16)

# 读取音频
rate, audio = wavfile.read('tone_440hz.wav')

# 音量减半
quiet = adjust_volume(audio, 0.5)
wavfile.write('tone_quiet.wav', rate, quiet)

# 音量加倍
loud = adjust_volume(audio, 2.0)
wavfile.write('tone_loud.wav', rate, loud)
```

### 案例2：音频拼接

```python
def concatenate_audio(file1, file2, output_file):
    """拼接两个音频文件"""
    # 读取两个文件
    rate1, audio1 = wavfile.read(file1)
    rate2, audio2 = wavfile.read(file2)

    # 确保采样率相同
    if rate1 != rate2:
        raise ValueError("采样率不匹配")

    # 拼接
    combined = np.concatenate([audio1, audio2])

    # 保存
    wavfile.write(output_file, rate1, combined)
    print(f"已拼接并保存到 {output_file}")

# 使用
# concatenate_audio('tone1.wav', 'tone2.wav', 'combined.wav')
```

### 案例3：添加淡入淡出效果

```python
def fade_in_out(audio_data, sample_rate, fade_duration=0.5):
    """
    添加淡入淡出效果

    参数:
        audio_data: 音频数据
        sample_rate: 采样率
        fade_duration: 淡入/淡出时长（秒）
    """
    fade_samples = int(sample_rate * fade_duration)
    audio_float = audio_data.astype(np.float32)

    # 淡入（线性）
    fade_in_curve = np.linspace(0, 1, fade_samples)
    audio_float[:fade_samples] *= fade_in_curve

    # 淡出（线性）
    fade_out_curve = np.linspace(1, 0, fade_samples)
    audio_float[-fade_samples:] *= fade_out_curve

    return audio_float.astype(np.int16)

# 生成音频并添加淡入淡出
audio = generate_tone(440, 3)
audio_faded = fade_in_out(audio, 44100, fade_duration=0.5)
wavfile.write('tone_faded.wav', 44100, audio_faded)
```

### 案例4：音频混音

```python
def mix_audio(file1, file2, output_file, weight1=0.5, weight2=0.5):
    """
    混合两个音频文件

    参数:
        weight1, weight2: 混音权重（总和应为 1.0）
    """
    # 读取
    rate1, audio1 = wavfile.read(file1)
    rate2, audio2 = wavfile.read(file2)

    if rate1 != rate2:
        raise ValueError("采样率不匹配")

    # 对齐长度（填充零）
    max_len = max(len(audio1), len(audio2))
    if len(audio1) < max_len:
        audio1 = np.pad(audio1, (0, max_len - len(audio1)))
    if len(audio2) < max_len:
        audio2 = np.pad(audio2, (0, max_len - len(audio2)))

    # 转换为浮点数混音
    mixed = (audio1.astype(np.float32) * weight1 +
             audio2.astype(np.float32) * weight2)

    # 防止溢出
    mixed = np.clip(mixed, -32768, 32767)

    # 保存
    wavfile.write(output_file, rate1, mixed.astype(np.int16))
    print(f"混音已保存到 {output_file}")

# 使用
# mix_audio('music.wav', 'voice.wav', 'mixed.wav', 0.7, 0.3)
```

## 音频分析

### 计算音频特征

```python
def analyze_audio(sample_rate, audio_data):
    """分析音频基本特征"""
    # 时长
    duration = len(audio_data) / sample_rate

    # 振幅统计
    max_amplitude = np.max(np.abs(audio_data))
    mean_amplitude = np.mean(np.abs(audio_data))

    # RMS (均方根) - 音量度量
    rms = np.sqrt(np.mean(audio_data.astype(np.float32)**2))

    # 峰值因子
    crest_factor = max_amplitude / rms if rms > 0 else 0

    print("=" * 50)
    print("音频分析")
    print("=" * 50)
    print(f"时长: {duration:.2f} 秒")
    print(f"采样率: {sample_rate} Hz")
    print(f"样本数: {len(audio_data)}")
    print(f"最大振幅: {max_amplitude}")
    print(f"平均振幅: {mean_amplitude:.2f}")
    print(f"RMS: {rms:.2f}")
    print(f"峰值因子: {crest_factor:.2f}")

# 使用
rate, audio = wavfile.read('tone_440hz.wav')
analyze_audio(rate, audio)
```

### 频谱分析

```python
from scipy import signal

def plot_spectrogram(sample_rate, audio_data):
    """绘制频谱图"""
    # 计算频谱图
    frequencies, times, spectrogram = signal.spectrogram(
        audio_data, sample_rate)

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram),
                   shading='gouraud', cmap='viridis')
    plt.ylabel('频率 (Hz)')
    plt.xlabel('时间 (秒)')
    plt.title('频谱图')
    plt.colorbar(label='强度 (dB)')
    plt.ylim(0, 5000)  # 只显示 0-5000 Hz
    plt.tight_layout()
    plt.show()

# 使用
# plot_spectrogram(rate, audio)
```

## 实用工具函数

### 音频信息查看器

```python
def audio_info(filename):
    """显示 WAV 文件信息"""
    rate, data = wavfile.read(filename)

    print(f"\n文件: {filename}")
    print("=" * 50)
    print(f"采样率: {rate} Hz")
    print(f"数据类型: {data.dtype}")
    print(f"形状: {data.shape}")

    if len(data.shape) == 1:
        print("声道: 单声道")
    else:
        print(f"声道: {data.shape[1]} 声道")

    duration = len(data) / rate
    print(f"时长: {duration:.2f} 秒")

    # 文件大小
    import os
    size_bytes = os.path.getsize(filename)
    print(f"文件大小: {size_bytes / 1024:.2f} KB")

# 使用
# audio_info('tone_440hz.wav')
```

### 音频格式转换

```python
def convert_to_mono(stereo_data):
    """立体声转单声道（取平均）"""
    if len(stereo_data.shape) == 1:
        return stereo_data  # 已经是单声道
    return np.mean(stereo_data, axis=1).astype(stereo_data.dtype)

def resample_audio(audio_data, orig_rate, new_rate):
    """重采样音频"""
    from scipy import signal

    # 计算重采样比例
    num_samples = int(len(audio_data) * new_rate / orig_rate)

    # 重采样
    resampled = signal.resample(audio_data, num_samples)

    return resampled.astype(audio_data.dtype)

# 示例
# rate, audio = wavfile.read('stereo.wav')
# mono = convert_to_mono(audio)
# wavfile.write('mono.wav', rate, mono)
```

## 常见问题

### 问题1：数据类型不匹配

```python
# 错误：float64 数组超出范围 [-1, 1]
audio = np.sin(2 * np.pi * 440 * np.linspace(0, 1, 44100))
# wavfile.write('test.wav', 44100, audio)  # 错误！

# 正确方法1：归一化到 [-1, 1] 并转换为 int16
audio_int = (audio * 32767).astype(np.int16)
wavfile.write('test.wav', 44100, audio_int)

# 正确方法2：使用 float32 格式（归一化到 [-1, 1]）
audio_float = audio.astype(np.float32)
wavfile.write('test.wav', 44100, audio_float)
```

### 问题2：音频剪裁失真

```python
# 音量过大导致剪裁
audio = generate_tone(440, 1, amplitude=2.0)  # 振幅超过 1.0

# 检测剪裁
clipped = np.sum(np.abs(audio) >= 32767)
if clipped > 0:
    print(f"警告: {clipped} 个样本被剪裁")

# 解决：归一化
audio_normalized = audio / np.max(np.abs(audio)) * 32767 * 0.9
```

## 小结

- `wavfile.read()` 读取 WAV 文件
- `wavfile.write()` 保存 WAV 文件
- 注意数据类型（int16, float32）
- 单声道形状 (N,)，立体声 (N, 2)
- 采样率常用 44100 Hz
- 使用 `scipy.signal` 进行高级处理

## 下一步

文件 I/O 模块学习完毕！接下来学习优化算法，这是 SciPy 最强大的功能之一。

→ 继续学习：`../03-优化算法/`
