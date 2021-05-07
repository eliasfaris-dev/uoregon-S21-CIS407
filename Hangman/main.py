"""
Hangman
"""
import string


def main():
    hangman()




def hangman():
    word = input("Type in a word for hangman(No spaces): ")
    word_letters = set(word)
    alpha = set(string.ascii_uppercase)
    used_letters = set()

    user_guess = input("Guess a letter: ").upper()
    lives = 10

    while len(word_letters) > 0:
        print("You have", lives)
        word_in_list = [letter if letter in used_letters else '-' for letter in word]
        
        print("The word: ", ''.join(word_in_list))

        if used_letters in (alpha - used_letters):
            used_letters.add(used_letters)
            if used_letters in word_letters:
                word_letters.remove(used_letters)

            else:
                lives = lives - 1

        elif(used_letters in used_letters):
            print("You used this letter already. Try again")

        else:
            print("Not valid character. Try again")

    if lives == 0:
        print("You lost. Nice try")








main()


