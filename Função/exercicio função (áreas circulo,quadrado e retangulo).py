def circulo(raio):
    area_circulo= 3.14*raio**2
    return area_circulo
   
def retangulo(base,altura):
    area_retangulo=base*altura
    return area_retangulo
   
def quadrado(lado):
    area_quadrado=lado*lado
    return area_quadrado

def triangulo(lado):
    multi= (lado1*lado1)*3**0.5
    area_triangulo= multi/4
    return area_triangulo

def hexagono(area_hexagono):
    area_hexagono = area_triangulo*6
    return area_hexagono
    
def tabela_area():
    print("1 - circulo")
    print("2 - retangulo")
    print("3 - quadrado")
    print("4 - triangulo")
    print("5 - hexagono")
   
    forma=int(input("Digite qual forma você deseja: "))
    if forma == 1:
        raio=int(input("Digite o raio do circulo: "))
        print(circulo(raio))
        
    elif forma==2:
        base=int(input("Digite a base do retangulo: "))
        altura=int(input("Digite a altura do retangulo: "))
        print(retangulo(base,altura))
        
    elif forma==3:
        lado_quadrado=int(input("Digite o lado do quadrado :"))
        print(quadrado(lado))
        
    elif forma==4:
        lado1= int(input("Digite o lado: "))
        print(triangulo(lado1))
           
    elif forma==5:
        lado_hexagono= int(input("Digite um lado do hexágono: "))
        print(hexagono(lado_hexagono))
        
    else:
        print("Opção não identificada, escolha somente as opções disponiveis")
   
def circulo_perimetro(raio_circulo):
    perimetro_circulo= 3.14*2*r
    return raio_circulo 
   
def retangulo_perimetro(base, altura):
    lado_retangulo=base+base
    return lado_retangulo

def quadrado_perimetro(lado):
    perimetro_quadrado=lado*4
    return perimetro_quadrado

def triangulo_perimetro(lado1):
    lado_triangulo= lado1*3
    return lado_triangulo

def hexagono_perimetro(lado_hexagono):
    perimetro_hexagono = lado_hexagono*6
    return perimetro_hexagono

def tabela_perimetro():
    print("1 - circulo")
    print("2 - retangulo")
    print("3 - quadrado")
    print("4 - triangulo")
    print("5 - hexagono")
   
    forma=int(input("Digite qual forma você deseja: "))
    if forma == 1:
        raio=int(input("Digite o raio do circulo: "))
        print(circulo_perimetro(raio))
        
    elif forma==2:
        base=int(input("Digite a base do retangulo: "))
        altura=int(input("Digite a altura do retangulo: "))
        print(retangulo_perimetro(base,altura))
        
    elif forma==3:
         lado=int(input("Digite o lado do quadrado :"))
         print(quadrado_perimetro(lado))
        
    elif forma==4:
        lado1= int(input("Digite o lado: "))
        print(triangulo_perimetro(lado1))
           
    elif forma==5:
        lado_hexagono= int(input("Digite um lado do hexágono: "))
        print(hexagono_perimetro(lado_hexagono))
        
    else:
        print("Opção não identificada, escolha somente as opções disponiveis")
        
print("Digite 1 para calcular a área")
print("Digite 2 para calcular o perimetro")

num= int(input("Escolha uma das opções "))

if num == 1:
    tabela_area()
    
elif num == 2:    
    tabela_perimetro()