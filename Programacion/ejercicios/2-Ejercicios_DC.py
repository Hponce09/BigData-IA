"""
Ejercicio 1. Listas: control de notas
- Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7.
- Guarda en una variable primera_nota el primer elemento de la lista.
- Guarda en una variable ultima_nota el último elemento de la lista.
- Cambia la segunda nota de la lista por un 10.
- Añade una nueva nota, 8, al final de la lista.
- Guarda en una variable total_notas la cantidad de notas que hay en la lista.
- Muestra por consola la lista final, la primera nota, la última nota y el total de notas.

"""

print("Solucion de ejercicio 1")

notas = [6,8,5,9,7]
primera_nota = notas[0]
#ultima_nota = notas[len(notas)-1]
notas[1]=10
notas.append(8)
ultima_nota = notas[len(notas)-1]
total_notas = len(notas)

print(notas)
print(primera_nota)
print(ultima_nota)
print(total_notas)

"""
Ejercicio 2. Tuplas: datos fijos de un producto
- Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles.
- Por ejemplo: ("teclado", 25.50, 12).
- Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades.
- Calcula el valor total del stock multiplicando precio por unidades.
- Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock.

"""

print("\nSolucion de ejercicio 2")

producto = ("pantalla", 85.34, 17)
nombre_producto = producto[0]
precio_producto = producto[1]
unidades_producto = producto[2]
valor_total = precio_producto * unidades_producto
print(f"Nombre del producto: {nombre_producto}")
print (f"Precio del producto: {precio_producto}")
print(f"Unidades del producto: {unidades_producto}")
print(valor_total)

""""
Ejercicio 3. Diccionarios: ficha de alumno
- Crea un diccionario llamado alumno.
- El diccionario debe tener estas claves: nombre, edad, curso y nota.
- Usa valores concretos, por ejemplo: "Ana", 16, "IA" y 7.5.
- Muestra por consola el nombre del alumno usando la clave nombre.
- Muestra por consola la nota del alumno usando la clave nota.
- Cambia la nota del alumno por otro valor.
- Añade una nueva clave llamada aprobado. Su valor debe ser el resultado de comprobar si la nota es mayor o igual que 5.
- Muestra por consola el diccionario completo al final.

"""

print("\nSolucion de ejercicio 3")

alumno = {
    "nombre":"Axel",
    "edad":"33",
    "curso":"DAM",
    "nota":"7.9"
}

print(f"nombre del alumno {alumno['nombre']}")
print(f"nota del alumo {alumno['nota']}")
alumno['nota'] = 5
print(f"nota del alumo modificada {alumno['nota']}")
if alumno['nota'] >= 5:
    alumno["aprobado"]=alumno['nota']
else:
    alumno["reprobado"]=alumno['nota']
print(alumno)

"""
Ejercicio 4. Conjuntos: usuarios registrados
- Crea un conjunto llamado usuarios con estos nombres: Ana, Luis, Marta, Ana y Pedro.
- Crea una variable nuevo_usuario con el valor "Luis".
- Crea una variable usuario_existe que compruebe si nuevo_usuario está dentro del conjunto.
- Añade el usuario "Clara" al conjunto.
- Crea una variable total_usuarios con el número de usuarios únicos.
- Muestra por consola el conjunto final, usuario_existe y total_usuarios.

"""

print("\nSolucion de ejercicio 4")

usuarios = {'Ana', 'Luis', 'Marta', 'Ana', 'Pedro'}
usuario_nuevo = 'Luis'
usuario_existente = usuario_nuevo in usuarios
usuarios.add('Clara')
total_users = len(usuarios)
print(usuarios)
print(usuario_existente)
print(f"total de usuarios {total_users}")

"""
Ejercicio 5. Condiciones con and, or y not
- Crea las variables edad, tiene_permiso, es_socio y sancionado.
- Asigna valores concretos a esas variables.
- Crea una variable acceso_por_edad que sea True si la persona tiene al menos 16 años y tiene permiso.
- Crea una variable acceso_por_socio que sea True si la persona es socio y no está sancionada.
- Crea una variable puede_acceder que sea True si se cumple acceso_por_edad o acceso_por_socio.
- Muestra por consola las tres variables: acceso_por_edad, acceso_por_socio y puede_acceder.

"""

