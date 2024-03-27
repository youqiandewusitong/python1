# v1.0.0 手动输入置信因子，单次计算
# v1.1.0 自动匹配置信因子，循环计算，统计次数，手动退出
# v1.1.1
import subprocess
import time
def notice():
    print("-"*40,end='')
    print('''
1.本工具功能为测量A类不确定度
2.置信概率统一为68.3%
3.测量次数在[10,19]的置信因子统一取1.06
4.测量次数输入0既关闭软件
''',end='')
    print("-"*40)
loop,realLoop,loopSum= 0,0,0

ConfidenceProbability = [1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.03,1]
while loop != -1:
    loop += 1
    loopSum += 1
    if loop == 1:
        notice()
    n = int(input("测量次数 n = "))
    #t = float(input("t因子 t = "))
    if n == 0:
        break
    elif n < 3:
        print("测量次数不能少于三次！")
        time.sleep(3)
        subprocess.call("cls", shell=True)
        loop = 0
        continue
    elif n < 10:
        t = ConfidenceProbability[n-3]
    elif n < 20:
        t = ConfidenceProbability[7]
    elif n == 20:
        t = ConfidenceProbability[8]
    elif n > 20:
        t = ConfidenceProbability[9]
    t = float(input("t(可选)："))
    x=[]
    x_sum = 0
    for i in range(n):
        x.append(float(input("第 {} 个数据:".format(i+1))))
        x_sum += x[i]
    x_aver = x_sum/n
    x_SquDif = 1
    for i in range(n):
        x_SquDif *= (x[i] - x_aver) ** 2
    u = t * ((1/(n*(n-1))*x_SquDif) ** 0.5)  # 标准偏差计算
    print("U_a = ",u)
    ub = float(input("U_b = "))
    print("U = {}".format((ub**2 + u**2)**0.5))
    realLoop += 1
    print("-"*40)

#关闭
subprocess.call("cls", shell = True)
print('''
一共测量了{0}组数据，有效测量{1}组
'''.format(loopSum-1,realLoop))
time.sleep(3)