import random
print("have a try you have five chance")
const=4
while const>=0:
    answer=random.randint(0,8)
    # print(answer)
    guess=int(input(f"answer your number"))#比较的时候先转化为整数
    if guess==answer:
        print("you are right")
        break
    elif guess <= 0:
        const = -1
        print("good bye")
        break
    elif guess<answer and guess>0:#为真就直接跳过后面的
        const = const - 1
        if const == -1:
            print("you have no chance,good bye")
            break
        print("too small")
        print("try again")
        # const=const-1
        # if const==-1:
        #     print("good bye")

    elif guess>answer:
        const = const - 1
        if const == -1:
            print("you have no chance,good bye")
            break
        print("too big")
        print("try again")