

# -- Imprimindo os valores da lista --

numbers1 = [1,2,3,4,5,6]
print('Números da lista "numbers1":\n')

for i in numbers1:
    print(f'número {i} da lista "numbers"')

print() # Os prints sem argumentos, são usados para dar um espaçamento.

# -- Imprimindo os valores na lista nova --

print('Números da lista "new_numbers1" são:\n')
numbers2 = [1, 2, 3, 4, 5, 6]
new_numbers1 = []

for i in numbers2:
    new_numbers1.append(i)

print(new_numbers1,'\n')

# -- Multiplicando e imprimindo os valores na lista nova --

print('Números multiplicados por 10x da lista "doubled_numbers1" são:\n')
numbers3 = [10, 20, 30, 40, 50, 60]
doubled_numbers1 = []

for i in numbers3:
    doubled_numbers1.append(i * 10)

print(doubled_numbers1,'\n')

# --- Forma mais concisa de multiplicar e imprimir os valores na lista nova ---

print('Números multiplicados por 10x da lista "doubled_numbers2" são:\n')
numbers4 = [150, 250, 350, 450, 550, 650]
doubled_numbers2 = [i * 10 for i in numbers4]

print(doubled_numbers2,'\n')


