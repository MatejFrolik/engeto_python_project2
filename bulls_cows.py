from random import choice
from time import perf_counter as pc
from os import system

import rules_greeting

#    """
#     Description:
#     Connects values from *args with .join method.
#     Then adds separator before and after arguments.
    
#     Example: 
#     args = ("a", "b", "C")

#     Result:
#     ---------
#     a | b | C
#     ---------
#     """ 

# TODO main function
def bulls_cows_game() -> None:
    '''
    Description:
    The main function for running whole program.
    '''
    while True:
        pass

# TODO number generator function
def num_generator():   #return maybe (str,int,list with str/int....)
    '''
    Description:
    Return random 4digits number with 
    different numbers. It doesn't start with 0.
    '''
    pass

# TODO user imput function
def user_guess():   #return maybe (str,int,list with str/int....)
    '''
    Description:
    User input 4digits number. User is not allowed 
    to insert longer number or other characters. 
    '''
    pass

# TODO bulls and cows calculator function
def count_bulls_cows(number,guess) -> int:
     '''
    Description:
    Counts numbers for Bulls and Cows. 
    '''
    pass

if __name__ == "__main__":
    bulls_cows_game()
