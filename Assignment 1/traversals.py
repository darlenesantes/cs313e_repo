"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Darlene Santes and Darlene Santes, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: drs4423
UT EID 2:
"""


def row_zigzag_traversal(grid):
    """
    Performs a zigzag traversal of a 2D list, alternating between
    left-to-right and right-to-left traversal for each row from
    top-to-bottom, and returns a list of coordinates (row, column).

    pre:
    - grid is a 2D list representing a 2D matrix.
    - The rows and columns range from 1 to 10 (inclusive).
    - All rows in grid have the same number of columns.

    post:
    - Returns a list of tuples (row, column) representing the
      coordinates of all elements in the specified order.
    """
    # take advantage of -1
    # Look at even and odd rows
    result = []
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                result.append((row, col))
        else:
            for col in range(cols - 1, -1, -1):
                result.append((row, col))
    return result


def column_zigzag_traversal(grid):
    """
    Performs a zigzag traversal of a 2D list, alternating between
    top-to-bottom and bottom-to-top traversal for each column from
    left-to-right, and returns a list of coordinates (row, column).

    pre:
    - grid is a 2D list representing a 2D matrix.
    - The rows and columns range from 1 to 10 (inclusive).
    - All rows in grid have the same number of columns.

    post:
    - Returns a list of tuples (row, column) representing the
      coordinates of all elements in the specified order.
    """
    # Like the other one, odd and even numbered columns
    result = []
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Iterating through each column
    for col in range(num_cols):
        if col % 2 == 0:
            for row in range(num_rows):
                result.append((row, col))
        else:
            for row in range(num_rows - 1, -1, -1):
                result.append((row, col))
    return result


def main_diagonal_traversal(grid):
    """
    Performs a diagonal traversal of a 2D list, iterating from 
    the top-right to the bottom-left in the direction of the 
    main diagonal, and returns a list of coordinates (row, column).

    pre:
    - grid is a 2D list representing a 2D matrix.
    - The rows and columns range from 1 to 10 (inclusive).
    - All rows in grid have the same number of columns.

    post:
    - Returns a list of tuples (row, column) representing the
      coordinates of all elements in the specified order.
    """
    result = []
    # Starting from scratch
    # We need to start at the last column of the 0th row
    # Finding totals to work with
    rows = len(grid)
    cols = len(grid[0])

    # Traversing through the first row should be independently of the other rows
    # This row is traversed backward while the others are traversed normalled
    for col in range(cols - 1, -1, -1):
        # Traverse diagonals in the first row
        row = 0
        while col < cols and row < rows:
            result.append((row, col))
            col += 1
            row += 1

    # Traversing through the other rows with a normal diagonal
    # starting at that first column
    for row in range(1, rows):
        col = 0
        while col < cols and row < rows:
            result.append((row, col))
            col += 1
            row += 1

    return result

def secondary_diagonal_traversal(grid):
    """
    Performs a diagonal traversal of a 2D list, iterating from 
    the top-left to the bottomt-right in the direction of the 
    main diagonal, and returns a list of coordinates (row, column).

    pre:
    - grid is a 2D list representing a 2D matrix.
    - The rows and columns range from 1 to 10 (inclusive).
    - All rows in grid have the same number of columns.

    post:
    - Returns a list of tuples (row, column) representing the
      coordinates of all elements in the specified order.
    """
    # Like the other one!! FINALLY SOMETHING I CAN DO IN UNDER 20 MILLION HOURS
    result = []
    rows = len(grid)
    cols = len(grid[0])

    # Traversing the first row left to right
    for col in range(cols):
        row = 0
        while col >= 0 and row < rows:
            result.append((row, col))
            col -= 1
            row += 1
    # Traversing the other rows backward
    for row in range(1, rows):
        col = cols - 1
        while col >= 0 and row < rows:
            result.append((row, col))
            col -= 1
            row += 1

    return result


def spiral_traversal(grid):
    """
    Performs a spiral traversal of a 2D list, iterating from 
    the outside rows and columns inward, and returns a list
    of coordinates (row, column).

    pre:
    - grid is a 2D list representing a 2D matrix.
    - The rows and columns range from 1 to 10 (inclusive).
    - All rows in grid have the same number of columns.

    post:
    - Returns a list of tuples (row, column) representing the
      coordinates of all elements in the specified order.
    """
    result = []
    rows = len(grid)
    cols = len(grid[0])
    # total_elems = rows * cols
    traversal = 0

    # Keeping track of spiral borders (index of rows and columns)
    top = 0
    bottom = rows - 1
    right = cols - 1
    left = 0

    while top <= bottom and left <= right:
        # Traversing the top of spiral
        # starts at left, ends at right + 1
        if traversal % 4 == 0:
            for col in range(left, right + 1):
                result.append((top, col))
            top += 1
        elif traversal % 4 == 1:
            # Traversing the right border of spiral
            # Starts at top ends at bottom + 1
            for row in range(top, bottom + 1):
                result.append((row, right))
            right -= 1
        elif traversal % 4 == 2:
            # Traversing bottom (backwards) of spiral
            # Starts at right and ends at left (in range left - 1)
            for col in range(right, left - 1 , -1):
                result.append((bottom, col))
            bottom -= 1
        else:
            # Traversing left border of spiral
            # Starts at bottom and ends at top -1 (b/c backwards)
            for row in range(bottom, top - 1, -1):
                result.append((row, left))
            left += 1
        traversal += 1

    return result
