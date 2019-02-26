#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    for rot in range(d):
        l = []
        
        f = a[0]
        for i in range(1, len(a)):
            l.append(a[i])
        l.append(f)
        a = l
        print(a)



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = [5, 4]

    n = int(nd[0])

    d = int(nd[1])

    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)
    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
