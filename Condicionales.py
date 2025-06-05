# edad=int(input("Ingresa tu edad:"))
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("No eres mayor de edad")

# num1=int(input("Ingrese el número que desea multiplicar:"))
# num2=int(input("Ingrese el segundo número que desea multiplicar:"))

# if num1 < 100:
#     print("El número aplica")
# elif num2 > 100:
#     print("El número no aplica")
# else:
#     print("NADA")


Edad=int(input("Ingrese su año de nacimiento :"))
if Edad ==1920 and Edad <=1940:
    print("Eres genaracion silenciosa")
elif Edad >1946 and Edad <=1964:
   print("Eres de la generación de los baby boomer")
elif Edad >1965 and Edad <=1979:
    print("Eres de la generación X")
elif Edad >1980 and Edad <=2000:
    print("Eres de la generación Y")
elif Edad >2001 and Edad <= 2010:
    print("Eres de la generación Z")
else:
    print("No aplica")
    
