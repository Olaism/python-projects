import random

def displayName(name):
    print("Good Luck !", name, "\n")

def getWords():
    return ["rainbow", "computer", "science", "programming",
            "python", "prayer", "mathematics", "player", "condition",
            "reverse", "water", "board", "geeks"]

def getWordsFromFile(filname):
    words = []
    with open(filname, "r") as f_obj:
        content = f_obj.readlines()
    for word in content:
        words.append(word.strip())
    return words

def takeAGuess(words):
    return random.choice(words)

def play(noOfTurn, guessedWord):
    guesses = ''
    while noOfTurn > 0:

        failed = 0

        for char in guessedWord:

            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("You won!")
            print("The word is", guessedWord)
            break
        guess = input("\n\nGuess a character:- ")
        guesses += guess

        if guess not in guessedWord:
            noOfTurn -= 1

            print("Wrong")
            print("You have", noOfTurn, "more guesses")

            if noOfTurn == 0:
                print("You lose!")

def main():
    name = input("What's your name?")
    displayName(name)

    words = getWordsFromFile('dictionary.txt')

    guessedWord = takeAGuess(words)

    print("Guess the characters", end=": " )

    turns = len(guessedWord)

    play(turns, guessedWord)

if __name__ == "__main__":
    main()