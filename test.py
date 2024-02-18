  
my_list = [3, 7 ,5, 'ok']
my_list.append(my_list)

for index, data in enumerate(my_list):
    if data == 'ok':
        print("Elemento encontrado no índice", index)
    else:
        print('Elemento não encontrado')
       