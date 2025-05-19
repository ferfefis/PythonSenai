print("Celcius para Fahrenheit e Kelvin")

def kelvin(celcius):
    k = celcius+237
    return k

def fahrenheit(celcius):
    f = celcius*1.8 + 32
    return round(f, 2)

celcius = int(input("Digite a temperatura em graus celcius: "))

print("A temperatura em Fahrenheit é ",fahrenheit(celcius) , 'e em Kelvin é', kelvin(celcius))