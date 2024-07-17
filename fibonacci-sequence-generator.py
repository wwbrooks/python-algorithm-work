##!/usr/bin/env python3
# 
# Author:   Bill Brooks <wwbrooks@gmail.com>
# Language: Python 3.9.x
# Creation: Tue Mar 12 19:42:55 PDT 2024
# Filename: fibonacci-sequence-generator.py
# Link:     
#           
# Descr:    The Fibonacci sequence begins with 0 and then 1 follows. All
#           subsequent values are the sum of the previous two, ex: 0, 1,
#           1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an
#           index, n (starting at 0), as a parameter and returns the nth value
#           in the sequence. Any negative index values should return -1.
#           
# Ex: If the input is:           
#           
#   7
#
# the output is:
# 
#   fibonacci(7) is 13
#

# 
def fibonacci(n):
    """Generates and returns the n-th fibonacci value"""
    the_sequence = [0, 1, 1]
    results = 0
    
    if ( n < 0 ):
        results = -1
    elif (n == 0):
        results = the_sequence[n]
    elif (n == 1):
        results = the_sequence[n]
    else: 
        # value supplied is greater than one

        for itr in range(2, n):
            # print(f' iteration # {itr}')
            # print(f' adding to the array: {the_sequence[(itr)]} + {the_sequence[(itr-1)]}')
            next_element = the_sequence[(itr)] + the_sequence[(itr-1)]
            # print(f'{next_element}', end=' ')
            the_sequence.append(next_element)
            # print('')

        # print('the fib sequence is now: ', the_sequence)    
        results = the_sequence[n]
        
    return (results) 


if __name__ == '__main__':
    start_num = int(input('Enter the desired fibonacci number: '))
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
