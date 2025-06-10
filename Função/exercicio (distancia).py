def distancia(km, velocidade):
    tempo_percurso = km / velocidade
    print("Levará", tempo_percurso, "horas")
   
km = int(input("Digite a distância em km: "))
velocidade = int(input("Digite a velocidade: "))
distancia(km, velocidade)
