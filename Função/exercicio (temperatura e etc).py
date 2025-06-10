def verificar_qualidade(temperatura, umidade, estacao):
   
    if estacao == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print("Ideal para o inverno")
           
    elif estacao == "verao":
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 40 and umidade <= 65:
                print("Ideal para o verão")
   
   
temperatura = int(input("Qual a temperatura? "))
umidade = int(input("Qual a umidade? "))
estacao = str(input("Qual a estação? "))
verificar_qualidade(temperatura, umidade, estacao)