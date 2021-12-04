#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def solution(problem):
    problem = [float(i) for i in problem]
    count = 0
    for i in range(1, len(problem)):
        if problem[i] > problem[i-1]:
            count += 1 
    return count


if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


