###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.\n")

my_name = "Jeisona"
my_city = "Medellín"

print(my_name)
print(my_city)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.\n")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\n--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
entero = int(cadena)
float = float(entero)

print('\nNúmero entero:', entero)
print('Número float:', float)

float_number = 3.99
entero_number = int(float_number)
print('Número float:', float_number)
print('Número entero:', entero_number) # El número se trunca, no se redondea

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

my_age = 23
my_height = 1.70
print(f'\nHola! Me llamo {my_name} y tengo {my_age} años, mido {my_height} metros.')

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.14159) / 2)
print('\nValor PI:',3.1416)
print('Valor redondeado:', round(3.14159))
print('Resultado de la división entera:', resultado)