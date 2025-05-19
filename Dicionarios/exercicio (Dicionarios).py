print("Dicionarios")
#------------- Dicionarios ------------------

# Criar
aluno = {
    "nome": "Fernanda",
    "idade": 16,
    "altura": 1.66,
    "matriculado": True 
}

filme_martins = {
    "nome": "The Batman",
    "protagonista": "Batman",
    "ator/atriz": "Robert Pattison",
    "diretor": "Matt Reeves",
    "lançado": True 
    }

filme_veto = {
   "nome": "Moana - Um mar de aventuras",
   "protagonista": "Moana",
   "ator/atriz": "Auli'i Cravalho",
   "diretor": "John Musker e Ron Clements",
   "lançado": True 
   }

filme_ferfefis = {
    "nome": "Lilo & Stitch - Live Action",
    "protagonista": "Stitch",
    "ator/atriz": "Chris Sanders",
    "diretor": "Todd Cherniawsky",
    "lançado": False
    }
#print(aluno) 

# Adicionar campo
aluno["Peso"] = 57

#print(aluno)

# Alterar campo
aluno["Idade"] = 17

#print(aluno)

# Deletar campo
del aluno["altura"]

#print(aluno)

# Verificar
if "altura" in aluno:
    print("Altura existente")
else:
    #print("Altura inexistente")
    print()
    
# Exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Exibir uma lista de dicionarios
lista_filmes = [filme_martins, filme_veto, filme_ferfefis]

  # Escolhendo os campos
for filme in lista_filmes:
    print(f"{filme['nome']}")
    
  # Exibindo todos
for filme in lista_filmes:
    for chave, valor in filme.items():
        print(f"{chave} - {valor}")
    print("")