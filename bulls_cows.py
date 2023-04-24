import random
from time import perf_counter as pc
from os import system

#import rules_greeting

# TODO main function
def bulls_cows_game() -> None:
    '''
    Description:
    The main function for running whole program.
    '''
    while True:
        pass

def num_generator() -> str:   

    '''
    Description:
    Return random 4digits number with 
    different numbers. It doesn't start with 0.
    '''
    run = True
    while run:
        num_gen = random.sample('0123456789', 4)
   #     num_gen = ''.join(num_gen)
        if num_gen[0] == '0':
            continue
        else:
            return ''.join(num_gen)


def user_guess() -> str:   
    '''
    Description:
    User input 4digits number. User is not allowed 
    to insert longer number or other characters. 
    '''
    run = True
    while run:
        guess = input('Enter a 4 digits number which doesn\'t start with 0: ')
        if len(guess) != 4 or not guess.isdigit() or guess[0] == '0':
            print('Wrong input, please enter 4 digits number one more time')
        else:
            return guess


# TODO bulls and cows calculator function
def count_bulls_cows(number,guess) -> int:
     '''
    Description:
    Counts numbers for Bulls and Cows. 
    '''
     pass

