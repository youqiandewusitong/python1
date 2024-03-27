# x=1000
# def myfunc():
#     # nonlocal  x=100#要先声明非局部变量再给他赋值
#     global x#访问外部用global
#     x=100
#     def funcb():
#         print(x)
#     return funcb
# x=1000
# print(x)
# func=myfunc()#必须这样才可以调用函数
# func()
# print(x)


#次方
# def power(num):
#     def func(number):
#         return number ** num
#     return func
# #如果嵌套有几个def返回多少个值，如果要求值的话
# five=power(5)
# print(five(5))

# def fun():
#     def func():
#         print("Hello World")
#     return func
# #将返回值赋值给原函数，所以要加return
# a=fun()
# a()

#装饰器
# def func1(func):
#     print("Hello World")
#     return func
# # 函数里面的参数要想传出去都加return
# #TypeError: 'NoneType' object is not callable这种问题就是没有return找不到
# @func1
# def func2():
#     print('new bee')
# func2()

