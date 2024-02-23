import random

from hangman_words import lista_palavras

palavra_escolhida = random.choice(lista_palavras)
tamanho_palavra = len(palavra_escolhida)

fim_de_jogo = False
vidas = 6

from hangman_art import logo

print(logo)

# Código de teste
# print(f'Pssst, a solução é {palavra_escolhida}.')

exibicao = []
for _ in range(tamanho_palavra):
  exibicao += "_"

while not fim_de_jogo:
  palpite = input("Dê um palpite: ").lower()

  if palpite in exibicao:
    print(f"Você já adivinhou {palpite}.\n")

  for posicao in range(tamanho_palavra):
    letra = palavra_escolhida[posicao]

    if letra == palpite:
      exibicao[posicao] = letra

  if palpite not in palavra_escolhida:
    print(
        f"Você adivinhou {palpite}, que não está na palavra. Você perde uma vida.\n"
    )

    vidas -= 1
    if vidas == 0:
      fim_de_jogo = True
      print("\nVocê perdeu!\n")

  print(f"{' '.join(exibicao)}")

  if "_" not in exibicao:
    fim_de_jogo = True
    print("\nVocê ganhou!\n")

  from hangman_art import estagios
  print(estagios[vidas])
