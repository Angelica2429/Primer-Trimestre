# print("Información del producto y costo")
# producto1=str(input("Ingrese el nombre del producto:"))
# valor=float(input("Ingrese el valor unitario:"))
# cantidad=int(input("Ingrese la cantidad comprada:"))
# tup1=(producto1,valor)
# lista1=[tup1,cantidad]
# informacion={producto1:lista1}
# ope=valor*cantidad
# print(f"El valor que pago por {producto1}es de {ope}")

# print("Información del producto y costo")
# productoa=("Guanabana")
# costo_x_unidad1=10000
# compra_total1=5
# productob=("pan")
# costo_x_unidad2=11000
# compra_total2=2
# productoc=("portatil")
# costo_x_unidad3=3500000
# compra_total3=10
# tupa=("productoa,costo_x_unidad1")
# tupb=("productob,costo_x_unidad2")
# tupc=("productoc,costo_x_unidad3")
# listaA=[tupa,compra_total1,tupb,compra_total2,tupc,compra_total3]
# productos={"Producto1":productoa,"Producto2":productob,"Producto3":productoc}
# opera1=productoa,costo_x_unidad1*compra_total1
# opera2=productob,costo_x_unidad2*compra_total2
# opera3=productoc,costo_x_unidad3*compra_total3

# print(opera1,opera2,opera3)

print("Registro de notas")
nombre=input("Ingrese su nombre:")
asignatura1=input("Ingrese la primera asignatura:")
asignatura2=input("Ingrese la segunda asignatura:")
asignatura3=input("Ingrese la tercera asignatura:")
listaa=[asignatura1,asignatura2,asignatura3]
nota1_a=float(input(f"Ingrese el primer valor de {asignatura1}:"))
nota1_b=float(input(f"Ingrese el segundo valor de {asignatura1}:"))
nota1_c=float(input(f"Ingrese el tercer valor de {asignatura1}:"))
nota2_a=float(input(f"Ingrese el primer valor de {asignatura2}:"))
nota2_b=float(input(f"Ingrese el segundo valor de {asignatura2}:"))
nota2_c=float(input(f"Ingrese el tercer valor de {asignatura2}:"))
nota3_a=float(input(f"Ingrese el primer valor de {asignatura3}:"))
nota3_b=float(input(f"Ingrese el segundo valor de {asignatura3}:"))
nota3_c=float(input(f"Ingrese el tercer valor de {asignatura3}:"))
promedio1=(nota1_a+nota1_b+nota1_c)/3
promedio2=(nota3_a+nota2_b+nota2_c)/3
promedio3=(nota3_a+nota3_b+nota3_c)/3
tupla1=(asignatura1,promedio1)
tupla2=(asignatura2,promedio2)
tupla3=(asignatura3,promedio3)

lis=[tupla1,tupla2,tupla3]
calificaciones={
    "Nombre":nombre,
    "Materias":listaa
    
}
print(calificaciones)
promedio_final=(promedio1+promedio2+promedio3)/3
print(f"El promedio final de {nombre} es de:",promedio_final)