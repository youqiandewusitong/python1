# num1=3.1415926
# num2=22.3456
# num1='{:.6}'.format(num1)
# num2='{:.6}'.format(num2)
# print('{:<14d} {:>14d}'.format(num1,num2))
num1 = 3.1415926
num2 = 22.3456
num=3
# num1 = round(num1, 6)#四舍五入，不好用，直接去掉
# num2 = round(num2, 6)
print('{:<14.6f} {:>14.6f}'.format(num1,num1))#多个要调整格式就一起输入
print('{:<14.6f} {:>14.6f}'.format(num2,num2))