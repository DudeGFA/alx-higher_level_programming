#!/usr/bin/python3
# Author - God'sfavour Idowu-Agida

import sys
queen_positions = []
x, y, l = 0, 0, 1
def divi(list1, list2):
    if list1[0]/list1[1] == list2[0]/list2[1]:
        return True
    return False
def check_col(queen_positions, l):
    if l == 0:
        return False
    for position in queen_positions:
            if queen_positions[l][1] == position[1] or divi(queen_positions[l], position):
                if queen_positions[l][1] == int(sys.argv[1]) - 1:
                    queen_positions[l - 1][1] += 1
                    check_col(queen_positions, l - 1)
                queen_positions[l][1] += 1
                check_col(queen_positions, l)
    return True
def place_queen(queen_positions, l):
    while l < int(sys.argv[1]):
        if check_col(queen_positions, l) == True:
            l += 1
            if l + 1 == int(sys.argv[1]):
                print(queen_positions)
            continue
        else:
            return

for i in range(int(sys.argv[1])):
    queen_positions.append([i, 0])

for i in range(1, int(sys.argv[1])):
    queen_positions[0][1] = i
    l = 1
    place_queen(queen_positions, l)
