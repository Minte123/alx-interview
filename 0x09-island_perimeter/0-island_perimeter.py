#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Function to find the perimeter of an island
    Parameters
    ----------
    grid : list
      list of list of integers 0 represents water and 1 represents
    Returns
    -------
      perimeter of the island described in grid
    """
    if not grid or any(type(arr) != list for arr in grid):
        return 0
    width = len(grid[0]) - 1
    if any(len(arr) != width + 1 for arr in grid):
        return 0
    islands = connections = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                islands += 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    connections += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    connections += 1
    return 4 * islands - 2 * connections


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert(island_perimeter(grid) == 12)
