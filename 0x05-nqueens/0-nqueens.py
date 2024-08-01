#!/usr/bin/python3
"""
Solve N Queens problem
"""
import sys


class NQueen:
    """ Class for solving N Queen """

    def __init__(self, n):
        """ Initialize variables """
        self.n = n
        self.board = [0 for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        """ Check if (row, col) safe """
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == row - i:
                return False
        return True

    def solve(self, row):
        """ Place queens recursively """
        if row == self.n:
            solution = [[i, self.board[i]] for i in range(self.n)]
            self.solutions.append(solution)
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.board[row] = col
                    self.solve(row + 1)

    def get_solutions(self):
        """ Get all solutions """
        self.solve(0)
        return self.solutions


def main():
    """ Main function to solve """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(n)
    solutions = queen.get_solutions()

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
