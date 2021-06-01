
# Got help from www.youtube.com/watch?v=5s_IGC2sxwQ
board = [ " " for x in range(10)]


def insertLetter(letter,pos):
    board[pos] = letter


def printBoard(board):
    print('  |  ')
    print(' ' + board[1] + ' | ' + board[2] + '  |  ' + board[3])
    print("-------------------")
    print('  |  ')
    print(' ' + board[4] + ' | ' + board[5] + '  |  ' + board[6])
    print('  |  ')
    print("-------------------")
    print(' ' + board[7] + ' | ' + board[8] + '  |  ' + board[9])


def winner(x,y):
    """
    How to tell if someone won
    """
    return (x[1] == y and x[2] == y and x[3] == y) or (x[1] == y and x[4] == y and x[7] == y)

