import random
import time
# Paso 1
def fibonnacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonnacci(n-1) + fibonnacci(n-2)


# Paso 2
def fibonnacci_iterativo(n):
	if n == 0:
		return 0
	previo2 = 0
	previo = 1
	suma = 0
	for i in range(2, n):
		suma = previo+previo2
		previo2 = previo
		previo = suma
	return previo;


# Paso 3 y 4 --- la comparación con el fibonnacci_iterativo
def fibo_tabla(n):
	arreglo_fibonnacci = [0]*n
	arreglo_fibonnacci[0] = 0
	arreglo_fibonnacci[1] = 1
	for i in range(2, n):
		arreglo_fibonnacci[i] = arreglo_fibonnacci[i-1] + arreglo_fibonnacci[i-2];
	return arreglo_fibonnacci[n]


# Paso 5 ------------
def fibo_iter_modulo(n, modulo):
	if n == 0:
		return 0
	anterior = 0
	actual = 1
	proximo = 0
	for i in range(2, n):
		proximo = (actual%modulo+anterior%modulo)%modulo;
		anterior = actual;
		actual = proximo;
	return actual;


def fibo_recursivo_modulo(n, modulo):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return (fibonnacci(n-1) % modulo + fibonnacci(n-2) % modulo) % modulo


# profe =>  Paso 6
def multiplicar_matrix_2_2(a, b):
	c = [[0,0],[0,0]]
	c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
	c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
	c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
	c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
	return c

# profe =>  Paso 7
def potencia_matrices(matrix, potencia):
	if potencia == 0:
		return [[0,0],[0,1]]
	if potencia == 1:
		return matrix
	if potencia % 2 == 0:
		return potencia_matrices(multiplicar_matrix_2_2(matrix, matrix), potencia // 2)
	else:
		return multiplicar_matrix_2_2(potencia_matrices(multiplicar_matrix_2_2(matrix, matrix), (potencia-1) // 2), matrix)


# profe =>  Paso 8-------------------
def multiplicar_matrix_2_2_mod(a, b, modulo):
	c = [[0,0],[0,0]]
	c[0][0] = ((a[0][0] * b[0][0]) % modulo + (a[0][1] * b[1][0]) % modulo) % modulo
	c[0][1] = ((a[0][0] * b[0][1]) % modulo + (a[0][1] * b[1][1]) % modulo) % modulo
	c[1][0] = ((a[1][0] * b[0][0]) % modulo + (a[1][1] * b[1][0]) % modulo) % modulo
	c[1][1] = ((a[1][0] * b[0][1]) % modulo + (a[1][1] * b[1][1]) % modulo) % modulo
	return c


def potencia_matrices_mod(matrix, potencia, modulo):
	if potencia == 0:
		return [[0,0],[0,1]]
	if potencia == 1:
		return matrix
	if potencia % 2 == 0:
		return potencia_matrices_mod(multiplicar_matrix_2_2_mod(matrix, matrix, modulo), potencia // 2, modulo)
	else:
		return multiplicar_matrix_2_2_mod(potencia_matrices_mod(multiplicar_matrix_2_2_mod(matrix, matrix, modulo), (potencia-1) // 2, modulo), matrix, modulo)



fibo_matrix = [[0,1],[1,1]]
numero_random = random.randint(0, 500)
b = fibonnacci_iterativo(numero_random) % 50
c = fibo_iter_modulo(numero_random, 50)
l = potencia_matrices_mod(fibo_matrix, numero_random, 50)

print(b)
print(c)
print(l[0][0])
print(l)

