# Estrutura With serve, principalmente para a abertura e fechamento de arquivos.

# -- Sem estrutura With --

arquivo = open("arquivo_vazio.txt", "w")


arquivo.write("Oi")
arquivo.close() # Serve, como o nome já diz.. para fechar o arquivo aberto. 


# -- Com estrutura With --

with open("arquivo_vazio.txt", "w") as arquivo:
    arquivo.write("Boa Tarde")


with open("arquivo_vazio.txt", "r") as arquivo:
    print(arquivo.read())   


### "w" é um parâmetro de 'Editar o arquivo'.
### "r" é um parâmetro de 'leitura de arquivo'. 