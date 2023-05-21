# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:22:45 2023

@author: 50512
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import warnings
warnings.filterwarnings("ignore")

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts) # REMPLAZA AQUI EL NOMBRE DE TU CHROME DRIVER

driver.get('https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores-Portatiles') #URL Semilla
driver.execute_script("window.scrollTo({top: 5000, behavior: 'smooth'});") #Hacer Scroll
sleep(2)
driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
sleep(2)
driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'});")
sleep(3)

productos = driver.find_elements_by_xpath('//div[contains(@class," search-results-list")]')
i=1
print("Total de productos 1pag. : ",len(productos))
print("********")
for producto in productos:
    
    marca=producto.find_element_by_xpath('.//a/div/div/div/b[contains(@class,"title")]').text
    nombre=producto.find_element_by_xpath('.//span/b[contains(@class,"pod-subTitle")]').text
    
    try: #Porque no todos los productos están en promociones
        precio=producto.find_element_by_xpath('.//span[contains(@class,"primary high jsx")]').text
    except:
        precio=producto.find_element_by_xpath('.//span[contains(@class,"primary medium jsx")]').text
    
    print(i)
    print(marca)
    print(nombre)
    print(precio)
    print()
    i=i+1
driver.close()