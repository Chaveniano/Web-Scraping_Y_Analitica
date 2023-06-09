# -*- coding: utf-8 -*-
"""
OBJETIVO:
    - Extraer el precio, titulo y descripcion de productos en Mercado Libre.
    - Aprender a realizar extracciones verticales y horizontales con Selenium.
    - Aprender a definir user_agents en Selenium
CREADO POR: Sebastian Chaves
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import warnings
warnings.filterwarnings("ignore")

# Definimos el User Agent en Selenium utilizando la clase Options
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts) # REMPLAZA AQUI EL NOMBRE DE TU CHROME DRIVER

#URL SEMILLA
driver.get('https://listado.mercadolibre.com.ec/smart-watch#D[A:smart%20watch]')


# LOGICA DE MAXIMA PAGINACION CON LAZO WHILE
# VECES VOY A PAGINAR HASTA UN MAXIMO DE 10
PAGINACION_MAX = 10
PAGINACION_ACTUAL = 1

# Mientras la pagina en la que me encuentre, sea menor que la maxima pagina que voy a sacar... sigo ejecutando...
while PAGINACION_MAX > PAGINACION_ACTUAL:

  links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]')
  links_de_la_pagina = []
  for a_link in links_productos:
    links_de_la_pagina.append(a_link.get_attribute("href"))
  # Q: Pero leaonrdo, porque no hiciste for link in link_productos, y simplemente ibas y volvias haciendo click en el contenedor que me lleva a la otra pagina?
  # A: Porque al yo irme y volver, pierdo la referencia de links_productos que tuve inicialmente. Y selenium me daria error porque le intentaria dar click a algo que no existe en el DOM actual.
  # Es por esto que, la mejor estrategia es obtener todos los links como cadenas de texto y luego iterarlos.

  for link in links_de_la_pagina:

    try:
      # Voy a cada uno de los links de los detalles de los productos
      driver.get(link)

      # Rara vez da error si no utilizamos una espera por eventos:
      # precio_element = WebDriverWait(driver, 10).until(
      #   EC.presence_of_element_located((By.XPATH, '//span[includes(@class,"price-tag")]'))
      # )
      titulo = driver.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]').text
      simbolo=driver.find_element(By.XPATH, '//span[@class="andes-money-amount__currency-symbol"]').text
      precio = driver.find_element(By.XPATH, '//span[@class="andes-money-amount__fraction"]').text
      descripcion=driver.find_element(By.XPATH, '//p[@class="ui-pdp-description__content"]').text
      print (titulo)
      print (simbolo,precio.replace('\n', '').replace('\t', ''))
      print("Descripcion: ",descripcion[0:50],'...')
      print(" ")

      # Aplasto el boton de retroceso
      driver.back()
    except Exception as e:
      print (e)
      # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
      driver.back()

  # Logica de deteccion de fin de paginacion
  time.sleep(3)
  try:
    # Intento obtener el boton de SIGUIENTE y le intento dar click
    #puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
    puedo_seguir_horizontal = driver.find_element(By.XPATH, '//a[@title="Siguiente"]')
    puedo_seguir_horizontal.click()
  except:
    
    # Si obtengo un error al intentar darle click al boton, quiere decir que no existe
    # Lo cual me indica que ya no puedo seguir paginando, por ende rompo el While
    break

  PAGINACION_ACTUAL += 1