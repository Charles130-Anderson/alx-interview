#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes):
    """A function that returns true if all box in
    boxes can be opened
    """
    n = len(boxes)
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # The first box is initially unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()  # Get a box from the stack
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                stack.append(key)

    return all(visited)  # Check if all boxes have been visited

# Test cases


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
