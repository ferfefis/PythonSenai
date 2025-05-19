print("Calculador de despesas")

valor = 0
num_despesas = 0 

while True: 
    print("Calculador de despesas")
    print("Para adicionar o valor da despesa, digite 1")
    print("Para mostrar a quantidade e o valor total das despesas, digite 2")
    print("Para sair, clique no 0")
    menu = int(input("O que você quer fazer hoje? "))
    if menu == 0:
        print("Você saiu!")
        break
    elif menu == 1:
        adicionar_valor = int(input("Qual valor você quer adicionar? Digite aqui:"))
        print("Você adicionou ", adicionar_valor , "reais em sua despesa")
        num_despesas += 1
        valor = adicionar_valor + valor
        
    elif menu == 2:
        print("Você tem o total de ", num_despesas , "despesas, que somam " , valor , "reais de despesas")
        
    else:
        print("Opção inválida!")