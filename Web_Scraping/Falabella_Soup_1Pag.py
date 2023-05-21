# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:00:37 2023

@author: 50512
"""
import requests
from bs4 import BeautifulSoup
#import warnings
#warnings.filterwarnings("ignore") #Temproral, porque sé cual es el Warning

custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
}

#url_semilla = "https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores--Portatiles-"
url_semilla = "https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores-Portatiles"

resp = requests.get(url_semilla)
soup = BeautifulSoup(resp.text, 'lxml')

#descargas = soup.find_all('a', class_="download-button")
productos=soup.find_all('div',class_="jsx-200723616 search-results-list")
i = 0
print(len(productos))
for producto in productos:
    marca = producto.find('b',class_="pod-title").text
    nombre = producto.find('b',class_="pod-subTitle").text
    #input(nombre)
    precio = producto.find('ol',class_="jsx-2112733514 ol-4_GRID pod-prices fa--prices li-separation")
    #precio = precio.find('span',class_="jsx-2889528833").text
    precio=precio.select_one(".jsx-2889528833").text
    #input("dd")
    print(i)
    print(marca)
    print(nombre)
    print(precio)
    print()
    i+=1