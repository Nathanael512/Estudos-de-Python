# Juros Simples

C = 100
taxa_juros = 0.05

for periodo in range(1,6):
    M = C * (1 + taxa_juros * periodo)
    print(f'--- Ano {periodo}---')
    print(f'Montante: R$ {M:.2f}')
    print(f'-------------------\n')


# Juros Compostos
    
I = 100
taxa_composta = 0.05

# VP = Valor Presente, TJ = Taxa de Juros, NP Número de período, VF = Valor futuro

def juros_compostos(VP, TJ, NP):  # Aqui foi criado uma função para calcular os juros, sem precisar refazer a mesma lógica
    VF = VP * (1+TJ) ** NP
    return VF

for periodo_c in range(1,6):
    T = I * (1 + taxa_composta) ** periodo_c # Para usar a função juros_compostos basta: T = juros_compostos(I, taxa_composta, periodo_c)
    print(f'--- Ano {periodo_c}---')
    print(f'Montante: R$ {T:.2f}')
    print(f'-------------------\n')




