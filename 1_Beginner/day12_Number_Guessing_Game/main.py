# The Guessing Number Game
from tools import clear
from art import logo
import random


def show_attempts():
    print(f"You have {attempts} attemps remaining to guess the number")


def check_guess(user_guess, secret_number):
    if user_guess > 100 or user_guess < 0:
        return 1
    if user_guess == secret_number:
        return 0
    if user_guess > secret_number:
        return 2
    if user_guess < secret_number:
        return 3


clear()
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 101)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
if difficulty == "hard":
    attempts = 5

win = 0
while attempts > 0:
    show_attempts()
    user_guess = int(input("Make a guess: "))
    if check_guess(user_guess, secret_number) == 0:
        attempts = 0
        win = 1
    elif check_guess(user_guess, secret_number) == 1:
        attempts -= 1
        print("Not a correct guess")
    elif check_guess(user_guess, secret_number) == 2:
        attempts -= 1
        print("Too high.")
    elif check_guess(user_guess, secret_number) == 3:
        attempts -= 1
        print("Too low.")

if win == 1:
    print(f"You got it! The answer was {secret_number}")
else:
    print("You've run out of guesses, you lose")
