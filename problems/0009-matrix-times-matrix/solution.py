def matrixmul(
    a: list[list[int | float]],
    b: list[list[int | float]]
) -> list[list[int | float]] | int:

    c = []

    if len(a[0]) == len(b):
        for i in range(len(a)):
            row = []

            for j in range(len(b[0])):
                total = 0

                for k in range(len(a[i])):
                    prod = a[i][k] * b[k][j]
                    total += prod

                row.append(total)

            c.append(row)
    else:
        return -1

    return c