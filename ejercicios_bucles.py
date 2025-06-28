# print("Ejercicio # 1")
# total=0
# num1=int(input("Ingrese el primer número a sumar:"))
# while num1 != 0:
#    total += num1
#    num1=int(input("Ingrese el primer número a sumar:"))
# print(f"Su total es {total}")
   
# print("Ejercicio # 2")            
# intentos=0                 
# clave="python123"
# ingresar=input("Ingrese la clave para poder ingresar:") 
# while ingresar != clave:                                          #Cuando ingrese al bucle la interacción y inició
#    intentos += 1                                                  #Es decir que cuando comienze el bucle ya lleva uno vez preguntado 
#    if intentos == 0:                                              #Entonces de una vez ya le agrega a la variable "intentos" un intento 
#       ingresar=input("Ingrese la clave para poder ingresar:")     #Seguidamente por descarte realiza la siguiente pregunta si se equivocó de co
#    else:
#       ingresar=input("Contraseña equivocada,vuelve a intentarlo:")

# print("Contraseña correcta")
 
# print("Ejercicio # 3")
# productos=[]                                 #La que alamacena  (mochila)
# agregar=(input("Ingrese un producto:"))      #Lo que se le agrega a la mochila
# while agregar != "fin":                      #Comienza el bucle,verificando si se puede agregar y de lo contrario si dice fin, saldria automaticamente
#     productos.append(agregar)                #Luego si es diferente a la palabra para salir, se le agrega a la mochila lo solicitado 
#     agregar=(input("Ingrese un producto:"))  #Seguidamente repite el proceso de solicitar y repite el bucle hasta que sea igual a la palabra
# print(productos)                             #Como agrgar no ha sido diferente, se repite el proceso
# print("Programa finalizado")

# print("Ejercicio # 4")
# numero=int(input("Ingrese el número con que quiere empezar a contar (del 1 al 10):"))
# while numero <10:
#    if numero % 2 == 0:
#       print(f"{numero} es par")
#    else:
#       print(f"{numero} es impar")
#    numero+=1

# print("Ejercicio # 5")
# notas=[]
# print("Si desea saber el promedio ingrese (promediar)")
# nota1=input("Ingrese una nota de 0 a 5 o promediar :")
# while nota1.lower() != "promediar":
#     notas.append(nota1)
#     nota1=input("Ingrese una nota de 0 a 5 o promediar:")
#     notas=list(map(float, notas))
#     cant=len(notas)
#     suma=sum(notas)
#     result=suma/cant
        
# print(f"Sus notas fueron {notas} y su promedio fue de {result}")      

# print("Ejercicio # 6")
# conteo="si"
# while conteo.lower() == "si":
#    tabla=int(input("Ingrese la tabla que desea conocer:"))
#    conteo=1
   
#    while conteo <=10:
#       resul=tabla*conteo
#       print(f"{tabla}x{conteo}={resul}")
#       conteo += 1
#    print(f"Acabas de ver la tabla del {tabla}")
#    conteo =input("Desea ver otra tabla (si/no):")
   
# print("Ejercicio # 7")
# adi_num=64
# while True:
#     try:


# print("Ejercicio # 8")
# while True:
#     tupla=("limon","pera","banano","manzana","mandarina")
#     fruta=input("Adivine la fruta:")
#     if fruta.lower() in tupla:
#      print("Correcto adivinaste una fruta")
#      break


# print("Ejercicio # 10")

# while True:
#     try:
#      print("1-Suma")
#      print("2-Resta")
#      print("3-Multiplicación")
#      print("4-División")
#      print("5-Salir")
#      elegir=int(input("Seleccione una operacion con el número de opsión:"))
    
#      match elegir:
#         case 1 :
#             print("Has elegido la suma")
#             numer1=int(input("Por favor, ingrese el primer número para la suma:"))
#             numer2=int(input("Por favor, ingrese el segundo número para la suma:"))
#             resultado=numer1+numer2
#             print(f"{numer1} + {numer2} = {resultado}")
#         case 2 :
#             print("Has elegido la resta")
#             numer1=int(input("Por favor, ingrese el primer número para la resta:"))
#             numer2=int(input("Por favor, ingrese el segundo número para la resta:"))
#             resultado=numer1-numer2
#             print(f"{numer1} - {numer2} = {resultado}")
#         case 3 :
#             print("Has elegido la multiplicación")
#             numer1=int(input("Por favor, ingrese el primer número para la multiplicación :"))
#             numer2=int(input("Por favor, ingrese el segundo número para la multiplicación:"))
#             resultado=numer1*numer2
#             print(f"{numer1} * {numer2} = {resultado}")
#         case 4 :
#             print("Has elegido la división")
#             numer1=int(input("Por favor, ingrese el primer número para la división:"))
#             numer2=int(input("Por favor, ingrese el segundo número para la división:"))
#             resultado=numer1/numer2
#             print(f"{numer1} / {numer2} = {resultado}")
#         case 5 :
#             print("Has elegido salir del programa")
#             break
#     except:
#         print("Ingresa números enteros, vuelve a intentarlo")
                     