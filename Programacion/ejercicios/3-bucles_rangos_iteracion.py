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



"""
Ejercicio 4. Números pares, impares y múltiplos
Usando range, recorre los números del 1 al 50.
El programa debe:
- Contar cuántos números son pares.
- Contar cuántos números son impares.
- Contar cuántos números son múltiplos de 5.
- Mostrar los tres resultados finales.
Condición: Debe utilizar for, range, el operador módulo % y contadores
"""

print("\nSolucion de ejercicio 4")

pares = 0
impares = 0
multiplo5 = 0


for n in range (1,51):
    if n % 2 == 0:
        pares += 1
    elif n % 2 == 1:
        impares += 1

    if n % 5 == 0:
        multiplo5 += 1
        
    #print(n)

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros multiplos de 5: {multiplo5}")

"""
Ejercicio 5. Validación de contraseña
Crea una variable llamada password con una contraseña de prueba.
El programa debe:
- Comprobar si la contraseña tiene al menos 8 caracteres.
- Comprobar si contiene el símbolo @.
- Comprobar que no sea igual a 12345678.
- Si cumple todas las condiciones, mostrar Contraseña válida.
- En caso contrario, mostrar Contraseña no válida.
Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro
del texto puede utilizarse "@" in password.
"""

print("\nSolucion de ejercicio 5")

password = input("ingrese contraseña: ")
cantidad = len(password)
if cantidad >= 8 and password != "12345678" and "@" in password:
    print("contrasena valida")
else:
    print("contrasena invalida")


"""
Ejercicio 6. Inventario de productos
Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades
disponibles.
inventario = {
 "ratón": 12,
 "teclado": 5,
 "monitor": 0,
 "cable": 25
}
El programa debe:
- Mostrar todos los productos y sus unidades.
- Mostrar qué productos están agotados.
- Calcular cuántas unidades hay en total.
- Mostrar cuántos productos tienen menos de 10 unidades.
Condición: Debe utilizar diccionarios, items(), acumuladores, contadores e if.
"""
print("\nSolucion de ejercicio 6")


inventario = {
 "ratón": 12,
 "teclado": 5,
 "monitor": 0,
 "cable": 25
}
menosTenUni={}
agotados = {}
total = 0
for pro, unid in inventario.items():
    print(pro , unid)
    if unid <= 0:
        agotados[pro],[unid]=inventario[pro],[unid]
    if unid < 10 and unid > 1:
        menosTenUni[pro],[unid]=inventario[pro],[unid]
    total += inventario[pro]
    

for a,b in agotados.items():
    print(f"agotados : producto {a} {b}")

for inv in menosTenUni.items():
    print(f"productos con menos de 10 unidades: {inv}")

print(f"total: {total}")

"""
Ejercicio 7. Búsqueda en una lista
Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar.
El programa debe:
- Recorrer la lista buscando ese nombre.
- Si encuentra el nombre, mostrar en qué posición está.
- Cuando lo encuentre, detener la búsqueda.
- Si no lo encuentra, mostrar Alumno no encontrado.
Condición: Debe utilizar listas, for, enumerate, if, break y una variable booleana de control
"""

print("\nSolucion de ejercicio 7")

alumnos = ["Mateo", "Sofía", "Lucas", "Valentina", "Martín", "Emma", "Leo", "Lucía", "Hugo", "Olivia"]
search = input("nombre de la busqueda: ")
mensaje = ""

for i,b in enumerate(alumnos):
    if b.lower() == search.lower():
        mensaje = (f" posicion: {i}, busqueda: {b}")
        break
    else:
        mensaje ="Alumno no encontrado."

    #print(b)


print(mensaje)
    

"""
Ejercicio 8. Limpieza de datos
Crea una lista con varios números, incluyendo positivos, negativos y ceros.
El programa debe:
- Recorrer la lista completa.
- Ignorar los números negativos usando continue.
- Sumar solo los números positivos.
- Contar cuántos ceros hay.
- Mostrar la suma final y la cantidad de ceros.
Condición: Debe utilizar listas, for, continue, un acumulador y un contador.
"""

