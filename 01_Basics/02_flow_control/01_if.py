### 
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar diferentes bloques de código según ciertas condiciones.
### 

import os
import subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Limpiar la consola al inicio del programa

# print('\nSentencia simple condicional')
#  
# edad = 18 
#  
# if edad >= 18: # Si la condición es verdadera, se ejecuta el bloque de código indentado
#      print('Eres mayor de edad.')
#      
#     
# print('\nSentencia simple condicional')
# edad = 16
# if edad >= 18: 
#     print('Eres mayor de edad.')
# else: # Si la condición es falsa, se ejecuta este bloque de código
#     print('Eres menor de edad.')
#     
# print('\nSentencia condicional con elif')
# nota = 3
# if nota >= 9:
#     print('Excelente')
# elif nota >= 7:
#     print('Aprobado')
# elif nota < 7:
#     print('Reprobado')
# else:
#     print('Nota inválida')   #El else no es necesario, pero es una buena práctica para manejar casos no contemplados.
#     
# print('\nCondiciones múltiples')
# edad = 50
# tiene_carnet = False
# 
# if edad >= 18 and tiene_carnet: # Ambas condiciones deben ser verdaderas
#     print('Puedes conducir.')
# else:
#     print('No puedes conducir.')
#     
#     
# # Un pueblo re x
# if edad >= 18 or tiene_carnet: # Al menos una condición debe ser verdadera
#     print('Puedes conducir en el pueblo re x.')
# else:
#     print('Pagar soborno a la policía')
#     
#     
# print('\n Anidar condiciones')
# edad = 20 
# tiene_dinero = True
# 
# if edad >= 18:
#     if tiene_dinero:
#         print('Puedes salir a la discoteca.')
#     else:
#         print('No tienes dinero para salir.')
# else:
#     print('Eres menor de edad, no puedes salir a la discoteca.')
#     if tiene_dinero:
#         print('Puedes ir al cine con tus amigos.')
#     else:
#         print('Mejor quédate en casa viendo Netflix.')
#         
#         
# número = 7
# if número: # true 
#     print('El número es considerado verdadero en un contexto booleano.')
#     
# número = 0
# if número: # false 
#     print('El número es considerado verdadero en un contexto booleano.')
#     
# numero = 3
# tres = numero == 3 
# if tres: # true 
#     print('El número es igual a 3.') 
#     
# 
# print('\nLa condición ternaria')
# # es una forma compacta de escribir una sentencia if-else en una sola línea
# # [código si cumple la condición] if [condición] else [código si no cumple la condición]
# 
# edad = 17
# mensaje = 'Mayor de edad' if edad >= 18 else 'Menor de edad'
# print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

input1 = float(input('Introduce el primer número: '))
input2 = float(input('Introduce el segundo número: '))

print('\nComparación de números:')
if input1 > input2:
    print(f'El número {input1} es mayor que {input2}.')
else:
    print(f'El número {input2} es mayor que {input1}.')

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

input1 = float(input('\nIntroduce el primer número: '))
input2 = float(input('Introduce el segundo número: '))
operacion = input('Introduce la operación que deseas realizar (+, -, *, /): ')

print('\nResultado de la operación:')

if operacion == '+':
    resultado = input1 + input2
    print(f'{input1} + {input2} = {resultado}')
elif operacion == '-':
    resultado = input1 - input2
    print(f'{input1} - {input2} = {resultado}')
elif operacion == '*':
    resultado = input1 * input2
    print(f'{input1} * {input2} = {resultado}')
elif operacion == '/':
    if input2 != 0:
        resultado = input1 / input2
        print(f'{input1} / {input2} = {resultado}')
    else:
        print('Error: No se puede dividir entre cero.')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

input_year = int(input('\n Introduce un año para verificar si es bisiesto:'))
if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    print(f'El año {input_year} es bisiesto.')
else:
    print(f'El año {input_year} no es bisiesto.')

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

input_age = int(input('\nIntroduce una edad para categorizar:'))

if 0 <= input_age <= 2:
    print('Bebé.')
elif 3 <= input_age <= 12:
    print('Niño.')
elif 13 <= input_age <= 17:
    print('Adolescente.')
elif 18 <= input_age <= 64:
    print('Adulto.')
elif input_age >= 65:
    print('Adulto mayor.')
else:
    print('Edad inválida.')