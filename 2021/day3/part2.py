#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def oxy_value(vslice):
    if len(vslice) == 1:
        return vslice[0]
    zeros = vslice.count('0')
    ones = vslice.count('1')
    return '0' if zeros > ones else '1'

def co2_value(vslice):
    if len(vslice) == 1:
        return vslice[0]
    zeros = vslice.count('0')
    ones = vslice.count('1')
    return '1' if ones < zeros else '0'

def filter_options(curr_options, digit, index):
    return [num for num in curr_options if num[index] == digit]

def vertical_slice(curr_options, index):
    return [num[index] for num in curr_options]

def solution(problem):
    problem = [i.strip() for i in problem]

    oxy = ''
    co2 = ''

    oxy_options = problem.copy()
    co2_options = problem.copy()

    for i in range(len(problem[0])):
        oxy_slice = vertical_slice(oxy_options, i)
        oxy_val = oxy_value(oxy_slice)
        oxy_options = filter_options(oxy_options, oxy_val, i)
        oxy += oxy_val

        co2_slice = vertical_slice(co2_options, i)
        co2_val = co2_value(co2_slice)
        co2_options = filter_options(co2_options, co2_val, i)
        co2 += co2_val

    oxy = int(oxy, 2)
    co2 = int(co2, 2)
    print(f'Oxy (dec): {oxy}')
    print(f'CO2 (dec): {co2}')
    return oxy * co2

    

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


