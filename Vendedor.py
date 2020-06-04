f = open('file.txt', 'r')

NroRutas = int(f.readline()) 
Rutas = []

for i in range(NroRutas):
  NroCalles = int(f.readline()) 
  Calles = []

  for j in range(NroCalles-1):
    costo = int(f.readline())
    Calles.append(costo)
  
  Rutas.append(Calles)

#print(Rutas)
RutaNumero = 1
for RutaActual in Rutas :
  mayor = 0
  secuencia = []

  CostoTemp = 0
  TempSecuencia = []

  CalleActual = 1
  TempSecuencia.append(CalleActual)
  
  for Costo in RutaActual :
    CalleActual+=1
    TempSecuencia.append(CalleActual)
    CostoTemp += Costo

    if mayor <= CostoTemp :
      mayor = CostoTemp
      secuencia = TempSecuencia[:]

    if CostoTemp <= 0 :
      CostoTemp = 0
      TempSecuencia = []
      TempSecuencia.append(CalleActual)
  print("Ruta " + str(RutaNumero))
  print(mayor)
  print(secuencia)
  RutaNumero += 1
