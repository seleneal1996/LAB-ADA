#Selene Barrios Cornejo
import random
import time

def fibonnacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonnacci(n-1) + fibonnacci(n-2)

n=40
t0=time.time()
print('El fibonacci de ',n,'es',fibonnacci(n))
t1=time.time()
tiempo1=round(t1-t0,0)
print(tiempo1)

def fibonnacci_iterativo(n):
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


for i in [10,20,30,40,50,60,70,80,90,100]:
  t0=time.time()
  fibonnacci_iterativo(i)
  t1=time.time()
  tiempo1=round(t1-t0,0)
  print(i,"&",fibonnacci_iterativo(i),"&",tiempo1)

def fibo_iter_modulo(n, modulo):
  if n == 0:
    return 0
  anterior = 0
  actual = 1
  proximo = 0
  for i in range(1, n):
   a=(anterior+actual)%modulo
   proximo = a%modulo
   anterior = actual
   actual = proximo
  return actual
print("El fibonacci de (2^30)%2^20 es:",fibo_iter_modulo(1073741824,1048576))
