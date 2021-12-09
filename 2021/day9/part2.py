#!/usr/bin/env python3

from math import prod

def get_valid_directions(i, j, i_len, j_len):
    directions = []
    if i > 0:
        directions.append((i-1, j))
    if j > 0:
        directions.append((i, j-1))
    if i < i_len - 1:
        directions.append((i+1, j))
    if j < j_len - 1:
        directions.append((i, j+1))
    return directions

def is_local_minimum(heightmap, i, j, i_len, j_len):
    directions = get_valid_directions(i, j, i_len, j_len)
    less_than = [heightmap[i][j] < heightmap[x][y] for (x, y) in directions]
    return all(less_than)

def basin(heightmap, locations, i, j, i_len, j_len):
    locations.add((i, j))
    directions = get_valid_directions(i, j, i_len, j_len)
    for x, y in directions:
        if heightmap[i][j] < heightmap[x][y] < 9 and (x, y) not in locations:
            locations = basin(heightmap, locations, x, y, i_len, j_len)
    return locations

def solution(problem):
    heightmap = [[int(i) for i in line] for line in problem]
    
    i_len = len(heightmap)
    j_len = len(heightmap[0])
    
    basin_sizes = []
    
    for i in range(i_len):
        for j in range(j_len):
            if is_local_minimum(heightmap, i, j, i_len, j_len):
                basin_sizes.append(len(basin(heightmap, set(), i, j, i_len, j_len)))
    
    return prod(sorted(basin_sizes, reverse=True)[:3])

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))
