def main(num1, num2):
    # code here
    pass
    sums = num1 + num2
    sub = num1 - num2
    print(f'{num1}+{num2}={sums}')
    print(f'{num1}-{num2}={sub}')


if __name__ == '__main__':
    string = input()
    i = 0
    num1 = 0
    num2 = 0
    while i < len(string):
        if string[i] == ',':
            num1 = int(string[0:i])
            num2 = int(string[i+1:])
            break
        i += 1

    main(num1, num2)
