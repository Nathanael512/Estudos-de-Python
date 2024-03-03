import csv

with  open("Python\\manipulando_dados\\csv\\csv0\\advertising.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv): # Ao invés de só pegar os valores das linhas, o enumerate pega o índice da linha (o 'i' dps do for).
        if i == 0:
            print('Cabeçalho: ' + str(linha))
        else:
             print('Valor: ' + str(linha))   
    
    

# Estrutura with ela vai permitir que vc faça o trabalho que vc quer nos dados, e dps ela vai fechar. 
## Normalmente seria assim: arquivo = "advertising.csv"
### "r" é um parâmetro de 'leitura de arquivo'. 
### "w" é um parâmetro de 'Editar o arquivo'.


