combustivel = input("Digite o nome do combustível abastecido: ")

if combustivel == "Gasolina" or combustivel == "gasolina" or combustivel == "Etanol" or combustivel == "etanol":
    litros = float(input("Digite a quantidade de litros abastecida: "))
    if combustivel == "Gasolina" or combustivel == "gasolina":
        valor = litros * 5.80
        print(f"O combustível abastecido foi {combustivel}. O valor a ser pago é de R${valor:.2f}")
    else:
        valor = litros * 4.90
        print(f"O combustível abastecido foi {combustivel}. O valor a ser pago é de R${valor:.2f}")
else:
    print(f"O combustível {combustivel} não foi encontrado no sistema. Tente novamente.")