import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youStr]

print(f"Computer chose {reverseDict[computer]} and you chose {reverseDict[you]}")

if(computer == you):
    print("It's a draw!!")

# else:
#     if((computer - you) == -1 or (computer - you) == 2):
#         print("You lose!")
#     else:
#         print("You win!")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")
        
    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong!!")