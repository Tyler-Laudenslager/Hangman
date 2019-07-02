import word_generator as generator
from nltk.corpus import wordnet
import hangman
import sys

def generate_array(word):

    array = ['_' for i in range(len(word))]
    return array

def print_array(array):
    for i in array:
        print(i, end=' ')
        
def check_letter(letter, random_word, word_array, game):

    if letter in random_word:
        for i in range(len(random_word)):
            if letter == random_word[i]:
                word_array[i] = letter
            else:
                pass
    else:
        game.add_body_part()
def add_guessed_letter(array, letter):

    if letter in array:
        pass
    else:
        array.append(letter)

def check_if_won(array, game):
    space = '_'
    if space in array:
        return False    
    else:
        return True
def play_again_won():
    print()
    print("""You won the game would you like to play again""")
    choice = input("Press 'y' for yes 'n' for no: ")
    if choice == 'y':
        return True
    if choice == 'n':
        return False
def definition(word):
    synsets = wordnet.synsets(word)
    print("Definition: ")
    for synset in synsets:
        print(synset.definition())
def play_again_lost(word):
    print()
    print("The word we were looking for was: " + word)
    definition(word)
    print()
    print("""You lost the game would you like to play again""")
    choice = input("Press 'y' for yes 'n' for no: ")
    if choice == 'y':
        return True
    if choice == 'n':
        return False
def game_engine():
    game.display_board()
    print()
    print("Your word to guess is:")
    print_array(word_array)
    print()
    print()
    print("Your guessed letters: ")
    print_array(guessed_letters)
    print()
    letter = input("Input the letter you wish to guess: ")
    check_letter(letter, random_word, word_array, game)
    add_guessed_letter(guessed_letters, letter)
def display_last_board():
    game.display_board()
    print()
    print("Your word to guess is:")
    print_array(word_array)
    print()
    print()
    print("Your guessed letters: ")
    print_array(guessed_letters)
    print()   
if __name__ == "__main__":
    while True:
        play_again = True
        if play_again:
            random_word = generator.get_word().lower()
            guessed_letters = []
            word_array = generate_array(random_word)

            game = hangman.Hangman()
            print()
            print("""Welcome to Hangman
To play just guess a letter if the letter is in the word it will be added
if not you get a body part on the hanged man""")

            while True:
                
                game_engine()
                if check_if_won(word_array, game):
                    display_last_board()
                    if play_again_won():
                        play_again = True
                        break
                    else:
                        print("Press Enter to exit the game")
                        input()
                        sys.exit(0)
                    break
                if game._wrong_guess >= 6:
                    display_last_board()
                    if play_again_lost(random_word):
                        play_again = True
                        break
                    else:
                        print("Press Enter to exit the game")
                        input()
                        sys.exit(0)
                else:
                    pass
        else:
            break

    print("Press Enter to Quit the Game")
    input()
        

        
