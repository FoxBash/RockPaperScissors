import random

comp = 0
user = input("Enter your user name")
being = 0


def game(x, y):
    global user,comp,being
    if x == 1: # Rock
        if y == 1:
            return "Rock, Rock so a tie"
        elif y == 2:
            being+=1
            return "Rock, Paper so "+str(user)+" wins"
        elif y == 3:
            comp+=1
            return "Rock, Scissors So computer wins"
        else:
            return "Enter number 1, 2 or 3 ONLY!!"
    elif x == 2: # Paper
        if y == 1:
            comp+=1
            return "Paper, Rock So Computer Wins"
        elif y == 2:
            return "Paper, Paper so a Tie"
        elif y == 3:
            being+=1
            return "Paper, Scissors So "+str(user)+" wins"
        else:
            return "Enter number 1, 2 or 3 ONLY!!"

    elif x == 3: # Scissors
        if y == 1:
            being+=1
            return "Scissors, Rock so "+str(user)+" wins "
        elif y == 2:
            comp+=1
            return "Scissors, Paper so Computer wins"
        elif y == 3:
            return "Scissors, Scissors So a tie"

        else:
            return "Enter number 1, 2 or 3 ONLY!!"



v = 1
while v <= 3:
        y = int(input("Choose between 1, 2, 3"))
        x = random.randint(1,4)
        print(game(x, y))
        v+=1

if being > comp:
    print("Humans ruleeeeeeee!!!!!!!!!")
elif being == comp:
    print("Its a tie better next time")
else:
    print("Computers are taking over the world")