print("\nSolucion de ejercicio 5")
edad = 15
tiene_permiso = True
es_socio = True
sancionado = False

if edad >= 16 and tiene_permiso:
    acceso_por_edad = True
else:
    acceso_por_edad = False
if es_socio or sancionado:
    acceso_por_socio = True
else:
    acceso_por_socio = False
if acceso_por_edad or acceso_por_socio:
    puede_acceder = True
else:
    puede_acceder = False
print(acceso_por_edad)
print(acceso_por_socio)
print(puede_acceder)

"""
Ejercicio 6. if, elif y else: clasificación de matrícula
- Crea las variables nota_media, renta_baja y familia_numerosa.
- Asigna valores concretos a esas variables.
- Crea una variable mensaje.
- Si la nota_media es menor que 5, mensaje debe ser No admitido.
- Si la nota_media es mayor o igual que 9, mensaje debe ser Beca completa.
- Si la nota_media es mayor o igual que 7 y además renta_baja o familia_numerosa es True, mensaje debe ser Beca parcial.
- Si la nota_media es mayor o igual que 5, mensaje debe ser Admitido sin beca.
- En cualquier otro caso, mensaje debe ser Revisar solicitud.
- Muestra por consola el valor final de mensaje.

"""

print("\nSolucion de ejercicio 6")

nota_media = 6
renta_baja = True
familia_numerosa = False

mensaje = ""

if nota_media < 5:
    mensaje = "No admitido"
    print(mensaje)
elif nota_media >= 9:
    mensaje = "Beca completa"
    print(mensaje)
elif nota_media >= 7 and (renta_baja == True or familia_numerosa == True):
    mensaje = "Beca parcial"
    print(mensaje)
elif nota_media >= 5:
    mensaje = "Admitido sin beca"
    print(mensaje)
else:
    mensaje = "Revisar solicitud"
    print(mensaje)


"""
Ejercicio 7. Ternaria: mensaje de resultado
- Crea una variable nota con un valor numérico.
- Usa un condicional ternario para guardar en resultado el texto Aprobado si la nota es mayor o igual que 5, o Suspenso en caso contrario.
- Usa otro condicional ternario para guardar en tipo_nota el texto Alta si la nota es mayor o igual que 8, o Normal en caso contrario.
- Muestra por consola la nota, el resultado y el tipo de nota.

"""

print("\nSolucion de ejercicio 7")
nota = 8

resultado = "Aprobado" if nota >= 5 else "Suspenso"
tipo_nota = "Alta" if nota >= 8 else "Normal"


print(nota)
print(resultado)
print(tipo_nota)


"""
Ejercicio 8. match-case: menú de aplicación
- Crea una variable opcion con un texto: crear, editar, borrar, listar u otra opción.
- Crea una variable mensaje.
- Usa match-case para asignar un mensaje distinto según la opción elegida.
- Si opcion es "crear", mensaje debe ser Creando registro.
- Si opcion es "editar", mensaje debe ser Editando registro.
- Si opcion es "borrar", mensaje debe ser Borrando registro.
- Si opcion es "listar", mensaje debe ser Mostrando registros.
- Para cualquier otro valor, mensaje debe ser Opción no reconocida.
- Muestra por consola el valor de mensaje.

"""
print("\nSolucion de ejercicio 8")

opcion = "Borrar"
mensaje = ""

match opcion:

    case "crear":
        mensaje = "Creando registro."
        print(mensaje)
    case "editar":
        mensaje = "Editando registro."
        print(mensaje)
    case "borrar":
        mensaje = "Borrando registro."
        print(mensaje)
    case "listar":
        mensaje = "Listando registro."
        print(mensaje)
    case _:
        mensaje = "Opción no reconocida"
        print(mensaje)
