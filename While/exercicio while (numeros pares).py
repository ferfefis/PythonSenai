print("Números pares e sua quantidade")

inicio = int(input("Digite um número: "))

quant = 0
n = 0 

while n < inicio:
    n = n + 1
    if n % 2 == 0:
        print(n)
        quant += 1
print("A quantidade de números pares até seu número é ", quant)        
        
        
