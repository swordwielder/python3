#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestEvenWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def longestEvenWord(sentence):
    a = sentence.split(' ')
    evennum=0
    stringreturned=""
    for word in a:
        if len(word)%2==0 and len(word)>evennum:
            evennum=len(word)
            stringreturned=word
    
    if evennum > 0:
        return stringreturned
    else:
        return "00"
    # Write your code here

if __name__ == '__main__':
