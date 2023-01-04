#!/usr/bin/python3
""" a function that checks if all the boxes can be opened
Parameters
----------
boxes : list
    list of lists that might contain keys to the other boxes
Returns
-------
boolean
    True if all the boxes can be opend, else False
"""


def canUnlockAll(boxes):
    """
    determine opened boxes
    """
    num_box = len(boxes)
    box_state = [False for x in range(num_box)]
    box_state[0] = True
    for i in range(num_box):
        for j in range(len(boxes[i])):
            try:
                if boxes[i][j] != i and box_state[boxes[i][j]] is False:
                    box_state[boxes[i][j]] = True
            except IndexError:
                continue
    if False in box_state:
        return False
    else:
        return True
