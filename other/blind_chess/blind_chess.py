# Early notes:

"""
Define game
    https://en.wikipedia.org/wiki/Chess_notation
    https://en.wikipedia.org/wiki/Blindfold_chess
    define pieces
        define available moves for each piece
    define board boundary
        board is 8x8 (64 squares)
    randomize movement
    define current positions
        describe the current board locations for all remaining pieces
            describe them from top-left to bottom-right
    English	K king	Q queen	R rook, castle	B bishop	N knight	(P) pawn	Chess	Check	Checkmate/Mate
  



#Only used to make the board (not really reusable)
def board_dict_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for letter in letters:
        x = 1
        while x < 9:
            print ("\"" + letter + str(x) + "\"" + ":0,")
            x+=1
            
            
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = 9

while y > 1:
    y-=1
    for x in letters:
        print ('(board['+'\''+x+str(y)+'\'])')
"""


board = {
"a1":['WRa'],
"a2":['WPa'],
"a3":[''],
"a4":[''],
"a5":[''],
"a6":[''],
"a7":['BPa'],
"a8":['BRa'],
"b1":['WNa'],
"b2":['WPb'],
"b3":[''],
"b4":[''],
"b5":[''],
"b6":[''],
"b7":['BPb'],
"b8":['BNa'],
"c1":['WBa'],
"c2":['WPc'],
"c3":[''],
"c4":[''],
"c5":[''],
"c6":[''],
"c7":['BPc'],
"c8":['BBa'],
"d1":['WK'],
"d2":['WPd'],
"d3":[''],
"d4":[''],
"d5":[''],
"d6":[''],
"d7":['BPd'],
"d8":['BK'],
"e1":['WQ'],
"e2":['WPe'],
"e3":[''],
"e4":[''],
"e5":[''],
"e6":[''],
"e7":['BPe'],
"e8":['BQ'],
"f1":['WBb'],
"f2":['WPf'],
"f3":[''],
"f4":[''],
"f5":[''],
"f6":[''],
"f7":['BPf'],
"f8":['BBb'],
"g1":['WNb'],
"g2":['WPg'],
"g3":[''],
"g4":[''],
"g5":[''],
"g6":[''],
"g7":['BPg'],
"g8":['BNb'],
"h1":['WRb'],
"h2":['WPh'],
"h3":[''],
"h4":[''],
"h5":[''],
"h6":[''],
"h7":['BPh'],
"h8":['BRb']
}





K = king
Q = queen
R = rook
B = bishop
N = knight
x = captures
+ = check
++ = checkmate
O-O = Castles King's side

intial_board = """
['BRa']['BNa']['BBa']['BK']['BQ']['BBb']['BNb']['BRb']
['BPa']['BPb']['BPc']['BPd']['BPe']['BPf']['BPg']['BPh']
['']['']['']['']['']['']['']['']
['']['']['']['']['']['']['']['']
['']['']['']['']['']['']['']['']
['']['']['']['']['']['']['']['']
['WPa']['WPb']['WPc']['WPd']['WPe']['WPf']['WPg']['WPh']
['WRa']['WNa']['WBa']['WK']['WQ']['WBb']['WNb']['WRb']
"""



accepted action is:
    position1 to position2
        so if a position1 has a piece and can legally move to position2, move/replace/swap piece 


def whose_turn():
    player1 = True
    player2 = False
    #swap boolean at the end of turn

def current_board():
    print(board['a8'],board['b8'],board['c8'],board['d8'],board['e8'],board['f8'],board['g8'],board['h8'])
    print(board['a7'],board['b7'],board['c7'],board['d7'],board['e7'],board['f7'],board['g7'],board['h7'])
    print(board['a6'],board['b6'],board['c6'],board['d6'],board['e6'],board['f6'],board['g6'],board['h6'])
    print(board['a5'],board['b5'],board['c5'],board['d5'],board['e5'],board['f5'],board['g5'],board['h5'])
    print(board['a4'],board['b4'],board['c4'],board['d4'],board['e4'],board['f4'],board['g4'],board['h4'])
    print(board['a3'],board['b3'],board['c3'],board['d3'],board['e3'],board['f3'],board['g3'],board['h3'])
    print(board['a2'],board['b2'],board['c2'],board['d2'],board['e2'],board['f2'],board['g2'],board['h2'])
    print(board['a1'],board['b1'],board['c1'],board['d1'],board['e1'],board['f1'],board['g1'],board['h1'])


def legal_move():
    If key/position exists in board/dictionary
        
    

def move_piece():
    moving a piece is swapping the value of one key for another
    how do you move a value to a diff key?
        "WPd to d4" = remove WPd from it's current key and put it into the dest key
        Blindfold for me = memorize positions and play based on those only 

def capture_piece():
    if key contains piece and is replaced:
        print (replacement piece + "takes " + current piece)
        
def castling():
    




        





        
