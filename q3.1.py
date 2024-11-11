# 3.	Você está desenvolvendo uma ferramenta de análise de dados que precisa identificar números duplicados 
# em uma lista grande de valores. A lista pode ter milhões de elementos, e é necessário escolher um algoritmo 
# eficiente para encontrar esses duplicados. 
# Implemente duas funções em Python que encontrem números duplicados em uma lista:
# a.	A primeira função deve verificar cada elemento comparando-o com todos os outros, uma abordagem de força bruta.
# b.	A segunda função deve utilizar uma estrutura de dados adequada para melhorar a eficiência da busca de duplicados.

def find_duplicates_bf(arr):
    duplicates = set()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.add(arr[i])
    return duplicates

lista = [1, 2, 6, 3, 7, 8, 2, 4, 6, 2, 9]
print(find_duplicates_bf(lista)) 
