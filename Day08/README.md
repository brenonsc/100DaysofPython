# Funções de Saudação

Aqui estão algumas funções de saudação que você pode usar para cumprimentar pessoas de diferentes maneiras:

<div align="center">   <img src="https://i.gifer.com/Buo.gif" alt="Goofy greeting"> </div>

<br>

## 1. Saudação Padrão

Esta função simplesmente imprime uma saudação padrão.

```python
def saudacao():
    print("Olá Angela")
    print("Como vai você, Jack Bauer?")
    print("O tempo não está agradável hoje?")

saudacao()
```

<br>

## 2. Saudação com Nome

Esta função aceita um parâmetro `nome` e o utiliza para personalizar a saudação.

```python
def saudacao_com_nome(nome):
    print(f"Olá {nome}")
    print(f"Como vai você, {nome}?")

saudacao_com_nome("Jack Bauer")
```

<br>

## 3. Saudação com Nome e Local

Esta função aceita dois parâmetros, `nome` e `local`, para personalizar ainda mais a saudação.

```python
def saudacao_com(nome, local):
    print(f"Olá {nome}")
    print(f"Como está o tempo em {local}?")

saudacao_com("Jack Bauer", "Em lugar algum")
saudacao_com("Em lugar algum", "Jack Bauer")
```

<br>

## Exemplo de Uso

```python
saudacao_com(local="Londres", nome="Angela")
```

<br>

## Observações

- Sinta-se à vontade para modificar ou expandir essas funções conforme necessário para entender seus usos e aprender a usá-las de forma eficiente!