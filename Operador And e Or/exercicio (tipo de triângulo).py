print("Qual é o triângulo?")

lado1 = int(input("Digite o valor do primeiro lado do triangulo "))
lado2 = int(input("Digite o valor do segundo lado do triangulo "))
lado3 = int(input("Digite o valor do terceiro lado do triangulo "))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("O triândulo é equilátero")
elif lado1 == lado2 and lado2 == lado3 and lado2!=lado3 or lado1 == lado2 and lado2!=lado3  and lado1 == lado3 or lado1!=lado2 and lado2 == lado3 and lado1 == lado3 or lado1!=lado2 and lado2!=lado3 and lado1==lado3 or lado1 == lado2 and lado2!=lado3 and lado1!=lado3 or lado1!=lado2 and lado2==lado3 and lado1!=lado3 :  
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
