#!/usr/bin/python36 -tt

import sys
import random

def display_board(board):
    print('TIC-TAC-TOE\n')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('---|---|---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('---|---|---')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' \n')


def new_board():
    test_board = [' '] * 10
    display_board(test_board)
    return test_board

def place_marker(board, mark, position):
    board[position] = mark
    display_board(board)

def win_check(board,mark):
    win_combos = [(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,5,7),(3,6,9),(4,5,6),(7,8,9)]
    for k in win_combos:
       if board[k[0]] == board[k[1]] == board[k[2]] == mark:
           return True
    return False

def chose_first():
    player = random.randint(1,2)
    print('Random Player Selection ---\n')
    print('Player {} will go first!'.format(player))
    return player

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        print('This place is already taken Please enter new position\n')
        return False

def full_board_check(board):
    if not ' ' in board:
        return True
    else:
        return False

def player_choice(board,player):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        try:
            position =  int(input('Player {} Please assign the position b/w 1 to 9\n'.format(player)))
        except:
            print('Please enter valid input b/w 1 to 9\n')
    return position

def replay():
    choice = input('Press y to play again and n for exit\n')
    if choice == 'y':
        return True
    return False

def player_input():
    mark = [' ']*3
    mark[1] = input('Player 1 Please pick a mark x or o\n')
    if mark[1] == 'x':
        mark[2] = 'o'
    elif mark[1] == 'o':
        mark[2] = 'x'
    else:
        print('{} is not a valid input please run again and enter either x or o\n'.format(mark[1]))
        exit(0)
    print('Player 1 mark is {} and Player 2 mark is {}\n'.format(mark[1],mark[2]))
    return mark

def main():
    board = new_board()
    mark = player_input()
    player = chose_first()
    while True:
        if full_board_check(board):
            if replay():
                board = new_board()
                player = chose_first()
                continue
            break
        position = player_choice(board,player)
        place_marker(board, mark[player], position)
        if win_check(board,mark[player]):
            print ('Player {} Won The Game!!!!\n'.format(player))
            if replay():
                board = new_board()
                player = chose_first()
                continue
            else:
                break
        if player == 1:
            player = 2
        else:
            player = 1

if __name__ == "__main__":
    main()
