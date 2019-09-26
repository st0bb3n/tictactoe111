# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:02:05 2019

@author: Steven Kyle Y Esguerra SN: 201905959
@author2: Ivan Patrick Frondozo SN: 201907500
"""

import sys

'''
Main board, global
'''
board = [['|_|', '|_|', '|_|'], #Global board, updating
         ['|_|', '|_|', '|_|'],
         ['|_|', '|_|', '|_|']]

'''
Main menu function
'''
def main(): #main menu
    print('1 - Play')
    print('2 - Show empty board with coordinates')
    print('')
    print('3 - Exit')
    print('')

    selector = int(input(''))

    if selector == 1:
        player1()
    elif selector == 2:
        printBoard()
    elif selector == 3:
        print("Exiting")
        sys.exit(0)
    else:
        print("Invalid")
        main()

'''
Prints empty board
'''
def initBoard(): #initializes board
    print('------------')
    print(*board[0], sep='')
    print(*board[1], sep='')
    print(*board[2], sep='')
    print('------------')
    
'''
Prints the board with corresponding coordinate
'''    
def printBoard(): #intializes empty board
    empty = [['00', '01', '02'], #empty board with coordinates
            ['10', '11', '12'],
            ['20', '21', '22']]
    print(empty[0])
    print(empty[1])
    print(empty[2])
    print('')
    main()
       
'''
Runs of board is filled
'''    
def boardfilled(): #checker for board content
    print('------------')
    print(*board[0], sep='')
    print(*board[1], sep='')
    print(*board[2], sep='')
    print('------------')
    print("Board is filled")
    return 0
    
'''
Place piece function, dedicated to player 1
'''
def placePiece(board,row,col,piece): #placepiece for player 1
    if board[row][col] == '|_|' and (row == 0 or row == 1 or row == 2) and ( col == 0 or col == 1 or col == 2) and (piece == '|X|' or piece == '|O|'):
        board[row][col] = piece
        winCheck(board,piece)
        return 0
    elif board[row][col] == '|X|' or '|O|':
        player1()
        return -1
        
'''
Place piece function, dedicated to player 2
''' 
def placePiece2(board,row,col,piece): #placepiece for player 2
    if board[row][col] == '|_|' and (row == 0 or row == 1 or row == 2) and ( col == 0 or col == 1 or col == 2) and (piece == '|X|' or piece == '|O|'):
        board[row][col] = piece
        winCheck2(board,piece)
        return -1
    elif board[row][col] == '|X|' or '|O|':
        player2()
        return -1
    
'''
Win conditions function, dedicated to player 1
'''    
def winCheck(board,piece): #win conditions for player 1
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
    elif board[0][0] != '|_|' and board[0][1] != '|_|' and board[0][2] != '|_|' and board[1][0] != '|_|' and board[1][1] != '|_|' and board[1][2] != '|_|' and board[2][0] != '|_|' and board[2][1] != '|_|' and board[2][2] != '|_|':
        boardfilled()
    else:
        player2()
        return -1
        
'''
Win conditions function, dedicated to player 2
'''       
def winCheck2(board,piece): #winconditions for player 2
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
    elif board[0][0] != '|_|' and board[0][1] != '|_|' and board[0][2] != '|_|' and board[1][0] != '|_|' and board[1][1] != '|_|' and board[1][2] != '|_|' and board[2][0] != '|_|' and board[2][1] != '|_|' and board[2][2] != '|_|':
        boardfilled()
    else:
        player1()
        return -1
        
'''
Player 1 flow 
'''    
def player1(): #player 1 algo
    print('------------')
    print(*board[0], sep='')
    print(*board[1], sep='')
    print(*board[2], sep='')
    print('------------')
    print("X turn")
    x1 = int(input("ROW: "))
    y1 = int(input("COL: "))
    #piece = str(input("X or O case sensitive: "))
    #piece = 'X'
    if (x1 == 0 or x1 == 1 or x1 == 2) and (y1 == 0 or y1 == 1 or y1 == 2):
        placePiece(board,x1,y1,'|X|')
    else: 
        print("Invalid, place a piece again")
        player1()
    #isFilled()
    #winCheck(board,piece)
    
'''
Player 2 flow
'''
def player2(): #player 2 algo
    print('------------')
    print(*board[0], sep='')
    print(*board[1], sep='')
    print(*board[2], sep='')
    print('------------')
    print("O turn")
    x1 = int(input("ROW: "))
    y1 = int(input("COL: "))
    #piece = 'O'
    if (x1 == 0 or x1 == 1 or x1 == 2) and (y1 == 0 or y1 == 1 or y1 == 2):
        placePiece2(board,x1,y1,'|O|')
    else: 
        print("Invalid, place a piece again")
        player2()
    #isFilled()
    #winCheck2(board,piece)


if __name__ == "__main__": #pycharm runs it if this was set xdddddd
    main()

