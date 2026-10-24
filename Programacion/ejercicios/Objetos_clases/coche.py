"""
1. Crear una clase y sus objetos
Define la clase Coche. Dentro de ella, escribe un __init__ que reciba la marca y el modelo y los
guarde como atributos de cada objeto.
Una vez definida la clase, fuera de ella:
- Crea dos objetos que representen coches distintos.
- Muestra la marca y el modelo de cada uno.
- Cambia el modelo del primer coche y comprueba que el segundo conserva el suyo.
"""

print("ejercicio 1\n")

class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_datos(self):
        return f"marca: {self.marca}, modelo: {self.modelo}"


coche_1 = Coche('mazda','sedan')
coche_2 = Coche('toyota','cruiser')

print(coche_1.marca)
print(coche_1.modelo)

print(coche_2.marca)
print(coche_2.modelo)

print(coche_1.mostrar_datos())

coche_1.modelo = 2026
print(f'modelo cambiado coche 1: {coche_1.modelo}')
print(f'verificacion modelo coche 2: {coche_2.modelo}')

"""
2. Modificar el estado de un objeto
Escribe la definición completa de la clase CochePruebas. Los tres métodos siguientes deben
quedar definidos dentro del cuerpo de la clase:
- __init__(): crea el atributo de instancia velocidad con valor inicial 0, en km/h.
- acelerar(): aumenta en 10 la velocidad del propio objeto.
- detener(): pone a cero la velocidad del propio objeto
"""
print("ejercicio 2\n")

class CochePruebas:
    def __init__(self):
        self.velocidad = 0
        

    def acelerar(self):
         self.velocidad = self.velocidad + 10
         return self.velocidad
        

    def detener(self):
         self.velocidad = 0
         return self.velocidad
        

coche_pruebas_1 = CochePruebas()
coche_pruebas_2 = CochePruebas()



print(f"coche 2:{coche_pruebas_2.acelerar()}")

print(f"coche1: {coche_pruebas_1.acelerar()}")
print(f"coche 2:{coche_pruebas_2.acelerar()}")

print(f"coche1: {coche_pruebas_1.acelerar()}")
print(f"coche 2:{coche_pruebas_2.acelerar()}")

print(f"coche1: {coche_pruebas_1.acelerar()}")
print(f"coche 2:{coche_pruebas_2.acelerar()}")

print(f"coche1: {coche_pruebas_1.detener()}")

"""
3. Heredar atributos y métodos
Define una clase Vehiculo. Su inicializador debe guardar marca y modelo, y su método
describir() debe devolver un texto que incluya ambos atributos.
Define después una clase CocheElectrico que herede de Vehiculo. Dentro de ella, escribe un
inicializador que reutilice el de Vehiculo mediante super() y guarde también autonomia_km.
Utiliza describir() por herencia, sin volver a definirlo.
Fuera de las clases, crea un coche eléctrico y comprueba que puedes consultar sus tres atributos
y utilizar la descripción heredada
"""

print("ejercicio 3\n")

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"descripcion heredada\n modelo: {self.modelo}, marca: {self.marca}"

class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo,autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km

    def describir(self):
        datos_Iniciales = super().describir()
        return f"{datos_Iniciales} y {self.autonomia_km}"


coche_eletrico = CocheElectrico('mazda','sedan',120)

print(coche_eletrico.marca)
print(coche_eletrico.modelo)
print(coche_eletrico.autonomia_km)

print(coche_eletrico.describir())


"""
4. Sobrescribir un método heredado
Define una clase Motor para representar motores de coches. Su inicializador debe guardar
modelo y su método arrancar() debe devolver "Motor en marcha". Crea dos subclases:
- MotorGasolina: su método arrancar() debe devolver "Motor de gasolina en marcha".
- MotorElectrico: su método arrancar() debe devolver "Motor eléctrico en marcha".
Ambas subclases deben utilizar el inicializador heredado de Motor, sin definir otro __init__.
Después, crea un motor de cada tipo con modelos distintos y comprueba sus modelos y
mensajes de arranque.
"""

print("ejercicio 4\n")

class Motor:
    def __init__(self,modelo):
        self.modelo = modelo

    def arrancar(self):
        return f"Motor en marcha"  

