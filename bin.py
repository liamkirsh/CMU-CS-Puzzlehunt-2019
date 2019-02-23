import sys

"""
Given three equal length binary strings, this script finds a series of bit
shifts to the first two binary strings such that applying an AND, OR, or XOR
to them generates the third string. The script uses a brute force algorithm
to find a solution, if it exists, in no more than the number of operations
specified. Each bit shift qualifies as an operation.

Syntax: <max-operations> <x> <y> <z>
"""

debug = 0

def main():
    inp = raw_input()
    tokz = inp.split()
    m = int(tokz[0])
    x = [int(t) for t in tokz[1]]
    y = [int(t) for t in tokz[2]]
    z = [int(t) for t in tokz[3]]
    if debug: print m, x, y, z
    try_to_solve(x, y, z, m, [])

def lshift(lst):
    cpy = list(lst)
    cpy.append(0)
    return cpy[1:]

def rshift(lst):
    cpy = list(lst)
    cpy = cpy[:-1]
    cpy = [0] + cpy
    return cpy

def do_and(x, y):
    return [a and b for a, b in zip(x, y)]

def do_or(x, y):
    return [a or b for a, b in zip(x, y)]

def do_xor(x, y):
    return [a ^ b for a, b in zip(x, y)]

def try_to_solve(x, y, z, moves_remaining, ops):
    if not cmp(do_and(x, y), z):
        print "Success"
        print ops + ["and"]
        sys.exit(0)
    elif not cmp(do_or(x, y), z):
        print "Success"
        print ops + ["or"]
        sys.exit(0)
    elif not cmp(do_xor(x, y), z):
        print "Success"
        print ops + ["xor"]
        sys.exit(0)
    
    if debug: print "x",x,"\ny",y
    if debug: print "moves remaining", moves_remaining
    if moves_remaining == 0:
        return

    # try shifting x
    if debug: print "left shift x"
    try_to_solve(lshift(x), y, z, moves_remaining - 1, ops + ["lshift x"])

    if debug: print "right shift x"
    try_to_solve(rshift(x), y, z, moves_remaining - 1, ops + ["rshift x"])

    if debug: print "left shift y"
    try_to_solve(x, lshift(y), z, moves_remaining - 1, ops + ["lshift y"])

    if debug: print "right shift y"
    try_to_solve(x, rshift(y), z, moves_remaining - 1, ops + ["rshift y"])
    
main()
