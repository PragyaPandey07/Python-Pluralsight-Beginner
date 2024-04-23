import random

def roll_dice() :
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main() :
    player1 = input('Enter player 1 name ')
    player2 = input('Enter player 2 name ')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1, 'and', player2, 'rolled', roll2)

    if(roll1 > roll2) :
        print('The winner is', player1)
    elif(roll1 == roll2) :
        print("It's a TIE")
    else :
        print('The winner is', player2)

main() 