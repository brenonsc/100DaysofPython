print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro!")

escolha1 = input("\nVocê está em uma encruzilhada. Para onde você quer ir? Digite \"esquerda\" ou \"direita\"\n")

if escolha1.lower() == "esquerda":
  escolha2 = input("\nVocê chegou a um lago. Há uma ilha no meio dele. Digite \"esperar\" para esperar por um barco. Digite \"nadar\" para nadar até lá.\n")
  
  if escolha2.lower() == "esperar":
    escolha3 = input("\nVocê chegou à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe?\n")
    
    if escolha3.lower() == "vermelha":
      print("\nVocê entrou em uma sala pegando fogo. Fim de jogo!")
      
    elif escolha3.lower() == "amarela":
      print("\nVocê encontrou o tesouro! Você venceu!")
      
    elif escolha3.lower() == "azul":
      print("\nVocê entrou em uma sala lotada de monstros famintos. Fim de jogo!")
      
    else:
      print("\nVocê escolheu uma porta que não existe. Fim de jogo!")
      
  else:
    print("\nVocê é atacado por uma truta zangada. Fim de jogo!")
    
else:
  print("\nVocê caiu em um buraco. Fim de jogo!")
