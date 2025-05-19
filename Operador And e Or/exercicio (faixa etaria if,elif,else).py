print("Faixa etária")

ano_nascimento = int(input("Digite seu ano de nascimento "))
ano_atual = int(input("Digite o ano em que estamos "))
if ano_atual <= 2025 and ano_atual >= 1908 and ano_nascimento >= 1908 and ano_nascimento <= 2025:

    idade = ano_atual - ano_nascimento

    if idade <= 10:
        print(idade, "Você é criança")
    elif idade >= 11 and idade <= 17:
        print(idade , "Você é adolescente")
    elif idade >= 18 and idade <= 59:
        print(idade, "Você é adulto")
    elif idade >= 60:
        print(idade, "Você é idoso")
else:
    print("Ano inválido")
