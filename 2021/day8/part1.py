#!/usr/bin/env python3

#  aaaa
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 

def parse_input(input):
    pass

def solution(problem):
    problem = [p.split(' | ') for p in problem]
    # signals = [p[0].split() for p in problem]
    outputs = [p[1].split() for p in problem]
    
    count = 0
    for output in outputs:
        count += len([o for o in output if len(o) in [2, 3, 4, 7]])
    return count

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


