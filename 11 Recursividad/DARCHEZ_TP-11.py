import sys
sys.setrecursionlimit(20000)

# ------- Ejercicio 1 ---------

def fact(x):
    return 1 if x == 0 else x * fact(x - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"El factorial de {i} es {fact(i)}")

# ------- Ejercicio 2 ---------

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)
    
num1 = int(input("¿Hasta qué posición querés ver la serie de fibonacci? "))

print("Fibonacci: ")
for i in range(num1 + 1):
    print(fibonacci(i))

# ------- Ejercicio 3 ---------

def potencia(base, expo):
    if expo == 0:
        return 1
    else:
        return base * potencia(base, expo - 1)

num2 = int(input("Ingresa la base: "))
expo = int(input("Ingresa el exponenete: "))

resultado = potencia(num2, expo)
print(f"{num2} elevado a {expo} es {resultado}")

# ------- Ejercicio 4 ---------

def decimal_binario(num3):
    if num3 == 0:
        return ""
    else:
        return decimal_binario(num3 // 2) + str(num3 % 2)

numero = int(input("Ingresá un número entero positivo: "))
if numero == 0:
    print("0")
else:
    print(f"{numero} en binario es {decimal_binario(numero)}")

# ------- Ejercicio 5 ---------

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
texto = input("Ingresá una palabra: ").lower()
if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")

# ------- Ejercicio 6 ---------

def suma_digitos(num4):
    if num4 < 10:
        return num4
    else:
        return num4 % 10 + suma_digitos(num4 // 10)
    
num = int(input("Ingresá un número: "))
print(f"La suma de los dígitos de {num} es {suma_digitos(num)}")

# ------- Ejercicio 7 ---------

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("¿Cuántos bloques hay en el nivel más bajo? "))
print(f"Los bloques necesarios son {contar_bloques(nivel)}")

# ------- Ejercicio 8 ---------

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num5 = int(input("Ingresá un número: "))
dig = int(input("Ingresá un dígito del 0 al 9: "))

print(f"El dígito {dig} aparece {contar_digito(num5, dig)} veces en {num5}")