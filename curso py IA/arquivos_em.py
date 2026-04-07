# ************************* manipulando arquivos *************************

# abrir um arquivo
arquivo = open('arquivo.txt', 'r')  # 'r' para leitura
conteudo = arquivo.read()  # ler o conteúdo do arquivo
print(conteudo)  # imprimir o conteúdo
arquivo.close()  # fechar o arquivo

# escrever em um arquivo
arquivo = open('arquivo.txt', 'w')  # 'w' para escrita (sobrescreve o arquivo)
arquivo.write('Olá, mundo!')  # escrever no arquivo
arquivo.close()  # fechar o arquivo

# adicionar ao arquivo
arquivo = open('arquivo.txt', 'a')  # 'a' para adicionar (append)
arquivo.write('\nAdicionando uma nova linha.')  # adicionar uma nova linha
arquivo.close()  # fechar o arquivo

# ler o arquivo linha por linha
arquivo = open('arquivo.txt', 'r')
for linha in arquivo:
    print(linha.strip())  # imprimir cada linha sem espaços extras
    arquivo.close()  # fechar o arquivo

# usando with para manipular arquivos (garante que o arquivo seja fechado)
with open('arquivo.txt', 'r') as arquivo: # 'with' para abrir o arquivo e garantir que ele seja fechado automaticamente
    conteudo = arquivo.read()
    print(conteudo)


