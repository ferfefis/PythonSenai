def cadastro (isbn, titulo, autor, categoria, ano_da_publicacao):
    livro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano da publicacao": ano_da_publicacao,
    }
    livros.append(livro)
    
livros = []


while True:
    print("Menu das funções")
    print("")

    print("Digite 1 para cadastrar o livro: ")
    print("Digite 2 para visualizar os livros cadastrados: ")
    print("Digite 3 para ver a quantidade total de livros cadastrados: ")
    print("Digite 4 para gerar uma lista com o título dos livros cadastrados: ")
    print("Digite 0 para sair")
    print("")
    
    escolha = int(input("Digite sua escolha: "))
    if escolha == 0:
        print("Você saiu!")
        break
        
    elif escolha == 1:
        isbn = int(input("Digite o código do livro: "))
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        categoria = input("Digite qual a categoria do livro: ")
        ano_da_publicacao = int(input("Digite o ano de publicação do livro: "))

        cadastro(isbn, titulo, autor, categoria, ano_da_publicacao)
        print("Você cadastrou o seu livro")
            
    elif escolha == 2:
        for livro in livros:
            for chave, valor in livro.items():
                print(f"{chave} - {valor}")
               
    elif escolha == 3:
        print(len(livros))
            
    elif escolha == 4:
        for livro in livros:
            print(livros[1])
        
    

