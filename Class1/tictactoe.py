theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '1|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

theBoard = {'0': ' ', '1': ' ', '2': ' ',
                '3': ' ', '4': ' ', '5': ' ',
                '6': ' ', '7': ' ', '8': ' '}

def printBoard(board):
        print(board['0'] + '|' + board['1'] + '|' + board['2'])
        print('-+-+-')
        print(board['3'] + '|' + board['4'] + '|' + board['5'])
        print('-+-+-')
        print(board['6'] + '|' + board['7'] + '|' + board['8'])

import random
random.seed(2)

##random.



##pick an empty spot randomly for example in location 0-8
##pick x



##openspot=
turn ='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' +turn + '. Move on which space?')
    move=random.randint(0,8)
    theBoard[move]=turn
    if turn=='X':
        turn = 'O'
    else:
        turn = 'X'
        printBoard(theBoard)











pdb.set_trace()
positions = theBoard.values()
def get_empty_positions(board):
    return set([key if value ==' 'else'not-empty'for(key,value)in board.items()])-set(['not-empty'])
return[key for(key,value) in board.items() if value =='']

theBoard['top-R']='X'
    get_empty_positions()







