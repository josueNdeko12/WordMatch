from colorama import Fore, Style, init
from utils import *

# Display the amount of tries remaining and the list of guesses after each attempt. Display the actual
# word of no more tries left.
def display_progress(attempts_remaining, guesses_list, correct, word):
    if correct == False and attempts_remaining == 0:
        for n in range(len(guesses_list)):
            print("Attempt", n+1, guesses_list[n])
        print("THE CORRECT WORD:", word)
    elif correct == False:
        print("YOU HAVE", attempts_remaining, "ATTEMPTS REMAINING")
        for n in range(len(guesses_list)):
            print("Attempt", n+1, guesses_list[n])
    else:
        print("YOU GUESSED IT!!!")
        for n in range(len(guesses_list)):
            print("ATTEMPT", n+1, guesses_list[n])

# If guess is not correct, color-code each char
def add_color(guess, word):
    word_dict = make_dict(word)
    init()
    new_word = [''] * len(word)

    for x in range(len(word)):
        if word[x] == guess[x]:
            new_word[x] = Fore.GREEN + word[x] + Style.RESET_ALL
            word_dict[word[x]] -= 1

    for x in range(len(word)):
        if not new_word[x]:
            if guess[x] in word and guess[x] in word_dict:
                if word_dict[guess[x]] > 0:
                    new_word[x] = Fore.YELLOW + guess[x] + Style.RESET_ALL
                    word_dict[guess[x]] -= 1
            else:
                new_word[x] = Fore.RED + guess[x] + Style.RESET_ALL

    return "".join(new_word)