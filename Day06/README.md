# Simulador de Labirinto - Reeborg's World

Este é um simples simulador de andar em um labirinto usando Reeborg's World, um ambiente de programação visual para ajudar a aprender programação.

<div align="center">   <img src="https://i.makeagif.com/media/4-14-2018/Rv_Qav.gif" alt="Maze"> </div>

<br>

## Descrição do Código

O código abaixo faz o robô navegar pelo labirinto até encontrar a saída:

```python
move()

def turn_right():    
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

<br>

## Como Usar

1. Cole o código no ambiente de programação [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).

2. Execute o código para que o robô comece a andar no labirinto.

3. O robô seguirá as regras especificadas no código para encontrar a saída.

<br>

## Observações

- Certifique-se de que o ambiente de programação Reeborg's World está configurado corretamente para executar o código.

- Você pode ajustar o código conforme necessário para diferentes labirintos ou adicionar funcionalidades extras, como detectar armadilhas ou contornar obstáculos.