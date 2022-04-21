def sparse_matrix_multiply(matrix_a, matrix_b):
    if (len(matrix_a[0]) != len(matrix_b)):
        return [[]]
    aSparse = sparsify(matrix_a)
    bSparse = sparsify(matrix_b)
    cMatrix = [[0] * len(matrix_a[0]) for _ in range(len(matrix_a))]
    for (i,j) in aSparse.keys():
        for k in range(len(matrix_b[0])):
            if (j,k) in bSparse.keys():
                cMatrix[i][k] += aSparse[(i,j)] * bSparse[(j,k)]
    return cMatrix


def sparsify(matrix):
    matDict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                matDict[(i,j)] = matrix[i][j]
    return matDict

one = [[1,2,3],[3,4,4]]
two = [[2,2,2],[3,3,3],[4,4,4]]
three = sparse_matrix_multiply(one, two)
for r in three:
    print(r)