import numpy as np
from numpy import random as rd
def Cuadraditos(M):
  m=len(M)
  n=len(M[0])
  for i in range(m):
    for j in range(n):
       if i==1 and j==1:
         return 1
       else:
         sum=0
         while(m>=1 and n>=1):
           sum+=m*n
           m=m-1
           n=n-1
         return sum
a = rd.randint(0,1,(6,6)) 
print(a)
i=int(input('Ingrese cordenada i:'))
j=int(input('Ingrese cordenada j:'))
b=a[i:,:j]
print(b)
print(Cuadraditos(b))