#!/usr/bin/env python3

import math
import os
import random
import re
import sys

class Point:
    def __init__(self, coord_string):
        coords = coord_string.split(',')
        self.x = int(coords[0])
        self.y = int(coords[1])

class Vent:
    def __init__(self, coords_string):
        coords = coords_string.split(' -> ')
        self.p1 = Point(coords[0])
        self.p2 = Point(coords[1])
    
    def range(self):
        if self.horizontal():
            r = range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y) + 1)
            return [(self.p1.x, y) for y in r]
        elif self.vertical():
            r = range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x) + 1)
            return [(x, self.p1.y) for x in r]
    
    def orthogonal(self):
        return self.horizontal() or self.vertical()
    
    def horizontal(self):
        return self.p1.x == self.p2.x
    
    def vertical(self):
        return self.p1.y ==self.p2.y

class SeaFloor:
    def __init__(self, vent_strings):
        self.vents = [Vent(vent) for vent in vent_strings]
        self.maxX = max([max(vent.p1.x, vent.p2.x) for vent in self.vents])
        self.maxY = max([max(vent.p1.y, vent.p2.y) for vent in self.vents])
        self.board = self.__calculateBoard()

    def __calculateBoard(self):
        board = [[0 for _ in range(self.maxX + 1)] for _ in range(self.maxY + 1)]
        for vent in self.vents:
            if vent.orthogonal():
                for (x, y) in vent.range():
                    board[y][x] += 1
        return board
    
    def intersections(self):
        count = 0
        for row in self.board:
            for point in row:
                if point > 1:
                    count += 1
        return count
    

def solution(problem):
    floor = SeaFloor(problem)
    
    return floor.intersections()

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


