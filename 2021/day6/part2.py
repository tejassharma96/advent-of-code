#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def iterate(fish):
    zero_days = fish[0]
    
    for i in range(1, 9):
        fish[i-1] = fish[i]
    
    fish[6] += zero_days
    fish[8] = zero_days
        

def solution(problem):
    fish = [int(i) for i in problem[0].split(',')]
    fish_stages = { i: fish.count(i) for i in range(9) }
    
    for _ in range(256):
        iterate(fish_stages)
    
    return sum(fish_stages.values())

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))