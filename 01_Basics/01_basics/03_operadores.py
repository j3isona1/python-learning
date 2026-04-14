# OPERADORES ARITMÉTICOS
print("=== OPERADORES ARITMÉTICOS ===")
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b  # Residuo
potencia = a ** b

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")

# OPERADORES DE COMPARACIÓN
print("\n=== OPERADORES DE COMPARACIÓN ===")
x = 15
y = 20

print(f"{x} > {y}: {x > y}")   # ¿15 es mayor que 20? 
print(f"{x} < {y}: {x < y}")   # ¿15 es menor que 20? 
print(f"{x} == {y}: {x == y}") # ¿15 es igual a 20? 
print(f"{x} != {y}: {x != y}") # ¿15 es diferente a 20?

# LÓGICA: IF / ELSE
print("\n=== LÓGICA: IF / ELSE ===")
edad = 23

if edad >= 18:
    print(f"Tienes {edad} años. ¡Eres mayor de edad!")
else:
    print(f"Tienes {edad} años. Aún eres menor de edad.")

# LÓGICA: IF / ELIF / ELSE
print("\n=== IF / ELIF / ELSE ===")
calificacion = 85

if calificacion >= 90:
    print("Calificación: A (Excelente)")
elif calificacion >= 80:
    print("Calificación: B (Bueno)")
elif calificacion >= 70:
    print("Calificación: C (Aceptable)")
else:
    print("Calificación: F (Reprobado)")

# OPERADORES LÓGICOS (AND, OR, NOT)
print("\n=== OPERADORES LÓGICOS ===")
dinero = 500
tiene_trabajo = True

if dinero > 100 and tiene_trabajo:
    print("Puedes invertir en acciones")
else:
    print("Necesitas más dinero o empleo")

# OR (O)
puede_entrar = False
es_vip = True

if puede_entrar or es_vip:
    print("¡Entra a la fiesta VIP!")
else:
    print("No puedes entrar")

# NOT (NO)
es_fin_de_semana = False

if not es_fin_de_semana:
    print("Es día laboral, ¡a trabajar!") 