# 5.	Imagine que você está desenvolvendo uma aplicação de gerenciamento de tarefas, onde cada tarefa é 
# armazenada em uma estrutura de dados do tipo "pilha". A cada nova tarefa adicionada, ela é empilhada no topo. 
# Para facilitar a visualização e o gerenciamento das tarefas, você precisa de uma função que retorne qual é 
# a tarefa mais recente (a que está no topo da pilha), pois essa é a próxima tarefa a ser concluída.
# Implemente uma função tarefa_no_topo(pilha_de_tarefas) que:
# a.	Receba uma pilha de tarefas.
# b.	Retorne o elemento que está no topo da pilha, sem removê-lo.

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

def tarefa_no_topo(pilha_de_tarefas):
    return pilha_de_tarefas.peek()


notas = Stack()
notas.push(9)
notas.push(7)

tarefa_recente = tarefa_no_topo(notas)
print(f"Tarefa mais recente: {tarefa_recente}")

notas.push(2)

tarefa_recente = tarefa_no_topo(notas)
print(f"Tarefa mais recente: {tarefa_recente}")