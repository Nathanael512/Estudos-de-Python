# O "For" no Python é diferente de outras linguagens, no Python o "For" é utilizado para trabalhar com listas. O "For" passa por cada um dado que a lista tem.

frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)  # Ele executa em sequência separado cada dado.

for i in range(5):
    print(i)

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")





nomes = ["Tomie", "Ayako"]


for nome in nomes:  # : é utilizado para o Python entender que a instrução foi finalizada.
   print("Olá, " + nome) # Aqui o operador + é usado para concatenar os dados.  
    
    
numeros =  [1, 2, 3]

for n in numeros:
    print(3 + n)
