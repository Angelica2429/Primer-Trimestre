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
print("Ejercicio #6")
produc1=int(input("Ingrese el precio del primer producto:"))
produc2=int(input("Ingrese el precio del segundo número:"))
precio_total=produc1+produc2
des=0.10/precio_total
if precio_total >= 100:
    des=0.10/precio_total 
    print(f"tiene un descuento del 10% su total a pagar es de {des}")
else:
    print("No tiene descuento")
print("Ejercicio #7")






