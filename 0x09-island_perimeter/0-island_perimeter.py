#!/usr/bin/python3
"""
Module to calculate island perimeter.
"""


def island_perimeter(grid):
    """
    Calculate island perimeter in grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume all four sides contribute
                perimeter += 4
                # Check if there is a neighboring land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove two sides
                # Check if there is a neighboring land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove two sides

    return perimeter
