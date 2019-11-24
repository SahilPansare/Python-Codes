from IPython.display import clear_output

def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker=input('Player 1, do you want X or O? ').upper()
    
    if marker=='X':
        return ('X','O')
    
    else:
        return ('O','X')

def place_marker(board, marker, position):
    
    board[position]=marker

def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or
        (board[4]==board[5]==board[6]==mark) or
        (board[7]==board[8]==board[9]==mark) or
        (board[1]==board[4]==board[7]==mark) or
        (board[2]==board[5]==board[8]==mark) or
        (board[3]==board[6]==board[9]==mark) or
        (board[1]==board[5]==board[9]==mark) or
        (board[3]==board[5]==board[7]==mark))

import random

def choose_first():
    
    if random.randint(0,1)==0:
        return 'Player 2'
        
    else:
        return 'Player 1'

def space_check(board, position):
    
    return board[position]==' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    return True

def player_choice(board):
    
    position=0
    while position not in range(1,10) or not space_check(board, position):
            
        position=int(input('Choose a position-'))
        
    return position

def replay():
    
    choice=input('Do you want to play again(Y/N)-')
    return choice=='Y'

print('Welcome to TIC TAC TOE!')

while True:

    my_board=[' ']*10
    player1_marker, player2_marker=player_input()
    turn=choose_first()
    print(turn +' will go first')

    play_game=input('Are you ready to play the game? (Y/N)')

    if play_game=='Y':
        game_on = True

    else:
        game_on = False

    while game_on:
        if turn=='Player 1':
            
            
            display_board(my_board)
            position=player_choice(my_board)
            place_marker(my_board, player1_marker, position)

            if win_check(my_board, player1_marker):
                display_board(my_board)
                print('Player 1 won the game')
                game_on=False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print('DRAW')
                    break

                else:
                    turn='Player 2'
        else:
            display_board(my_board)
            position=player_choice(my_board)
            place_marker(my_board, player2_marker, position)

            if win_check(my_board, player2_marker):
                display_board(my_board)
                print('Player 2 won the game')
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print('DRAW')

                else:
                    turn='Player 1'


    if not replay():
        break

