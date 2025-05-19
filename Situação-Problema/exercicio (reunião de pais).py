import inputs
print("Reunião de pais")
print("")

print("Menu de opções")
print("Digite 1 para cadastrar o nome")
print("Digite 2 para exibir o total de pais")
print("Digite 3 para exibir a lista de nomes em ordem alfabética")
print("Digite 4 para a confirmação de presença dos pais")
print("Digite 5 para exibir o relatório da chamada")
print("Digite 6 para sair")
print("")

nomes = []
presentes = []
ausente = []

while True:
    opcao= inputs.input_int("Digite sua escolha: ")
    print("")


    if opcao == 1:
        nome= inputs.input_str("Digite o nome que quer cadastrar: ")
        if nome in nomes:
            print("Nome ja cadastrado!")
        else:
            nomes.append(nome)
            print("Nome cadastrado")
                    
    elif opcao == 2:
        print("O número total de pais inscritos até agora são ", len(nomes))
                    
    elif opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
                        
    elif opcao == 4:
        nome= inputs.input_str("Digite o nome para verificar se está presente: ")
        if nome in nomes:
            presentes.append(nome)
            print("Nome adicionado na lista de presentes!")
        
        else:
            ausentes.append (nome)
            print("Nome adicionado na lista de ausentes!")
            
    elif opcao == 5:
        print("Lista de presentes: ")
        for item in presentes:
            print(item)
        print()
        print("Lista de ausentes: ")
        for item1 in ausentes:
            print(item1)
                            
    elif opcao == 6:
        print("Você saiu!")
        break
                
    else:
        print("Opção não encontrada")