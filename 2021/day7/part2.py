#!/usr/bin/env python3

from statistics import mean
from math import ceil, floor

def solution(problem):
    crabs = [int(i) for i in problem[0].split(',')]
    mean_location = mean(crabs)
    optimal_locations = (floor(mean_location), ceil(mean_location))
    fuel = [0, 0]
    for crab in crabs:
        for i, loc in enumerate(optimal_locations):
            diff = abs(crab - loc)
            # 1+2+3+... formula
            fuel[i] += diff * (diff + 1) // 2

    return min(fuel)

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


