#BARRIOS CORNEJO SELENE
#Lab 7 
import time
class fibonnacci:

	def recursivo(self,n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		recursivo(n-1) + recursivo(n-2)

	def fibonnacci_iterativo_array(self,n):
		fib=[0,1]
		for index in range(2,n+1):
			element=fib[index-1]+fib[index-2]
			fib.append(element)
		return fib

	def fibo_iter_modulo(self,n, modulo):
	  if n == 0:
	    return 0
	  anterior = 0
	  actual = 1
	  proximo = 0
	  for i in range(1, n):
	  	proximo = (actual%modulo+anterior%modulo)%modulo
	  	anterior = actual
	  	actual = proximo
	  return actual
	#print(fibo_iter_modulo(256,1048576))

	def f_iterativo_3variables(self,n):
	  if n == 0:
	    return 0
	  anterior = 0
	  actual = 1
	  proximo = 0
	  for i in range(1, n):
	    proximo = anterior+actual
	    anterior = actual
	    actual = proximo
	  return actual

F=fibonnacci()
#n = [2 ** x for x in range(8,31)]
#modulo = [2 ** x for x in range(8,21)]
for i in range(5):
	print(F.f_iterativo_3variables(i))

