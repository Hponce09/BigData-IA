import numpy as np

"""
Ejercicio 1. Crear la estructura de datos
Crea una estructura de datos en Python que guarde toda la información de la tabla anterior.
Piensa primero cuál es la forma más cómoda de organizar los datos: una lista para cada columna, un
diccionario de listas o una lista de diccionarios.
Recomendación: usa un diccionario donde cada clave sea una columna.
- "nombre"
- "edad"
- "puntos"
- "estudios_superiores"
- Para estudios_superiores, usa valores booleanos: True o False
"""
datos = [
    {"Nombre": "Ana", "Edad": 23, "Puntos": 43, "Estudios superiores": True},
    {"Nombre": "Paco", "Edad": 21, "Puntos": 38, "Estudios superiores": False},
    {"Nombre": "Marta", "Edad": 19, "Puntos": 41, "Estudios superiores": True},
    {"Nombre": "Luis", "Edad": 25, "Puntos": 35, "Estudios superiores": False},
    {"Nombre": "Elena", "Edad": 22, "Puntos": 39, "Estudios superiores": True},
    {"Nombre": "Carlos", "Edad": 20, "Puntos": 36, "Estudios superiores": True},
    {"Nombre": "Sara", "Edad": 18, "Puntos": 34, "Estudios superiores": False},
    {"Nombre": "Miguel", "Edad": 27, "Puntos": 45, "Estudios superiores": False},
    {"Nombre": "Lucia", "Edad": 21, "Puntos": 42, "Estudios superiores": True},
    {"Nombre": "Andres", "Edad": 24, "Puntos": 37, "Estudios superiores": False},
]

import pandas as pd
df = pd.DataFrame(datos)
print(df)
"""
Ejercicio 3. Explorar el DataFrame
Usa métodos básicos de pandas para conocer mejor los datos antes de modificarlos.
Debes mostrar las primeras filas, el tamaño del DataFrame, las columnas, los tipos de datos, la
información general y las estadísticas básicas.
- head()
- shape
- columns
- dtypes
- info()
- describe()
"""
print("\n ejercicio 3\n")

print(f"primeras filas: \n{df.head()}")
print(f"número de filas y columnas: \n{df.shape}")
print(f"nombres de las columnas: \n{df.columns}")
print(f"tipos de datos: \n{df.dtypes}")
print(f"información general: \n{df.info()}")
print(f"estadísticas básicas: \n{df.describe()}")

"""
Ejercicio 4. Crear una regla de selección
Queremos decidir si una persona es apta para el trabajo.
Antes de programarlo, escribe la lógica con tus propias palabras.
- Si tiene 22 años o más, será apta si tiene al menos 40 puntos.
- Si tiene menos de 22 años, solo será apta si tiene estudios superiores y al menos 35 puntos.
- En cualquier otro caso, no será apta.

solo sera apto en dos condiciones la primera si es mayor de 22 y tiene 40 o mas puntos o si tiene menos de 22, debe tener estudios superiores y al menos 35 puntos.  
"""
 

"""
Ejercicio 5. Añadir una nueva columna
Añade al DataFrame una nueva columna llamada apto.
La columna debe contener True si la persona es apta y False si no lo es.
Después, muestra el DataFrame completo con la nueva columna
"""
print("\n ejercicio 5\n")

df["Apto"] =((df['Edad'] >= 22) & (df['Puntos'] >= 40)) | (df['Edad'] < 22) & ((df['Puntos'] >= 35) & (df['Estudios superiores']))

print(df)

"""
Ejercicio 6. Contar personas aptas y no aptas
Usa pandas para contar cuántas personas son aptas y cuántas no.
El objetivo es practicar el recuento de valores dentro de una columna.
- Método recomendado: value_counts()
"""

print("\n ejercicio 6\n")

print(df['Apto'].value_counts())

"""
Ejercicio 7. Filtrar candidatos aptos
Crea un nuevo DataFrame llamado candidatos_aptos.
Debe contener solo las personas que han sido aceptadas para el trabajo.
Después, muestra esa tabla por pantalla.
"""
print("\n ejercicio 7\n")

