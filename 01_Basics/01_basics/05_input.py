### 
# 05 - Entrada de usuario input()
# La función input() se utiliza para obtener datos del usuario a través de la consola.
###

print('¿Cuál es tu nombre?') # \n para agregar un salto de línea después de la pregunta
name = input() # La función input() devuelve una cadena de texto (str)

print(f'Hola, {name}! Bienvenido a Python.')

age = input('¿Cuántos años tienes?\n')
print(f'Tu edad es {age} años.') # La edad se almacena como una cadena de texto, no como un número.
print(f'Dentro de 20 años tendrás {int(age) + 20} años.') # Convertimos la edad a entero para poder sumar 20.

print('Obtener múltiples valores a la vez:')
country, city = input('¿Cuál es tu país y ciudad de residencia?\n').split(' ') # La función split() divide la cadena en una lista usando el espacio como separador.
print(f'Vives en {city}, {country}.')