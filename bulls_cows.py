import random
import time
from os import system

#import rules_greeting


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
    run = False

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

def count_bulls_cows(number,guess) -> int:
    '''
    Description:
    Counts numbers for Bulls and Cows. 
    '''
    bulls = 0
    cows = 0
    for x in range(len(user_guess())):
        if guess[x] == number[x]:
            bulls += 1
        elif guess[x] in number:
            cows += 1
    return (cows,bulls)



