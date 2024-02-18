print("Bem-vindo à calculadora de gorjetas!")
total = float(input("\nQual o valor total da conta? R$"))
divisao = int(input("Quantas pessoas vão dividir a conta? "))
gorjeta = int(
    input(
        "Qual a porcentagem de gorjeta que você gostaria de dar? 10, 12 ou 15? "
    ))

valor_total = (total + (total * (gorjeta / 100))) / divisao

print(f"\nCada pessoa deve pagar R${valor_total:.2f}")