class MotorGasolina(Motor):

    def arrancar(self):
        return f"Motor de gasolina en marcha"

class MotorElectrico(Motor):

    def arrancar(self):
        return f"Motor eléctrico en marcha" 
        
motor_1 = MotorGasolina(2019)
motor_2 = MotorElectrico(1999)

print(motor_1.arrancar())
print(motor_2.arrancar())


"""
5. Utilizar el polimorfismo
Reutiliza las clases del ejercicio anterior. Escribe una función poner_en_marcha(motor) que
llame al método arrancar() del objeto recibido y devuelva su resultado. Después:
- Crea una lista con un objeto MotorGasolina y otro MotorElectrico.
- Recorre la lista con un bucle y utiliza poner_en_marcha() para mostrar el mensaje de cada
motor.
La función debe funcionar sin comprobar el tipo del motor con type() o isinstance().
Finalmente, añade una clase MotorDiesel que herede de Motor y cuyo método arrancar()
devuelva "Motor diésel en marcha". Incorpora un motor diésel a la lista y comprueba que
funciona sin modificar la función poner_en_marcha() ni el bucle.
"""

print("ejercicio 5\n")

def poner_en_marcha(motor):
    return motor.arrancar()


motores=[motor_1,motor_2]

for m in motores:
    print(f"{poner_en_marcha(m)}\n")

class MotorDiesel(Motor):

    def arrancar(self):
        return f"Motor diésel en marcha"

motor3 = MotorDiesel(2023)

motores.append(motor3)

for m in motores:
    print(poner_en_marcha(m))

"""
6. Ampliar un método heredado con super()
Retoma las clases del ejercicio 3. Escribe una nueva versión de CocheElectrico que conserve su
inicializador y defina su propio método describir().
Ese método debe aprovechar la descripción de Vehiculo mediante super(), añadir una frase con
la autonomía en kilómetros y devolver el mensaje completo. Reutiliza la descripción original sin
volver a escribirla manualmente.
Una vez definida esta versión de la clase, crea un coche eléctrico y comprueba tanto la
descripción ampliada como la conservación de sus atributos.
"""

print("ejercicio 6\n")


class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo,autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km

    def describir(self):
        datos_Iniciales = super().describir()
        return f"{datos_Iniciales} {self.autonomia_km} km"

coche_eletrico = CocheElectrico('mazda','sedan',120)

print(coche_eletrico.marca)
print(coche_eletrico.modelo)
print(coche_eletrico.autonomia_km)

print(coche_eletrico.describir())


"""
7. Mostrar datos con f-strings
Utiliza estos datos:
marca = "Seat"
modelo = "Ibiza"
anio = 2020
Escribe un único print() con una f-string que inserte los valores de las tres variables en una frase
legible.
Después, cambia los valores de las variables y comprueba que el mensaje se actualiza sin
modificar el print(). No necesitas crear ninguna clase.
"""

print("ejercicio 7\n")

marca = "Seat"
modelo = "Ibiza"
anio = 2020

print(f'el auto {marca} modelo {modelo} del ano {anio}')


marca = "Toyota"
modelo = "City verso"
anio = 2020

print(f'el auto {marca} modelo {modelo} del ano {anio}')


"""
8. Gestionar una entrada incorrecta con try y except
Pide al usuario los kilómetros recorridos por un coche con input() e intenta convertirlos a un
entero con int() dentro de un bloque try.
- Si la conversión funciona, muestra "Kilómetros indicados:" seguido del número.
- Si se produce ValueError, muestra "Debes escribir un número entero.".
- Fuera del try / except, muestra siempre "Programa finalizado.".
Haz dos pruebas en ejecuciones distintas: introduce primero 12000 y después doce mil.
Comprueba que el programa muestra el mensaje adecuado y llega al mensaje final en ambos
casos.
Solo debes comprobar si la entrada puede convertirse a entero. No hace falta repetir la pregunta
ni utilizar un bucle.
"""

print("ejercicio 8\n")



try:
    distancia = input('Ingresa los kilómetros recorridos ')
    distancia_km = int(distancia)

    print(f'Kilómetros indicados: {distancia_km}')
except:
    print('Debes escribir un número entero')


print('Programa finalizado')