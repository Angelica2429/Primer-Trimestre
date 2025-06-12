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
# suma=produc1+produc2                        #Se suman los valores, si se cumple la condición se saca el 10% que seria con la formula de 
# if suma >= 100:                             #la suma * 10 (o el porcentaje) y eso se lo divide entre 100 al final el total que de,se lo resta con la suma de los valores
#     des=suma * 10 / 100 
#     total=suma-des
#     print(f"tiene un descuento del 10% y el valor a pagar es {total}")
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
# if  num10 % 3 == 0 and num10 % 5 ==0:
#     print("El número es multiplo del 5 y al 3")
# elif num10 % 3 == 0:
#     print("El número es multiplo del 3")
# elif num10 % 5 == 0:
#     print("El número es multiplo de 5")
# else:
# #     print("El número no es multiplo ni de 5 o 3")
# print("Ejercicio #10")
# num11=int(input("Ingrese un número a dividir:"))
# num12=int(input("Ingrese un número divisor:"))                     #Si cuando se usa % con un número es 0 aplica como divisible o multiplo
# num13=int(input("Ingrese otro número divisor:"))
# if num11% num12==0 and num11% num13 == 0:
#     print(f"{num11} es divisible entre {num12} y {num13}")
# elif num11% num12 ==0:
#     print(f"{num11} es solo divisible entre {num12}")
# elif num11 % num13 == 0:
#     print(f"{num11} es solo divisible entre {num13}")
# else:
#     print(f"{num11} no es divisible entre {num12} ni {num13}")

# # # print("Ejercicio #11")
# lista1=[]
# lista1.append(int(input("Ingrese un número:")))
# lista1.append(int(input("Ingrese un número:")))
# lista1.append(int(input("Ingrese un número:")))
# lista1.append(int(input("Ingrese un número:")))
# lista1.append(int(input("Ingrese un número:")))
# print(lista1)
# if lista1[2] < 10:
#     print(f"{lista1 [2]} es menor a 10")
# else:
#     print(f"{lista1 [2]} es mayor a 10")

# print("Ejercicio #12")
# lista2=[3,5,7,9]
# if lista2[0] == 7:
#     print("La lista si tiene 7")
# elif lista2[1] == 7:
#     print("La lista si tiene 7")
# elif lista2[2] == 7:
#     print("La lista si tiene 7")
# elif lista2[3] == 7:
#     print("La lista si tiene 7")
# else:
#     print("La lista no tiene 7")

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

# print("Ejercicio #15")
# lista5=[]
# lista5.append(input("Ingrese un color:"))
# lista5.append(input("Ingrese un color:"))
# lista5.append(input("Ingrese un color:"))
# if lista5[1].lower()=="azul":
#     lista5[1]=(input("Ingrese el nuevo color:"))
#     print(f"El nueva lista actualizada quedó así:{lista5}")
# else:
#     print("No es necesario cambiar el color") 

# print("Ejercicio #16")
# tup0=(5,8,12,20)
# if tup0[0]<tup0[3]:
#     print("Orden ascendente")
# else:
#     print("Orden decendente")

# print("Ejercicio #17")
# tup0_1=(25,32,28)
# if tup0_1[1]>= 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor a 30")

# # print("Ejercicio #18")
# tup1=(1,2,3)
# if tup1[1]==2:
#     lista1=list(tup1)
#     lista1[1]=10
#     tup1=tuple(lista1)
#     print(f"La actualización quedo así {tup1}")
# else:
#     print(f"No es necesario cambiar la tupla")

# print("Ejercicio #21")
# info={'nombre':'Juan','Edad':17}
# valor_de_edad=info['Edad']
# valor_de_nombre=info['nombre']
# if valor_de_edad>=18:
#     print(f"{valor_de_nombre} es mayor de edad, teniendo {valor_de_edad} años")
# else:
#     print(f"{valor_de_nombre} es menor de edad, teniendo {valor_de_edad} años")
    
# print("Ejercicio #22")
# info={'nombre':'Lucia','Edad':20}
# ed=info['Edad']
# nom=info['nombre']
# if ed>18:
#     info['Edad']=21
#     ed=info['Edad']
#     print(f"La edad de {nom} ahora es {ed}")
# else:
# #     print(f"No es necesario cambiar la edad de {nom}")

    
# # print("Ejercicio #23")
# dato={'nombre':'Lucia'}
# if 'ciudad' in dato:
#     print("No es necesario agragarle clave")
# else:
#     dato['ciudad']='Bogotá'
#     print(dato)

# print("Ejercicio #24")
# productos={'producto':'pan','precio':'1200'}
# if 'precio' in productos:
#     prec=productos['precio']
#     print(f"El {producto} tiene precio y es de {prec}")
# # else:
# #     print(f"El {producto} no tiene precio")

# print("Ejercicio #25")
# products={'pan':'1200','leche':'2000'}
# if 'pan' in products:
#     precio=products['pan']
#     print(f"el precio del producto es de {precio} ")
# else:
#     print("Producto no disponible")
