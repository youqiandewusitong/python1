import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.array([363.2,353.2,343.2,333.2,323.2,313.2 ])
y = np.array([113.0,110.0,107.0,104.0,102.0,99.0])
coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)
x_new = np.linspace(x[0], x[-1], 100)
y_new = poly(x_new)
plt.scatter(x, y, label='原始数据')
plt.plot(x_new, y_new, 'r', label='拟合方程')
plt.xlabel('T (k) ')
plt.ylabel('v (mL) ')
plt.text(365.5,98,'→',color=(0.2,0.1,0.1))
plt.text(310,113.75,'↑',color=(0.2,0.1,0.1),fontsize=10)
# plt.xlim(x.min() - 8.3, x.max() + 1)
# plt.ylim(y.min() - 70, y.max() + 10)
plt.legend()
plt.grid(True)  # 添加网格线
# 获取回归线的方程
equation = f'y = {poly.coeffs[0]:.2f}x + {poly.coeffs[1]:.2f}'
plt.text(345, 114, equation)  # 在指定位置添加文本
plt.show()