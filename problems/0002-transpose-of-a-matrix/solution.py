def transpose_matrix(a):
    result = []

    for col in range(len(a[0])):      # loop through columns of original
        new_row = []
        for row in range(len(a)):     # loop through rows of original
            new_row.append(a[row][col])
        result.append(new_row)

    return result