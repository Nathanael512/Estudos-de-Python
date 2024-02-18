
# Lista: Definida por colchetes `[]`. Exemplo: `lista = [1, 2, 3]`.

# booleano
# número = 11
# verdadeiro = "Verdade"
# if número == 10:
#   print(verdadeiro)

# lista (Array) vetores

lista1 = [1, 'Renato', 3.0, [1, 2, 3]]
nome1= lista1[1]
numero_da_lista = lista1[3][1]

print(lista1[3]) # print(lista1[Aqui eu escreve o item que eu quero imprimir])
print(lista1[3][1]) # print(lista1[sub-array][Para imprimir o dado de uma sub-array, eu devo fazer outra chave, e colocar dessa chave a posição desejada])
print(nome1) # print(Ou eu posso imprimir o dado através da variável que esteja atrelada ao dado, no caso; a variável 'nome1' está atrelado a posição 1/Renato)
print(numero_da_lista) # Posso criar uma variável para imprimir a posição do dado de uma sub-array

# lista com método

lista2 = [10, 20, 30, 40]
print(lista2)
lista2.append(50) # .append é usado para adicionar um dado, no caso é o '50'
print(lista2) # Como eu adicionei o dado '50', ele vai ser imprimido novamente. 
numero_retirado = lista2.pop(0) # .pop é usado para remover um dado, o dado retirado será colocado na variável 'numero_retirado'
print(lista2) # Como eu removi o '10', ele não será imprimido
print(numero_retirado) # Aqui estou mandando imprimir o dado que foi retirado  


lista2.insert(0, 'Nathan')  # .insert é usado para inserir um dado a uma posição, no caso o nome 'Nathan' será inserido na posição 0.
print(lista2)

pos = lista2.index('Nathan') # .index é usado para mostra a posição de um dado em uma array
print(pos)  

rem = lista2.remove(40) # .remove é usado para remover um dado, no caso será removido o 40.
print(lista2)
print(rem)

temperaturaMedia = []
temperaturaMedia.append(31.9)
temperaturaMedia.append(35.4)
temperaturaMedia.append(26.4)
temperaturaMedia.append(24.3)
temperaturaMedia.append(22.9)

for i in temperaturaMedia:
    print(i)


lista3 = [100, 150, 200, 250]

lista3.append(300)

print(lista3)

pessoa = ["Tomie", "Ayako", [7, 12]]

print(pessoa)
print(pessoa[2]) # Índice do elemento começa sempre a partir do 0

for i in pessoa:
    print(i)






