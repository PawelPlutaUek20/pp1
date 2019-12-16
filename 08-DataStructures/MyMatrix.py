class Matrix():

    @staticmethod
    def create(x,y):
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
    def create2(x,y):
        matrix = [[0 for col in range(y)] for row in range(x)]
        return matrix
    
    @staticmethod
    def create_unit(x):
        identity_matrix = Matrix.create2(x,x)
        for i in range(x):
            identity_matrix[i][i] = 1
        return identity_matrix
    
    @staticmethod
    def fill_random(matrix,m,n):
        import random
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = random.randint(m,n)
        return matrix
        
    @staticmethod
    def transpose(matrix):
        transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return transposed_matrix
        
m = Matrix.create2(3,5)
Matrix.fill_random(m,1,9)
Matrix.print(m)
print()
t = Matrix.transpose(m)
Matrix.print(t)