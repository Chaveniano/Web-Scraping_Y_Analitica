# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:35:59 2023

@author: 50512
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

#Token="Token 09288a8077df38f82b7a3343fc2c1ed8e472625b"
Token= "Token 4ad87cfd10c4160472739ddf8227f531373c82ea"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
    "authorization":Token
}
url_api = "https://www.voscreen.com/api/v3/user/stats/"
response = requests.get(url_api,headers=headers)  # se puede ver que es un API .GET ya que lo dice en el chrome en la pestaña de Headers
print(response)  # 403=No acceso por seguridad, 200=OK
print(response.json())
data = response.json()
paginas=data["total_pages"]
print("total de paginas= ", paginas)
paginas=int(paginas)+1
consolidado = []

for i in range(1,paginas):
    print(i)
    url_api = "https://www.voscreen.com/api/v3/user/stats?page=" + str(i)
    response = requests.get(url_api,headers=headers)  # se puede ver que es un API .GET ya que lo dice en el chrome en la pestaña de Headers
    print(response)  # 403=No acceso por seguridad, 200=OK
    data = response.json()
    # Extraigo los datos del diccionario
    dias = data["stats"]  # Recordar:Acceder a valores de un diccionario lo hago a travès de corchetes
    #print(dias)
    for dia in dias:
        print(dia)
        consolidado.append({
            "total":dia["q_count"],
            "Buenas":dia["success"],
            "Malas":dia["fail"]
        })
df=pd.DataFrame(consolidado)
print(df.shape)
###########GRAFICARLO
y1=df['total'].tolist()
y2=df['Buenas'].tolist()
y3=df['Malas'].tolist()
promedio=df.describe()
print(promedio)
promedio_total=[]
promedio_Buenas=[]
promedio_Malas=[]
x=df.index.tolist()
print("dias:   ", x)
print("Buenas: ",y2)
print("Malas:  ",y3)
conteo=0
cantidad=len(x)
for valor in x:
    conteo=conteo+1
    z_B=df.loc[cantidad-conteo:cantidad,'Buenas']
    z_M=df.loc[cantidad-conteo:cantidad,'Malas']
    z_T=df.loc[cantidad-conteo:cantidad,'total']
    promedio_total.append(z_T.mean())
    promedio_Buenas.append(z_B.mean())
    promedio_Malas.append(z_M.mean())
promedio_total=promedio_total[::-1]
promedio_Buenas=promedio_Buenas[::-1]
promedio_Malas=promedio_Malas[::-1]
plt.scatter(x,y1, label='Total',color='black')
plt.scatter(x,y2,label='Buenas',color='green')
plt.scatter(x,y3,label='Malas',color='red')
plt.plot(x,promedio_total,label='Promedio acumulado total',color='black',linewidth=2)
plt.plot(x,promedio_Buenas,label='Promedio acumulado Buenas',color='green',linewidth=2)
plt.plot(x,promedio_Malas,label='Promedio acumulado Malas',color='red',linewidth=2)

plt.title('Cantidades Realizadas')
plt.ylabel('Cantidad')
plt.xlabel('Dias atràs')

plt.legend()
plt.grid()
plt.show()
#NORMALIZACION DE DATOS al reverso para verlo mas facil
df_v1=pd.DataFrame(consolidado)
df_v1['Buenas']=df_v1['Buenas']*100/df_v1['total']
df_v1['Malas']=df_v1['Malas']*100/df_v1['total']
conteo=0
cantidad=len(x)
porcentaje_Buenas=[]
porcentaje_Malas=[]
for valor in x:
    conteo=conteo+1
    p_B=df_v1.loc[cantidad-conteo:cantidad,'Buenas']
    p_M=df_v1.loc[cantidad-conteo:cantidad,'Malas']
    porcentaje_Buenas.append(p_B.mean())
    porcentaje_Malas.append(p_M.mean())

porcentaje_Buenas=porcentaje_Buenas[::-1]
porcentaje_Malas=porcentaje_Malas[::-1]

###########GRAFICARLO
y2=df_v1['Buenas'].tolist()
y3=df_v1['Malas'].tolist()
x=df_v1.index.tolist()

plt.scatter(x,y2,label='Buenas',color='green')
plt.scatter(x,y3,label='Malas',color='red')
plt.plot(x,porcentaje_Buenas,label='Promedio % acumulado Buenas',color='green',linewidth=2)
plt.plot(x,porcentaje_Malas,label='Promedio % acumulado Malas',color='red',linewidth=2)

plt.title('Porcentaje de Realizadas')
plt.ylabel('%')
plt.xlabel('Dias atràs')

plt.legend()
plt.grid()

plt.show()