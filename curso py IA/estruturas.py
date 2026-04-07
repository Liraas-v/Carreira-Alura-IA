# estruturas de dados em python


# ******************** listas ******************************

lista = [1, 2, 3, 4, 5]
print(lista)
# listas são mutáveis, ou seja, podemos alterar seus elementos
lista[0] = 10
print(lista)
# resultado: [10, 2, 3, 4, 5]

# ****************** como manipular uma lista **********************

#remover um elemento da lista
lista.remove(3)
    # remove o elemento 3 da lista
print(lista)
# resultado: [10, 2, 4, 5]

# como adicionar um elemento na lista
lista.append(6)
    # append adiciona um elemento no final da lista
print(lista)
# resultado: [10, 2, 4, 5, 6]

# como exibir o ultimo elemento da lista
print(lista[-1]) # resultado: 6, o índice -1 representa o último elemento da lista

# como particionar a lista em sublistas
sublista = lista[1:4] # resultado: [2, 4, 5]
                     # o índice 1 é o início da sublista e o índice 4 é o final da sublista (não incluído)
print(sublista)
                                 
# len 
print(len(lista)) # resultado: 5
# a função len retorna o número de elementos da lista


# *************************** tuplas **********************************

tupla = (1, 2, 3, 4, 5)
print(tupla)
# tuplas são imutáveis, ou seja, não podemos alterar seus elementos
# tupla[0] = 10 # isso vai gerar um erro, pois tuplas


# *************************** dicionários **********************************

dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print(dicionario)
# para acessar um valor do dicionário, usamos a chave correspondente
print(dicionario['nome']) # resultado: João
# um dicionário é uma coleção de pares chave-valor, onde cada chave é única e está associada a um valor correspondente
# exemplo "idade" é a chave e 30 é o valor correspondente


# *************************** como manipular um dicionário **********************************

# alterar o valor de uma chave
dicionario['idade'] = 31 # isso vai alterar o valor da chave "idade" para 31
print(dicionario) # resultado: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo'}

# como adicionar um novo par chave-valor ao dicionário
dicionario['profissão'] = 'Engenheiro' # isso vai adicionar um novo par chave-valor ao dicionário, onde a chave é "profissão" e o valor é "Engenheiro"
print(dicionario) # resultado: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# como remover um par chave-valor do dicionario
del dicionario['cidade'] # isso vai remover o par chave-valor onde a chave é "cidade"
print(dicionario) # resultado: {'nome': 'João', 'idade': 31, 'profissão': 'Engenheiro'}

# .get 
print(dicionario.get('nome')) # resultado: João
# o método get retorna o valor associado à chave especificada, ou None se a chave não estiver presente no dicionário
print(dicionario.get('cidade')) # resultado: None, pois a chave "cidade" foi removida do dicionário

# .keys
print(dicionario.keys()) # resultado: dict_keys(['nome', 'idade', 'profissão'])
# o método keys retorna uma visão das chaves do dicionário

# .values
print(dicionario.values()) # resultado: dict_values(['João', 31, 'Engenheiro'])
# o método values retorna uma visão dos valores do dicionário

# pop 
print(dicionario.pop('profissão')) # resultado: Engenheiro
# o método pop remove o par chave-valor associado à chave especificada e retorna o valor correspondente. Se a chave não estiver presente no dicionário, ele gera um erro KeyError
print(dicionario) # resultado: {'nome': 'João', 'idade': 31}




# *************************** conjuntos **********************************
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# *************************** filas **********************************

from collections import deque
fila = deque([1, 2, 3, 4, 5])
print(fila)
# pilhas
pilha = [1, 2, 3, 4, 5]
print(pilha)



# estruturas de repeticão em python

# *************************** for **********************************

for i in range(5): # o numero colocado dentro do range é o número de vezes que o loop vai ser executado, e ele começa a contar a partir de 0 e termina em 4 (5 não incluído)
    print(i)
# resultado: 0, 1, 2, 3, 4
# o loop for itera sobre uma sequência de números gerada pela função range, que começa em 0 e termina em 5 (não incluído)

# *************************** while **********************************

contador = 0
while contador < 5: # o loop while é executado enquanto a condição contador < 5 for verdadeira
    print(contador)
    contador += 1 # isso é equivalente a contador = contador + 1, ou seja, incrementa o valor de contador em 1 a cada iteração do loop
# resultado: 0, 1, 2, 3, 4


# *************************** if,else e elif **********************************

x = 10
if x > 0: # a estrutura if é usada para executar um bloco de código se uma condição for verdadeira
    print("x é positivo") # resultado: x é positivo, pois a condição x > 0 é verdadeira
elif x < 0: # a estrutura elif é usada para verificar uma condição adicional quando a condição if é falsa
    print("x é negativo") # so seria executado se a condição x < 0 fosse verdadeira, mas como x é 10, essa condição é falsa e esse bloco de código não é executado
else: # a estrutura else é usada para executar um bloco de código quando nenhuma das condições anteriores for verdadeira
    print("x é zero") # so é executado se as condições if e elif forem falsas, mas como x é 10, essa condição é falsa e esse bloco de código não é executado

# *************************** break e continue **********************************

for i in range(10):
    if i == 5:
        break # o comando break é usado para sair imediatamente do loop quando a condição i == 5 for verdadeira, ou seja, quando i for igual a 5, o loop é interrompido e o programa continua a execução após o loop
    print(i) # resultado: 0, 1, 2, 3, 4
for i in range(10):
    if i == 5:
        continue # o comando continue é usado para pular a iteração atual do loop quando a condição i == 5 for verdadeira, ou seja, quando i for igual a 5, o comando continue é executado e o programa pula para a próxima iteração do loop, sem executar o código abaixo do comando continue para essa iteração específica
    print(i) # resultado: 0, 1, 2, 3, 4, 6, 7, 8, 9 (o número 5 é pulado devido ao comando continue)

# *************************** funções **********************************

def saudacao(nome): # a palavra-chave def é usada para definir uma função em python, seguida pelo nome da função e parênteses que podem conter parâmetros. No exemplo, a função saudacao recebe um parâmetro chamado nome
    print(f"Olá, {nome}!") # o corpo da função é indentado e contém o código que será executado quando a função for chamada. No exemplo, a função imprime uma mensagem de saudação usando o valor do parâmetro nome
saudacao("João") # resultado: Olá, João!, a função saudacao é chamada com o argumento "João", que é passado para o parâmetro nome da função, e a função executa o código dentro do seu corpo, imprimindo a mensagem de saudação com o nome fornecido

# uma função sempre deve ter um nome, pode ter parâmetros (opcionais) e deve conter um bloco de código que define o que a função faz. As funções são reutilizáveis e podem ser chamadas várias vezes em um programa, permitindo a modularização e organização do código.
# dentro dos () são argumentos, ou seja, os valores que são passados para a função quando ela é chamada. Esses argumentos são usados para fornecer informações ou dados que a função pode processar e usar em seu código. No exemplo da função saudacao, o argumento nome é usado para personalizar a mensagem de saudação com o nome fornecido quando a função é chamada.


