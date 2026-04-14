### 
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar diferentes bloques de código según ciertas condiciones.
### 

import os
os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola al inicio del programa

print('\nSentencia simple condicional')
 
edad = 18 
 
if edad >= 18: # Si la condición es verdadera, se ejecuta el bloque de código indentado
     print('Eres mayor de edad.')
     
    
print('\nSentencia simple condicional')
edad = 16
if edad >= 18: 
    print('Eres mayor de edad.')
else: # Si la condición es falsa, se ejecuta este bloque de código
    print('Eres menor de edad.')
    
print('\nSentencia condicional con elif')
nota = 3
if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Aprobado')
elif nota < 7:
    print('Reprobado')
else:
    print('Nota inválida')   #El else no es necesario, pero es una buena práctica para manejar casos no contemplados.
    
print('\nCondiciones múltiples')
edad = 50
tiene_carnet = False

if edad >= 18 and tiene_carnet: # Ambas condiciones deben ser verdaderas
    print('Puedes conducir.')
else:
    print('No puedes conducir.')
    
    
# Un pueblo re x
if edad >= 18 or tiene_carnet: # Al menos una condición debe ser verdadera
    print('Puedes conducir en el pueblo re x.')
else:
    print('Pagar soborno a la policía')