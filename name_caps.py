#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):         #it prints the name with 1st letter of each word capitalized but 123arfa remaining as it is.
    s = s.split(" ")
    new_s = ""
    for word in s:
        new_s = new_s + word.capitalize() + " "
    new_s = new_s.strip()
    return new_s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
