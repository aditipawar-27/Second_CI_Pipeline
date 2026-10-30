def transpose_matrix(matrix):
    """Return the transpose of a rectangular matrix."""
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be rectangular")

    return [list(column) for column in zip(*matrix)]