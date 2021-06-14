def sparse_matrix_multiply(matrix_a, matrix_b):
    if len(matrix_a[0]) == len(matrix_b):
        matrix_c = []
        for i in range(len(matrix_a)):
            matrix_c.append([])
            for j in range(len(matrix_b[0])):
                matrix_c[i].append(0)
                for k in range(len(matrix_a[0])):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return matrix_c
    else:
        return [[]]

one = [[1,2],[3,4]]
two = [[2,2],[2,2]]
three = sparse_matrix_multiply(one, two)
for r in three:
    print(r)