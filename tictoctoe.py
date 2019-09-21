# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:32:00 2019

@author: Stob
"""
import sys

board = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]

n = 9

def initBoard():
    #board = [['*', '*', '*'],
      #       ['*', '*', '*'],
       #      ['*', '*', '*']]
    print(board[0])
    print(board[1])
    print(board[2])
    
def printBoard():
    empty = [[],
             [],
             []]
    print(empty[0])
    print(empty[1])
    print(empty[2])
    
def boardfilled():
    print("Board is filled")
    return 0
#def isFilled():
 #   ctr = 0
  #  for a in (0,3):
   #     if board[a] == 'X' or 'O':
    #        ctr += 1
    #if ctr == 9:
     #   print("EMPTY")
    #else:
     #   winCheck()
    
def placePiece(board,row,col,piece):
    if board[row][col] == '*' and (row == 0 or row == 1 or row == 2) and ( col == 0 or col == 1 or col == 2) and (piece == 'X' or piece == 'O'):
        board[row][col] = piece
        winCheck(board,piece)
        return -1
    elif board[row][col] == 'X' or 'O':
        player1()
        return -1
        
def placePiece2(board,row,col,piece):
    if board[row][col] == '*' and (row == 0 or row == 1 or row == 2) and ( col == 0 or col == 1 or col == 2) and (piece == 'X' or piece == 'O'):
        board[row][col] = piece
        winCheck2(board,piece)
        return -1
    elif board[row][col] == 'X' or 'O':
        player2()
        return -1
    
def winCheck(board,piece):
    if board[0][0] == piece and board[0][1] == piece and board[0][2] == piece:
        print(piece, "win")
        return -1
    elif board[1][0] == piece and board[1][1] == piece and board[1][2] == piece:
        print(piece, "win")
        return -1
    elif board[2][0] == piece and board[2][1] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] == piece and board[1][0] == piece and board[2][0] == piece:
        print(piece, "win")
        return -1
    elif board[0][1] == piece and board[1][1] == piece and board[2][1] == piece:
        print(piece, "win")
        return -1
    elif board[0][2] == piece and board[1][2] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] != '*' and board[0][1] != '*' and board[0][2] != '*' and board[1][0] != '*' and board[1][1] != '*' and board[1][2] != '*' and board[2][0] != '*' and board[2][1] != '*' and board[2][2] != '*':
        boardfilled()
    else:
        player2()
        return -1
        
def winCheck2(board,piece):
    if board[0][0] == piece and board[0][1] == piece and board[0][2] == piece:
        print(piece, "win")
        return -1
    elif board[1][0] == piece and board[1][1] == piece and board[1][2] == piece:
        print(piece, "win")
        return -1
    elif board[2][0] == piece and board[2][1] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] == piece and board[1][0] == piece and board[2][0] == piece:
        print(piece, "win")
        return -1
    elif board[0][1] == piece and board[1][1] == piece and board[2][1] == piece:
        print(piece, "win")
        return -1
    elif board[0][2] == piece and board[1][2] == piece and board[2][2] == piece:
        print(piece, "win")
        return -1
    elif board[0][0] != '*' and board[0][1] != '*' and board[0][2] != '*' and board[1][0] != '*' and board[1][1] != '*' and board[1][2] != '*' and board[2][0] != '*' and board[2][1] != '*' and board[2][2] != '*':
        boardfilled()
    else:
        player1()
        return -1
        
def player1():
    print(board[0])
    print(board[1])
    print(board[2])
    print("X turn")
    x1 = int(input("ROW: "))
    y1 = int(input("COL: "))
    #piece = str(input("X or O case sensitive: "))
    #piece = 'X'
    if (x1 == 0 or x1 == 1 or x1 == 2) and (y1 == 0 or y1 == 1 or y1 == 2):
        placePiece(board,x1,y1,'X')
    else: 
        print("inv")
        player1()
    #isFilled()
    #winCheck(board,piece)
    

def player2():
    print(board[0])
    print(board[1])
    print(board[2])
    print("O turn")
    x1 = int(input("ROW: "))
    y1 = int(input("COL: "))
    #piece = 'O'
    if (x1 == 0 or x1 == 1 or x1 == 2) and (y1 == 0 or y1 == 1 or y1 == 2):
        placePiece2(board,x1,y1,'O')
    else: 
        print("inv")
        player2()
    #isFilled()
    #winCheck2(board,piece)
    
player1()
        
