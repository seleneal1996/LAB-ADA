# -*- coding: utf-8 -*-
"""ADA4L_divide_conquista.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dcINykHICA9-kPCRTKo5bH-5AxmtrV7

#DIVIDE Y CONQUISTA
"""

#Nota: no estoy muy segura :,c ...
#Barrios Cornejo Selene
def maxSubSum(A,n):
  if n==1:
    return A[0]
  m=n/2
  izq_MSS=maxSubSum(A,m)
  der_MSS=maxSubSum(A+m,n-m)
  izqsum=0
  dersum=0
  sum=0
  for i in range(m,n):
    sum+=A[i]
    dersum= max(dersum,sum)
  sum=0
  for i in range(m-1,0,-1):
    sum+=A[i]
    izqsum=max(izqsum,sum)
  ans=max(izq_MSS,der_MSS)
  return max(ans,izqsum+dersum)
a=int(input('a:'))
lon=list(range(a))
resul=list(range(a))
for i in range(0,a):
  b=int(input('b:'))
  lon[i]=b
  A=list(range(b))
  for j in range(0,b-1):
    dato=int(input('dato:'))
    A[j]=dato
    r=maxSubSum(A,b-1)
    resul[i]=r
for k in range(0,a):
  if resul[k]>0:
    print("La mejor parte de la ruta", (k+1),"su suma es",(resul[i]))
  else:
    print("La ruta",(k+1),"no tiene calles interesantes")
A.clear()
lon.clear()