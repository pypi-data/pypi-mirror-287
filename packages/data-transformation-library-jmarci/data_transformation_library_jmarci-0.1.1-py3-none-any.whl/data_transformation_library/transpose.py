def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    """
    Transposes a 2D matrix.

    Parameters:
    ----------
    input_matrix : list[list[float]]
        A list of lists of floats representing the input matrix to be transposed.

    Returns:
    -------
    list[list[float]]
        A list of lists of floats representing the transposed matrix, where the rows of the input matrix become the columns of the output matrix and vice versa.

    Raises:
    ------
    TypeError
        If `input_matrix` is not a list.

    Example:
    -------
    >>> input_matrix = [
    ...     [1.0, 2.0, 3.0],
    ...     [4.0, 5.0, 6.0]
    ... ]
    >>> transpose2d(input_matrix)
    [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
    """
    if not isinstance(input_matrix, list):
        raise TypeError("input_matrix must be a list")
        
    # Find the number of rows and columns in the input matrix
    num_rows = len(input_matrix)
    num_cols = len(input_matrix[0])

    # Create an empty list to store the transposed matrix
    output_matrix = [[None] * num_rows for _ in range(num_cols)]

    # Iterate over columns
    for i in range(num_rows):
        for j in range(num_cols):
            output_matrix[j][i] = input_matrix[i][j]
    return output_matrix
