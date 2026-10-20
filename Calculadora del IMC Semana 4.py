# Calcula el Indice de Masa Corporal 

print("=== CALCULADORA DE IMC ===")

# 1. VALIDACIÓN DEL NOMBRE (No permitir campos vacíos)
while True:
    nombre = input("ingresa_tu_nombre: ").strip().title()
    if nombre == "":
        print("Error: El nombre no puede quedar vacío. Inténtalo de nuevo.")
    else:
        break  # Sal si el nombre es válido

# 2. VALIDACIÓN DE LA EDAD (Evitar letras y vacíos)
while True:
    entrada_edad = input("ingresa_tu_edad: ").strip()
    if entrada_edad == "":
        print("Error: El campo de edad no puede quedar vacío.")
        continue  # Regresa al inicio del bucle
    try:
        edad = int(entrada_edad)
        if edad <= 0 or edad >100:
            print("Error: La edad debe ser un número mayor a cero y menor a cien.")
        else:
            break  # Sal si es un entero válido
    except ValueError:
        print("Error: Debes ingresar un número entero válido (sin letras).")

# 3. VALIDACIÓN DEL PESO (Evitar letras y vacíos)
while True:
    entrada_peso = input("ingresa_tu_peso_en_kilogramos: ").strip()
    if entrada_peso == "":
        print("Error: El campo de peso no puede quedar vacío.")
        continue
    try:
        # Reemplazamos coma por punto
        peso = float(entrada_peso.replace(',', '.'))
        if peso <= 0 or peso >200:
            print("Error: El peso debe ser real, mayor a cero y menor a 200 kilos.")
        else:
            break  # Sal si es un decimal válido
    except ValueError:
        print("Error: Debes ingresar una cifra numérica válida.")

# 4. VALIDACIÓN DE LA ESTATURA (Evitar letras y vacíos)
while True:
    entrada_estatura = input("ingresa_tu_estatura_en_metros: ").strip()
    if entrada_estatura == "":
        print("Error: El campo de estatura no puede quedar vacío.")
        continue
    try:
        estatura = float(entrada_estatura.replace(',', '.'))
        if estatura <= 0 or estatura >2.50:
            print("Error: La estatura debe ser un número mayor a cero y menor a 2.50 metros.")
        else:
            break  # Sal si es un decimal válido
    except ValueError:
        print("Error: Debes ingresar una cifra numérica válida.")

# Analizando datos
imc = peso / (estatura ** 2)

# Mostrando Información (usamos :.2f para que el IMC solo muestre 2 decimales y se vea limpio)
print(f"""
Resumen de Datos
Nombre: {nombre}
Edad: {edad} años
Peso: {peso} kg
Estatura: {estatura} m
IMC: {imc:.2f}
""")