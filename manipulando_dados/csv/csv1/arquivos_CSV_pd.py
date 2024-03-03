import pandas as pd

tabela = pd.read_csv('Python\\manipulando_dados\\csv\\csv1\\advertising1.csv', sep=',')
print(tabela)

# Como somar os valores de uma coluna no Pandas.

print(tabela['Vendas'].sum()) 
## método .sum é usado para somar. 
## Se quiser mudar a coluna que vai ser somada, é só trocar o parâmetro ('TV') pelos outros parâmetros (Radio, Jornal ou Vendas.. nesse caso).



