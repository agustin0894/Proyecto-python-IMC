#Calcula el Indice de Masa Corporal 
#Datos del Usuario
nombre=input("ingresa_tu_nombre:").title()
edad=int(input("ingresa_tu_edad:"))
peso=float(input("ingresa_tu_peso_en_kilogramos:"))
estatura=float(input("ingresa_tu_estatura_en_metros:"))
#Analizando datos
imc=peso/(estatura ** 2)
#Mostrando Información
print(f"""
Resumen de Datos
Nombre: {nombre}
Edad: {edad} años
Peso: {peso} kg
Estatura: {estatura} m
IMC: {imc}
""")


