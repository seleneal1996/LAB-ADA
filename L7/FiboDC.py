def multiplicar(a, b):
	c = [[0,0],[0,0]]
	c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
	c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
	c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
	c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
	return c

def potencia_matrices(matrix, potencia):
	if potencia == 0:
		return [[0,0],[0,1]]
	if potencia == 1:
		return matrix
	if potencia % 2 == 0:
		return potencia_matrices(multiplicar(matrix, matrix), potencia // 2)
	else:
		return multiplicar(potencia_matrices(multiplicar(matrix, matrix), (potencia-1) // 2), matrix)

fibo_matrix = [[0,1],[1,1]]
numero= 18
matrix = potencia_matrices(fibo_matrix, numero)
print(matrix)
print("El f(",numero,") es:",matrix[0][1])