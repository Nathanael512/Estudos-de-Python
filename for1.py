# No Python o "For" é um pouco diferente de outras linguagens, ele é mais utilizado para inteira em uma lista.

frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)

for i in range(5):
    print(i)

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")



nomes = ["Tomie", "Ayako"]

for nome in nomes: # : é utilizado para finalizar a instrução.
    print("Olá, " + nome) # Aqui o operador + é utilizado para concatenar os nomes.

numeros = [1, 2, 3]

for n in numeros:
    print(3 + n)

    
# Busca por elemento
    
my_list = [3, 7 ,5, 'ok']
index = 0

for data in my_list:
    if data == 'ok':
        print("Elemento encontrado no índice", index)
    else:
        print('Elemento não encontrado')
    index = index + 1        
    

my_list = [3, 7 ,5, 'ok']
my_list.append(my_list)

for index, data in enumerate(my_list):
    if data == 'ok':
        print("Elemento encontrado no índice", index)
    else:
        print('Elemento não encontrado')
       