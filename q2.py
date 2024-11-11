
# 2.	Imagine que você está desenvolvendo uma aplicação para processar uma lista com 5 milhões de registros. 
# Sua tarefa é implementar uma função para ordenar esses registros de maneira eficiente.
# a.	Implemente uma função para ordenar a lista.
# b.	Determine a complexidade de tempo do algoritmo de ordenação escolhido usando a notação Big O.

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge(sleft, sright)

def merge(left, right):
    result = []
    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result

lista = [54,26,93,17,77,31,44,55,20]
merge_lista = merge_sort(lista)
print(merge_lista)