print("Datos de la mascota")
mascota=input("Ingrese el nombre de la mascota:")
tipo_de_mascota=input("Ingrese la raza de la mascota que posee:")
edad=int(input("Ingrese la edad de su mascota:"))
dueño=input("Ingrese el nombre del dueño:")
ciudad=input("Ingrese la ciudad donde recide:")

Pet={
    "nombre":mascota,
    "Tipo":tipo_de_mascota,
    "Edad":edad,
    "Dueño":dueño,
    "Ciudad":ciudad
}
print(f"{dueño},su mascota,{mascota} es un {tipo_de_mascota} tiene {edad} años y redicen en {ciudad}")