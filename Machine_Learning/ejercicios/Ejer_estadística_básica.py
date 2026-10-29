# %%
from pathlib import Path
import pandas as pd
import math


BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "datos_estadistica_alumnos.csv")


"""
Ejercicio 1. Carga y exploración de datos
- Carga el archivo CSV en un DataFrame llamado df.
- Muestra las primeras filas.
- Guarda la columna puntos_prueba en una variable llamada puntos.
- Muestra cuántos datos hay en la columna.
- Explica con tus palabras qué representa cada fila del CSV.
Pandas que puedes usar: read_csv(), head(), len().

"""

puntos = list(df["puntos_prueba"])


print("Ejercicio 1\n")

print(df.head())
print(f"datos de la columna: {len(puntos)}")

# Cada fila muestra los datos de ese alumno (id y nombre), las horas que dedicó a estudiar (horas_estudio), 
# la calificación obtenida en el examen (puntos_prueba), el numero de ejercicios entregados (ejercicios_entregados) 
# y el tiempo que estubo activo en la plataforma virtual (minutos_plataforma).

"""
Ejercicio 2. Media
- Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len().
- Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda.
- Calcula la misma media con el Método 3: pandas usando .mean().
- Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas.
- Comprueba que los tres resultados coinciden.
- Explica qué significa esa media en el contexto de la prueba.
Pandas que puedes usar: df["puntos_prueba"].mean().

"""
print("\nEjercicio 2\n")

suma = 0
# Método 1: bucle
for valor in puntos:
    suma+=valor

media_bucle = suma/len(puntos)

# Método 2: funciones
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

# Método 3: pandas
media_pandas = df["puntos_prueba"].mean()

print(f"Media programacion: {media_bucle}")
print(f"Media pyhton: {media_funciones}")
print(f"Media pandas:{media_pandas}")

# La media nos muestra el rendimiento geneneral del grupo, podemos analizar el rendimiento de un 
# alumno con respecto al la media del grupo

"""
Ejercicio 3. Mediana
- Calcula la mediana de puntos_prueba con el Método 1: ordenar la lista, comprobar si la cantidad de datos es par o impar y acceder por índice.
- Calcula la misma mediana con el Método 2: sorted(), len() y acceso por índice. En este caso map() no es necesario.
- Calcula la misma mediana con el Método 3: pandas usando .median().
- Muestra los tres resultados con nombres claros: mediana_bucle, mediana_funciones y mediana_pandas.
- Comprueba que los tres resultados coinciden.
- Explica por qué la mediana representa el centro de los datos.
Pandas que puedes usar: df["puntos_prueba"].median().

"""
print("\nEjercicio 3\n")
auxiliar = 0
# Método 1: bucle

print(puntos)

"""
for i in  range(len(puntos)):
    for j in range(i+1 ,len(puntos)):
        if puntos[i]>puntos[j]:
            auxiliar = puntos[j]
            puntos[j] = puntos[i]
            puntos[i] = auxiliar
            

print (puntos)

if len(puntos) % 2 == 0:
    
    print(len(puntos))
    for x in range(puntos[4],puntos[5]):
        suma = puntos[4]+puntos[5]
    
    mediana_bucle = suma/2
    print(f"Mediana por programacion: {mediana_bucle}")
else:
    print("impar")
"""
# Método 2: funciones

ordenada = sorted(puntos)
print(ordenada)
cantida = len(puntos)
print(f"cantidad: {cantida}")
suma_Funcinon = ordenada[4]+ordenada[5]
mediana_funcion = suma_Funcinon/2
print(f"mediana por funcion: {mediana_funcion}")

# Método 3: pandas

serie = pd.Series(puntos)
mediana_pandas = serie.median()
print(f"Mediana por pandas{mediana_pandas}")

# la mediana representa el centro de los datos por que es la que parte los datos buscando el centro por la posicion fisica

