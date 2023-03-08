import numpy as np
import random
import math
import pygame
import sys


NULL = 0

NUM_ROW = 6
NUM_COLUMN = 7

HUMAN = 0
COMPUTER = 1

WIN_LEN = 4



HUMAN_MARK = 1
COMPUTER_MARK = 2

COLOUR_BLACK = (0,0,0)
COLOUR_GREEN = (0,255,0)
COLOUR_BLUE = (0,0,255)
COLOUR_RED = (255,0,0)

BIG_POSITIVE = 100000000000
BIG_NEGATIVE = -100000000000

class Connect_Four:

    def __init__(self):
        board = ()

    def create_board(self):
        return  np.zeros((NUM_ROW,NUM_COLUMN))

    def print_board(self,board):

        print(np.flip(board,0))

    def drop_circle(self,board,r,c,PLAYER_MARK):
        board[r][c] = PLAYER_MARK

    def get_next_valid_row(self,board,col):
        for row in range(NUM_ROW):
            if board[row][col] == 0:
                return row
    def check_winner_move(self,board,PLAYER_MARK):
        for col in range(NUM_COLUMN - 3):
            for row in range(NUM_ROW):
                if board[row][col] == PLAYER_MARK and board[row][col + 1] == PLAYER_MARK and board[row][col + 2] == PLAYER_MARK and board[row][col + 3] == PLAYER_MARK:
                    return True

        for col in range(NUM_COLUMN):
            for row in range(NUM_ROW - 3):
                if board[row][col] == PLAYER_MARK and board[row + 1][col] == PLAYER_MARK and board[row + 2][col] == PLAYER_MARK and board[row + 3][col] == PLAYER_MARK:
                    return True

        for col in range(NUM_COLUMN - 3):
            for row in range(3, NUM_ROW):
                if board[row][col] == PLAYER_MARK and board[row - 1][col +1] == PLAYER_MARK and board[row-2][col+2] == PLAYER_MARK and board[row-3][col+3] == PLAYER_MARK:
                    return True

        for col in range(NUM_COLUMN - 3):
            for row in range(NUM_ROW - 3):
                if board[row][col] == PLAYER_MARK and board[row+1][col+1] == PLAYER_MARK and board[row+2][col+2] == PLAYER_MARK and board[row + 3][col+3] == PLAYER_MARK:
                    return True

    def is_terminal_node(self,board):
        return self.check_winner_move(board,HUMAN_MARK) or self.check_winner_move(board,COMPUTER_MARK) or len(self.get_val_loc(board)) == 0

    def is_val_loc(self,board,column):
        return board[NUM_ROW-1][column] == 0

    def get_val_loc(self,board):
        val_loc = []
        for col in range(NUM_COLUMN):
            if self.is_val_loc(board,col):
                val_loc.append(col)
        return val_loc
    def pos_score(self,board,PLAYER_MARK):
        score = 0
        mid_array = [int(i) for i in list(board[:,NUM_COLUMN // 2])]
        mid_count = mid_array.count(PLAYER_MARK)
        score += mid_count*3

        #horizontal scoring positions
        for row in range(NUM_ROW):
            row_arr = [int(i) for i in list(board[row,:])]
            for col in range(NUM_COLUMN-3):
                win_arr = row_arr[col:col+WIN_LEN]
                score+=self.eval_value(win_arr,PLAYER_MARK)
        #vertical scoring positions
        for col in range(NUM_COLUMN):
            col_arr = [int(i) for i in list(board[:,col])]
            for row in range(NUM_ROW-3):
                win_arr = col_arr[row:row+WIN_LEN]
                score+=self.eval_value(win_arr,PLAYER_MARK)
        #second diagonal
        for row in range(NUM_ROW-3):
            for col in range(NUM_COLUMN-3):
                win_arr = [board[row-i+3][i+col] for i in range(WIN_LEN)]
                score += self.eval_value(win_arr,PLAYER_MARK)
        #first diagonal(primary)
        for row in range(NUM_ROW-3):
            for col in range(NUM_COLUMN-3):
                win_arr = [board[i+row][i+col] for i in range(WIN_LEN)]
                score += self.eval_value(win_arr,PLAYER_MARK)
        return score

    def eval_value(self,win_arr,PLAYER_MARK):
        score = 0
        enemy = HUMAN_MARK

        if PLAYER_MARK == HUMAN_MARK:
            enemy = COMPUTER_MARK


        if win_arr.count(PLAYER_MARK) == 4:
            score+=100
        elif win_arr.count(PLAYER_MARK) == 3 and win_arr.count(NULL) == 1:
            score+=10
        elif win_arr.count(PLAYER_MARK) == 2 and win_arr.count(NULL) == 2:
            score+=5
        if win_arr.count(enemy) == 3 and win_arr.count(NULL) == 1:
            score-=80

        return score

    def minimax(self,board,depth,alpha,beta,maximizing_player):
        val_loc = self.get_val_loc(board)
        isTerminal = self.is_terminal_node(board)

        if depth == 0 or isTerminal:
            if isTerminal:
                if self.check_winner_move(board,COMPUTER_MARK):
                    return (None,BIG_POSITIVE)
                elif self.check_winner_move(board,HUMAN_MARK):
                    return (None,BIG_NEGATIVE)
                else:
                    return (None,0)
            else:
                return (None,self.pos_score(board,COMPUTER_MARK))
        if maximizing_player:
            val = -math.inf
            column = random.choice(val_loc)
            for plc in val_loc:
                row =self.get_next_valid_row(board,plc)
                new_board = board.copy()
                self.drop_circle(new_board,row,plc,COMPUTER_MARK)
                new_score = self.minimax(new_board,depth-1,alpha,beta,False)[1]
                if new_score > val:
                    val = new_score
                    column = plc

                alpha = max(alpha,val)
                if alpha >= beta:
                    break
            return column,val
        else:
            val = -math.inf
            column = random.choice(val_loc)
            for plc in val_loc:
                row = self.get_next_valid_row(board,plc)
                new_board = board.copy()
                self.drop_circle(new_board,row,plc,HUMAN_MARK)
                new_score = self.minimax(new_board,depth-1,alpha,beta,True)[1]
                if new_score < val:
                    val = new_score
                    column = plc

                beta = min(beta,val)
                if alpha >= beta:
                    break
            return column,val












