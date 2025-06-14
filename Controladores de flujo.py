# contador=1
# while contador <= 100:
#     print(f"Contador:{contador}")
#     contador -= 1

while True:
    texto =input("Escribe algo (o escribe 'salir' para terminar ):").lower
    if texto == "salir":
        break
    print(f"Escribiste:{texto}")