"""
Ejercicio 4. Moda
- Calcula la moda de puntos_prueba con el Método 1: recorre la lista con un bucle y crea un diccionario de frecuencias.
- Calcula la misma moda con el Método 2: usa set(), count(), max() y una lambda para encontrar el valor más repetido.
- Calcula la misma moda con el Método 3: pandas usando .mode().
- Muestra los tres resultados con nombres claros: moda_bucle, moda_funciones y moda_pandas.
- Comprueba que los tres resultados coinciden.
- Explica qué significa que ese valor sea la moda.
Pandas que puedes usar: df["puntos_prueba"].mode().

"""
print("\nEjercicio 4\n")
# Método 1: bucle
contador = {}

for c in puntos:
    if c in contador:
        contador[c]+=1
        
    else:
        contador[c]=1

print(f"Moda bucle: {contador}")

# Método 2: funciones

moda_funcion = max(set (puntos),key = lambda x : puntos.count(x))
print(f"Moda funciones: {moda_funcion}")


# Método 3: pandas

serie_moda= pd.Series(puntos)
moda_pandas= serie_moda.mode()
print(f"Moda de pandas: \n{moda_pandas}")

#este valor es el que mas se repite en los datos es la moda

"""
Ejercicio 5. Desviación de cada dato respecto a la media
- Calcula primero la media de puntos_prueba.
- Calcula una lista de desviaciones con el Método 1: bucle for y append(). Cada valor debe ser punto - media.
- Calcula la misma lista con el Método 2: map() y lambda.
- Calcula las mismas desviaciones con el Método 3: pandas, restando la media directamente a la columna y creando una columna llamada desviacion.
- Muestra las tres versiones y comprueba que contienen los mismos valores.
- Explica qué significa que una desviación sea positiva, negativa o cero.
Pandas que puedes usar: df["desviacion"] = df["puntos_prueba"] - media.

"""
print("\nEjercicio 5\n")

# Método 1: bucle

desviacion=0
desviaciones_lista=[]

for i in puntos:
    desviacion = i - media_bucle
    desviaciones_lista.append(desviacion)

print(f'lista desviacion bucles: \n{desviaciones_lista}')

# Método 2: funciones
media_funciones

lista_des = list(map(lambda x : x - media_funciones,puntos))

print(f'lista desviacion funciones: \n{lista_des}')


# Método 3: pandas
media_pandas

df['desviacion'] = df['puntos_prueba']-media_pandas

print(f'lista desviacion pandas: \n{df}')

# la desviacion nos indica cuanto se aleja un valor con repecto al valor de la media

"""
Ejercicio 6. Varianza
- Calcula la varianza de puntos_prueba con el Método 1: bucle for, desviaciones, cuadrados y promedio final.
- Recuerda: primero se calcula cada desviación, después se eleva al cuadrado y finalmente se hace la media de esos cuadrados.
- Calcula la misma varianza con el Método 2: map(), lambda, sum() y len().
- Calcula la misma varianza con el Método 3: pandas usando ddof=0.
- Muestra los tres resultados con nombres claros: varianza_bucle, varianza_funciones y varianza_pandas.
- Comprueba que los tres resultados coinciden.
- Explica qué nos dice la varianza sobre el grupo.
Pandas que puedes usar: df["puntos_prueba"].var(ddof=0).

"""
print("\nEjercicio 6\n")
# Método 1: bucle
contador_diferencia = 0
contador_dato = 0
diferencias_cuadrado = []
for v in puntos:
    diferencias_cuadrado.append((v-media_bucle)**2)
    contador_dato += 1

print(diferencias_cuadrado)
print(contador_dato)

for i in diferencias_cuadrado:
    contador_diferencia += i

varianza_bucle = contador_diferencia/contador_dato

print(f'varianza bucle: {varianza_bucle}')

# Método 2: funciones

diferencia_funciones = list(map(lambda x : x **2,lista_des))

suma = sum(diferencia_funciones)

