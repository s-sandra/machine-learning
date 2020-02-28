"""
The flatten function takes a list (which may contain lists of lists of lists …) and puts all items
into a single list on the same level.
"""
def flatten(nested):
    # return when list element is not a list
    if not isinstance(nested, list):
        return [nested]

    # start with empty list and concatenate list of flattened 
    # sublists together
    return sum([flatten(sublist) for sublist in nested], [])

"""
Outputs the set of all possible subsets of the inputted list.
"""
def powerset(elements):
    powerset = [[]]  # powerset always contains empty set

    for element in elements:
        # add current element to each subset in current powerset and
        # concatenate the result to current powerset
        powerset += [[element] + subset for subset in powerset]

    return powerset

"""
Generates all possible permutations of a list
"""
def all_perms(elements):

    perms = []

    if len(elements) == 1:
        return elements

    # for each element in list, swap with each
    # other element in list
    for x in range(len(elements)):
        for y in range(len(elements)):

            # don't swap with itself
            if y != x:
                elements[y], elements[x] = elements[x], elements[y]

                # freeze the first element and concatenate it to
                # permutations of rest of list
                perms += [flatten([elements[0]] + [z]) for z in all_perms(elements[1:])
                          if flatten([elements[0]] + [z]) not in perms]  # duplicates occur
    return perms

import numpy as np
import re

"""
:arg1: n - an integer greater than 0
:arg2: end_corner - one of the corners of the square (1, 2, 3 or 4)

Prints a matrix, with 0 in the center, that increments in a
clockwise spiral, with n in the passed end_corner.
"""
def number_spiral(n, end_corner):
    if n == 0:
        print("0")
        return
    if n < 0:
        return

    matrix = np.full(shape=(n, n), fill_value=-1)
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3
    directions = [LEFT, DOWN, RIGHT, UP]

    # set starting position and direction
    if end_corner == 1:
        row = 0
        col = 0
        direction = DOWN
    elif end_corner == 2:
        row = 0
        col = n - 1
        direction = LEFT
    elif end_corner == 3:
        row = n - 1
        col = 0
        direction = RIGHT
    else:
        row = n - 1
        col = n - 1
        direction = UP

    def out_of_range(r, c):
        if r == -1 or c == -1:
            return True
        if r == n or c == n:
            return True
        return False

    def valid_cell(r, c):
        return not out_of_range(r, c) and matrix[r][c] == -1

    # change current row and col to go in current direction
    def go(r, c):
        if direction == RIGHT:
            c += 1
        elif direction == LEFT:
            c -= 1
        elif direction == UP:
            r -= 1
        elif direction == DOWN:
            r += 1

        return r, c

    count = n ** 2 - 1
    matrix[row][col] = count
    count -= 1

    while count >= 0:

        test_row, test_col = go(row, col)
        if valid_cell(test_row, test_col):
            row, col = test_row, test_col
        else:
            direction += 1  # change direction
            direction = directions[direction % 4]
            row, col = go(row, col)

        matrix[row][col] = count
        count -= 1

    # convert matrix to string and use regex to replace
    # all brackets with whitespace
    print(re.sub("\[|\]", " ", np.array_str(matrix)))
