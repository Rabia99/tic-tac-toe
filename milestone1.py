# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:02:04 2019

@author: HP
"""

#2 players should be able to play the game..
#board should be printed every time a player makes a move...
#able to accept the input of player position and then place a symbol on the board....


#............STEP1.............#

# func that print a board
from IPython.display import clear_output
def display_board(board):
    print('  |  |')
    print(' '+ board[7]+'|'+board[8]+'|'+board[9])
    print('  |  |')
    print('---------')
    print('  |  |')
    print(' '+ board[4]+'|'+board[5]+'|'+board[6])
    print('  |  |')
    print('---------')
    print('  |  |')
    print(' '+ board[1]+'|'+board[2]+'|'+board[3])
    print('  |  |')
test_board=['#','X','O','X','O','X','O','X','O','X']   
display_board(test_board)  
            
#................STEP2................#

# func that can take in player input  and assign their marker as 'X' or 'O'.
def player_input():
    marker= ''
    while not(marker=='X' or marker=='O'):
        marker=input('player1:Do you want to be X or O?').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
player_input()    

#...............STEP3...........#

#func that takes in board list object,a marker('X'or'O'),and a desired position(no 1-9)and assigns it to the board
def place_marker(board,marker,position):
    board[position]=marker
place_marker(test_board,'$',8)
display_board(test_board)

#.................STEP4...........#

#func that takes in board and checls who won
def win_check(board,marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or
    (board[4]==marker and board[5]==marker and board[6]==marker) or
    (board[1]==marker and board[2]==marker and board[3]==marker) or
    (board[7]==marker and board[4]==marker and board[1]==marker) or
    (board[8]==marker and board[5]==marker and board[2]==marker) or
    (board[9]==marker and board[6]==marker and board[3]==marker) or
    (board[7]==marker and board[5]==marker and board[3]==marker) or
    (board[9]==marker and board[5]==marker and board[1]==marker)) 
    
win_check(test_board,'X')    

#................STEP5.....................#

#func that randomly decide which player got 1st
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return 'player1'
    

#.....................STEP6.....................#
        
#func that returns boolean that space on the board is easily available
def space_check(board,position):
    return board[position]==' '

#...................STEP7.................#
    
#func that checks if board is full and returns boolean..true if full
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True

#...................STEP8...............#

#func that asks for players next position and then uses func from step 6 to check if its a
#free position...if it is return the position for later use
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose ur nxt position:(1-9)'))
    return position


#......................STEP9.....................#
    
#func that asks user if they wants to play again and return a boolean true if they wants tonplay again
def replay():
    return input('Do you want to play again? enter yes or no:').lower().startswith('y')


#............................STEP10......................#
    
#use while loops n funcs yu've made to run game
print('welcome to tic tac toe game!!')
while True:
    #reset the board
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+'will go 1st!!')
    play_game=input('are u ready to play? enter yes or no.')
    
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn=='Player1':
            #player1's turn
            
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('congo!!!...you won the game!!!!')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('the game is a draw')
                    break
                else:
                    turn='player2'
                   
        else:
            #player2's turn
             display_board(theBoard)
             position=player_choice(theBoard)
             place_marker(theBoard,player2_marker,position)
            
             if win_check(theBoard,player2_marker):
                 display_board(theBoard)
                 print('congo!!!...player2 has won the game!!!!')
                 game_on=False
             else:
                 if full_board_check(theBoard):
                     display_board(theBoard)
                     print('the game is a draw')
                     break
                 else:
                     turn='player1'
                     
    if not replay():
        break
                     
                     
                     
           
             
                    
                
                

    
      
        
    
        
  

    

        
    
    
    
    
    

            
    
