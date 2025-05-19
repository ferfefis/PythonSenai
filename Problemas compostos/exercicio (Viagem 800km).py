#passo a passo

#1 Quantos litros de combustível e quantos reais é necessário para fazer a viagem de 800km?

#2 autonomia do carro, a distância da viagem e o valor do litro do combustível

#3
#passo1: Subtrair a distância percorrida pelos quilômetros percorridos
#passo2: Pegar o resultado e dividir pela autonomia do carro
#passo3: Pegar o resultado novamente e subtrair pelos 10 litros que ainda tem
#passo4: Multiplicar o resultado pelo valor do combustível
#passo5: Exibir quantos litros e quantos reais serão utilizados

print("Viagem 800km")

Subtração = 800 - 90
Divisão = Subtração / 7
Sub2 = Divisão - 10
Multiplicação = Sub2 * 6.90

print("O total de litros necessários é de " , Divisão)

print("O total de dinheiro necessário é de ", Multiplicação)