print(bool(0))
a = 9//2
print(a)

s = "Seat Ibiza"
print(s.lower())

a = [10, 20, 30, 40, 50]
removido = a.pop(0)
print(f"removido:{removido}")
a.append(50)
print(a)

'¿Cómo se crea un diccionario vacío o cómo se accede de forma segura a una clave que podría '
'no existir en un diccionario d devolviendo un valor por defecto (por ejemplo, 0 si no existe)? Escribe el '
'método que se usa sobre el diccionario.'

b={}
print(b.get("km", 0))

for a in range(0,4):
    print(a)
    

marcas = ["Seat", "Ford"]
precios = [12000, 15000]
for i, marca in enumerate(marcas,start=1):
 print(i, marca)
for marca, precio in zip(marcas, precios):
 print(marca, precio)
for clave, valor in {"km": 12000}.items():
 print(clave, valor)


 d = {"marca": "Seat", "anio": 2020}

 print(d.items())

 'Tienes dos conjuntos: a = {1, 2} y b = {2, 3}. Escribe la operación utilizando el operador correspondiente '
 '(&, | o -) que permita obtener los elementos que están en a pero NO en b (diferencia).'

 a = {1, 2} 
 b = {2, 3}

result= a-b
print(result)

marcas = ["Seat", "Ford"] 
precios = [12000, 15000]
for m, p in zip(marca, precios):
    print(m, p)

doble= lambda x:x*2 if x>0 else 0 
print(doble(-3))