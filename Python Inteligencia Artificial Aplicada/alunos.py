lista_de_nomes = ["joao", "maria", "jose", "ana", "carlos"]
listas_de_medias = [8.5, 5.2 , 4.3 , 9.3, 3.5]

# percorra a lista de medias e adicione 1 ponto para os alunos, onde a media maxima é 10 

for i in range(len(listas_de_medias)): 
    # percorre a lista de medias usando o indice i
    # range(len(listas_de_medias)) retorna uma sequência de números de 0 até o tamanho da lista de medias - 1, permitindo acessar cada elemento da lista usando o indice i
    # dentro do loop, verifica se a media do aluno é menor que 10, se for, adiciona 1 ponto a media e verifica se a media ultrapassou 10, se sim, define a media como 10
    if listas_de_medias[i] < 10:
        listas_de_medias[i] += 1
        if listas_de_medias[i] > 10:
            listas_de_medias[i] = 10
# imprima a lista de nomes e medias atualizada
for i in range(len(lista_de_nomes)):
    print(f"{lista_de_nomes[i]}: {listas_de_medias[i]}")    
