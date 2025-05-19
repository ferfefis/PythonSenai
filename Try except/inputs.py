print("Inputs")

#input str
def input_str(recado):
    while True: 
        nome=input(recado)
        
        if not nome.isalpha():
            print("Digite apenas letras")
            
        else:
            return nome
        
 #input int       
def input_int(recado):
    while True:
        try:
            numero=int(input(recado))
            return numero
            
        except ValueError:
            print("Digite apenas números inteiros")
            
 #input float           
def input_float(recado, decimal = 2):
    while True:
        try:
            numero2=float(input(recado))
            return round(numero2, decimal)
        
        except ValueError:
            print("Digite apenas números")


            
        
    
       
        
    
    