# edad = int(input("Ingrese su edad: "))

# if edad > 18:
#     print("Es mayor de edad.")

# --------------------------------------------

# nota = int(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# --------------------------------------------

# number = int(input("Ingrese un numero PAR: "))

# if number % 2 == 0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")

# ---------------------------------------------

# edad = int(input("Ingrese su edad: "))

# if edad < 12:
#     print("Eres un niño/a")
# elif edad >= 12 and edad < 18:
#     print("Eres un adolescente")
# elif edad >= 18 and edad < 30:
#     print("Eres un adulto/a joven")
# else: 
#     print("Eres un adulto/a")

# ------------------------------------------------

# contra = input("Ingrese una contraseña (8 - 14 caracteres): ")

# if len(contra)>= 8 and len(contra)<= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# -------------------------------------------------

# import statistics
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = statistics.mode(numeros_aleatorios)
# mediana = statistics.median(numeros_aleatorios)
# media = statistics.mean(numeros_aleatorios)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo")
# else:
#     print("Sin sesgo")

# ---------------------------------------------------------

# frasePalabra = str(input("Ingrese una frase o una palabra: "))

# if frasePalabra.endswith(("a", "e", "i", "o", "u")):
#     print(f"{frasePalabra}!")
# else:
#     print(frasePalabra)

# -------------------------------------------------------

# nombre = str(input("Ingrese su nombre: "))
# num = int(input("Presione: 1.MAYUSCULAS, 2.minusculas, 3.Primer letra mayuscula: "))
 
# if num == 1:
#     print(nombre.upper())
# elif num == 2:
#     print(nombre.lower())
# else:
#     print(nombre.title())

# -----------------------------------------------------------

# magnitud = int(input("Ingrese la magnitud del terremoto (1-7): "))

# if magnitud < 3:
#     print("Muy leve")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy fuerte")
# else:
#     print("Extremo")

# ---------------------------------------------------------------------

# hemisferio = input("Hemisferio (N/S): ").strip().upper()
# mes = int(input("Mes (1-12): "))
# dia = int(input("Dia (1-31): "))

# if hemisferio == "N":
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
#         estacion = "Primavera"
#     elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
#         estacion = "Verano"
#     else:
#         estacion = "Otoño"

# elif hemisferio == "S":
#     if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
#         estacion = "Otoño"
#     elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
#         estacion = "Invierno"
#     else:
#         estacion = "Primavera"
# else:
#     estacion = "Hemisferio inválido"

# print(f"La estación es: {estacion}")