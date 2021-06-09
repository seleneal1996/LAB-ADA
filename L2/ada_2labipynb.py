# -*- coding: utf-8 -*-
"""ADA_2labipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XdOQ9Tmyqdma6CPH0-6xOORn5FsrgInT
"""

import random
import time
def bubble_sort(arr):
  #Mis Variables para analisis
  comparacion=0
  asignacion=0
  c_objeto=0
  n=len(arr) #tam del vector
  asignacion=asignacion+ 2# tam + i en el primer for
  c_objeto=c_objeto+1# creacion de objeto 
  for i in range(n):
    comparacion=comparacion+1#del for 
    asignacion=asignacion+1# j del segundo for
    c_objeto=c_objeto+1#range de forma iterativa
    for j in range(0,n-i-1):
      comparacion=comparacion+1#comparacion del for 
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        asignacion=asignacion+3#del swap 
      comparacion=comparacion+1#del if 
      asignacion=asignacion+1# del segundo for
    comparacion=comparacion+1#el iterador se sale del rango
    asignacion=asignacion+1#incremento del primer for
  comparacion=comparacion+1#el iterador se vuelve a salir del rango
  return (comparacion,asignacion,c_objeto,0)

def insertion_sort(A):
  #Mis variables
  comp = 0
  asig = 0
  n = len(A) # tam del Vector
  i = 1
  asig = asig + 2 # tam arreglo y el i 
  while i < n:
      comp = comp + 1 # Comparacion del while 
      var = A[i]
      j = i - 1
      asig = asig + 2 # De var y j
      while j >= 0 and A[j] > var:
          comp = comp + 2 # del while
          A[j + 1] = A[j]
          j = j - 1
          asig = asig + 2 # A[j+1] y de j 
      comp = comp + 2 # del while 
      A[j + 1] = var
      i = i + 1
      asig = asig + 2 # A[j + 1] e i 
  comp = comp + 1 # del while 
  return (comp, asig, 0, 0)

def Generando2(n, mode, a=0,b=100):
    comp=0
    asig=0
    c_objeto=0
    Malloc=0
    if mode == 'creciente':
        return list(range(n))
    elif mode == 'decreciente':
        return list(range(n - 1, -1, -1))
    A = [None] * n
    asig=asig+1
    c_objeto=c_objeto+1
    Malloc=Malloc+n
    for i in range(n):
        A[i] = random.randint(a, b)
        comp= comp+1
        asig=asig+2
    return A
print("****BURBUJA")

print("i,","comparacion,","asignacion,","TOTAL,","tiempo")
for i in [5, 10, 50, 100, 500, 1000, 5000, 10000]:
  t0=time.time()
  A = Generando2(i,'creciente')
  (comparacion, asignacion, c_objeto, malloc) = bubble_sort(A)
  t1=time.time()
  tiempo1=round(t1-t0,0)
  comparaciones= comparacion * 2     
  Asignaciones  = asignacion * 8     
  C_objeto   = c_objeto * 200
  Malloc = 50 + (malloc * 10)
  TOTAL  = comparaciones + Asignaciones + C_objeto + Malloc
  print(i,",",comparacion,",",asignacion,",",TOTAL,",",tiempo1)
print("COMPARACIONES:",comparaciones)
print("ASIGNACIONES:",Asignaciones)

for i in [5, 10, 50, 100, 500, 1000, 5000, 10000]:
  t2=time.time()
  A = Generando2(i,'decreciente')
  (comparacion, asignacion, c_objeto, malloc) = bubble_sort(A)
  t2=time.time()
  tiempo1=round(t1-t0,0)
  comparaciones= comparacion * 2     
  Asignaciones  = asignacion * 8     
  C_objeto   = c_objeto * 200
  Malloc = 50 + (malloc * 10)
  TOTAL  = comparaciones + Asignaciones + C_objeto + Malloc
  print(i,",",comparacion,",",asignacion,",",TOTAL,",",tiempo1)
print("COMPARACIONES:",comparaciones)
print("ASIGNACIONES:",Asignaciones)

print("**** INSERT")

for i in [5, 10, 50, 100, 500, 1000, 5000, 10000]:
  t3_=time.time()
  A = Generando2(i,'creciente')
  (comp, asig, c_objeto, malloc) = insertion_sort(A)
  t0_=time.time()
  tiempo3=round(t3_-t0_,0)
  comparaciones= comp*2     
  Asignaciones  = asig*8     
  C_objeto   = c_objeto * 200
  Malloc = 50 + (malloc * 10)
  TOTAL  = comparaciones + Asignaciones + C_objeto + Malloc 
  print(i,",",comparaciones,",",Asignaciones,",",TOTAL,",",tiempo3)
print("COMPARACIONES:",comparaciones)

for i in [5, 10, 50, 100, 500, 1000, 5000, 10000]:
  t0_=time.time()
  A = Generando2(i,'decreciente')
  (comp, asig, c_objeto, malloc) = insertion_sort(A)
  t1_=time.time()
  tiempo3=round(t1_-t0_,0)
  comparaciones= comp*2     
  Asignaciones  = asig*8     
  C_objeto   = c_objeto * 200
  Malloc = 50 + (malloc * 10)
  TOTAL  = comparaciones + Asignaciones + C_objeto + Malloc 
  print(i,",",comparacion,",",asignacion,",",TOTAL,",",tiempo3)
print("COMPARACIONES:",comparaciones)
print("ASIGNACIONES:",Asignaciones)