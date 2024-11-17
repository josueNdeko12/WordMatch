import random
from guess import *
from display import *

word_list = []
guesses_list = []
attempts_remaining = 6
correct = False

# Randomly select a word from the list of 5-letter words
def select_word(word_list):
    word = random.choice(word_list)
    return word

def main(attempts_remaining, guesses_list, correct):
    make_list(word_list)
    word = select_word(word_list)
    while attempts_remaining > 0 and correct == False:
        guess = get_guess(attempts_remaining, word)
        attempts_remaining -=1
        print("YOU HAVE", attempts_remaining, "ATTEMPTS REMAINING")
        colored_guess = add_color(guess, word)
        add_to_guesses_list(colored_guess, guesses_list)
        #print(attempts_remaining)
        correct = check_guess(guess, word, correct)
        display_progress(attempts_remaining, guesses_list, correct, word)

main(attempts_remaining,guesses_list, correct)