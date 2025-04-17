# print("------Ejercicio 1------")
# def imprimir_hola_mundo():
#     print("Hola Mundo!")
     
# imprimir_hola_mundo()


# print("------Ejercicio 2------")
# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"

# nombre_ingresado = input("¿Cuál es tu nombre? ")
# saludo = saludar_usuario(nombre_ingresado)
# print(saludo)


# print("------Ejercicio 3------")
# def informacion_personal(nombre, apellido, edad, residencia):
#     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# nombre_ingresado = input("Ingrese su nombre: ")
# apellido_ingresado = input("Ingrese su apellido: ")
# edad_ingresada = input("Ingrese su edad: ")
# residencia_ingresada = input("Ingrese su residencia: ")
# presentacion = informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)
# print(presentacion)


# print("------Ejercicio 4------")
# from math import pi
# def calcular_area_circulo(radio):
#     return pi * radio**2
# def calcular_perimetro_circulo(radio):
#     return 2 * pi * radio

# radio_ingresado = float(input("Ingrese el radio: "))
# area = calcular_area_circulo(radio_ingresado)
# perimetro = calcular_perimetro_circulo(radio_ingresado)
# print(f"El area del circulo es {area} y el perimetro es {perimetro}")


# print("------Ejercicio 5------")
# def segundos_a_horas(segundos):
#     return segundos / 3600

# segundos_ingresados = float(input("Ingrese los segundos: "))
# horas = segundos_a_horas(segundos_ingresados)
# print(f"{segundos_ingresados} segundos, en horas, son {horas} horas")


# print("------Ejercicio 6------")
# def tabla_multiplicar(numero):
#     for i in range (1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# numero_ingresado = int(input("Ingrese un numero entero: "))
# tabla_multiplicar(numero_ingresado)


# print("------Ejercicio 7------")
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multi = a * b
#     divi = a / b
#     return (suma, resta, multi, divi) # (0, 1, 2, 3)

# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("Ingrese el segundo numero: "))
# resultado = operaciones_basicas(num1, num2)
# print(f"La suma es {resultado[0]}")
# print(f"La resta es {resultado[1]}")
# print(f"La multiplicacion es {resultado[2]}")
# print(f"La division es {resultado[3]}")


# print("------Ejercicio 8------")
# def calcular_imc(peso, altura):
#     return peso / (altura * altura)

# peso_ingresado = float(input("Ingrese su peso en kg: "))
# altura_ingresada = float(input("Ingrese su altura en metros: "))
# resultado = calcular_imc(peso_ingresado, altura_ingresada)
# print(f"Su indice de masa corporal es {resultado}")


# print("------Ejercicio 9------")
# def celsius_a_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
    
# temp_celsius = float(input("Ingrese la temperatura en celsius: "))
# fahrenheit = celsius_a_fahrenheit(temp_celsius)
# print(f"{temp_celsius}° celsius equivalen a {fahrenheit}° fahrenheit")


# print("------Ejercicio 10------")
# def calcular_promedio(a, b, c):
#     return (a + b + c) / 3

# num1 = float(input("Ingrese primer numero: "))
# num2 = float(input("Ingrese segundo numero: "))
# num3 = float(input("Ingrese tercer numero: "))
# promedio = calcular_promedio(num1, num2, num3)
# print(f"El promedio de los 3 numero es {promedio}")