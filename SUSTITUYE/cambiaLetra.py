entrada="aeiou"
salida="AEIOU"
numero="12345"
cambio=str.maketrans(entrada,numero)
str=input("Escribe:")
print(str.translate(cambio))
