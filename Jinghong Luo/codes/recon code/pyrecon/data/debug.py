import numpy as np


data = np.load( "1hole_repeater.npz")[
    "sysmat"
]
data = np.reshape(data,(12,10000))
i = 0
row_sum = np.sum(data[i, :])

print(f"第 {i} 行的和为: {row_sum}")
i = 8
row_sum = np.sum(data[i, :])

print(f"第 {i} 行的和为: {row_sum}")
i = 9
row_sum = np.sum(data[i, :])

print(f"第 {i} 行的和为: {row_sum}")
i = 10
row_sum = np.sum(data[i, :])

print(f"第 {i} 行的和为: {row_sum}")
i = 11
row_sum = np.sum(data[i, :])

print(f"第 {i} 行的和为: {row_sum}")