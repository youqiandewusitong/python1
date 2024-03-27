import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.array([106.7,109.5,112.2,115.3,118.4,121.7 ])
y = np.array([313.2,323.2,333.2,343.2,353.2,363.2])
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
x_new = np.linspace(x[0], x[-1], 100)
y_new = poly(x_new)
plt.scatter(x, y, label='原始数据')
plt.plot(x_new, y_new, 'r', label='拟合方程')
plt.xlabel('p (kpa) ')
plt.ylabel('T (k) ')
plt.text(122.4,310.0,'→',color=(0.2,0.1,0.1))
plt.text(105.72,366.5,'↑',color=(0.2,0.1,0.1),fontsize=10)
# plt.xlim(x.min() - 8.3, x.max() + 1)
# plt.ylim(y.min() - 70, y.max() + 10)
plt.legend()
plt.grid(True)  # 添加网格线
# 获取回归线的方程
equation = f'y = {poly.coeffs[0]:.2f}x + {poly.coeffs[1]:.2f}'
plt.text(116, 370, equation)  # 在指定位置添加文本
plt.show()