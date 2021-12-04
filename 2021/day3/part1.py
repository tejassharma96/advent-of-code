#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def ordered_binary_pair(vslice):
    zeros = vslice.count('0')
    ones = vslice.count('1')
    return ('0', '1') if zeros > ones else ('1', '0')


def solution(problem):
    problem = [i.strip() for i in problem]
    vertical_slices = [[num[i] for num in problem] for i in range(len(problem[0]))]
    pairs = [ordered_binary_pair(vslice) for vslice in vertical_slices]

    gamma = ''.join([pair[0] for pair in pairs])
    epsilon = ''.join([pair[1] for pair in pairs])

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon

    

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


