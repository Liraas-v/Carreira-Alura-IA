# um novo aluno foi matriculado na escola, precisamos alocar o aluno em uma sala aleatoria.

import random # biblioteca random é usada para gerar números aleatórios, o que nos permite alocar o aluno em uma sala de forma aleatória

def alocar_aluno_fiap(nome_aluno, sala_de_aula): # a função alocar_aluno_fiap recebe dois parâmetros: nome_aluno, que é o nome do aluno a ser alocado, e sala_de_aula, que é uma lista de salas disponíveis para alocação
    sala_aleatoria = random.choice(sala_de_aula) # a função random.choice é usada para selecionar aleatoriamente um elemento da lista sala_de_aula, que representa as salas disponíveis para alocação
    print(f"O aluno {nome_aluno} foi alocado na sala {sala_aleatoria}.") # a função imprime uma mensagem indicando o nome do aluno e a sala em que ele foi alocado

# exemplo de uso da função alocar_aluno_fiap
salas = ["Sala 101", "Sala 102", "Sala 103", "Sala 104"] # lista de salas disponíveis para alocação
alocar_aluno_fiap("Henrique", salas) # a função alocar_aluno_fiap é chamada com o nome do aluno "Henrique" e a lista de salas, e a função executa o código para alocar o aluno em uma sala aleatória e imprimir a mensagem correspondente

