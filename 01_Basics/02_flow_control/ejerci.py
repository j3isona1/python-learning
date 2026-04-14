mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:14]
print(secreto)

#Otra lista
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambiar el primer y último elemento
print(numeros)

#Otra xd
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print(sandwich)

lista = [1, 2, 3]
lista_duplicada = lista * 2
print(lista_duplicada)