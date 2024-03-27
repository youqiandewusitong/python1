my_class=('newbee','tiger','cat')
print(my_class)
# print('newbee'in set)
del my_class#元组只能这么删
try:
    print(my_class)
except NameError:
    print("NameError")#删了之后再print会出现异常属于NameError
list=[1,2,3,[4,5]]
list.pop(3)
print(list)#列表只能下标
# set={1,2,3,4,5,[66,7]}#set.remove([66,7])的问题在于，集合（set）中的元素必须是可哈希（hashable）的，而列表（list）是不可哈希的。因此，不能将列表作为集合的元素。如果需要存储不可哈希的对象，可以使用元组（tuple）代替列表。
# set.remove([66,7])#错误写法
set={1,2,3,4,5}
print(set)
set.pop()#集合里面pop不能传参数
print(set)
# dic=