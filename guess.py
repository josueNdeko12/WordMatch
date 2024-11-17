
# After word is color-coded, add it to the list of guesses. Return colored_word
def add_to_guesses_list(colored_guess, guesses_list):
    guesses_list.append(colored_guess)

# Get the guess from user and decrease tries left after each guess
def get_guess(attempts_remaining, word):
    allowed = False
    while not allowed:
        guess = input("Enter your guess: ").upper()
        if guess == word:
            break
        check = guess_allowed(guess)
        if check == False:
            print("Your word is not found in our 'allowed guesses list'")
        else:
            allowed = True
    attempts_remaining -=1
    return guess

# Check if the guesed word is the correct word. Then, check if guess is in allowed-guesses. Call add_color if wrong.
# Ensure that the guess have 5 chars, else print an error message.
def check_guess(guess, word, correct):
    if guess == word:
        correct = True
    return correct

# Returns True if the guess is in the allowed words list, otherwise returns False
def guess_allowed(guess):
    if len(guess) != 5:
        return False
    with (open("w1.txt", "r") as file):
        lines = file.readlines()
        lo, hi = 0, len(lines) -1

        while lo <= hi:
            mid = (hi+lo) // 2
            curr = lines[mid]
            curr = curr.strip("\n").upper()
            if curr == guess:
                return True
            elif guess > curr:
                lo = mid +1
            else:
                hi = mid -1
    return False