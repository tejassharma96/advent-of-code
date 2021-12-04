#!/usr/bin/env python3

import math
import os
import random
import re
import sys

class Board:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.status = [[False] * self.cols for _ in range(self.rows)]
        self.solved = False
        self.score = -1
    
    def mark(self, num):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == num:
                    self.status[i][j] = True
                    self.solved = self.is_solved()
                    if self.solved:
                        self.score = self.score_sum() * num
                    break
                
    def is_solved(self):
        def vertical():
            vertical_slices = [[row[i] for row in self.status] for i in range(self.cols)]
            for vslice in vertical_slices:
                if all(vslice):
                    return True

            return False
        
        def horizontal():
            for row in self.status:
                if all(row):
                    return True

            return False

        def diagonal():
            diag1 = [self.status[i][i] for i in range(self.cols)]
            diag2 = [self.status[i][self.cols - 1 - i] for i in range(self.cols)]
            
            return all(diag1) or all(diag2)

        return vertical() or horizontal() # or diagonal()
    
    def score_sum(self):
        score = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.status[i][j]:
                    score += self.board[i][j]
        return score
    
    def printBoard(self):
        for i in range(self.rows):
            row = ''
            for j in range(self.cols):
                if self.status[i][j]:
                    row += f'[{self.board[i][j]}]\t'
                else:
                    row += f'{self.board[i][j]}\t'
            print(row)

def solution(problem):
    numbers = [int(i) for i in problem.pop(0).split(',')]
    
    boards = []
    curr = []
    for line in problem:
        if len(line) == 0:
            if len(curr) > 0:
                boards.append(Board(curr))
            curr = []
            continue
        
        curr.append([int(i) for i in line.split()])
    
    if len(curr) > 0:
        boards.append(Board(curr))
        
    print(f'{len(boards)} boards')
    for i, board in enumerate(boards):
        print(f'Board {i}:')
        board.printBoard()
    
    for num in numbers:
        print(num)
        for i, board in enumerate(boards):
            board.mark(num)
            if board.solved:
                print(f'Board {i} wins:')
                board.printBoard()
                return board.score
    
    return -1

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


