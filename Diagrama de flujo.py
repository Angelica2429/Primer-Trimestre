# # print("Ejercicio 1")
# # nom1=input("Ingrese su nombre:")
# # edad1=int(input("Ingrese su edad:"))
# # if edad1 >= 18:
# #     print("Puedes ingresar tu cuenta bancaria")
# # else:
# #     print("No puedes solicitar el credito")
# # cuent=input("Ingrese su cuenta bancaria:")
# # cant=float(input("Ingresar la cantidad del credito que desea"))
# # print(f"{nom1} se le enviará {cant} a su cuenta {cuent}")

# print("Ejercicio 2")
# nom2=input("Ingrese su nombre:")
# edad2=int(input("Ingrese su edad:"))
# if edad2 <= 4:
#     print("Puedes pasar gratis")
# elif edad2 ==5 and edad2 <= 18:
#     print("Pagas 5 euros")
# else:
#     print("Pagas 18 euros")

print("Ejercicio 3")
print("Suma = s")
print("Resta =  r")
print("Multiplicación = m")
print("División = d")
 
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
Opera=input("Ingrese la letra de la operación que desea realzar:").lower()
if Opera == "s":
    result1=num1+num2
    print(f"Su resultado de la suma fue: {result1}")
elif Opera == "r":
    result2=num1-num2
    print(f"Su resultado de la resta fue: {result2}")
elif Opera == "m":
    result3=num1*num2
    print(f"Su resultado de la multiplicación fue: {result3}")
elif Opera == "d":
    result4=num1//num2
    print(f"Su resultado de la división fue: {result4}")
else:
    print("La operación no es valida")