# ---------- Ejercicio 1 ---------
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# ---------- Ejercicio 2 ---------
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# ---------- Ejercicio 3 ---------
frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Manzana', 'Pera', 'Naranja']

# ---------- Ejercicio 4 ---------
contactos = {input("Nombre: "): input("Número: ") for i in range(5)}

nombre = input("Buscar: ")
print(contactos[nombre] if nombre in contactos else "No está en la agenda.")

# ---------- Ejercicio 5 ---------
frase = input("Escribí una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# ---------- Ejercicio 6 ---------
alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# ---------- Ejercicio 7 ---------
parcial1 = {"Ana", "Luis", "Juan", "Sofía"}
parcial2 = {"Sofía", "Pedro", "Juan", "María"}

ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", al_menos_uno)

# ---------- Ejercicio 8 ---------
stock = {
    "manzanas": 10,
    "bananas": 5,
    "peras": 8
}

producto = input("¿Qué producto querés consultar/modificar? ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = input("¿Le agregas unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades? "))
        stock[producto] += cantidad
        print(f"Stock nuevo de {producto}: {stock[producto]}")
else:
    nuevo = input("Producto no encontrado. ¿Querés agregarlo? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input(f"¿Cuántas unidades de {producto} querés agregar? "))
        stock[producto] = cantidad
        print(f"{producto} agregado con stock {cantidad}.")

# ---------- Ejercicio 9 ---------
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (hh:mm): ")
evento = input("¿Qué evento querés agendar?: ")

agenda[(dia, hora)] = evento
print("Evento agregado.")

dia_consulta = input("Día a consultar: ").lower()
hora_consulta = input("Hora a consultar: ")

clave = (dia_consulta, hora_consulta)

if clave in agenda:
    print(f"Evento: {agenda[clave]}")
else:
    print("No hay eventos en ese horario.")

# ---------- Ejercicio 10 ---------
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

invertido = {}

for pais, capital in original.items():
    invertido[pais] = capital

print("Diccionario invertido:", invertido)