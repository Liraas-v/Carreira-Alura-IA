# *************************** pandas **********************************

import pandas as pd # a comunidade costuma chamar de pd

# criar um arquivo .txt a partir de perguntas vindas de uma lista em python
# ler as perguntas do arquivo .txt 
# obter respostas para as perguntas 
# salvar os resultados em um arquivo .csv usando pandas
# ler o arquivo .csv usando pandas e exibir os resultados

lista_perguntas = ["Qual e a capital da Franca?", "Quem e o presidente dos Estados Unidos?", "Qual e a fórmula da agua?"]
with open('perguntas.txt', 'w') as arquivo: # 'w' para escrita (sobrescreve o arquivo)
    for pergunta in lista_perguntas:
        arquivo.write(pergunta + '\n') # escrever cada pergunta em uma nova linha

# ler as perguntas do arquivo .txt
with open('perguntas.txt', 'r') as arquivo: # 'r' para leitura
    perguntas = arquivo.readlines() # ler todas as linhas do arquivo e armazenar em uma lista
    perguntas = [pergunta.strip() for pergunta in perguntas] # remover espaços extras e quebras de linha
print(perguntas) # resultado: ['Qual é a capital da França?', 'Quem é o presidente dos Estados Unidos?', 'Qual é a fórmula da água?']

# 'obter respostas para as perguntas 
respostas = ["A capital da França é Paris.", "O presidente dos Estados Unidos é Trump.", "A fórmula da água é H2O."]

# salvar os resultados em um arquivo .csv usando pandas
dados = {'Pergunta': perguntas, 'Resposta': respostas} # criar um dicionário com as perguntas e respostas, onde as perguntas vao estar na coluna 'Pergunta' e as respostas na coluna 'Resposta', com espaços para melhor visualização no arquivo .csv
df = pd.DataFrame(dados) # criar um DataFrame a partir do dicionário
df.to_csv('perguntas_respostas.csv', index=False) # salvar o DataFrame em um arquivo .csv, index=False para não incluir o índice no arquivo

# ler o arquivo .csv usando pandas e exibir os resultados
df_lido = pd.read_csv('perguntas_respostas.csv') # ler o arquivo .csv e armazenar em um DataFrame
print(df_lido) # exibir o conteúdo do DataFrame lido, resultado:
              #                                           Pergunta                                         Resposta
              # 0  Qual é a capital da França?         A capital da França é Paris.
              # 1  Quem é o presidente dos Estados Unidos?  O presidente dos Estados Unidos é Trump.
              # 2  Qual é a fórmula da água?           A fórmula da água é H2O. 
              

