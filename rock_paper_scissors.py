import random

computer_choice = random.choice(["rock", "paper", "scissors"])

user_choice = input("Rock, Paper or Scissors ? ")

if(computer_choice == user_choice) :
    print("It's a TIE")
elif(user_choice == "rock" and computer_choice == "scissors") :
    print("You WIN !!")
elif(user_choice == "paper" and computer_choice == "rock") :
    print("You WIN !!")
elif(user_choice == "scissors" and computer_choice == "paper") :
    print("You WIN !!")
else :
    print("You lose, Computer WINS :)") 