total_datos = len(diferencias_cuadrado)

varianza_funciones = suma/total_datos

print(f'varianza funciones: {varianza_funciones}')

# Método 3: pandas
 
varianza_pandas = df["puntos_prueba"].var(ddof=0)

print(f'varianza pandas: {varianza_pandas}')

# la varianza nosmuestra un valor bastante alejado de respecto a la media del grupo

"""
Ejercicio 7. Desviación estándar
- Calcula la desviación estándar con el Método 1: parte de la varianza calculada con bucles y aplica la raíz cuadrada.
- Calcula la misma desviación estándar con el Método 2: usa map(), lambda, sum(), len() y raíz cuadrada.
- Calcula la misma desviación estándar con el Método 3: pandas usando .std(ddof=0).
- Muestra los tres resultados con nombres claros: desviacion_estandar_bucle, desviacion_estandar_funciones y desviacion_estandar_pandas.
- Comprueba que los tres resultados coinciden o que solo cambian por pequeños decimales.
- Explica por qué la desviación estándar es más fácil de interpretar que la varianza.
Pandas que puedes usar: df["puntos_prueba"].std(ddof=0).

"""
print("\nEjercicio 7\n")
# Método 1: bucle

desviacion_estandar_bucle = varianza_bucle**0.5
print(f'desviacion estandar bubles: {desviacion_estandar_bucle}')

# Método 2: funciones

desviacion_estandar_funciones = math.sqrt(varianza_funciones)
print(f'desviacion estandar funciones: {desviacion_estandar_funciones}')

# Método 3: pandas

desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)
print(f'desviacion estandar pandas: {desviacion_estandar_pandas}')

#La desviación estándar utiliza las mismas unidades originales de los datos, a diferencia 
#de la varianza, cuyas unidades están elevadas al cuadrado y resultan imprecisas
"""
Ejercicio 8. Normalización min-max
- Calcula el mínimo y el máximo de puntos_prueba.
- Normaliza cada valor con el Método 1: bucle for y append(), usando la fórmula (valor - mínimo) / (máximo - mínimo).
- Normaliza los mismos valores con el Método 2: min(), max(), map() y lambda.
- Normaliza los mismos valores con el Método 3: pandas usando .min(), .max() y operaciones sobre columnas. Crea una columna llamada puntos_normalizados.
- Muestra las tres versiones y comprueba que contienen los mismos valores.
- Explica qué significa que un valor normalizado sea 0, 0.5 o 1.
Pandas que puedes usar: min(), max() y operaciones directas sobre columnas.

"""
print("\nEjercicio 8\n")
# Método 1: bucle
min_bucle = 999
max_bucle = 0
dato_r = 0 

resultado=[]

for i in puntos:
    if min_bucle > i:
        min_bucle = i
    elif max_bucle < i:
        max_bucle = i

#print(f"maximo: {min_bucle}\nminimo: {max_bucle}")

for i in puntos:
    dato_r = (i - min_bucle) / (max_bucle - min_bucle)
    resultado.append(dato_r)

print(f'bucle\n{resultado}')


# Método 2: funciones

min_funciones = min(puntos)
max_funciones = max(puntos)

resultado_funciones = list(map((lambda x:(x - min_funciones)/(max_funciones - min_funciones)),puntos))
print(f'funciones:\n{resultado_funciones}')

#print(f'minimo funciones: {min_funciones}\nmax funciones: {max_funciones}')

# Método 3: pandas
min_pandas = df['puntos_prueba'].min()

max_pandas = df['puntos_prueba'].max()

#print(f'minimo pandas: {min_pandas}\nmaximo: {max_pandas}')

df['puntos_normalizados'] = (df['puntos_prueba'] - min_pandas)/(max_pandas - min_pandas)
print(f'pandas\n{df}')

