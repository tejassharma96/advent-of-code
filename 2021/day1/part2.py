#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def solution(problem):
    problem = [float(i) for i in problem]
    count = 0
    for i in range(4, len(problem)+1):
        prev = sum(problem[i-4:i-1])
        curr = sum(problem[i-3:i])
        if curr > prev:
            count += 1 
    return count

    

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


