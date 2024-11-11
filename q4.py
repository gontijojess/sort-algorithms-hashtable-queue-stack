# 4.	Imagine que você está desenvolvendo uma aplicação de notas escolares onde os resultados das 
# avaliações de cada aluno são armazenados em uma pilha, de modo que as últimas notas lançadas ficam no topo. 
# Para gerar um relatório de desempenho, é necessário exibir as notas em ordem crescente, o que permite visualizar 
# facilmente a evolução e as tendências de desempenho do aluno.
# a.	Sua tarefa é criar uma função que ordene os valores dessa pilha em ordem crescente.

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

def sort_stack(stack):
    temp_stack = Stack()
    
    while not stack.is_empty():
        temp = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        
        temp_stack.push(temp)
    
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


notas = Stack()
notas.push(3)
notas.push(1)
notas.push(4)
notas.push(2)

print("Notas antes da ordenação:")
notas.display()

sort_stack(notas)

print("Notas após a ordenação crescente:")
notas.display()