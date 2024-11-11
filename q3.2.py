# 3.	Você está desenvolvendo uma ferramenta de análise de dados que precisa identificar números duplicados 
# em uma lista grande de valores. A lista pode ter milhões de elementos, e é necessário escolher um algoritmo 
# eficiente para encontrar esses duplicados. 
# Implemente duas funções em Python que encontrem números duplicados em uma lista:
# a.	A primeira função deve verificar cada elemento comparando-o com todos os outros, uma abordagem de força bruta.
# b.	A segunda função deve utilizar uma estrutura de dados adequada para melhorar a eficiência da busca de duplicados.

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return duplicates

lista = [1, 2, 6, 3, 7, 8, 2, 4, 6, 2, 9, 12, 3, 24, 15, 2, 12]
print(find_duplicates(lista))
