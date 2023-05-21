# Lottery
## Descripcion
Es una aplicación que permite obtener y analizar los resultados de diferentes loterías. Utiliza solicitudes HTTP para acceder a una API que proporciona los datos de los sorteos. A continuación, se resumen las principales funcionalidades del código:

El usuario puede especificar la cantidad de días de resultados que desea obtener y seleccionar la lotería de interés.
* Se realiza una solicitud a la API para obtener los resultados más recientes de la lotería seleccionada.
* Se procesan los datos obtenidos y se almacenan en un DataFrame para su posterior análisis.
* Se itera sobre los resultados históricos de los sorteos para obtener información detallada.
* Se generan estadísticas básicas sobre los números y series ganadoras.
* Se generan propuestas de números y series que superen un umbral de frecuencia definido.
* Se imprimen los resultados y propuestas generadas.

## Requisitos del sistema
Para ejecutar el código proporcionado, se requiere un entorno de desarrollo de Python con las siguientes dependencias y requisitos del sistema:

1. Python: El código está escrito en Python, por lo que necesitarás tener instalado Python en tu sistema. Se recomienda utilizar Python 3.x, preferiblemente la versión más reciente.

2. Bibliotecas:

* requests: Puedes instalar esta biblioteca ejecutando el siguiente comando en tu terminal: pip install requests
* pandas: Puedes instalar esta biblioteca ejecutando el siguiente comando en tu terminal: pip install pandas
* numpy: Puedes instalar esta biblioteca ejecutando el siguiente comando en tu terminal: pip install numpy

3. Conexión a Internet: El código realiza solicitudes a una API en línea para obtener los datos de los sorteos de lotería. Por lo tanto, necesitarás una conexión a Internet activa para acceder a la API y obtener los resultados.

## Funcionamiento
El código Python proporcionado realiza una serie de operaciones relacionadas con la obtención y el análisis de resultados de diferentes loterías. A continuación, se describe brevemente qué hace cada parte del código:

1. Importación de bibliotecas:

requests: Permite realizar solicitudes HTTP para obtener datos de una API.
pandas: Se utiliza para manipular y analizar datos en forma de DataFrames.
numpy: Proporciona soporte para operaciones numéricas y manejo de matrices.

2. Solicitud de entrada al usuario:

Se solicita al usuario que ingrese la cantidad de días de resultados que desea obtener.
Se muestra un menú de opciones para que el usuario elija una lotería.

3. Obtención de datos de la API:

Se construye una URL utilizando la elección del usuario y se realiza una solicitud GET a una API que proporciona los resultados de la lotería seleccionada.
Se extraen los datos de respuesta en formato JSON y se almacenan en un DataFrame de pandas llamado df_sorteo.

4. Bucle de obtención de resultados históricos:

Se itera sobre los identificadores de los sorteos obtenidos anteriormente.
Se construye una nueva URL para obtener los resultados históricos de cada sorteo.
Se realiza una solicitud GET a la API y se almacenan los datos de respuesta en un DataFrame llamado df_ganadores.
Los resultados de cada sorteo se concatenan en el DataFrame consolidado.

5. Análisis de datos y generación de estadísticas:

Se realizan operaciones de limpieza y transformación en el DataFrame consolidado para extraer información relevante de los números y series ganadoras.
Se realizan análisis estadísticos básicos sobre los números y series ganadoras, generando porcentajes y conteos.
Se definen funciones para generar propuestas de números y series que superen un umbral de frecuencia definido.
Se generan propuestas de números y series basadas en los análisis anteriores.

6. Resultados finales:

Se imprimen por pantalla las propuestas generadas para los diferentes elementos analizados, tanto para todos los resultados como para el premio mayor.

## Autor

- Nombre: Sebastian Chaves Tequia
- Contacto: sebastianchavestequia@gmail.com
