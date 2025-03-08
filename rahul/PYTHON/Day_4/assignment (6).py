#Guessing Number Program :   
 
'''You need to write a program that will generate a random number between 1 to 10 this number will have to be guessed
 
by the user and if they guess the number then print a message saying you guessed the number also print the number
 
of tries it took for the user to guess the number.
 
Also give a limit of 5 guesses to the user if they don’t guess in 5 tries then print a message saying they
 
didn’t guess the number and print the actual number.
 
 
Guess a number between 1 and 10: 1
 
Your guess is too low you have 4 left
 
Guess a number between 1 and 10: 3
 
Your guess is too low you have 3 left
 
Guess a number between 1 and 10: 9
 
Your guess is too high you have 2 left
 
Guess a number between 1 and 10: 9
 
Your guess is too high you have 1 left
 
Guess a number between 1 and 10: 9
 
Your guess is too high you have 0 left
 
You did not guess the number, The number was 5'''


import random
number_to_guess = random.randint(1, 10)
attempts = 5
while attempts > 0:
    guess = int(input(f"Guess a number between 1 and 10: "))
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
        print(f"It took you {6 - attempts} tries.")
        break
    else:
        if guess < number_to_guess:
            print(f"Your guess is too low, you have {attempts - 1} left.")
        else:
            print(f"Your guess is too high, you have {attempts - 1} left.")
    attempts -= 1

if attempts == 0:
    print(f"You did not guess the number. The number was {number_to_guess}.")