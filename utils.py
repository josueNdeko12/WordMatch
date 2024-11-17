# Takes a string and return a dictionary with each character of the string and their occurences
def make_dict(guess):
    guess_dict = dict()
    for i in (guess):
        if i in guess_dict:
            guess_dict[i] +=1
        else:
            guess_dict[i] = 1
    return guess_dict

# On the first attempt, create a list containig the words from "words" file
def make_list(word_list):

    '''
    with open("all.txt", "r") as file:
        with open("w1.txt", "w") as output:
            for word in file:
                if len(word) == 6 or len(word) == 5:
                    word = word.strip("\n")
                    word = word.upper()
                    word_list.append(word)
                    output.write(str(word))
                    output.write(str("\n"))
    '''

    with open("wordle-answers-alphabetical.txt", "r") as file:
        for word in file:
            word = word.strip("\n")
            word = word.upper()
            word_list.append(word)
