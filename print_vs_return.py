#

nome = "Nathan"
valor_do_print = print("Obter", nome)
print("Na variável", valor_do_print)

# 

def mostra(*args):
    print(*args)


nome1 = "Nata"
valor_do_print1 = mostra("Obter", nome1)
mostra("Na variável", valor_do_print1)

# 

def mostra(nome):
    novo_nome = '*** '
    novo_nome += nome
    novo_nome += ' ***'
    return novo_nome  


valor_do_print2 = mostra('Natanael')
print("Na variável", valor_do_print2)


valor_do_print3 = mostra("Nathaniel")
print("Na variável", valor_do_print3)




