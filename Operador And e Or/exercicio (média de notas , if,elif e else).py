print("Média de notas")

nota1= int(input("Digite sua primeira nota "))
nota2= int(input("Digite sua segunda nota "))
if nota1 > 0 and nota1 <= 100 and nota2 > 0 and nota2 <= 100:
    adicao= nota1+nota2
    nota_geral= adicao / 2

    if nota_geral >= 70:
        print(nota_geral, "Voce foi aprovado")
    elif nota_geral >= 50 and nota_geral < 70:
            print(nota_geral , "Voce ficou de recuperação")
    elif nota_geral < 50:
        print(nota_geral, "Voce foi reprovado")
else: print("Sua nota é inválida") 
        
