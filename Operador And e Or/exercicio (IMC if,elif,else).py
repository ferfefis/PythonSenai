print("Qual é o seu IMC?")

peso = float(input("Digite seu peso em kilos "))
altura = float(input("Digite sua altura em metros "))

imc = peso/altura**2

if imc <= 19.1:
    print(f'{imc:.2f} , "Você está abaixo do peso"')
    
elif imc >= 19.1 and imc <= 27.3:
    print(f'{imc:.2f} , "Você está com o peso ideal"')
      
elif imc >= 27.3 and imc <= 32.3:
    print(f'{imc:.2f}, "Você está acima do peso"')
    
elif imc >= 32.4:
    print(f'{imc:.2f}, "Você está obeso"')