from nltk.corpus import words
import random

def get_word():
    
    word_list = words.words()
    number = random.randint(0,len(word_list)-1)
    return word_list[number]

