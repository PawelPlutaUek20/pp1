import random
class Matrix():

    @staticmethod
    def create2(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    
    @staticmethod
    def create(x,y):
        matrix = [[0 for col in range(y)] for row in range(x)]
        return matrix
    
    @staticmethod
    def create_unit(x):
        identity_matrix = Matrix.create(x,x)
        for i in range(x):
            identity_matrix[i][i] = 1
        return identity_matrix
    
    @staticmethod
    def fill_random(matrix,m,n):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = random.randint(m,n)
        return matrix
        
    @staticmethod
    def transpose(matrix):
        transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return transposed_matrix
    
    @staticmethod
    def create_diagonal(x,m,n):
        matrix = Matrix.create(x,x)
        for i in range(x):
            matrix[i][i] = random.randint(m,n)
        return matrix
    
    @staticmethod
    def compare(matrix1, matrix2):
        if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    if matrix1[i][j] == matrix2[i][j]:
                        return True
        return False
        
# m = Matrix.create(3,5)
# Matrix.fill_random(m,1,9)
# Matrix.print(m)

# t = Matrix.transpose(m)
# Matrix.print(t)

# d = Matrix.create_diagonal(5,10,50)
# Matrix.print(d)

# m1 = Matrix.create(3,5)
# m2 = Matrix.create(3,5)
# print(Matrix.compare(m1,m2))