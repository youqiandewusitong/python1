def main(num):
    number = []
    i = -1
    j = 1
    total = ''
    while num // 8 > 0:
        i += 1
        number.append(num % 8)
        num //= 8
    number.append(num )
    number.reverse()
    for i in range(len(number)):
        total += str(number[i])
    return total


def main1(num):
    j = -1
    total1 = ''
    number1 = []
    while num // 16 > 0:
        j += 1
        num2 = num % 16
        if num2 > 9:
            num2 = chr(ord('A') + num2 - 10)
        else:
            num2 = str(num2)
        number1.append(num2)
        num//= 16
    number1.append(str(num))
    number1.reverse()
    for j in range(len(number1)):
        total1 += str(number1[j])
    return total1


if __name__ == '__main__':
    num=128
    main(num)
    main1(num)
    print(num,main(num),main1(num))
    num=456789#num的值发生了改变，所以要再加一个
    main(num)
    # main1(num)
    print(num, main(num),main1(num))

