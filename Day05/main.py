import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '*', '-', '+']

print("Bem-vindo ao Gerador de Senhas PyPassword!")
num_letras = int(input("Quantas letras você gostaria em sua senha?\n")) 
num_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
num_numeros = int(input(f"Quantos números você gostaria?\n"))

lista_senha = []

for char in range(1, num_letras + 1):
  lista_senha.append(random.choice(letras))

for char in range(1, num_simbolos + 1):
  lista_senha += random.choice(simbolos)

for char in range(1, num_numeros + 1):
  lista_senha += random.choice(numeros)

random.shuffle(lista_senha)

senha = ""
for char in lista_senha:
  senha += char

print(f"Sua senha é: {senha}")
