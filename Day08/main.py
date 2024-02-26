def saudacao():
  print("Olá Angela")
  print("Como vai você, Jack Bauer?")
  print("O tempo não está agradável hoje?")
saudacao()

def saudacao_com_nome(nome):
  print(f"Olá {nome}")
  print(f"Como vai você, {nome}?")
saudacao_com_nome("Jack Bauer")

def saudacao_com(nome, local):
  print(f"Olá {nome}")
  print(f"Como está o tempo em {local}?")

saudacao_com("Jack Bauer", "Em lugar algum")
saudacao_com("Em lugar algum", "Jack Bauer")

saudacao_com(local="Londres", nome="Angela")