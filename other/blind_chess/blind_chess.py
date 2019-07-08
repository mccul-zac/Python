two_kings_on_board = True

board = {
    "a1": ['WRa'],
    "a2": ['WPa'],
    "a3": ['   '],
    "a4": ['   '],
    "a5": ['   '],
    "a6": ['   '],
    "a7": ['BPa'],
    "a8": ['BRa'],
    "b1": ['WNa'],
    "b2": ['WPb'],
    "b3": ['   '],
    "b4": ['   '],
    "b5": ['   '],
    "b6": ['   '],
    "b7": ['BPb'],
    "b8": ['BNa'],
    "c1": ['WBa'],
    "c2": ['WPc'],
    "c3": ['   '],
    "c4": ['   '],
    "c5": ['   '],
    "c6": ['   '],
    "c7": ['BPc'],
    "c8": ['BBa'],
    "d1": ['WK-'],
    "d2": ['WPd'],
    "d3": ['   '],
    "d4": ['   '],
    "d5": ['   '],
    "d6": ['   '],
    "d7": ['BPd'],
    "d8": ['BK-'],
    "e1": ['WQ-'],
    "e2": ['WPe'],
    "e3": ['   '],
    "e4": ['   '],
    "e5": ['   '],
    "e6": ['   '],
    "e7": ['BPe'],
    "e8": ['BQ-'],
    "f1": ['WBb'],
    "f2": ['WPf'],
    "f3": ['   '],
    "f4": ['   '],
    "f5": ['   '],
    "f6": ['   '],
    "f7": ['BPf'],
    "f8": ['BBb'],
    "g1": ['WNb'],
    "g2": ['WPg'],
    "g3": ['   '],
    "g4": ['   '],
    "g5": ['   '],
    "g6": ['   '],
    "g7": ['BPg'],
    "g8": ['BNb'],
    "h1": ['WRb'],
    "h2": ['WPh'],
    "h3": ['   '],
    "h4": ['   '],
    "h5": ['   '],
    "h6": ['   '],
    "h7": ['BPh'],
    "h8": ['BRb']
}


def current_board():
    print('          [ A-8 ][ B-8 ][ C-8 ][ D-8 ][ E-8 ][ F-8 ][ G-8 ][ H-8 ]')
    print('             -      -      -      -      -      -      -      -   ')
    print('[ A-8 ] - ' + str(board['a8']) + "" + str(board['b8']) + "" + str(board['c8']) + "" + str(board['d8']) + "" + str(board['e8']) + "" + str(board['f8']) + "" + str(board['g8']) + "" + str(board['h8']))
    print('[ A-7 ] - ' + str(board['a7']) + "" + str(board['b7']) + "" + str(board['c7']) + "" + str(board['d7']) + "" + str(board['e7']) + "" + str(board['f7']) + "" + str(board['g7']) + "" + str(board['h7']))
    print('[ A-6 ] - ' + str(board['a6']) + "" + str(board['b6']) + "" + str(board['c6']) + "" + str(board['d6']) + "" + str(board['e6']) + "" + str(board['f6']) + "" + str(board['g6']) + "" + str(board['h6']))
    print('[ A-5 ] - ' + str(board['a5']) + "" + str(board['b5']) + "" + str(board['c5']) + "" + str(board['d5']) + "" + str(board['e5']) + "" + str(board['f5']) + "" + str(board['g5']) + "" + str(board['h5']))
    print('[ A-4 ] - ' + str(board['a4']) + "" + str(board['b4']) + "" + str(board['c4']) + "" + str(board['d4']) + "" + str(board['e4']) + "" + str(board['f4']) + "" + str(board['g4']) + "" + str(board['h4']))
    print('[ A-3 ] - ' + str(board['a3']) + "" + str(board['b3']) + "" + str(board['c3']) + "" + str(board['d3']) + "" + str(board['e3']) + "" + str(board['f3']) + "" + str(board['g3']) + "" + str(board['h3']))
    print('[ A-2 ] - ' + str(board['a2']) + "" + str(board['b2']) + "" + str(board['c2']) + "" + str(board['d2']) + "" + str(board['e2']) + "" + str(board['f2']) + "" + str(board['g2']) + "" + str(board['h2']))
    print('[ A-1 ] - ' + str(board['a1']) + "" + str(board['b1']) + "" + str(board['c1']) + "" + str(board['d1']) + "" + str(board['e1']) + "" + str(board['f1']) + "" + str(board['g1']) + "" + str(board['h1']))


while two_kings_on_board:
    if ((['WK-'] in board.values()) & (['BK-'] in board.values())):
        # moves are defined position to position (i.e.,user input = 'a2 a4')
        print('')
        print('')
        move_input = input('Make a move: ')
        # swap_keys = turns move_input into list (i.e., ['a2', 'a4'])
        swap_keys = move_input.split(' ')
        # Need to figure out how to define checkmate without actually taking the king's position
        #Move to unoccupied space
        if ((board[swap_keys[0]] != ['   ']) & (board[swap_keys[1]] == ['   '])):
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
        elif ((board[swap_keys[0]] != ['   ']) & (board[swap_keys[1]] != ['   '])):
            #If spot1 and spot2 have pieces
            print('')
            print('')
            print('Before: ' + str(board[swap_keys[0]]) + str(board[swap_keys[1]]))
            x = board[swap_keys[0]]
            y = board[swap_keys[1]]
            board[swap_keys[0]] = ['   ']
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




