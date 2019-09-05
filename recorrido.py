palabra=input("Escribe una palabra cualquiera:")

#usar indice para recorrer letra por letra
indice=0

while indice<len(palabra):
    letra=palabra[indice]
    print(letra)
    indice += 1

#alternativa
for letra2 in palabra:
    print(letra2)