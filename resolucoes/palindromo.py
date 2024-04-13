# Solicitando a palavra como entrada
palavra = input("Digite uma palavra: ")

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
