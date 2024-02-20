import random
import os
from art import ending, logo
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
attempts_counter = 0
def start_game():
    global attempts_counter
    global chosen_number
    global guessed_number
    while attempts_counter != 1:
        if chosen_number == guessed_number:
            print(f"Congrats!!! You got it right! The answer was really: {chosen_number}")
            break
        elif chosen_number > guessed_number:
            attempts_counter -= 1
            print(f"Too low.\nGuess again.\nYou have {attempts_counter} attempts left to guess the number.")
            guessed_number = int(input("Make a guess: "))
            if attempts_counter == 1:
                print(f"You've run out of attempts. You lose.\nThe correct answer was: {chosen_number}.")   
        elif chosen_number < guessed_number:
            attempts_counter -= 1
            print(f"Too high.\nGuess again.\nYou have {attempts_counter} attempts left to guess the number.")
            guessed_number = int(input("Make a guess: "))
            if attempts_counter == 1:
                print(f"You've run out of attempts. You lose.\nThe correct answer was: {chosen_number}.")
play = 'Y'
while play == 'Y':
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        attempts_counter = 10
        print(f"You have {attempts_counter} attempts left to guess the number.")
        guessed_number = int(input("Make a guess: "))
        start_game()
        if chosen_number != guessed_number and attempts_counter == 0:
            print(f"You've run out of attempts. You lose.\nThe correct answer was: {chosen_number}.")
    else:
        attempts_counter = 5
        print(f"You have {attempts_counter} attempts left to guess the number.")
        guessed_number = int(input("Make a guess: ")) 
        start_game()
        if chosen_number != guessed_number and attempts_counter == 0:
            print(f"You've run out of attempts. You lose.\nThe correct answer was: {chosen_number}.")
    play = input("Press 'Y' to start a new game and 'N' to quit: ").upper()
    if play == 'Y':
        clear()
    else:
        clear()
        print(ending)