'''
Ejercicio 1. Control de notas
Crea una lista llamada notas con al menos 10 calificaciones numéricas.
El programa debe:
- Mostrar todas las notas.
- Calcular cuántas notas están aprobadas y cuántas suspendidas.
- Calcular la nota media.
- Mostrar la nota más alta y la nota más baja.
- Indicar si la media final está aprobada o suspendida.
Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.
'''

print("Solucion de ejercicio 1")

notas = [5.6,6,8,9.5,2.7,4,1.1,9.9,3.9,7.3]
aprobados = 0
suspendidas = 0
sumatoriaNotas=0
notaAlta = 0
notaBaja = 100
for nota in notas:
    sumatoriaNotas+=nota
    media = sumatoriaNotas/len(notas)

    if nota >=5:
        aprobados+=1
    else:
        suspendidas+=1

    if notaAlta < nota:
        notaAlta = nota
    elif notaBaja > nota:
        notaBaja = nota
        
    print(f"notas: {nota}")

if media >=5:
    mensaje = "la media final está aprobada"
else:
    mensaje = "la media final está suspendida"
#print(f"el total de las notas es: {sumatoriaNotas}")
#media = sumatoriaNotas/len(notas)
print(f"La media es: {media}")
print(f"La nota mas alta es :{notaAlta}")
print(f"La nota mas baja es :{notaBaja}")

print(f"Numeros de alumnos aprobados: {aprobados}")
print(f"Numeros de alumnos suspendidos: {suspendidas}")
print(mensaje)


"""
Ejercicio 2. Carrito de la compra
Crea dos listas: una con nombres de productos y otra con sus precios.
productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]
El programa debe:
- Mostrar cada producto con su precio.
- Calcular el precio total de la compra.
- Aplicar un descuento del 10% si el total supera 20 euros.
- Mostrar el total final que debe pagarse.
Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.
"""

print("\nSolucion de ejercicio 2")

productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 20.80]

totalPrecios = 0

for pro, pre in zip (productos,precios):
    print(pre,pro)
    totalPrecios+=pre

if totalPrecios > 20:
    descuento = totalPrecios * 0.20
    totalPagar = totalPrecios - descuento
    print(f"Pago con descuento incluido: {totalPagar}")
else:
    totalPagar = totalPrecios
    print(f"Pago sin descuento incluido: {totalPagar}")

print(f"Total de la compra es: {totalPagar}")

"""
Ejercicio 3. Registro de alumno
Crea un diccionario llamado alumno con los siguientes datos:
nombre
edad
curso
nota_media
faltas
El programa debe:
- Mostrar todos los datos del alumno.
- Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
- Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
- Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.
"""

print("\nSolucion de ejercicio 3")
aprSus = ""
aviso =""

alumno = {
    "nombre":"Juan",
    "edad": 17,
    "curso": "IA",
    "nota_media":8.5,
    "faltas":12
}

for a in alumno.items():
    print(a)

if alumno["nota_media"] >= 5:
    aprSus ="aprueba"
    print(f"{aprSus}")

if alumno["faltas"] > 10:
    aviso=f"Las faltas superan el rango establecido {alumno['faltas']}"
    print(f"Las faltas superan el rango establecido {alumno['faltas']}")

print(f"el alumno {aprSus}, pero {aviso}")