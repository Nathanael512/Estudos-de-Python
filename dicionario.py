

# dicionário


dic = {
    "nome": "Tomie",
    "nome1": "Ayako",
    "nome2": "Haruka",
    5: "cinco",
    "lista": [7, 12, 765]
}

dic['novo nome'] = "Matsuri"

print(dic)
print(dic['nome2'])
print(dic["lista"][2])
print(dic.keys())  # .keys é uma função para mostra só as chaves.
print(dic.values()) # .values é uma função para mostra só as chaves.


for chave, valor in dic.items():
    print(chave, valor)
