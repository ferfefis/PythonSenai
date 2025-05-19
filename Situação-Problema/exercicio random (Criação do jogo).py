import random
print("Jogo par ou ímpar")

while True:
    print("Você deseja jogar direto ou observar o menu de como jogar?")
    print("Aperte 1 se você quiser jogar")
    print("Aperte 2 se você deseja olhar o menu")
    print("Digite 3 para sair do jogo")
    escolha = int(input("Digite sua escolha: "))
    
    if escolha == 0:
        print("1° - Escolha se você quer ser par ou ímpar")
        print("2° - Digite um número de 0 a 10")
        print("3° - Descubra se você ganhou ou não")
        print("Qual a funcionalidade do jogo?")
        print("O jogo funciona da seguinte maneira: O jogador e o computador decidem quem vai ser par ou ímpar, em seguida, escolhem um número de 0 a 10. Após isso, a soma dos números é efetuada e o resultado e ele sendo par ou ímpar irá definir quem ganhou")
    elif escolha == 1:
        impar_par = int(input("Digite 1 se você deseja ser par ou 2 se você deseja ser ímpar: "))
        num = int(input("Digite um número de 0 a 10: "))
        num2 = random.randint(1,10)
        soma = num + num2
        print ("")
        print("Eu escolhi o número:" , num2)
        print("Você escolheu o número:" , num)
        print("")
        if impar_par == 1 and soma % 2 == 0:
           print(soma, "A soma é par, você ganhou!")
        elif impar_par == 1 and soma % 2 == 1:
           print(soma, "A soma é ímpar, você perdeu!")
        elif impar_par == 2 and soma % 2 == 0:
           print(soma, "A soma é par, você perdeu!")
        else:
            print(soma, "A soma é ímpar, você ganhou!")
        
    elif escolha == 3:
        print("Você saiu!")
        break
    
    else:
        print("Opção inválida")