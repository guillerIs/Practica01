entrada="aeiou"
salida="AEIOU"
cambio=str.maketrans(entrada,salida)
str=input("Escribe:")
print(str.translate(cambio))
