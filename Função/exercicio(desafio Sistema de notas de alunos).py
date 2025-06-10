print("Sistema de notas de alunos!")

def menu():
    print("1 - Calcular a média")
    print("2 - Cadastrar os nomes")
    print("3 - Exibir o resultado final")
    print("0 - Sair")


def calcular_media (n1, n2, n3): #calcula a média dos alunos
    media = (n1 + n2 + n3) / 3
    return media

def verificar_situacao (media): #verifica se o aluno esta aprovado,reprovado ou de recuperação
    if media >= 7:
        return "Aprovado"
    
    elif media >= 5 and media <7:
        return "Recuperação"
    
    elif media <5:
        return"Reprovado"

def cadastrar_aluno(alunos): #Coleta os dados do aluno
    nome = input("Digite o nome: ")
    aluno = {
    "nome" : nome,
    }
    m = calcular_media(n1, n2, n3)
    s = verificar_situacao(m)
    aluno["media"] = m
    aluno["situação"] = s
            
    alunos.append(aluno)
            
def mostrar_relatorio(alunos):
    for aluno in alunos:
        for chave, valor in aluno.items():
            print(f"{chave}-{valor}")
            
            
alunos = []

while True:
    menu()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 0:
        print("Você saiu!")
        break
    
    elif escolha == 1:
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))
        verificar_situacao(calcular_media(n1, n2, n3))
        print("Média calculada com sucesso!")
        
    elif escolha == 2:
        cadastrar_aluno(alunos)
        print("Nome cadastrado!")
        
    elif escolha == 3:
        mostrar_relatorio(alunos)
        
        
    else:
        print("Essa escolha não existe!")
            
    
    

