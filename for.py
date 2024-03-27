import copy
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     for each in i:
#         print(each,end=' ')#每打印一个字在末尾打一个空格
#     print()#一层循环打印一行空白行
# for i in range(3):
#     A.append(i*3)
#     print(A)
A=[0]*3#先定义三个数的列表 ，后面依次替换一个一个数-----------------------------------一定要先定义
# print(A)
for i in range(3):
    A[i]=[0]*3#再赋值
    print(A)
    print()
# print(A)
a=copy.deepcopy(A)#深度复制
A[1][1]=3
B='fish'
c='fish'
print(B is c)#用is函数来判定是否是一个东西
x=[i+1 for i in range(8)]#0-7,不包括8
y=[i*3 for i in range(8)]
z=[ord(i) for i in 'fish']#大写字母“A”的ASCII值是65。'a'的值为97
h=[matrix[i][len(matrix)-1-i]for i in range(len(matrix))]#运算量小很多----------------------------------推荐使用
print(h,y)#[1, 5, 9] [0, 3, 6, 9, 12, 15, 18, 21]
print(z)
print(x)
print(y)
matrix.pop(1)#下标指的是数组元素对应位置
my_class=('newbee','tiger','cat')
print(my_class)
print([1,2,3]in matrix)
# print('newbee'in set)
del my_class#元组只能这么删
# print(my_class)
print(matrix)
# print(A)
# print(a)
