# ndimage 多维图像处理

`scipy.ndimage` 面向 NumPy 数组提供滤波、形态学、连通区域和几何变换，既可用于图像，也可用于一般规则栅格。

```python
import numpy as np
from scipy import ndimage

rng = np.random.default_rng(42)
image = np.zeros((100, 100))
image[30:70, 35:65] = 1
noisy = image + rng.normal(0, 0.2, image.shape)
```

## 高斯滤波

```python
smooth = ndimage.gaussian_filter(noisy, sigma=1.5)
```

## Sobel 边缘

```python
grad_x = ndimage.sobel(smooth, axis=1)
grad_y = ndimage.sobel(smooth, axis=0)
grad = np.hypot(grad_x, grad_y)
```

## 连通区域标记

```python
mask = smooth > 0.5
labels, n = ndimage.label(mask)
print(n)
```

## 缩放和旋转

```python
large = ndimage.zoom(image, 2, order=1)
rotated = ndimage.rotate(image, 30, reshape=False, order=1)
```

处理科学栅格时要特别关注像元大小、坐标变换、边界模式和 nodata；数组操作正确不等于空间参考一定正确。
