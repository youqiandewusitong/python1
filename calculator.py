def main(num):
    #code here
    num1=int(num[0])
    num2=int(num[1])
    sum=(1/2)*(num1*num2+(num1+num2)/(4*num2))
    final='{:.2f}'.format(sum)
    print(sum)


if __name__ == '__main__':
    string=input()
    num=string.split(' ')
    main(num);