# 0.0 = Significa que ese elemento era el valor mínimo absoluto de toda la lista original.
# 0.5 = Significa que ese valor está exactamente a mitad de camino entre el peor y el mejor resultado.
# 1.0 = Significa que ese elemento era el valor máximo absoluto de toda la lista original.

"""
Ejercicio 9. Estandarización z-score
- Calcula la media y la desviación estándar de puntos_prueba.
- Estandariza cada valor con el Método 1: bucle for y append(), usando la fórmula z = (valor - media) / desviación estándar.
- Estandariza los mismos valores con el Método 2: map(), lambda y las variables media y desviación estándar ya calculadas.
- Estandariza los mismos valores con el Método 3: pandas usando .mean(), .std(ddof=0) y operaciones sobre columnas. Crea una columna llamada puntos_estandarizados.
- Muestra las tres versiones y comprueba que contienen los mismos valores.
- Explica qué significa que un valor z sea positivo, negativo o cercano a 0.
Pandas que puedes usar: mean(), std(ddof=0) y operaciones directas sobre columnas.

"""
print("\nEjercicio 9\n")
# Método 1: bucle
z_score_bucle = []
z = 0
for i in puntos:
    z = (i - media_bucle)/desviacion_estandar_bucle
    z_score_bucle.append(z)

print(f"\nEstandarización z-score por medio de bucles:\n{z_score_bucle}")

# Método 2: funciones

z_score_funciones = list(map((lambda x : (x - media_funciones)/desviacion_estandar_funciones),puntos))
print(f"\nEstandarización z-score por medio de funciones:\n{z_score_funciones}")

# Método 3: pandas

df['puntos_estandarizados'] = (puntos - media_pandas)/desviacion_estandar_pandas
print(df)

#Si el Z-score es positivo, significa que ese valor está por encima de la media.
#Si el Z-score es negativo, significa que ese valor está por debajo de la media.
#Un Z-score de 0 exacto significa que el dato está exactamente en la media.

"""
Ejercicio 10. Interpretación final
- Indica qué alumnos están por encima de la media usando el Método 1: bucle for y condicional.
- Indica los mismos alumnos usando el Método 2: filter() y lambda.
- Indica los mismos alumnos usando el Método 3: filtrado de pandas con condiciones sobre columnas.
- Indica qué alumnos están por debajo de la media usando también los tres métodos.
- Indica qué alumno o alumnos tienen el valor normalizado más alto.
- Indica qué alumno o alumnos tienen el valor normalizado más bajo.
- Indica si hay algún valor que parezca especialmente alejado del resto.
- Escribe una conclusión breve sobre el rendimiento general del grupo.

"""
print("\nEjercicio 10\n")
# Método 1: bucle
print('bucle')
for i,v in enumerate(puntos):
    if v > media_bucle:
        nombre=df.iloc[i]['nombre']
        print(f'\nalumno por encima de la media: {nombre}')

for i,v in enumerate(puntos):
    if v < media_bucle:
        nombre=df.iloc[i]['nombre']
        print(f'\nalumno por debajo de la media: {nombre}')        #print(i)


# Método 2: funciones
print('funciones')
media_mayor = list(filter(lambda x: (x > media_funciones), puntos))
print(f'por encima de la media: \n{media_mayor}')

media_menor = list(filter(lambda x: (x < media_funciones), puntos))
print(f'por debajo de la media: \n{media_menor}')

# Método 3: pandas

print('pandas')

df_filtrado_mayor = df[df['puntos_prueba'] > media_pandas]
print(df_filtrado_mayor)

df_filtrado_menor = df[df['puntos_prueba'] < media_pandas]
print(df_filtrado_menor)

normalizado_alto = df.loc[df["puntos_normalizados"].idxmax()]['nombre']
print(f'alumno tienen el valor normalizado más alto: {normalizado_alto}')

normalizado_bajo = df.loc[df["puntos_normalizados"].idxmin()]['nombre']
print(f'alumno tienen el valor normalizado más bajo: {normalizado_bajo}')
