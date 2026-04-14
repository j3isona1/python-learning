###
# 03-Listas
# Secuencias mutables de elementos
### 

import os
import subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) # Limpiar la consola al inicio del programa

# Creación de listas
print('\nCreación de listas')
lista1 = [1, 2, 3, 4, 5]
lista2 = ['manzana', 'banana', 'cereza']
lista3 = [1, 'hola', 3.14, True]

lista_vacia = []
listas_de_listas = [lista1, lista2, lista3]
listas_de_listas2 = [[1, 2], ['a', 'b'], [True, False]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(listas_de_listas)
print(listas_de_listas2)
print(matrix)

# Acceso a elementos por índice 
print('\nAcceso a elementos por índice')
print(lista2[1]) # banana
print(lista2[0]) # manzana
print(lista2[-1]) # cereza
print(lista2[-2]) # banana

print(listas_de_listas2[1][0]) # a

# Slicing de listas (rebanado)
print('\nSlicing de listas')
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[2:]) # [3, 4, 5]   
print(lista1[:]) #Crear una copia de la lista completa

#Hay mas magia
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista2[::4]) #Elementos en posiciones pares
print(lista2[::-1]) #Reversa la lista

#Modificar elementos de la lista
lista2[0] = 100
print(lista2)

#Añadir elementos a la lista
lista1 = [1, 2, 3]

#forma larga y no eficiente
lista1 = lista1 + [4, 5, 6] # Concatenar listas
print(lista1)

#forma eficiente
lista1 += [7, 8, 9] # Agregar elementos a la lista existente
print(lista1)

#Recuperar longitud de la lista
print('Longitud de la lista:', len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:14]
print(secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambiar el primer y último elemento
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
lista_duplicada = lista * 2
print(lista_duplicada)
lista_duplicada = lista + lista # Otra forma de duplicar la lista

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]
centro = lista[len(lista) // 2]
print(centro)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
inver = lista[:len(lista) // 2][::-1] + lista[len(lista) // 2:]
print(inver)


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.



# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.