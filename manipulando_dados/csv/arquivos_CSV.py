import csv

with  open("Python\\manipulando_dados\\advertising.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        print(linha)
    
    

# Estrutura with ela vai permitir que vc faça o trabalho que vc quer nos dados, e dps ela vai fechar. 
## Normalmente seria assim: arquivo = "advertising.csv"
### "r" é um parâmetro de 'leitura de arquivo'. 
### "w" é um parâmetro de 'Editar o arquivo'.