candidatos_aptos = df[df['Apto']]
print(candidatos_aptos)

"""
Ejercicio 8. Filtrar candidatos con estudios superiores
Crea otro DataFrame con las personas que tienen estudios superiores.
Después, responde a las preguntas indicadas.
- Cuántas personas tienen estudios superiores.
- Cuántas de ellas son aptas.
- Hay alguna persona con estudios superiores que no sea apta.
"""
print("\n ejercicio 8\n")


candidatos_es = df[df['Estudios superiores']]
print(f"personas con {candidatos_es['Estudios superiores'].value_counts()}")
print(f"personas Apto y no {candidatos_es['Apto'].value_counts()}")

print(candidatos_es)

"""
Ejercicio 9. Ordenar los candidatos
Ordena el DataFrame por la columna puntos.
Debes mostrar la tabla ordenada de menor a mayor puntuación y después de mayor a menor
puntuación.
- Método recomendado: sort_values().
"""
print("\n ejercicio 9\n")
df_ordenado_men_may = df.sort_values(by='Puntos')
df_ordenado_may_men = df.sort_values(by='Puntos', ascending=False)

print(df_ordenado_men_may)
print(df_ordenado_may_men)

"""
Ejercicio 10. Calcular estadísticas
Calcula estadísticas básicas usando pandas.
Estas operaciones ayudan a interpretar los datos antes de tomar decisiones.
- Edad media.
- Puntuación media.
- Puntuación máxima.
- Puntuación mínima.
- Edad de la persona más joven.
- Edad de la persona más mayor.
- Métodos útiles: mean(), max(), min().
"""
print("\n ejercicio 10\n")
edad_media = df["Edad"].mean()
edad_max = df['Edad'].max()
edad_min = df['Edad'].min()

puntuacion_media = df['Puntos'].mean()
puntuacion_max = df['Puntos'].max()
puntuacion_min = df['Puntos'].min()

print(f"edad media: {edad_media}")
print(f"edad maxima: {edad_max}")
print(f"edad minima: {edad_min}")

print(f"puntuacion media: {puntuacion_media}")
print(f"puntuacion max: {puntuacion_max}")
print(f"puntuacion min: {puntuacion_min}")

"""
Ejercicio 11. Crear una columna de nivel
Añade una nueva columna llamada nivel.
La columna debe clasificar a cada persona según sus puntos.
- "alto" si tiene 40 puntos o más.
- "medio" si tiene entre 35 y 39 puntos.
- "bajo" si tiene menos de 35 puntos.
"""

print("\n ejercicio 11\n")
condiciones=[
    df['Puntos']>=40,
    df['Puntos']>=35
]

valores = ['Alto','Medio']

df['Nivel'] = np.select(condiciones,valores,default='Bajo')

print(df)

"""
Ejercicio 12. Agrupar por nivel
Agrupa los datos por la columna nivel.
Calcula cuántas personas hay en cada nivel, la media de edad en cada nivel y la media de puntos en
cada nivel.
- Método recomendado: groupby().
"""
print("\n ejercicio 12\n")
print('media de puntos')
print(df.groupby('Nivel')['Puntos'].mean())

print('media de edad')
print(df.groupby('Nivel')['Edad'].mean())

print('personas por nivel')
print(df['Nivel'].value_counts())


"""
Ejercicio 13. Seleccionar columnas concretas
Crea un nuevo DataFrame que solo contenga las columnas nombre, puntos y apto.
Este ejercicio sirve para practicar cómo seleccionar solo la información importante.
"""
print("\n ejercicio 13\n")

df_nuevo = df[["Nombre", "Puntos", "Apto"]]
print(df_nuevo)

"""
Ejercicio 14. Renombrar columnas
Renombra las columnas para que tengan nombres más descriptivos.
Por ejemplo, nombre puede pasar a Nombre del candidato y puntos a Puntuación.
"""

print("\n ejercicio 14\n")

df_modificado = df.rename(columns={'Nombre':'Nombre del candidato','Puntos':'Puntuacion'})
print(df_modificado)