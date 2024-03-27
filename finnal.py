num=input()
number=num.split(' ')
num1=int(number[0])
num2=int(number[1])
print('{:>{}.{}f} {:>{}.{}f}'.format(18.16054,num1,num2,17.676767,num1,num2))#传参方法，一个一个传
# 调节必须要写：
# num=input()
# number=num.split(' ')
# num1=int(number[0])
# num2=int(number[1])
# print('{:>17d.3f} {:>17d.3f}'.format(18.16054, num1, num2))这样不行，因为d是整形，后面加.3f