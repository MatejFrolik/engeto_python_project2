import random
import time
import os

import rules_greeting


def num_generator() -> str:   

    '''
    Description:
    Return random 4digits number with 
    different numbers. It doesn't start with 0.
    '''
    while True:
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
    while True:
        guess = input('Enter a 4 digits number which doesn\'t start with 0: ')
        if len(guess) != 4 or not guess.isdigit() or guess[0] == '0':
            print('Wrong input, please enter 4 digits number one more time')
        else:
            return guess

def count_bulls_cows(number,guess) -> int:
    '''
    Description:
    Counts numbers of Bulls and Cows. Compare guess number and random number. 
    '''
    bulls = 0
    cows = 0
    for i in range(4):
        if number[i] == guess[i]:
            bulls += 1
        elif number[i] != guess[i] and guess[i] in number:
            cows += 1
    return bulls, cows



def bulls_cows_game() -> None:
    '''
    Description:
    The main function for running whole program.
    '''

    print(f'''
              {rules_greeting.bulls_cows}
              {rules_greeting.rules}
              
              
              
              
              
              
              
              

              
              ''')
    
    os.system('clear')
    number = num_generator()
    guesses = 0
    program = True
    start = time.time()
    while program:
            user_input = user_guess()
            guesses += 1
            cows,bulls = count_bulls_cows(number,user_input)
            print(f'cows: {cows} bulls: {bulls}')
            if bulls == 4: 
                print(f'You entered correct number. Number o attempts: {guesses}.')
                program = False
                
    end = time.time()
    game_time = end-start
    print(f'It tooks you: {game_time} seconds.')

bulls_cows_game()
