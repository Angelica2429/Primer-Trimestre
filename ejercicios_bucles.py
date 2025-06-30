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
# import random
# eleccion = range(100)
# adiv_num = random.choice(eleccion)
# contador=1
# while True:
#     nume= int(input("Adivine el número:"))
#     if nume == adiv_num:
#         print("Correcto,adivinaste el número.")
#         break
#     elif nume < adiv_num: 
#         print("El número es mayor, intenta de nuevo.")
#     else:
#         print("El número es menor, intenta de nuevo.")
#     contador=contador+1
# print(f"Lo conseguiste con {contador} intentos")

# print("Ejercicio # 8")
# while True:
#     tupla=("limon","pera","banano","manzana","mandarina")
#     fruta=input("Adivine la fruta:")
#     if fruta.lower() in tupla:
#      print("Correcto adivinaste una fruta")
#      break
# print("Ejercicio # 11")  
# nom_ed={}
# clave=input("Ingrese el valor de la clave")

# print("Ejercicio # 9")
# dic={"limon":"lemon","pera":"pear","piña":"pineapple","mango":"mango","uva":"grape"}
# palabra=input("Ingrese la fruta que deseas traducir o (ingresa la palabra salir para terminar el programa):")
# while palabra.lower() != "salir":
#     if palabra in dic:
#         print(f"La traducción de {palabra} es {dic[palabra]}.")
#     else:
#         print(f"{palabra} no está disponible aún, intentelo de nuevo.")
#     palabra=input("Ingrese la fruta que deseas traducir o (ingresa la palabra salir para terminar el programa):")
# print("Ha salido del programa")

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
print("Ejercicio # 11") 
personas = {}
while True:
    nombre = input("Escribe un nombre (o 'salir' para terminar): ")
    if nombre == "salir":
        break
    edad = input(f"Escribe la edad de {nombre}:")
    personas[nombre] = edad

print("El diccionario de las personas es:")
print(personas)

print("Ejercicio # 12") 
colores = ["rojo", "azul", "verde", "amarillo", "naranja"]
color =input("Ingrese un color y si desea salir ingrese (salir):")
while color != "salir":
    if color in colores:
        print(f"El color {color} está en la lista")
    else:
        print("El color no está en la lista. Intenta otra vez.")
    color =input("Ingrese un color y si desea salir ingrese (salir):")
print("Has salido del programa")

# print("Ejercicio # 13") 
cont="si"
while cont.lower() == "si":
   pote=int(input("Ingrese el nuúmero que desea ver sus potencias:"))
   cont=1
   
   while cont <=5:
      resul=pote**cont
      print(f"{pote}**{cont}={resul}")
      cont += 1
   print(f"Acabas de ver las potencias del {pote}") 
   cont =input("Desea ver otras potencias (si/no):")
print("Has salido del programa")
    
print("Ejercicio # 14")
cuadrados = []
contador = 0
while contador < 5:
    numero = int(input("Escribe un número: "))
    cuadrados.append(numero * numero)
    contador += 1
print(f"Los cuadrados son:{cuadrados}")
print("Ejercicio # 15")
estudiantes = {}
while True:
    nombre = input("Nombre del estudiante (escribe 'fin' para terminar): ")
    if nombre == "fin":
        break
    nota =float(input(f"Nota final de {nombre}:"))
    estudiantes[nombre] = nota

print("lista de estudiantes y sus notas:")
print(estudiantes)


    

