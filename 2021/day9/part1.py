#!/usr/bin/env python3

def is_local_minimum(heightmap, i, j, i_len, j_len):
    directions = []
    if i > 0:
        directions.append((i-1, j))
    if j > 0:
        directions.append((i, j-1))
    if i < i_len - 1:
        directions.append((i+1, j))
    if j < j_len - 1:
        directions.append((i, j+1))
    less_than = [heightmap[i][j] < heightmap[x][y] for (x, y) in directions]
    return all(less_than)

def solution(problem):
    heightmap = [[int(i) for i in line] for line in problem]
    
    i_len = len(heightmap)
    j_len = len(heightmap[0])
    
    risk_level = 0
    
    for i in range(i_len):
        for j in range(j_len):
            if is_local_minimum(heightmap, i, j, i_len, j_len):
                risk_level += heightmap[i][j] + 1
    
    return risk_level

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


