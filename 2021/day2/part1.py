#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def solution(problem):
    depth = 0
    dist = 0
    for instruction in problem:
        i = instruction.split()
        direction = i[0]
        amount = int(i[1])
        if direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
        elif direction == "forward":
            dist += amount

    return depth * dist

    

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


