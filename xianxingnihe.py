import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.array([16.7, 14.3, 12.5, 11.1, 10, 9.1, 8.3])
y = np.array([143.2, 123.0, 108.6, 96.6, 87.5, 79.8, 73.4])
coefficients = np.polyfit(x, y, 1)  # 预测新的数据，拟合数据
poly = np.poly1d(coefficients)  # 创建一个多项式的对象1d 是一维的意思dimension 形成一个多项式，没有y
# x_new = np.linspace(x[0], x[-1], 100)
# y_new = poly(x_new)//可以省略
plt.scatter(x, y, label='原始数据')
plt.plot(x, y, 'r', label='拟合方程')
plt.xlabel('1/v (1/L) ')
plt.ylabel('p (kpa) ')
plt.text(17.68, 1.6, '→', color=(0.2, 0.1, 0.1))
plt.text(-0.29, 152, '↑', color=(0.2, 0.1, 0.1), fontsize=10)
plt.xlim(x.min() - 8.3, x.max() + 1)
plt.ylim(y.min() - 70, y.max() + 10)
plt.legend()  # 图例
plt.grid(True)  # 添加网格线
# 获取回归线的方程
equation = f'y = {poly.coeffs[0]:.2f}x + {poly.coeffs[1]:.2f}'
plt.text(10, 155, equation)  # 在指定位置添加文本
plt.show()
