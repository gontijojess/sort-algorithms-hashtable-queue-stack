# 11.	Uma empresa de atendimento ao cliente precisa gerenciar o fluxo de clientes em uma fila de espera. 
# Quando um cliente chega, ele é adicionado ao final da fila, e os atendentes sempre atendem o cliente que está 
# no início da fila. A empresa também quer saber quantos clientes ainda estão na fila a qualquer momento.
# Implemente uma classe FilaAtendimento que simule essa fila de atendimento ao cliente com as seguintes funções:
# a.	adicionar_cliente(nome): adiciona um cliente ao final da fila.
# b.	atender_cliente(): remove o cliente do início da fila e exibe o nome do cliente que está sendo atendido.
# c.	tamanho_fila(): retorna o número de clientes restantes na fila.

import sys
sys.stdout.reconfigure(encoding='utf-8')

class FilaAtendimento:
    def __init__(self):
        self.fila = [] 

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if not self.fila:
            print("Não há mais clientes para serem atendidos.")
        else:
            cliente_atendido = self.fila.pop(0)
            print(f"Cliente em atendimento: {cliente_atendido}")

    def tamanho_fila(self):
        return len(self.fila)

fila_atendimento = FilaAtendimento()

fila_atendimento.adicionar_cliente("Marco Alberto")
fila_atendimento.adicionar_cliente("Ana Clara")
fila_atendimento.adicionar_cliente("João de Souza")
fila_atendimento.adicionar_cliente("Maria Aparecida")

print(f"Número de clientes na fila: {fila_atendimento.tamanho_fila()}")
fila_atendimento.atender_cliente()
print(f"Número de clientes na fila: {fila_atendimento.tamanho_fila()}")
fila_atendimento.atender_cliente()
print(f"Número de clientes na fila: {fila_atendimento.tamanho_fila()}")
fila_atendimento.atender_cliente()
print(f"Número de clientes na fila: {fila_atendimento.tamanho_fila()}")
fila_atendimento.atender_cliente()
print(f"Número de clientes na fila: {fila_atendimento.tamanho_fila()}")
fila_atendimento.atender_cliente()