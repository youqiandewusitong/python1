def main(num):
    # code here
    pass
    if int(num[0]) // 10 == 0:
        num[0] = '0' + num[0]
    if int(num[1]) // 10 == 0:
        num[1] = '0' + num[1]
    if int(num[2])//10==0:
        num[2] = '0' +'0'+'0'+ num[2]
    elif int(num[2])//100==0:
        num[2] = '0' +'0'+num[2]
    elif int(num[2])//1000==0:
        num[2] = '0'+ num[2]
    time = num[2] + num[0] + num[1]
    print(time)


num = [0, 0, 0]
if __name__ == '__main__':
    string = input()
    num = string.split('/')  # 分割
    main(num)
