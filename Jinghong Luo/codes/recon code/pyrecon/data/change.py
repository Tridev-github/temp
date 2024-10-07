import numpy as np
from scipy.ndimage import zoom

# 加载npz文件（确保路径是正确的）
data = np.load(r'C:\Users\ljh040217\Desktop\pyrecon\data\hotrod_phantom_data_180x180.npz')  # 使用 r'' 来处理路径
array = data['phantom']  # 假设数组保存在键 'arr_0' 中

# 缩放数组至100x100
zoom_factor = (100/array.shape[0], 100/array.shape[1])
resized_array = zoom(array, zoom_factor)

# 保存为新的npz文件
np.savez(r'C:\Users\ljh040217\Desktop\pyrecon\data\hotrod_phantom_data_100x100.npz',phantom = resized_array)
