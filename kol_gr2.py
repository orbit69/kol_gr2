class Matrix:
	def __init__(self, a, b, c, d):
		self._matrix = [[0 for col in range(2)] for row in range(2)]
		self._matrix[0][0] = a;
		self._matrix[0][1] = b;
		self._matrix[1][0] = c;
		self._matrix[1][1] = d;

	def add(self, mtrx):
		tmp = Matrix(0, 0, 0, 0)
		for i in range (0, 2):
			for j in range (0, 2):
				tmp._matrix[i][j] = self._matrix[i][j] + mtrx._matrix[i][j]
		return tmp

	def print_matrix(self, string):
		print "Macierz ", string
		print self._matrix[0]
		print self._matrix[1]

	def multiply(self, mtrx):
		tmp = Matrix(0, 0, 0, 0)
		for i in range (0, 2):
			for j in range (0, 2):
				for k in range (0, 2):
					tmp._matrix[i][j] += self._matrix[k][j] * mtrx._matrix[i][k]
		return tmp;

	
			


matrix_1 = Matrix(4,5,6,7)
matrix_1.print_matrix("matrix_1")

matrix_2 = Matrix(2,2,2,1)
matrix_2.print_matrix("matrix_2")

matrix_3 = matrix_2.add(matrix_1)
matrix_3.print_matrix("matrix_3")

matrix_4 = matrix_1.multiply(matrix_2)
matrix_4.print_matrix("matrix_4")

