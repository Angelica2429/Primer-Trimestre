# print("Ejercicio #1")
# num1=int(input("Ingrese un número:"))
# if num1 <0:
#     print("El número es negativo")
# elif num1 ==0:
#     print("El número es cero")
# else:
#     print("El número es positivo")

# print("Ejercicio #2")
# num3=int(input("Ingrese un número:"))
# num4=int(input("Ingrese un número"))
# if num3 > num4:
#     print(f"{num3} es mayor que {num4} ")
# if num3 < num4:
#     print(f"{num4} es mayor que {num3}")
# else:
#     print("los números son iguales")

# print("Ejercicio #3")
# num5=int(input("Ingrese un número:"))
# oper=num5 % 2             #para sacar el par o impar; si el residuo da 0 es par de lo contrario es impar#
# if oper == 0:
#     print("El número es par")
# else:
#     print("El número es impar")

# print("Ejercicio #4")
# num6=int(input("Ingrese un número:"))
# if num6 ==10 and num6 <=20:
#     print("El número está en el rango")
# else:
#     print("El número no se encuentra en el rango")

# print("Ejercicio #5")
# num7=int(input("Ingrese un número:"))
# num8=int(input("Ingrese un número:"))
# num9=int(input("Ingrese un número:"))
# if num7 < num9 > num8:
#     print(f"{num9} es mayor que {num8} y {num7}")
# elif num7 < num8 > num9:
#     print(f"{num8} es mayor que {num9} y {num7}")
# elif num8 < num7 > num9:
#     print(f"{num7} es mayor que {num9} y {num8}")
# else:
#     print("No se sabe")

# print("Ejercicio #6")
# produc1=int(input("Ingrese el precio del primer producto:"))
# produc2=int(input("Ingrese el precio del segundo número:"))
# precio_total=produc1+produc2
# porce=10                                             #establezco o pregunto el porcentaje,luego hago una operacion para sacar el dewscuento del precio final
# if precio_total >= 100:                              #es poner el precio final luego eso lo divido por 100 que seria el porcentaje final y por ultimo ese resultado lo multiplico por el porcentaje del descuento
#     des=precio_total/100*porce
#     print(f"tiene un descuento del 10% su descuento es de {des}")
# else:
#     print("No tiene descuento")

# print("Ejercicio #7")
# edad=int(input("Ingresa tu edad:"))
# if edad >= 18:
# #     print("Puedes votar")
# # else:
# #     print("No puedes votar")

# print("Ejercicio #8")
# precio=int(input("Ingrese el precio del producto:"))
# tipo_de_cliente=input("¿Eres VIP o normal?:").lower()
# if tipo_de_cliente=="vip":
#     porcentaje=precio/100 *20
#     print(f"Su descuento como VIP será de {porcentaje}")
# else:
#     print("No tienes descuento ")

# print("Ejercicio #9")
# num10=int(input("Ingrese un número:"))
# multi=(5*(num10//5))-(3*(num10//3)) 
# if  multi==0:
#     print("El número es multiplo del 5 y al 3")
# else:
# #     print("El número no es multiplo del 5 o 3")
# print("Ejercicio #10")
# num11=int(input("Ingrese un número:"))
# num12=int(input("Ingrese un número:"))
# multi2=(num12*(num11//2))-(num11*(num11//2))
# if  multi2==0:
#     print("El número es divisible entre dos")
# else:
#     print("El número no es divisible entre dos")

# # print("Ejercicio #11")
# lista1=[]
# lista1=int(input("Ingrese un número:")),int(input("Ingrese un número:")),int(input("Ingrese un número:")),int(input("Ingrese un número:")),int(input("Ingrese un número:"))
# print(lista1)
# if lista1[2] < 10:
#     print(f"{lista [2]} es menor a 10")
# else:
#     print(f"{lista [2]} es mayor a 10")

# print("Ejercicio #12")
# lista2=[3,5,7,9]
# if lista2[2] == 7:
#     print(f"la lista tiene {lista[2]}")
# else:
#     print("El número no tiene 7")

# print("Ejercicio #13")
# lista3=[4,6,2,8]
# ope=lista3[0]+lista3[1]
# if ope > 10:
#     print("La suma es alta")
# else:
#     print("La suma es baja")

# print("Ejercicio #14")
# lista4=["Ana","Luis","Pedro","Marta"]
# if lista4 [3]== "Marta":
#     print("El  nombre es correcto")
# else:
#     print("El número no es correcto")

print("Ejercicio #15")
lista5=[]
lista5=input("Ingrese un color:"),input("Ingrese un color:"),input("Ingrese un color:").lower()
if lista5[1]=="azul":
    n=lista5.([1])
    a=lista5[1].append(input("Ingrese el nuevo color:"))
    print(f"El nueva lista actualizada quedó así:{lista5}")
else:
    print("No es necesario cambiar el color")