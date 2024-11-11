# 6.	Imagine que você está desenvolvendo uma aplicação para gerenciar pedidos de uma loja,
#  onde cada pedido possui um número único de identificação que é armazenado em uma pilha 
# (estrutura de dados que organiza os pedidos pela ordem de chegada). Sua equipe deseja analisar 
# esses pedidos para encontrar quantos deles possuem um número de identificação ímpar, pois isso 
# pode indicar um tipo especial de pedido para uma promoção. .
# a.	Sua tarefa é criar uma função que retorne a quantidade de pedidos com número de identificação ímpar na pilha de pedidos.

class Stack:
    def __init__(self):
        self.itens = []
    
    def is_empty(self):
        return len(self.itens) == 0
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"
    
    def size(self):
        return len(self.itens)
    
    def display(self):
        print("Pilha:", self.itens)

def counting_odd_orders(stack):
    quantity_odds = 0
    temp = Stack()
    while not stack.is_empty():
        order = stack.pop()
        if order % 2 != 0:
            quantity_odds += 1
        temp.push(order)
    while not temp.is_empty():
        stack.push(temp.pop())
    return quantity_odds


pedidos = Stack()
pedidos.push(9)
pedidos.push(7)
pedidos.push(2)
pedidos.push(4)
pedidos.push(1)

qtd_pedidos_impares = counting_odd_orders(pedidos)
print(f"Quantidade de pedidos impares: {qtd_pedidos_impares}")