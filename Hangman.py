import random

## Base Variables
guesses_left = 10
win = False

words = [
    "banana",
    "wow",
    "harvest",
    "moon",
    "sun",
    "smelly",
    "amazing",
    "hangman",
    "owl"
    ]

secret_word = random.choice(words)
dashes = ""

## Stores guessed variables ##
guessed_dict = {
    }
    
## Creates initial censored word, as a list ##
dashes_list = dashes.split()
for i in range(len(secret_word)):
    dashes_list.append("-")
dashes = "".join(dashes_list)

## ERROR AND DEBUGGING CODE ##
error_dict = {
    "type_error":"You must enter a single, lowercase letter.",
    "amount_error":"You must enter only one letter."
    }
    
def throw_error(error, dictionary):
    print("{} : {}".format(error, dictionary[error]))

## Retrieves a user input ##
def get_guess(error_dict):
    legal_guesses = "abcdefghijklmnopqrstuvwxyz"
    guess = input("Enter a guess : ")
    if guess not in legal_guesses:
        throw_error("type_error", error_dict)
        return False
    if (guess == legal_guesses):
        print("Clever bastard.")
        throw_error("amount_error", error_dict)
        return False
    elif (len(guess) > 1):
        throw_error("amount_error", error_dict) 
        return False
    elif (len(guess) == 0):
        throw_error("amount_error", error_dict)
        return False
    else:
        return guess

    
## Updates dashes based on guesses
def update_dashes(guess, secret_word, dashes_list):
    if guess in secret_word:
        for i in range(len(secret_word)):
            if (secret_word[i] == guess):
                dashes_list[i] = guess
                print("Letter '{}' found, in position {}.".format(guess, i+1))
    else:
        print("Letter '{}' not found.".format(guess))
    return dashes_list
    
## Driver Code ##
while guesses_left > 0:
    print("- - - - - - - - - -")
    print("Guesses remaining : {}".format(guesses_left))
    current_guess = get_guess(error_dict)
    
    if (current_guess == False):
        continue
    
    dashes_list = update_dashes(current_guess, secret_word, dashes_list)
    print("- - - - - - - - - -")
    print(dashes_list)
    
    dashes = "".join(dashes_list)
    
    if (current_guess not in secret_word):
        guesses_left -= 1
    
    if (dashes == secret_word):
        win = True
        break
    
if (win):
    print("You win!")
    print("The word was : '{}'.".format(secret_word))
else:
    print("You lose!")
    print("The word was : '{}'.".format(secret_word))
