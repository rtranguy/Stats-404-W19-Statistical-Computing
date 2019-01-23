theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def win(theBoard):
    # X Diagonals (4)
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        return True
    elif theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    # X Rows
    elif theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        return True
    elif theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
        return True
    elif theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    # X Columns
    elif theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X':
        return True
    elif theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X':
        return True
    elif theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
        return True
    # O Diagonals (4)
    if theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O':
        return True
    elif theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O':
        return True
    # O Rows (3)
    elif theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O':
        return True
    elif theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O':
        return True
    elif theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O':
        return True
    # O Columns (3)
    elif theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O':
        return True
    elif theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O':
        return True
    elif theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O':
        return True
    else:
        return False
import random
def tictactoe():
    print(theBoard)
    play = list(theBoard.keys())
    #random.shuffle(play)
    print(random.shuffle(play))
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        theBoard[play[i]] = turn
        if win(theBoard):
            print('' +turn+ ' won! ')
        else:
            print('Tie!')
        if turn=='X':
            turn='O'
        else:
            turn='X'
    printBoard(theBoard)
tictactoe()
