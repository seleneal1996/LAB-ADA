#BARRIOS CORNEJO SELENE
#LAB 8
import numpy as np
from numpy import random as rd
#A la funcion cuadraditos ingresa la matrix
def Cuadraditos(M):
  m=len(M)
  n=len(M[0])
  #recorremos filas y columnas
  for i in range(m):
    for j in range(n):
      #Para los casos se entiende que si hubiera un i=0 y j =0 , no tendriamos cuadraditos
      # Si i=1 y j =1  tendriamos un cuadradito
       if i==1 and j==1:
         return 1
      #en caso que el i y j sean mayores a 1 empezamos a acumular los cuadraditos y disminuimos pos
       else:
         sum=0
         while(m>=1 and n>=1):
           sum+=m*n
           m=m-1
           n=n-1
         return sum
# se crea una matrix randon llena de 0s y tam 6*6
a = rd.randint(0,1,(6,6)) 
#imprimimos la matrix 
print(a)
#pedimos cordenadas 
i=int(input('Ingrese cordenada i:'))
j=int(input('Ingrese cordenada j:'))
#en una variable b asignamos la submatrix que obtenemos de las cordenadas , la imprimmos y le pasamos la funcion cuadraditos
b=a[i:,:j]
print(b)
print(Cuadraditos(b))
