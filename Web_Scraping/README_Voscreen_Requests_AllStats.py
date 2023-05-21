# Análisis y visualización de datos de Voscreen

Este código es un script de Python que utiliza la biblioteca `requests`, `pandas` y `matplotlib` para realizar un análisis y visualización de datos de Voscreen. Voscreen es una plataforma de aprendizaje de idiomas en línea que proporciona ejercicios interactivos de comprensión auditiva en varios idiomas.

El objetivo de este script es obtener datos de Voscreen a través de su API y visualizar la cantidad de ejercicios realizados, los aciertos y errores, así como calcular los promedios acumulados y porcentajes de aciertos y errores a lo largo del tiempo.

## Requisitos del sistema

- Python 3.x
- Las bibliotecas `requests`, `pandas` y `matplotlib`. Puedes instalarlas ejecutando el siguiente comando:


## Uso

1. Abre el archivo `main.py` en un entorno de desarrollo de Python o en la línea de comandos.
2. Asegúrate de tener configurado el token de autenticación. Puedes editar la variable `Token` en el código para insertar tu token de acceso válido.
3. Ejecuta el script. Los datos serán solicitados a la API de Voscreen y se generará una visualización gráfica.

## Resultados

El script generará dos gráficas:

1. "Cantidades Realizadas": Esta gráfica muestra la cantidad total de ejercicios realizados, la cantidad de aciertos y la cantidad de errores a lo largo del tiempo. También muestra el promedio acumulado de cada categoría.
2. "Porcentaje de Realizadas": Esta gráfica muestra el porcentaje de aciertos y errores en relación con la cantidad total de ejercicios realizados a lo largo del tiempo.

## Contribuciones

Siéntete libre de contribuir a este proyecto. Puedes enviar pull requests con mejoras o nuevas funcionalidades.

## Limitaciones

- Este código utiliza la API de Voscreen para obtener los datos. Asegúrate de tener un token de acceso válido para utilizar la API.
- El código puede requerir ajustes o modificaciones según los cambios en la API de Voscreen.

## Atribuciones

- Este proyecto es desarrollado por Sebastian Chaves Tequia.
- El código base utiliza las bibliotecas `requests`, `pandas` y `matplotlib` bajo sus respectivas licencias.

##Para encontrar el Token:
Ve a la página Web de Voscreen, ingresa con tu usuario,luego clic derecho, Inspeccionar, luego en Network, ve a la sección de Stats, aparecerá una línea en la sección de Inspeccionar que dice "Stats", seleccionala y baja la barra hasta encontrar el campo que dice "Authorization" Copia todo el texto que tiene asignado ese campo y pégalo en el código donde dice "Token= "{Aqui pegas tu texto}""
