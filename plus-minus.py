#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    a = [(0 if i==0 else (-1 if i<0 else 1 ) ) for i in arr]
    b=len(arr)

    ([print("%.5f"%(i))for i in [a.count(1)/b,a.count(-1)/b,a.count(0)/b]])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
