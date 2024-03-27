# printf('hello world')
print("welcome")
while 1:
    print("what woudld you like to do")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 exit")
    choice=int (input("enter your number"))
    if choice==1:
        num1=int (input("enter your first number"))
        num2=int (input("enter your second number"))
        num =num1+num2
        print(f"output:{num}")
    elif choice==2:
        num1 = int(input("enter your first number"))
        num2 = int(input("enter your second number"))
        num = num1 -num2
        print("output:",num)
    elif choice==3:
        num1=int(input("enter your first number"))
        num2=int(input("enter your second number"))
        num=num1*num2
        print("output:",num)
    elif choice==4:
        num1=int(input("enter your first number"))
        num2=int(input("enter your second number"))
        num=num1/num2
        print("output:",num)
    elif choice == 5:
        print("good bye")
        break
print("hello world")