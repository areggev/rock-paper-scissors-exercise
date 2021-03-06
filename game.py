# game.py
import random
import os
import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("Player_Name")
#print (PLAYER_NAME)

print("Welcome "+ PLAYER_NAME + " to Rock, Paper, Scissors, Shoot!")
#print(10)
#print(10, 99, "My message", "another message")
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
#print("USER CHOICE:")
#print(user_choice)
print("USER CHOICE: ", user_choice)
# validate the input such that only if it is one of the expected values
# ... will we continue with the rest of the program
# ... otherwise we'll stop the progam before it tries to do anything else
# ... and we'll ask the user to run the program again
# and
# or
# this is variable assignment using a single =
#x = 5
# this is equality checking with a double ==
# "is this equal to that?"
#
#if user_choice = "rock" or "paer" or "scissors": # THIS LINE IS PSEUDOCODE
# if user_choice == "rock":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)

if(user_choice == "rock") and (computer_choice == "scissors") or (user_choice == "paper") and (computer_choice == "rock") or (user_choice == "scissors") and (computer_choice == "paper"):
    print("Congratulations, you won!")
else:
    if(user_choice == "rock") and (computer_choice == "paper") or (user_choice =="paper") and (computer_choice == "scissors") or (user_choice == "scissors") and (computer_choice == "rock"):
        print("Sorry, you lost, please play again.")
    else:
        print("You tied, please play again.")

print("THANKS FOR PLAYING ROCKS, PAPER, SCISSORS. PLEASE PLAY AGAIN.")