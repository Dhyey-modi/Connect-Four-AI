import numpy as np
import random
import math
from Connect_Four import *

C1 = Connect_Four()
board = C1.create_board()
C1.print_board(board)

Game_Over = False
turn = 0
turn = random.randint(HUMAN,COMPUTER)
while not Game_Over:
    if turn == HUMAN:
        col = int(input("Enter the column you want:- "))

        if C1.is_val_loc(board,col):
            row = C1.get_next_valid_row(board,col)
            C1.drop_circle(board,row,col,HUMAN_MARK)

        if C1.check_winner_move(board,HUMAN_MARK):
            print("Player wins against AI")
            Game_Over = True
        turn += 1
        turn = turn % 2
        C1.print_board(board)

    if turn == COMPUTER and not Game_Over:
        col,minimax_val = C1.minimax(board,5,-math.inf,math.inf,True)
        if C1.is_val_loc(board,col):
            row = C1.get_next_valid_row(board,col)
            C1.drop_circle(board,row,col,COMPUTER_MARK)

            if C1.check_winner_move(board,COMPUTER_MARK):
                print("AI wins against the player")
                Game_Over = True
            C1.print_board(board)
            turn+=1
            turn=turn%2



