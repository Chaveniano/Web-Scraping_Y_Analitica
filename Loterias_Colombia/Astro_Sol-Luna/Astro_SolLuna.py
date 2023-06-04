# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:06:35 2023

@author: 50512
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def propuestas(conteo,limite):
  arry = np.array(conteo)
  percentile = np.percentile(arry, limite)

  Resultado = conteo.loc[lambda x : x > percentile]
  Resultado=Resultado.index.values
  return Resultado

porcen=80

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}
url = "https://superastro.com.co/resultados-super-astro-sol-super-astro-luna.php"
 
respuesta = requests.get(url, headers=headers)
 
soup = BeautifulSoup(respuesta.text,"lxml")
ids = ["respuestasol", "respuestaluna", "Astro_Sol", "Astro_Luna"]
consolidado_astro = []



for s in range(0, 2):
            #print(s)
            contenedor = soup.find(id=ids[s])
            lista_resultados = contenedor.find_all('tr')
            for sorteo in lista_resultados[1:]:
                columnas = sorteo.find_all('td')
                consolidado_astro.append({
                    "id": columnas[2].text,
                    "Nomb_premio": ids[s+2],
                    "N_Ganador": columnas[0].text,
                    "Signo": columnas[1].text,
                    "N1": str(columnas[0].text)[0],
                    "N2": str(columnas[0].text)[1],
                    "N3": str(columnas[0].text)[2],
                    "N4": str(columnas[0].text)[3],
                    "Fecha": columnas[3].text
                })
consolidado = pd.DataFrame(consolidado_astro)
consolidado=consolidado.replace("Acurio", "Acuario")
consolidado=consolidado.replace("Escorpio", "Escorpion")
#consolidado
Analisis_N1=consolidado.N1.value_counts()/sum(consolidado.N1.value_counts())*100
Analisis_N2=consolidado.N2.value_counts()/sum(consolidado.N2.value_counts())*100
Analisis_N3=consolidado.N3.value_counts()/sum(consolidado.N3.value_counts())*100
Analisis_N4=consolidado.N4.value_counts()/sum(consolidado.N4.value_counts())*100

Analisis_Signo=consolidado.Signo.value_counts()/sum(consolidado.Signo.value_counts())*100

#Analisis_S12=consolidado.S12.value_counts()/sum(consolidado.S12.value_counts())*100
#Analisis_S3=consolidado.S3.value_counts()/sum(consolidado.S3.value_counts())*100

Analisis_N1234=consolidado.N_Ganador.value_counts()
#Analisis_S123=consolidado.serie.value_counts()


Propuestas_N1_Sol_Luna=propuestas(Analisis_N1,porcen)
Propuestas_N2_Sol_Luna=propuestas(Analisis_N2,porcen)
Propuestas_N3_Sol_Luna=propuestas(Analisis_N3,porcen)
Propuestas_N4_Sol_Luna=propuestas(Analisis_N4,porcen)
Propuestas_Signo_Sol_Luna=propuestas(Analisis_Signo,porcen)
#Propuestas_S3_PM=propuestas(Analisis_S3,porcen)
Propuestas_N1234_Sol_Luna=propuestas(Analisis_N1234,porcen)
#Propuestas_Signo_Sol=propuestas(Analisis_Signo,porcen)

# print("N1: ",Analisis_N1)
# print("-----------")
# print("N2: ",Analisis_N2)
# print("-----------")
# print("N3: ",Analisis_N3)
# print("-----------")
# print("N4: ",Analisis_N4)
# print("-----------")
# print("sign: ",Analisis_Signo)
##############################################3
################################################
########## ASTRO SOL
print(".....")
print("..ASTRO SOL..")
print(".....")
consolidado_Sol=consolidado[consolidado["Nomb_premio"]=="Astro_Sol"]

Analisis_N1=consolidado_Sol.N1.value_counts()/sum(consolidado_Sol.N1.value_counts())*100
Analisis_N2=consolidado_Sol.N2.value_counts()/sum(consolidado_Sol.N2.value_counts())*100
Analisis_N3=consolidado_Sol.N3.value_counts()/sum(consolidado_Sol.N3.value_counts())*100
Analisis_N4=consolidado_Sol.N4.value_counts()/sum(consolidado_Sol.N4.value_counts())*100

Analisis_Signo=consolidado_Sol.Signo.value_counts()/sum(consolidado_Sol.Signo.value_counts())*100

#Analisis_S12=consolidado.S12.value_counts()/sum(consolidado.S12.value_counts())*100
#Analisis_S3=consolidado.S3.value_counts()/sum(consolidado.S3.value_counts())*100

Analisis_N1234=consolidado_Sol.N_Ganador.value_counts()
#Analisis_S123=consolidado.serie.value_counts()


