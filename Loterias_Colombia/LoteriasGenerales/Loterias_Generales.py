# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:04:52 2023

@author: Sebastian Chaves Tequia
"""

import requests
import pandas as pd
import numpy as np
#import tensorflow as tf
fin=int(input("Digite la cantidad de días que quiere traer: "))
print("Escriba el numero de la loteria a traer sus resultados")
print("2 - Loteria de Bogotá")
print("4 - Loteria de Boyacá")
print("6 - Loteria del Cauca")
print("8 - Loteria de Cruz Roja")
print("10 - Loteria del Cundinamarca")
print("15 - Loteria del Manizales")
print("16 - Loteria de Medellín")
print("22 - Loteria del Santander")
print("24 - Loteria del Valle")

eleccion = int(input())
eleccion=f"{eleccion:02d}"
eleccion=str(eleccion)

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}


url_api = f"https://portalapi.loteriademedellin.com.co/api/core/draw/latest-played?limit=100&lotteryId={eleccion}"
#print(url_api)
        
response = requests.get(url_api, headers=headers)  # se puede ver que es un API .GET ya que lo dice en el chrome en la pestaña de Headers
print(response)  # 403=No acceso por seguridad, 200=OK
#print(response.json())
data = response.json()
#data
df_sorteo=pd.json_normalize(data)
df_sorteo.head(3)

consolidado=pd.DataFrame()
contador=0
for i in zip (df_sorteo.drawId):
  
  N_sorteo=i[0]
  url_api = f"https://portalapi.loteriademedellin.com.co/api/core/results/history?lotteryId={eleccion}&drawId={N_sorteo}&page=0&size=100"
  response = requests.get(url_api, headers=headers)  # se puede ver que es un API .GET ya que lo dice en el chrome en la pestaña de Headers
  print(response)  # 403=No acceso por seguridad, 200=OK
  data = response.json()
  #data
  df_ganadores=pd.json_normalize(data,record_path =['content'])
  consolidado=pd.concat([consolidado,df_ganadores])
  df_ganadores.head(3)
  contador=contador+1
  if contador==fin:
    break

premios_diarios=df_ganadores.copy()
premios_diarios=premios_diarios.groupby(by=["description"]).count()
premios_diarios
premios_diarios=premios_diarios.iloc[:,[1]]#"description"]#["description","item"]]
premios_diarios

#consolidado
def extraer_n1(cadena):
   return cadena[0:-3]
def extraer_n2(cadena):
   return cadena[1:-2]
def extraer_n3(cadena):
   return cadena[2:-1]
def extraer_n4(cadena):
   return cadena[3:]
def extraer_s12(cadena):
   return cadena[0:-1]
def extraer_s3(cadena):
   return cadena[2:]               

consolidado["N1"]=consolidado["number"].apply(extraer_n1)
consolidado["N2"]=consolidado["number"].apply(extraer_n2)
consolidado["N3"]=consolidado["number"].apply(extraer_n3)
consolidado["N4"]=consolidado["number"].apply(extraer_n4)

consolidado["S12"]=consolidado["serie"].apply(extraer_s12)
consolidado["S3"]=consolidado["serie"].apply(extraer_s3)

consolidado[['number','serie','N1','N2','N3','N4','S12','S3']]=consolidado[['number','serie','N1','N2','N3','N4','S12','S3']].astype(int)
#consolidado=consolidado.reset_index()
consolidado.describe()#

#************************************Estadistica Basica
Analisis_N1=consolidado.N1.value_counts()/sum(consolidado.N1.value_counts())*100
Analisis_N2=consolidado.N2.value_counts()/sum(consolidado.N2.value_counts())*100
Analisis_N3=consolidado.N3.value_counts()/sum(consolidado.N3.value_counts())*100
Analisis_N4=consolidado.N4.value_counts()/sum(consolidado.N4.value_counts())*100

Analisis_S12=consolidado.S12.value_counts()/sum(consolidado.S12.value_counts())*100
Analisis_S3=consolidado.S3.value_counts()/sum(consolidado.S3.value_counts())*100

Analisis_N1234=consolidado.number.value_counts()
Analisis_S123=consolidado.serie.value_counts()

def propuestas(conteo,limite):
  arry = np.array(conteo)
  percentile = np.percentile(arry, limite)

  Resultado = conteo.loc[lambda x : x > percentile]
  Resultado=Resultado.index.values
  return Resultado

porcen=85
Propuestas_N1=propuestas(Analisis_N1,porcen)
Propuestas_N2=propuestas(Analisis_N2,porcen)
Propuestas_N3=propuestas(Analisis_N3,porcen)
Propuestas_N4=propuestas(Analisis_N4,porcen)
Propuestas_S12=propuestas(Analisis_S12,porcen)
Propuestas_S3=propuestas(Analisis_S3,porcen)
Propuestas_N1234=propuestas(Analisis_N1234,porcen)
Propuestas_S123=propuestas(Analisis_S123,porcen)

#****************************HORA BÁSICA PARA PREMIO MAYOR

consolidado=consolidado[consolidado["description"]=="PREMIO MAYOR"]

Analisis_N1=consolidado.N1.value_counts()/sum(consolidado.N1.value_counts())*100
Analisis_N2=consolidado.N2.value_counts()/sum(consolidado.N2.value_counts())*100
Analisis_N3=consolidado.N3.value_counts()/sum(consolidado.N3.value_counts())*100
Analisis_N4=consolidado.N4.value_counts()/sum(consolidado.N4.value_counts())*100

Analisis_S12=consolidado.S12.value_counts()/sum(consolidado.S12.value_counts())*100
Analisis_S3=consolidado.S3.value_counts()/sum(consolidado.S3.value_counts())*100

Analisis_N1234=consolidado.number.value_counts()
Analisis_S123=consolidado.serie.value_counts()

porcen=90
Propuestas_N1_PM=propuestas(Analisis_N1,porcen)
Propuestas_N2_PM=propuestas(Analisis_N2,porcen)
Propuestas_N3_PM=propuestas(Analisis_N3,porcen)
Propuestas_N4_PM=propuestas(Analisis_N4,porcen)
Propuestas_S12_PM=propuestas(Analisis_S12,porcen)
Propuestas_S3_PM=propuestas(Analisis_S3,porcen)
Propuestas_N1234_PM=propuestas(Analisis_N1234,porcen)
Propuestas_S123_PM=propuestas(Analisis_S123,porcen)

#******************************RESULTADOS TODO Y DE SOLO PREMIO MAYOR

print("N1:",Propuestas_N1.tolist())
print("N2:",Propuestas_N2.tolist())
print("N3:",Propuestas_N3.tolist())
print("N4:",Propuestas_N4.tolist())
print("S12:",Propuestas_S12.tolist())
print("S3:",Propuestas_S3.tolist())
print("COMPLETO N:",Propuestas_N1234.tolist())
print("COMPLETO S:",Propuestas_S123.tolist())


print("N1_PM:",Propuestas_N1_PM.tolist())
print("N2_PM:",Propuestas_N2_PM.tolist())
print("N3_PM:",Propuestas_N3_PM.tolist())
print("N4_PM:",Propuestas_N4_PM.tolist())
print("S12_PM:",Propuestas_S12_PM.tolist())
print("S3_PM:",Propuestas_S3_PM.tolist())
print("COMPLETO N_PM:",Propuestas_N1234_PM.tolist())
print("COMPLETO S_PM:",Propuestas_S123_PM.tolist())
