###
# 02 Booleans
# Valores lógicos:  True y False
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('\nBooleanos básicos:')
print(True)
print(False)   

## Operadores de comparación
print('\nOperadores de comparación:')
print('5 > 3:', 5 > 3)  # Mayor que
print('5 < 3:', 5 < 3)  # Menor que
print('5 == 3:', 5 == 3)  # Igual que
print('5 != 3:', 5 != 3)  # Diferente de
print('5 >= 3:', 5 >= 3)  # Mayor o igual que
print('5 <= 3:', 5 <= 3)  # Menor o igual que


print('\nComparación de cadenas:')
print('"manzana" < "pera":', "manzana" < "pera")  # true

# Operadores lógicos
print('\nOperadores lógicos:')
print('True and False:', True and False)  # AND False
print('True and True:', True and True)  # AND True
print('True or False:', True or False)  # OR True
print('False or False:', False or False)  # OR False
print('not True:', not True)  # NOT, False
print('not False:', not False)  # NOT, True

#Tabla de verdad para referencia
print('\nTabla de verdad para AND:')
print('A     B     A and B')
print('True  True  ', True and True)
print('True  False ', True and False)
print('False True  ', False and True)
print('False False ', False and False)

print('\nTabla de verdad para OR:')
print('A     B     A or B')
print('True  True  ', True or True)
print('True  False ', True or False)
print('False True  ', False or True)
print('False False ', False or False)