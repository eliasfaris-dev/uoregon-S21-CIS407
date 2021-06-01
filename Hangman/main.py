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
    user_guess = str(user_guess)
    lives = 10

    test = len(word_letters)

    while test > 0 and lives > 0:
        print("You have", lives)
        word_in_list = [letter if letter in used_letters else '*' for letter in word]
        
        print("The word: ", ''.join(word_in_list))
        user_guess = input("Guess a letter: ").upper()

        if user_guess in word:
            print("correct next guess")
            test -= 1

        if user_guess in (alpha - used_letters):
            used_letters.add(user_guess)

            if user_guess in word_letters:
                word_letters.remove(user)

            else:
                lives = lives - 1

        elif(user_guess in used_letters):
            print("You used this letter already. Try again")

        else:
            print("Not valid character. Try again")

    if lives == 0:
        print("You lost. Nice try")

    else:
        print("You won!")






main()


