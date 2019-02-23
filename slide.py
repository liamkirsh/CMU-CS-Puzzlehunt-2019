import sys

"""
Given a 3x3 sliding puzzle consisting of 0s, 1s, and one empty space, this
script finds the series of movements necessary so that all four corners of the 
puzzle are either 0s or 1s. The script uses a brute force algorithm to find a
solution, if it exists, in no more than the number of operations specified. Each movement qualifies as one operation.

Syntax: <max-operations> <puzzle>
Dots are used to indicate an empty space, e.g.:
7 1 0 1 1 . 0 1 0 0
== is equivalent to ==
[ 1 0 1 ]
[ 1 . 0 ]
[ 1 0 0 ]
"""

debug = 0

def main():
    puzzle = raw_input()
    puzzle = puzzle.split()
    m = int(puzzle[0])
    puzzle = puzzle[1:]
    print "max", m
    try_to_solve(puzzle, 0, m, -1, [])

def print_puzzle(puzzle):
    print puzzle[0:3]
    print puzzle[3:6]
    print puzzle[6:9]

def try_to_solve(puzzle, cnt, m, prev_move, moves_lst):
    if debug: print "cnt", cnt, "max", m

    if cnt > m:
        if debug: print "count > max"
        return
    if winner(puzzle):
        print "winner"
        print '\n'.join(moves_lst)
        sys.exit(0)

    d_ndx = puzzle.index('.')

    moves = possible_moves(d_ndx)
    if debug: print "possible moves", moves
    for p in moves:
        if p == prev_move: continue
        if debug: print ("moving ndx" + p + "to ndx" + d_ndx)
        new_puzzle = list(puzzle)
        new_puzzle[d_ndx] = new_puzzle[p]
        new_puzzle[p] = '.'
        try_to_solve(new_puzzle, cnt+1, m, d_ndx, moves_lst + [("move ndx " + str(p) + " to ndx " + str(d_ndx))])

def winner(lst):
    return (lst[0] == lst[2] and
            lst[0] == lst[6] and
            lst[0] == lst[8])

def possible_moves(ndx):
    result = []
    lft = ndx - 1
    rt = ndx + 1
    down = ndx + 3
    up = ndx - 3
    if lft >= 0 and lft not in (2,5,8):
        result.append(lft)
    if rt <= 8 and rt not in (0,3,6):
        result.append(rt)
    if down <= 8:
        result.append(down)
    if up >= 0:
        result.append(up)
    return result

main()
