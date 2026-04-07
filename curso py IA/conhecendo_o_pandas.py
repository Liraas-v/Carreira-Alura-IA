# ********************* manipulando dados com pandas *********************
import pandas as pd
# Criando um DataFrame a partir de um dicionário
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(dados)
print(df)
# Acessando colunas
print(df['Nome'])
# Acessando linhas
print(df.loc[0])  # Acessa a primeira linha
# Filtrando dados
filtro = df['Idade'] > 28
print(df[filtro])
# Adicionando uma nova coluna
df['Profissão'] = ['Engenheira', 'Médico', 'Professor']
print(df)
# Removendo uma coluna
df = df.drop('Cidade', axis=1)
print(df)
# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)
# Lendo um DataFrame de um arquivo CSV
df_novo = pd.read_csv('dados.csv')
print(df_novo)


# ************************* filtrando dados com pandas *************************
# Criando um DataFrame a partir de um dicionário
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(dados)


# ******************** Filtrando dados com base em uma condição ********************

filtro = df['Idade'] > 30 # resultado: um filtro booleano que retorna True para as linhas onde a idade é maior que 30 e False para as outras linhas
df_filtrado = df[filtro]
print(df_filtrado)

# *********************** Filtrando dados com base em múltiplas condições ***********************

filtro = (df['Idade'] > 30) & (df['Cidade'] == 'Belo Horizonte') # resultado: um filtro booleano que retorna True para as linhas onde a idade é maior que 30 e a cidade é igual a "Belo Horizonte", e False para as outras linhas
df_filtrado = df[filtro]
print(df_filtrado)

# ********************** Filtrando dados usando o método query **********************

df_filtrado = df.query('Idade > 30 and Cidade == "Belo Horizonte"') # resultado: um DataFrame filtrado que contém apenas as linhas onde a idade é maior que 30 e a cidade é igual a "Belo Horizonte". O método query permite escrever a condição de filtragem de forma mais legível e concisa, usando uma sintaxe semelhante à linguagem SQL.
print(df_filtrado)
