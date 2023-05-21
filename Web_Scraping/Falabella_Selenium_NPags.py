# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:41:09 2023

@author: 50512
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts) # REMPLAZA AQUI EL NOMBRE DE TU CHROME DRIVER

driver.get('https://www.falabella.com.co/falabella-co/category/cat1361001/Computadores--Portatiles-')
PAGINACION_MAX = 5
PAGINACION_ACTUAL = 1
i=1
#win = driver.find_element_by_tag_name("window")
#driver.send_keys("-", Keys.CTRL)
#driver.execute_script("document.body.style.zoom='30%'")
while PAGINACION_MAX > PAGINACION_ACTUAL:
    sleep(2)
    driver.execute_script("window.scrollTo({top: 5000, behavior: 'smooth'});")
    sleep(2)
    driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
    sleep(2)
    driver.execute_script("window.scrollTo({top: 5000, behavior: 'smooth'});")
    sleep(2)
    
    driver.execute_script("window.scrollTo({top: 7800, behavior: 'smooth'});")
    sleep(2)
    driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'});")
    sleep(3)
    
    productos = driver.find_elements_by_xpath('//div[contains(@class," search-results-list")]')
    sleep(3)
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
    try:
        puedo_seguir_horizontal = driver.find_element(By.XPATH, '//button[@id="testId-pagination-bottom-arrow-right"]')
        
        puedo_seguir_horizontal.click()
        
    except:
        
        break

    PAGINACION_ACTUAL += 1
driver.close()