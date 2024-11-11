# 10.	Imagine que você está desenvolvendo um sistema de gerenciamento de uma biblioteca, onde os livros 
# são organizados em uma fila para serem catalogados. Cada livro tem um número de identificação único, e 
# a biblioteca deseja oferecer um desconto especial para os livros cujos números de identificação são ímpares. 
# Para isso, você precisa implementar uma função que conte quantos livros na fila que possuem um 
# número de identificação ímpar.
# A função deve: 
# a.	Receber uma fila representando os números de identificação dos livros.
# b.	Retornar o número total de livros cuja identificação é um número ímpar.

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

def counting_odd_books(queue):
    quantity_odds = 0
    for livro_id in queue.itens:
        if livro_id % 2 != 0:
            quantity_odds += 1
    return quantity_odds


livros = Queue()
livros.enqueue(9)
livros.enqueue(7)
livros.enqueue(13)
livros.enqueue(2)
livros.enqueue(4)
livros.enqueue(12)
livros.enqueue(1)

qtd_livros_impares = counting_odd_books(livros)
print(f"Quantidade de livros impares: {qtd_livros_impares}")