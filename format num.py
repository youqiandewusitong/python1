def main(num):
    #code here
    sum=0
    for i in range(len(num)):
        sum+=float(num[i])
    # summary=round(float(sum),6)    #float默认保留1位小数

    summary='{:.6f}'.format(sum)#转化为字符串保留6位小数,最好用这个方法
    # summary=f'{num:.6f}'目前不支持用这个
    ave=sum/len(num)
    # average='{:.6f}'.format(sum/len(num))#和下面这种都可以
    average = '{:.6f}'.format(ave)
    print(summary)
    print(average)
    pass


if __name__ == '__main__':
    grade=input()
    num=grade.split(' ')
    print(num)
    main(num);