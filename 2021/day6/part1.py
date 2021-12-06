#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def iterate(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

def solution(problem):
    fish = [int(i) for i in problem[0].split(',')]
    
    for _ in range(80):
        iterate(fish)
    
    return len(fish)

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


