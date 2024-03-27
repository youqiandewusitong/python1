def change(string):
    num=[]
    negative=1
    #要转化字符就用negative来接受
    for i in string:
        if i=='+':
            negative=1
        if i=='-':
            negative=-1
        if i<'9' and i>'0' :
            num.append(i)
    num=''.join(num)
    num=int(num)*negative
    return num
string=input()
fin=change(string)
print(fin)
print(type(fin))