# to import random module
import random
# to create a range of random numbers between 1-10
n = random.randrange(1,100)
# to take a user input to enter a number
guess = int(input("Enter any number: "))
while n!= guess: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < n:
        print("Too low")
        # to again ask for input
        guess = int(input("Enter number again: "))
    # if guess is greater than n
    elif guess > n:
        print("Too high!")
        # to again ask for the user input
        guess = int(input("Enter number again: "))
    # if guess gets equals to n terminate the while loop
    else:
        break
print("you guessed it right!!")

"""A number guessing game aims to guess the number that the program has come up with. Essentially the program logic is:

The program randomly selects a number between 1 and 100 or any other combination of numbers.
It will then ask the player to enter his proposal.
It will then check if this number is the same as the one generated randomly by the computer; if so, the player wins.
If the player’s guess is not the same, then he will check if the number is higher or lower than the guess and tell the player."""
