#!/usr/bin/python3
"""
Rotate n x n matrix 90 degrees.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate matrix in place 90 degrees.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
