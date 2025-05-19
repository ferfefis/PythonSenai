import inputs
print("Inscrições para o evento escolar")
print("")

print("Menu de opções")
print("Digite 1 para cadastrar o nome")
print("Digite 2 para exibir o total de inscritos")
print("Digite 3 para exibir a lista de nomes em ordem alfabética")
print("Digite 4 para permitir a consulta de um nome")
print("Digite 5 para sair")
print("")

nomes = []

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
        print("O número total de inscritos até agora são ", len(nomes))
                    
    elif opcao == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
                        
    elif opcao == 4:
        nome = inputs.input_str("Digite o nome que quer consultar: ")
                    
        if nome in nomes:
            vari= inputs.input_str("Nome encontrado, você deseja removê-lo da lista? s/n")
                        
            if vari == "s":
                nomes.remove(nome)
                print("Nome removido")
                            
            elif vari == "n":
                print("O nome ainda está na lista!")
                            
            else:
                print("Opção não encontrada!")
                            
        else:
            vari1 = inputs.input_str("Nome não encontrado, deseja adicioná-lo? s/n")
                        
            if vari1 == "s":
                nomes.append (nome)
                print("O nome foi adicionado na lista")
                            
            elif vari1 == "n":
                print("O nome continua fora da lista")
                            
            else:
                print("Opção não encontrada!")
                            
    elif opcao == 5:
        print("Você saiu!")
        break
                
    else:
        print("Opção não encontrada")
                      
