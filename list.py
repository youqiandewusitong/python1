list =[1,2,0,3,4,5]
# list.sort(reverse=True) #降序
# list.sort()#升序
list.sort(key=abs)#绝对值排序
# list.append([3,45])#把数组直接加上[3,45]     append()可以直接加数字
# list.extend([3,4,5,6,7,8])#相当于JS...a    extend()方法是用于在列表的末尾添加另一个列表的元素。括号里面不能直接加数字，只能加列表。如果要添加一个数字，可以将其转换为列表形式后再进行添加。下面是一个示例代码
list.insert(3,10000)#插入一个数在相应的index里面
# list.remove(10000)#去除一个数
# list.reverse()#数组顺序取反
list.pop(4)#去除对应下标的东西
# list[len(list):]=[1,2,3,4]#相当于entend
# list[len(list)-4:len(list)-3]=[1,2,3,4]#后面的东西用[1,2,3,4]替代了,这种都是去前留后面的东西
# print(list[(len(list)-2):])#切片==slice
list2=list
print(list)
print(list2)