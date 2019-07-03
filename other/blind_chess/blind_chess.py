two_kings_on_board = True

board = {
    "a1": ['WRa'],
    "a2": ['WPa'],
    "a3": [''],
    "a4": [''],
    "a5": [''],
    "a6": [''],
    "a7": ['BPa'],
    "a8": ['BRa'],
    "b1": ['WNa'],
    "b2": ['WPb'],
    "b3": [''],
    "b4": [''],
    "b5": [''],
    "b6": [''],
    "b7": ['BPb'],
    "b8": ['BNa'],
    "c1": ['WBa'],
    "c2": ['WPc'],
    "c3": [''],
    "c4": [''],
    "c5": [''],
    "c6": [''],
    "c7": ['BPc'],
    "c8": ['BBa'],
    "d1": ['WK'],
    "d2": ['WPd'],
    "d3": [''],
    "d4": [''],
    "d5": [''],
    "d6": [''],
    "d7": ['BPd'],
    "d8": ['BK'],
    "e1": ['WQ'],
    "e2": ['WPe'],
    "e3": [''],
    "e4": [''],
    "e5": [''],
    "e6": [''],
    "e7": ['BPe'],
    "e8": ['BQ'],
    "f1": ['WBb'],
    "f2": ['WPf'],
    "f3": [''],
    "f4": [''],
    "f5": [''],
    "f6": [''],
    "f7": ['BPf'],
    "f8": ['BBb'],
    "g1": ['WNb'],
    "g2": ['WPg'],
    "g3": [''],
    "g4": [''],
    "g5": [''],
    "g6": [''],
    "g7": ['BPg'],
    "g8": ['BNb'],
    "h1": ['WRb'],
    "h2": ['WPh'],
    "h3": [''],
    "h4": [''],
    "h5": [''],
    "h6": [''],
    "h7": ['BPh'],
    "h8": ['BRb']
}


def current_board():
    print(board['a8'], board['b8'], board['c8'], board['d8'], board['e8'], board['f8'], board['g8'], board['h8'])
    print(board['a7'], board['b7'], board['c7'], board['d7'], board['e7'], board['f7'], board['g7'], board['h7'])
    print(board['a6'], board['b6'], board['c6'], board['d6'], board['e6'], board['f6'], board['g6'], board['h6'])
    print(board['a5'], board['b5'], board['c5'], board['d5'], board['e5'], board['f5'], board['g5'], board['h5'])
    print(board['a4'], board['b4'], board['c4'], board['d4'], board['e4'], board['f4'], board['g4'], board['h4'])
    print(board['a3'], board['b3'], board['c3'], board['d3'], board['e3'], board['f3'], board['g3'], board['h3'])
    print(board['a2'], board['b2'], board['c2'], board['d2'], board['e2'], board['f2'], board['g2'], board['h2'])
    print(board['a1'], board['b1'], board['c1'], board['d1'], board['e1'], board['f1'], board['g1'], board['h1'])


while two_kings_on_board:
    if ((['WK'] in board.values()) & (['BK'] in board.values())):
        # moves are defined position to position (i.e.,user input = 'a2 a4')
        print('')
        print('')
        move_input = input('Make a move: ')
        # swap_keys = turns move_input into list (i.e., ['a2', 'a4'])
        swap_keys = move_input.split(' ')
        # Need to figure out how to define checkmate without actually taking the king's position
        #Move to unoccupied space
        if ((board[swap_keys[0]] != ['']) & (board[swap_keys[1]] == [''])):
            print('')
            print('')
            print('Before: ' + str(board[swap_keys[0]]) + str(board[swap_keys[1]]))
            x = board[swap_keys[0]]
            y = board[swap_keys[1]]
            board[swap_keys[0]] = y
            board[swap_keys[1]] = x
            print('')
            print('')
            print('After: ' + str(board[swap_keys[0]]) + str(board[swap_keys[1]]))
            print('')
            print('')
            current_board()
        #Moving to occupied space (take a piece off the board)
        elif ((board[swap_keys[0]] != ['']) & (board[swap_keys[1]] != [''])):
            #If spot1 and spot2 have pieces
            print('')
            print('')
            print('Before: ' + str(board[swap_keys[0]]) + str(board[swap_keys[1]]))
            x = board[swap_keys[0]]
            y = board[swap_keys[1]]
            board[swap_keys[0]] = ['']
            board[swap_keys[1]] = x
            print('')
            print('')
            print('After: ' + str(board[swap_keys[0]]) + str(board[swap_keys[1]]))
            print('')
            print('')
            print(str(x) + ' takes ' + str(y))
            print('')
            print('')
            current_board()
        else:
            print('')
            print('')
            print('Invalid Move')
            print('')
            print('')
            current_board()
    else:
        two_kings_on_board = False
        print('')
        print('')
        print('Checkmate!')
