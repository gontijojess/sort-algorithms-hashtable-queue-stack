# 9.	Considere uma lista contendo números inteiros. Escreva uma função para ordenar essa 
# fila em ordem crescente de seus valores. Não deve ser usada nenhuma função pronta de ordenação.

import sys
sys.stdout.reconfigure(encoding='utf-8')

class Queue:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        return self.itens.pop(0) 

    def peek(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            for item in self.itens:
                print(item, end=" ")
            print()

def sort_queue_asc(queue):
    for i in range(queue.size()):
        for j in range(queue.size() - 1):
            if queue.itens[j] > queue.itens[j + 1]:
                queue.itens[j], queue.itens[j + 1] = queue.itens[j + 1], queue.itens[j]


lista_inteiros = Queue()
lista_inteiros.enqueue(4)
lista_inteiros.enqueue(5)
lista_inteiros.enqueue(14)
lista_inteiros.enqueue(1)
lista_inteiros.enqueue(9)
lista_inteiros.enqueue(20)
lista_inteiros.enqueue(8)
lista_inteiros.enqueue(2)

print("Fila de números antes da ordenção:")
lista_inteiros.display()

sort_queue_asc(lista_inteiros)

print("Fila de números após a ordenção crescente:")
lista_inteiros.display()