# def newbee(*args,num):
#     print(args[1])
#     print(num)
def newbee(num,*args):
    print(args[1])
    print(num)
def newbee2():
    return 1,2,3
newbee(1,2,3,4)#*args会将所有的东西打包为元组，所以num应该在num之前
a,b,c=newbee2()
d=newbee2()
print(a)
print(b)
print(c)#通过指定把元组分开
tuples=newbee2()
print(*d)#解开元组
print(newbee2())#通过return返回多个数转化为元组
h=[1,2,3,(1,2,3)]
print(*h)#也可以解开列表，但是不能使用两次
# newbee3(1,2,3,4,d=5,b=6,c=7)#字典不能和前面参数一样，例如我把a改成了d#要在函数定义后才可以用
def newbee3(a,*b,**c):
    print(a)
    print(b)
    print(c)
newbee3(1,2,3,4,d=5,b=6,c=7)#字典不能和前面参数一样，例如我把a改成了d
dic={'a':1,'b':2,'c':3}
dic1={'c':1,'d':2}#后面的c把前面的覆盖了，字典的解包方法
# print(**dic)#这样的操作是错的
print({**dic,**dic1})