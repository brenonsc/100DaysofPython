dicionario_de_programacao = {
  "Bug": "Um erro em um programa que impede o programa de funcionar como esperado.",
  "Função": "Um trecho de código que você pode chamar facilmente várias vezes.",
}

# Adicionando novos itens ao dicionário.
dicionario_de_programacao["Loop"] = "A ação de fazer algo repetidamente."

# Criando um dicionário vazio.
dicionario_vazio = {}

# Apagando um dicionário existente
# dicionario_de_programacao = {}
# print(dicionario_de_programacao)

# Editando um item em um dicionário
dicionario_de_programacao["Bug"] = "Uma mariposa no seu computador."

# Percorrendo um dicionário
# for chave in dicionario_de_programacao:
#   print(chave)
#   print(dicionario_de_programacao[chave])

# Aninhamento
capitais = {
  "França": "Paris",
  "Alemanha": "Berlim",
}

# Aninhando uma Lista em um Dicionário
registro_de_viagem = {
  "França": ["Paris", "Lille", "Dijon"],
  "Alemanha": ["Berlim", "Hamburgo", "Stuttgart"],
}

# Aninhando Dicionário em um Dicionário
registro_de_viagem = {
  "França": {"cidades_visitadas": ["Paris", "Lille", "Dijon"], "total_visitas": 12},
  "Alemanha": {"cidades_visitadas": ["Berlim", "Hamburgo", "Stuttgart"], "total_visitas": 5},
}

# Aninhando Dicionários em Listas
registro_de_viagem = [
{
  "pais": "França", 
  "cidades_visitadas": ["Paris", "Lille", "Dijon"], 
  "total_visitas": 12,
},
{
  "pais": "Alemanha",
  "cidades_visitadas": ["Berlim", "Hamburgo", "Stuttgart"],
  "total_visitas": 5,
},
]