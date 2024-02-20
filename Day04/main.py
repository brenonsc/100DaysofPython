import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [pedra, papel, tesoura]
print("PEDRA, PAPEL OU TESOURA?\n")
user_choice = int(
    input(
        "O que você escolhe? Digite 0 para PEDRA, 1 para PAPEL ou 2 para TESOURA.\n"
    ))
if user_choice >= 3 or user_choice < 0:
  print("Você digitou um número inválido, você perdeu!")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("O computador escolheu:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("Você venceu!")
  elif computer_choice == 0 and user_choice == 2:
    print("Você perdeu!")
  elif computer_choice > user_choice:
    print("Você perdeu!")
  elif user_choice > computer_choice:
    print("Você venceu!")
  elif computer_choice == user_choice:
    print("Empate!")
