import random
def dice():
    dice_number=random.randint(1,6)
    return dice_number
print("welcome to the dice")
while 1:
    choice=input("would you like to make a dice  y/n")
    if "y" in choice.lower():
        dice_number=dice()
        print(f"your dice is {dice_number}")
    elif "n" in choice.lower():
        exit()
        # break

