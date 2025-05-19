#uma pequena lista com os nomes dos cinco objetos
objetos = ["mesa", "ventilador", "caneta", "cadeira", "garrafa"]
print("")

#mais um objeto foi adicionado na lista
objetos.append("ar - condicionado")
print("")

#o segundo objeto da lista vai ser exibido
print(objetos[1])
print("")

#aqui, o objeto será removido e depois exibido
removido = objetos.pop(2)
print(removido)
print("")

#todos os itens serão exibidos
for objeto in objetos:
    print(objeto)
    print("")
    
#verificar se "cadeira" está na lista    
if "cadeira" in objetos:
    objetos.remove("cadeira")
else:
    objetos.append("cadeira")
#a lista estará em ordem    
print(objetos)
objetos.sort()
print("")

#o primeiro e o ultimo numero sera exibido
print(objetos)
print(objetos[0])
ultimo_elemento = objetos.pop()
objetos.append(ultimo_elemento)
print(ultimo_elemento)
print("")

#a lista ficará limpa
objetos.clear()
