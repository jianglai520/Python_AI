import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 创建图表，设置标题和标签
plt.figure(figsize=(8, 4))
plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='--')
plt.plot(x, y_cos, label='cos(x)', color='red')

plt.title('Sin vs Cos Waves', fontsize=16)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend() # 显示图例
plt.grid(True) # 显示网格
plt.show()