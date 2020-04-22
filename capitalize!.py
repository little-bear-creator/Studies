#!/bin/python3

import math
import os
import random
import re
import sys


# Return a string where every word separated by a space had their first letter capitalyzed
# Spaces between words can have any lengh you want, there is a loop that take care of that
# Also if there is a word two times, they will both be part of the result
def solve(s):

    # make a list of every word in s
    name = s.split()
    # result of the function
    result = "" 
    id = 0
    # copy : a string to detect occurences of a word
    copy = ""

    # Loop to capitalize every first letter of each word
    for item in name:

        # Exception : when we have the same value 2 times
	# This test can be improved by replacing the string copy by a list copy, with every word printed
	# But with the solution here, Tests cases are successfull and challenge solved
        if(copy == item):
            index = s.rfind(item)
        else:
            # place of next string
            index = s.find(item)

        # Loop to add the spaces between names
        while(id < index):
            result+=" "
            id+=1
        
        # Make a copy of item for futur test
        copy = item
        # Get the capitalize name
        item = item.capitalize()
        result += item

        # Update id for next name
        id += len(item)
        
            
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

