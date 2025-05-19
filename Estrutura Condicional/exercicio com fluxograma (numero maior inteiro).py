print("Qual é o maior entre os números inteiros")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1>n2:
    if n1>n3:
        print(n1, "é o maior número")
elif n3>n1:
     if n3>n2:
        print(n3, "é o maior número")
elif n2>n1:
     if n2>n3:
         print(n2, "é o maior número")
