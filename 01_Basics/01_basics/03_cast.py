### 
# 03 - casting de types
# Transformar un tipo de dato a otro
###

print('Conversión de tipos')
print(type('100')) 
# Transformar un string a un entero
print(type(int('100')))

print(type(float(3.14)))
print(int(3.8))
print(round(3.45))
print(round(3.14159, 2)) # Redondear a 2 decimales

print(bool(5)) # Cualquier número distinto de cero es True, incluso los negativos.
print(bool(0)) # Cero es False
print(bool('')) # Cadena vacía es False
print(bool(' ')) # Esta tiene un espacio y es true
print(bool('False')) # Esta es una cadena no vacía y es true
print(bool([])) # Lista vacía es False

