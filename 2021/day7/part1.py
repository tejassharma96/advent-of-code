#!/usr/bin/env python3

from statistics import median

def solution(problem):
    crabs = [int(i) for i in problem[0].split(',')]
    optimal_location = median(crabs)
    fuel = sum([abs(crab - optimal_location) for crab in crabs])
    
    return fuel

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


