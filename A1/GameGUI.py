import numpy as np
import random
import math
import pygame
import sys
from Connect_Four import *

SQUARE = 100
MAX_DEPTH = 6 #DEPTH YOU WANT AI TO EXPLORE

class GUI:
    def __init__(self):
        pygame.init()
        self.screen_width = NUM_COLUMN*SQUARE
        self.screen_height = (NUM_ROW+1)*SQUARE
        self.screen_size = (self.screen_width,self.screen_height)
        self.Radius = int(SQUARE/2 - 4)

    def get_event(self):
        return pygame.event.get()
    def update(self):
        pygame.display.update()
    def quit(self,event):
        if event.type == pygame.QUIT:
            sys.exit()
    def get_size(self):
        return self.screen_size
    def get_radius(self):
        return self.Radius
    def get_height(self):
        return self.screen_height
    def get_width(self):
        return self.screen_width
    def wait(self):
        pygame.time.wait(5000)

    def draw_circle(self,game_screen,pos_x):
        pygame.draw.circle(game_screen,COLOUR_RED,(pos_x,int(SQUARE/2 -1)),self.Radius)

    def draw_rect(self, screen):
        pygame.draw.rect(screen, COLOUR_BLACK, (0, 0, self.screen_width, SQUARE))
    def get_font(self):
        return pygame.font.SysFont("monospace", 75)

    def draw_board(self,board):


        for c in range(NUM_COLUMN):
            for r in range(NUM_ROW):
                pygame.draw.rect(game_screen, COLOUR_BLUE,
                                 (c * SQUARE, r * SQUARE + SQUARE, SQUARE, SQUARE))
                pygame.draw.circle(game_screen, COLOUR_BLACK, (
                    int(c * SQUARE + SQUARE / 2), int(r * SQUARE + SQUARE + SQUARE / 2)),
                                   self.Radius)

        for c in range(NUM_COLUMN):
            for r in range(NUM_ROW):
                if board[r][c] == HUMAN_MARK:
                    pygame.draw.circle(game_screen, COLOUR_RED, (
                        int(c * SQUARE + SQUARE / 2), self.screen_height - int(r * SQUARE + SQUARE / 2)),
                                       self.Radius)
                elif board[r][c] == COMPUTER_MARK:
                    pygame.draw.circle(game_screen, COLOUR_GREEN, (
                        int(c * SQUARE + SQUARE / 2), self.screen_height - int(r * SQUARE + SQUARE / 2)),
                                       self.Radius)
        self.update()


C1 = Connect_Four()
board = C1.create_board()
C1.print_board(board)

Game_Over = False
turn = 0

G1 = GUI()

game_screen = pygame.display.set_mode(G1.get_size())
G1.draw_board(board)
G1.update()

font = G1.get_font()

turn =  random.randint(HUMAN,COMPUTER)


while not Game_Over:
    for event in G1.get_event():
        G1.quit(event)
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(game_screen,COLOUR_BLACK,(0,0,G1.get_width(),SQUARE))
            pos_x = event.pos[0]
            if turn == HUMAN:
                G1.draw_circle(game_screen,pos_x)
        G1.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            G1.draw_rect(game_screen)
            if turn == HUMAN:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x/SQUARE))

            if C1.is_val_loc(board,col):
                row = C1.get_next_valid_row(board,col)
                C1.drop_circle(board,row,col,HUMAN_MARK)

                if C1.check_winner_move(board, HUMAN_MARK):
                    label = font.render("Player 1 Wins !!", 1, COLOUR_RED)
                    game_screen.blit(label, (40, 10))
                    Game_Over = True

                turn += 1
                turn = turn % 2
                C1.print_board(board)
                G1.draw_board(board)

    if turn == COMPUTER and not Game_Over:
        col,min_max_score = C1.minimax(board,MAX_DEPTH,-math.inf,math.inf,True)
        if C1.is_val_loc(board,col):
            row = C1.get_next_valid_row(board,col)
            C1.drop_circle(board,row,col,COMPUTER_MARK)


            if C1.check_winner_move(board,COMPUTER_MARK):
                label = font.render("Computer Wins",1,COLOUR_BLUE)
                game_screen.blit(label,(40,10))
                Game_Over = True

            C1.print_board(board)
            G1.draw_board(board)
            turn+=1
            turn = turn % 2

    if Game_Over:
        G1.wait()



