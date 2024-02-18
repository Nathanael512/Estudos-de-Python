fruits = []

fruits.append('orange')
fruits.append('apple')
fruits.append('banana')
fruits.sort() # função .sort coloca os elementos nas posições de ordem alfabética
fruits.pop(1)
fruits.insert(0, 'orange')
c = fruits.count('orange') # função .count serve para contar a quantidade de itens 

print(c)

# fruits.clear() # função .clear serve para limpar uma lista

print(fruits)