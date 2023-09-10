import random
import math

lower = int(input("Enter lower bound:- "))

upper = int(input("Enter upper bound:- "))

computerGuess = random.randint(lower, upper)

number_of_try = round(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", number_of_try, " chances to guess the integer!\n")

count = 0

while count < number_of_try:
    count += 1
    guess = int(input("\nGuess a number:- "))

    if computerGuess == guess:
        break
    elif computerGuess > guess:
        print("You guessed too small!")
    elif computerGuess < guess:
        print("You guessed too high!")

if computerGuess != guess:
    print("\nTime up!")
    print("\tThe number is %d" % computerGuess)
    print("\tBetter Luck Next Time!")
else:
    print("Congratulations, You did it in", count, "try!")