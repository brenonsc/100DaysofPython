# Dicionários em Python

Neste tutorial, exploraremos diferentes aspectos dos dicionários em Python e como usá-los para armazenar e organizar dados.

<div align="center">   <img src="https://64.media.tumblr.com/tumblr_me7tg97psk1rku7zwo1_500.gif" alt="Adventure Time Dictionary"> </div>

<br>

## 1. Definindo um Dicionário

```python
dicionario_de_programacao = {
  "Bug": "Um erro em um programa que impede o programa de funcionar como esperado.",
  "Função": "Um trecho de código que você pode chamar facilmente várias vezes.",
}
```

<br>

## 2. Adicionando e Editando Itens

```python
# Adicionando novos itens ao dicionário.
dicionario_de_programacao["Loop"] = "A ação de fazer algo repetidamente."

# Editando um item em um dicionário
dicionario_de_programacao["Bug"] = "Uma mariposa no seu computador."
```

<br>

## 3. Percorrendo um Dicionário

```python
for chave, valor in dicionario_de_programacao.items():
    print(f"{chave}: {valor}")
```

<br>

## 4. Aninhamento

### a) Aninhando Dicionários em Dicionários

```python
capitais = {
  "França": "Paris",
  "Alemanha": "Berlim",
}
```

### b) Aninhando Listas em Dicionários

```python
registro_de_viagem = {
  "França": ["Paris", "Lille", "Dijon"],
  "Alemanha": ["Berlim", "Hamburgo", "Stuttgart"],
}
```

### c) Aninhando Dicionário em um Dicionário

```python
registro_de_viagem = {
  "França": {"cidades_visitadas": ["Paris", "Lille", "Dijon"], "total_visitas": 12},
  "Alemanha": {"cidades_visitadas": ["Berlim", "Hamburgo", "Stuttgart"], "total_visitas": 5},
}
```

### d) Aninhando Dicionários em Listas

```python
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
```

<br>

## Conclusão

Os dicionários são estruturas de dados poderosas em Python que permitem armazenar dados de forma organizada e acessá-los de maneira eficiente. Com o aninhamento, você pode criar estruturas complexas para representar dados de forma mais elaborada. Experimente diferentes formas de usar dicionários em seus projetos para tirar o máximo proveito dessa funcionalidade.