def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    det = a * d - b * c

    if det == 0:
        return None

    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]