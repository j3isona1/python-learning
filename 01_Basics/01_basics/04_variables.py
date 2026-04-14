### 
# 04 - Variables
# Las variables son contenedores que almacenan datos. 
# En Python, no es necesario declarar el tipo de variable, ya que es un lenguaje de tipado dinámico.
###

# Asignación de variables
# my_name = 'jeisona'
# print(my_name)

# my_age = 23
# print(my_age) 

#my_age = 25
#print(my_age) 

## Python es de tipado dinámico, lo que significa que puedes cambiar el tipo de dato de una variable en cualquier momento.
# my_name = 'jeisona'
# print(type(my_name))
# 
# my_name = 23
# print(type(my_name))

# Tipado fuerte: Python no permite operaciones entre tipos incompatibles sin una conversión explícita.
# print(my_name + 10) # Esto generará un error porque no se pueden sumar un string y un entero sin convertir el entero a string o el string a entero.

# f-strings: Son una forma conveniente de formatear cadenas de texto. Permiten incluir expresiones dentro de las llaves {} que se evaluarán en tiempo de ejecución.
# print(f'Hola, mi nombre es {my_name} y tengo {my_age + 1} años.') # f-string para formatear la salida

# No recomendado forma de asignar variables
# my_name, my_age, city = 'jeisona', 23, 'Medellín'

#Convenciones de nombres de variables:
# mi_variable = 'ok' # snake_case
# MiVariable = 'ok' # PascalCase
# 
# MI_CONSTANTE = 'ok' # UPPER_SNAKE_CASE, se usa para constantes.



is_user_logged_in: bool = True
print(is_user_logged_in)

#is_user_logged_in: bool = 42
#print(is_user_logged_in)