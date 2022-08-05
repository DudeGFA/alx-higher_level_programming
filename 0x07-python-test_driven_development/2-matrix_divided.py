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
    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for no in row:
            if not isinstance(no, int) or not isinstance(no, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
