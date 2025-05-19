#passo a passo

#passo1: Achar a área do hexágono
#passo2: Solicitar a medida dos lados do triângulo
#passo3: Multiplicar o lado pelo lado do triângulo
#passo4: Descobrir raiz de 3
#passo5: Multiplicar a raiz pela multiplicação anterior
#passo6: Dividir por 4
#passo7: Multiplicar tudo por 6

print("Área do Hexágono")

lado = int(input("Digite um lado do hexágono " ))
lado2 = lado * lado
raiz = round( 3 ** 0.5 , 2)
multiplicação = lado2 * raiz
divisão = multiplicação / 4
multiplicação2 = round(divisão * 6, 2)

print("A área do hexágono é igual a " , multiplicação2)


