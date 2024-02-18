# Exemplo de f-string em Python

nome = 'Natanael'
idade = 24

mensagem = f"Olá!!, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)

# Exemplo de expressões dentro de uma f-string

a = 765
b = 961
c = a + b
print(c)

## Aqui em cima só é a junção das variáveis A e B na variável C. Só o resultado, só montra o dado somado de cada variável. 



## resultado = f"A soma de {a} e {b} é igual a {a+b}"
print(f"A soma de {a} e {b} é igual a {a+b}")


# Exemplo de formatação de números com f-string

valor = 1519.25012

## Limita o número de casas decimais para 2, arredondando.
print(f"O valor é: {valor:.2f}")


# Saída de múltiplas linhas

# Exemplo de f-string para saída de múltiplas linhas

nome1 = "Nathan"
idade1 = 23
profissao = "Jardineiro"

mensagem1 = f"""
Olá {nome1}

Bem-vindo(a) ao nosso sistema!

Aqui estão algumas informações sobre você:
- idade: {idade1} anos
- Profissão: {profissao}

Atenciosamente,
A equipe do sistema
"""

print(mensagem1)


# Exemplo de f-string para saída de múltiplas linhas com a função de receber informações do usuário

nome_usuario = input("Digite o seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
profissao_usuario = input("Digite sua profissão: ")

mensagem_usuario = f"""
Olá {nome_usuario}

Bem-vindo(a) ao nosso sistema!

Aqui estão as algumas informações sobre você:
- idade: {idade_usuario}
- Profissão: {profissao_usuario}

Atenciosamente, 
A equipe do sistema
"""

print(mensagem_usuario)

# usando dicionários 

## Exemplo de f-string com dicionário

pessoa = {
    "nome": "João",
    "idade": 30,
    "profissao": "programador"
}

mensagem2 = f"Olá, meu nome é {pessoa['nome']}, tenho {pessoa['idade']} anos e sou {pessoa['profissao']}."

print(mensagem2)

# Caracteres de escape em f-strings

## Exemplo de uso de quebra de linha com \n em f-string
nome2 = "João"
mensagem3 = f"Olá, {nome2}!\nBem-vindo ao nosso sistema."

print(mensagem3)


## Exemplo de uso de aspas dentro da f-string com \"

mensagem4 = f"Ele disse: \"Isso é incrível! \""

print(mensagem4)

# Barra invertida com f-string 

path = "C:\\Users\\Natha\\Documentos\\Texto.txt"
mensagem5 = f"Caminho do arquivo: {path}"
print(mensagem5)

# Tabulação com \t em f-string

nome3 = "Pedro"
mensagem6 = f"Nome:\nIdade:\t22"

print(mensagem6)


# Funções em f-string embutida len() em uma f-string

nome4 = "Mariana"
print(f"Olá, {nome4}! Seu nome tem {len(nome4)} letras.")

## Funções em f-string com input do usuário

nome_usuario1 = input('Digite seu nome: ')
print(f"Olá, {nome_usuario1}! Seu nome tem {len(nome_usuario1)} letras.")



# Exemplo usando uma função definida pelo usuário em uma f-string

def calcular_dobro(numero):
    return numero * 2

valor1 = 10
mensagem7 = f"O dobro de {valor1} é {calcular_dobro(valor1)}"

print(mensagem7)

## Mesmo código de cima com o acrescento da função Input

def calcular_dobro(numero):
    return numero * 2

valor2 = int(input('Digite o valor a ser dobrado: '))
mensagem8 = f"O dobro de {valor2} é {calcular_dobro(valor2)}"

print(mensagem8)


# Função com múltiplos parâmetros em uma f-string

def concatenar_nomes(nome5, nome6):
    return f"{nome5} e {nome6}"
    
nome5 = "Ada"
nome6 = "Alan"   
mensagem9 = f"Os nomes concatenados são: {concatenar_nomes(nome5, nome6)}"

print(mensagem9)


# Exemplos usando função de formatação em uma f_string 

def formatar_nome(nome7):
    return nome7.upper()

nome7 = "Alice"
mensagem10 = f"Olá, {formatar_nome(nome7)}. Bem-vindo(a)!"

print(mensagem10)



