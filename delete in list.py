# def change(string):
#      return string.replace('*','')
# string=input()
# change(string)
# string=change(string)
# print(string)


# def change(string):
#     return string.rstrip('*')
# string = input()
# string = change(string)
# print(string)#删除后面的*，前面的不删除
def change(list):
    list.reverse()
    index=0
    j=0
    for i in range(len(list)):
        if list[i]!='*':
            index=i
            break
    list.reverse()
    # for i in range(len(list)-index-1):
    #     print(i)
    #     if list[i]=='*':
    #         list[i]=list[i].replace('*','')
    #         print(list)
    # for i in range(len(list)):
    #
    #不用for因为它会自动加一，删除一个*如果星星连续，会往前面填充
    while(j<len(list)-index):
        if list[j]=='*':
            del list[j]
            print(list)
        else:
            j+=1

    final=''.join(list)
    return final

string = input()
list=list(string)
fin=change(list)
print(fin)