Propuestas_N1_Sol=propuestas(Analisis_N1,porcen)
Propuestas_N2_Sol=propuestas(Analisis_N2,porcen)
Propuestas_N3_Sol=propuestas(Analisis_N3,porcen)
Propuestas_N4_Sol=propuestas(Analisis_N4,porcen)
Propuestas_Signo_Sol=propuestas(Analisis_Signo,porcen)
#Propuestas_S3_PM=propuestas(Analisis_S3,porcen)
Propuestas_N1234_Sol=propuestas(Analisis_N1234,porcen)
#Propuestas_Signo_Sol=propuestas(Analisis_Signo,porcen)

# print("N1: ",Analisis_N1)
# print("-----------")
# print("N2: ",Analisis_N2)
# print("-----------")
# print("N3: ",Analisis_N3)
# print("-----------")
# print("N4: ",Analisis_N4)
# print("-----------")
# print("sign: ",Analisis_Signo)

##############################################3
################################################
########## ASTRO LUNA
print(".....")
print("..ASTRO LUNA..")
print(".....")
consolidado_Luna=consolidado[consolidado["Nomb_premio"]=="Astro_Luna"]

Analisis_N1=consolidado_Luna.N1.value_counts()/sum(consolidado_Luna.N1.value_counts())*100
Analisis_N2=consolidado_Luna.N2.value_counts()/sum(consolidado_Luna.N2.value_counts())*100
Analisis_N3=consolidado_Luna.N3.value_counts()/sum(consolidado_Luna.N3.value_counts())*100
Analisis_N4=consolidado_Luna.N4.value_counts()/sum(consolidado_Luna.N4.value_counts())*100

Analisis_Signo=consolidado_Luna.Signo.value_counts()/sum(consolidado_Luna.Signo.value_counts())*100

#Analisis_S12=consolidado.S12.value_counts()/sum(consolidado.S12.value_counts())*100
#Analisis_S3=consolidado.S3.value_counts()/sum(consolidado.S3.value_counts())*100

Analisis_N1234=consolidado_Luna.N_Ganador.value_counts()
#Analisis_S123=consolidado.serie.value_counts()


Propuestas_N1_Luna=propuestas(Analisis_N1,porcen)
Propuestas_N2_Luna=propuestas(Analisis_N2,porcen)
Propuestas_N3_Luna=propuestas(Analisis_N3,porcen)
Propuestas_N4_Luna=propuestas(Analisis_N4,porcen)
Propuestas_Signo_Luna=propuestas(Analisis_Signo,porcen)
#Propuestas_S3_PM=propuestas(Analisis_S3,porcen)
Propuestas_N1234_Luna=propuestas(Analisis_N1234,porcen)
#Propuestas_Signo_Sol=propuestas(Analisis_Signo,porcen)

# print("N1: ",Analisis_N1)
# print("-----------")
# print("N2: ",Analisis_N2)
# print("-----------")
# print("N3: ",Analisis_N3)
# print("-----------")
# print("N4: ",Analisis_N4)
# print("-----------")
# print("sign: ",Analisis_Signo)


print(".....")
print("..ASTRO SOL Y LUNA..")
print(".....")

print("Luna y Sol")
print("N1:",Propuestas_N1_Sol_Luna.tolist())
print("N2:",Propuestas_N2_Sol_Luna.tolist())
print("N3:",Propuestas_N3_Sol_Luna.tolist())
print("N4:",Propuestas_N4_Sol_Luna.tolist())
print("Signo:",Propuestas_Signo_Sol_Luna.tolist())
#print("S3:",Propuestas_S3.tolist())
print("COMPLETO N:",Propuestas_N1234_Sol_Luna.tolist())
#print("COMPLETO S:",Propuestas_S123.tolist())

print("--------------------")
print("Sol")
print("N1:",Propuestas_N1_Sol.tolist())
print("N2:",Propuestas_N2_Sol.tolist())
print("N3:",Propuestas_N3_Sol.tolist())
print("N4:",Propuestas_N4_Sol.tolist())
print("Signo:",Propuestas_Signo_Sol.tolist())
#print("S3:",Propuestas_S3.tolist())
print("COMPLETO N:",Propuestas_N1234_Sol.tolist())
#print("COMPLETO S:",Propuestas_S123.tolist())
print("--------------------")
print("Luna")
print("N1:",Propuestas_N1_Luna.tolist())
print("N2:",Propuestas_N2_Luna.tolist())
print("N3:",Propuestas_N3_Luna.tolist())
print("N4:",Propuestas_N4_Luna.tolist())
print("Signo:",Propuestas_Signo_Luna.tolist())
#print("S3:",Propuestas_S3.tolist())
print("COMPLETO N:",Propuestas_N1234_Luna.tolist())
#print("COMPLETO S:",Propuestas_S123.tolist())