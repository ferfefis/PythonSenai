print("Fatorial, ao Quadrado, ao Cubo ou Tabuada")
while True:
    print("Qual conta você quer fazer? Digite aqui: ")
    print("Aperte 0 para sair")
    print("Aperte 1 para fatorar")
    print("Aperte 2 para ao quadrado")
    print("Aperte 3 para ao cubo")
    print("Aperte 4 para a tabuada")
    menu = int(input("Digite o que você quer fazer: "))
    if menu != 0:
        n = int(input("Digite o número que você quer operar: "))
    if menu == 0:
        print("Você saiu!")
        break
    elif menu == 1:
        contador = 1
        fator = contador
        while contador <= contador:
            fator = fator * (contador+1)
            contador = contador + 1
        print(contador)
        print(fator)
    elif menu == 2:
        print(n**2)
    elif menu == 3:
        print(n**3)
    elif menu == 4:
        print(n*1)
        print(n*2)
        print(n*3)
        print(n*4)
        print(n*5)
        print(n*6)
        print(n*7)
        print(n*8)
        print(n*9)
        print(n*10)
    else:
        print("Opção inválida")
