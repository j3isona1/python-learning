### 
# 04 - Listas métodos
# Los métodos más importantes para trabajar con listas
###

import os
import subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Limpiar la consola al inicio del programa

lista1 = ['a', 'b', 'c', 'd']
lista1.append('e') # Agrega un elemento al final de la lista
print(lista1)

lista1.insert(1, 'x') # Inserta un elemento en la posición especificada
print(lista1)

lista1.extend(['f', 'g']) # Agrega los elementos de otra lista al final de la lista
print(lista1)

#Eliminar elementos de la lista
lista1.remove('x') # Elimina la primera ocurrencia del elemento especificado
print(lista1)

ultimo = lista1.pop() # Elimina y devuelve el último elemento de la lista
print(ultimo)
print(lista1)

# lista1.clear() # Elimina todos los elementos de la lista
# print(lista1)

# Eliminar con el del
del lista1[2] # Elimina el elemento en la posición especificada
print(lista1)

lista2 = ['a', 'b', 'c', 'd', 'e']
del lista2[1:4] # Elimina un rango de elementos
print(lista2) 

# Más métodos útiles
print('\nMás métodos útiles:')
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers) # Devuelve una nueva lista ordenada
print(sorted_numbers) # La lista original no se modifica

print('\nOrdenar cadenas de texto')
fruits = ['banana', 'apple', 'cherry', 'orange', 'lemon']
sorted_fruits = sorted(fruits) # Ordena alfabéticamente
print(sorted_fruits)

print('\nOrdenar cadenas de texto (mayúsculas y minúsculas)')
fruits = ['banana', 'apple', 'Cherry', 'Orange', 'lemon']
fruits.sort(key=str.lower) # Ordena ignorando mayúsculas y minúsculas
print(fruits)

# Más métodos útiles
animals = ['gato', 'perro', 'pez', 'pájaro', 'gato']
print(len(animals)) # Devuelve el número de elementos en la lista
print(animals.count('gato')) # Cuenta cuántas veces aparece un elemento
print('perro' in animals) # Verifica si un elemento está en la lista
