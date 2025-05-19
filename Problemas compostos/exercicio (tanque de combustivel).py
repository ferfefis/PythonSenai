#passo a passo

#1 Quanto custa encher o tanque do carro

#2 Capacidade do combustível do carro em litros, quanto litros o carro ja tem e o valor do litro em reais

#3
#passo1: Subtrair a capacidade total pelo tanque atual
#passo2: Multiplicar o resultado da subtração pelo preço do combustível
#passo3: Exibir o valor em reais

print("Tanque do carro")
capacidade = 50 - 20
multiplicar = capacidade * 5.80
print("O custo total do combustível é de"  , multiplicar , "reais")

print("Tanque do carro")
tanque = int(input("Digite a capacidade do tanque " ))
cheio = int(input("Digite o quanto o tanque ja está cheio " ))
valor = float(input("Digite o preço do litro do combustível " ))
capacidade = tanque - cheio
multiplicar = capacidade * valor

print("O custo total do combustível é de" , multiplicar , "reais")
