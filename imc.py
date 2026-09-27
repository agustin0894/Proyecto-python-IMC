#Script funcional que calcula el Indice de Masa Corporal 
#Datos del usuario
nombre=input("ingresa_tu_nombre:")
edad=int(input("ingresa_tu_edad:"))
peso=float(input("ingresa_tu_peso_en_kilogramos:"))
estatura=float(input("ingresa_tu_estatura_en_metros:"))
#Analizando datos
imc=peso/(estatura ** 2)
#Mostrando información
print("\n___resultados___")
print("nombre:",nombre)
print("edad:", edad, "años")
print("peso:", peso, "kg")
print("estatura:", estatura, "m")
print("IMC:", round(imc,2))