print("\nSolucion de ejercicio 8")

numeros = [-15, 42, 0, -8, 19, 0, -3, 7, -21, 5, 0, -12, 33, 0, -1]
positivos = 0
ceros = 0
for n in numeros:
    if n < 0:
        continue
    elif n == 0:
        ceros += 1
    else:
        positivos += n

    #print(n)

print(f'cantidad de  0 : {ceros}')
print(f'la sumatoria de positivos : {positivos}')

"""
Ejercicio 9. Clasificación de usuarios
Crea una lista de diccionarios. Cada diccionario representa un usuario con los siguientes datos:
nombre
edad
activo
puntos
El programa debe:
- Clasificar como Premium a los usuarios activos con 100 puntos o más.
- Clasificar como Estándar a los usuarios activos con menos de 100 puntos.
- Clasificar como Inactivo a los usuarios que no estén activos.
- Además, si el usuario es menor de 18 años, debe indicarse como usuario menor de edad.
- Mostrar el nombre de cada usuario y su clasificación.
Condición: Debe utilizar una lista de diccionarios, bucle for, booleanos, if, elif, else y operadores lógicos.
"""
print("\nSolucion de ejercicio 9")
clasificacion = ""
usuarios = [
    {"nombre": "Mateo", "edad": 14, "activo": True, "puntos": 150},
    {"nombre": "Sofía", "edad": 31, "activo": False, "puntos": 85},
    {"nombre": "Lucas", "edad": 19, "activo": True, "puntos": 320},
    {"nombre": "Valentina", "edad": 28, "activo": True, "puntos": 210},
    {"nombre": "Martín", "edad": 45, "activo": False, "puntos": 0},
    {"nombre": "Emma", "edad": 22, "activo": True, "puntos": 95},
    {"nombre": "Leo", "edad": 17, "activo": False, "puntos": 140},
    {"nombre": "Lucía", "edad": 29, "activo": True, "puntos": 480},
    {"nombre": "Hugo", "edad": 52, "activo": True, "puntos": 60},
    {"nombre": "Olivia", "edad": 26, "activo": False, "puntos": 175}
]
for u in usuarios:
    if u["activo"] and u["puntos"] >= 100:

        if u["edad"] >=18:
            clasificacion="premium"
            print(f"{u["nombre"]}, {clasificacion}")
        else:
            clasificacion="premium"
            print(f"{u["nombre"]}, {clasificacion}, usuario menor de edad")  
    elif u["activo"] and u["puntos"] < 100:    

        if u["edad"] >=18:
            clasificacion="estandar"
            print(f"{u["nombre"]}, {clasificacion}")
        else:
            clasificacion="estandar"
            print(f"{u["nombre"]}, {clasificacion}, usuario menor de edad")            
    else:

        if u["edad"] >= 18:
            clasificacion="inactivo"
            print(f"{u["nombre"]}, {clasificacion}")
        else:
            clasificacion="inactivo"
            print(f"{u["nombre"]}, {clasificacion}, usuario menor de edad")

    #print(u["nombre"],u["edad"])


"""
Ejercicio 10. Sistema de intentos
Crea una variable codigo_correcto y una lista llamada intentos con varios códigos introducidos.
El programa debe:
- Recorrer todos los intentos.
- Mostrar cada intento realizado.
- Si un intento está vacío, debe entrar en una condición donde se use pass como marcador.
- Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle.
- Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado.
Condición: Debe utilizar listas, for, if, elif, else, break, pass, una variable booleana y un condicional final.
"""

print("\nSolucion de ejercicio 10")
codigo_correcto = input("ingresa el codigo")
intentos = ["0000", "B456", "A123", "", "9999", "A123"]
intento = 0
for i in intentos:
    print(i)
    intento += 1
    last = len(intentos)
    if i == "":
        pass
    elif i == codigo_correcto:
        print("Acceso concedido")
        break
    else:
        #print(intento,last)
        if intento == last:
            print("Acceso denegado")
    #intento += 1
    #print(intento,last)
    #print(i)