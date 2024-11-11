# 8.	Imagine que você está desenvolvendo um sistema de atendimento em uma clínica médica. 
# Os pacientes entram na fila de atendimento conforme a ordem de chegada, mas, em alguns casos, 
# a clínica decide reverter a ordem da fila para que os últimos pacientes a chegarem sejam atendidos primeiro 
# (como, por exemplo, para um evento especial ou mutirão).
# Para implementar essa funcionalidade, você precisa criar uma função que inverta a ordem dos elementos 
# da fila, de modo que o primeiro paciente da fila passe a ser o último e o último passe a ser o primeiro.
# Implemente uma função inverter_fila, que:
# a.	Receba uma fila de pacientes (onde cada elemento representa um paciente em ordem de chegada).
# b.	Reposicione os elementos para que o primeiro elemento da fila se torne o último e vice-versa.
# c.	Retorne a fila com a ordem invertida.

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

def reverse_queue_order(queue):
    temp = []
    while not queue.is_empty():
        patient = queue.dequeue()
        temp.append(patient)
    while temp:
        patient = temp.pop()
        queue.enqueue(patient)
    return queue

fila_pacientes = Queue()
fila_pacientes.enqueue("Marco Alberto")
fila_pacientes.enqueue("Ana Clara")
fila_pacientes.enqueue("João de Souza")
fila_pacientes.enqueue("Maria Aparecida")
fila_pacientes.enqueue("Simone Silva")
fila_pacientes.enqueue("Lucas Pinheiro")

print("Ordem da fila antes da inversão:")
fila_pacientes.display()

# Inverter a fila
reverse_queue_order(fila_pacientes)

print("Ordem da fila após a inversão:")
fila_pacientes.display()