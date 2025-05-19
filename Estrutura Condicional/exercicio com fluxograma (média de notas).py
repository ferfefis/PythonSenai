nota1= int(input("Digite sua primeira nota "))
nota2= int(input("Digite sua segunda nota para saber se foi aprovado "))
           
notas1 = nota1 + nota2
notas = notas1/2

a_ou_r = ""

if notas >= 70:
    a_ou_r = notas
    print("Sua nota foi " ,notas, " você foi aprovado")
    
else:
    a_ou_r = notas
    print("Sua nota foi " , notas, " você foi reprovado")