# print("------Ejercicio 1------")
# for cont in range (101):
#     print(cont)

# print ("------Ejercicio 2------")
# numero = int(input("Ingrese un numero entero"))
# cont = 0
# if numero == 0:
#     cont = 1
# elif numero < 0:
#     numero *= -1  # Si es negativo, lo convertimos a positivo
# while numero > 0:
#     numero = numero // 10  
#     cont += 1
# print("El número tiene",cont,"dígitos")

# print ("------Ejercicio 3------")
# valor_1 = int(input("Ingrese el valor 1: "))
# valor_2 = int(input("Ingrese el valor 2: "))
# cont = 0
# if valor_1 > valor_2:
#     valor_1, valor_2 = valor_2, valor_1
# for num in range ((valor_1 + 1), valor_2):
#     cont += num
# print("La suma de los numero entre",valor_1,"y",valor_2,"es: ", cont)

# print ("------Ejercicio 4------")
# CORTE = 0
# suma = 0
# num = int(input(f"Ingrese un numero entero ({CORTE} PARA CORTAR): "))
# while num != 0:
#     suma += num 
#     num = int(input(f"Ingrese un numero entero ({CORTE} PARA CORTAR): "))
# print(f"El total acumulado es {suma}")

# print ("------Ejercicio 5------")
# from random import randint
# num_aleatorio = randint(0,9)
# num = int(input("Adivina el numero entre 1 y 9: "))
# intentos = 1
# while num != num_aleatorio:
#     num = int(input("Intenta de nuevo: "))
#     intentos += 1
# print(f"¡¡ADIVINASTE!! tan solo en {intentos} intentos")

# print ("------Ejercicio 6------")
# for numero in range(100, -1, -1):
#     if numero % 2 == 0:
#         print(numero)

# print ("------Ejercicio 7------")
# numeros = int(input("Ingrese un numero positivo: "))
# suma = 0
# for cont in range(1, numeros + 1):
#     suma += cont
# print(f"La suma de los numeros entre 0 y {numeros} es {suma}")

# print ("------Ejercicio 8------")
# cantidad = 100
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# for cont in range(cantidad):
#     num = int(input(f"Ingresá el número {cont + 1}: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
# print(f"Hay {pares} pares, {impares} impares, {positivos} positivos y {negativos} negativos")

# print ("------Ejercicio 9------")
# cantidad = 3
# suma = 0
# for cont in range (cantidad):
#     num = int(input(f"Ingresa el valor {cont + 1}: "))
#     suma += num
# promedio = suma / cantidad
# print(f"El promedio es {promedio}")

# print ("------Ejercicio 10------")
# numero = int(input("Ingresá un número: "))
# numero_invertido = 0
# while numero > 0:
#     digito = numero % 10 # Esto saca el ultimo digito
#     numero_invertido = numero_invertido * 10 + digito
#     numero = numero // 10 # Elimina ese digito del numero
# print(f"El número invertido es {numero_invertido}")