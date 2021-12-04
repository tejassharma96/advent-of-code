#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def solution(problem):
    depth = 0
    dist = 0
    aim = 0
    for instruction in problem:
        i = instruction.split()
        direction = i[0]
        amount = int(i[1])
        if direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        elif direction == "forward":
            dist += amount
            depth += aim * amount

    return depth * dist

    

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))


