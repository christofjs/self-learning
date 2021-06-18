# testing git credentials
def sparse_matrix_multiply(matrix_a, matrix_b):
    if len(matrix_a[0]) == len(matrix_b):
        sparse_a_dict = sparsify(matrix_a)
        sparse_b_dict = sparsify(matrix_b)
        matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
        for i,k in sparse_a_dict.keys():
            for j in range(len(matrix_b[0])):
                if (k,j) in sparse_b_dict.keys():
                    matrix_c[i][j] += sparse_a_dict[(i,k)] * sparse_b_dict[(k,j)]
        return matrix_c
    else:
        return [[]]

def sparsify(matrix):
    sparsed_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparsed_dict[(i,j)] = matrix[i][j]
    return sparsed_dict


one = [[1,2,3],[3,4,4]]
two = [[2,2,2],[3,3,3],[4,4,4]]
three = sparse_matrix_multiply(one, two)
for r in three:
    print(r)
