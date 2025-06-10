def calcular_frete(peso, ditancia, taxa_fixa):
    valor = (peso * 0.5) + (ditancia * 0.1) + taxa_fixa
    print("O valor é: ", valor)
   

peso = int(input("Digite o peso: "))
distancia = int(input("Digite a distância: "))
taxa_fixa = 15
calcular_frete(peso, distancia, taxa_fixa)