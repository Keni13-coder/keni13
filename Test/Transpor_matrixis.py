matr = [[1,2,3],
        [3,4,5],
        [6,7,8]]
'''
[1,3,6]
[2,4,7]
[3,5,8]
'''

def transpose_matrix(matrix):
    return  list(map(list, zip(*matrix)))

print(transpose_matrix(matr))