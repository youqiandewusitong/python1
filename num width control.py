num=int(input())
number=[]
while num//1000>0:
    number.append(num%1000)
    num=num//1000
number.append(num)
number.reverse()
# print(number)
for i in number:
    print(f'{i:03}',end=' ')#控制每个元素的宽度为3

