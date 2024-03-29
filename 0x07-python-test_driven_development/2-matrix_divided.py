#!/usr/bin/python3
"""provides matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        a new matrix with all elements divided by div.
    """
    f_err = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or matrix == [] or \
            (not all(isinstance(row, list) for row in matrix)):
        raise TypeError(f_err)
    for row in matrix:
        for no in row:
            if not isinstance(no, int) and not isinstance(no, float):
                raise TypeError(f_err)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
