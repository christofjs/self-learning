def sparse_matrix_multiply(matrix_a, matrix_b):
    if len(matrix_a[0]) == len(matrix_b):
        sparse_a_dict = sparsify(matrix_a)
        sparse_b_dict = sparsify(matrix_b)
        matrix_c = [[0] * len(matrix_a) for _ in range(len(matrix_b[0]))]
        for i in range(len(matrix_a)):
            for k in range(len(matrix_a[0])):
                for j in range(len(matrix_b[0])):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return matrix_c
    else:
        return [[]]

def sparsify(matrix):
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] != 0

one = [[1,2],[3,4]]
two = [[2,2],[2,2]]
three = sparse_matrix_multiply(one, two)
for r in three:
    print(r)