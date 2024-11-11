# 12.	Implemente uma tabela hash simples em Python usando a técnica de tratamento de colisão seguindo os requisitos:
# a.	Crie uma classe chamada TabelaHash com um construtor que aceite um tamanho inicial para a tabela.
# b.	Implemente o método inserir(chave, valor) para adicionar uma chave e seu valor correspondente à tabela.
# c.	Implemente o método buscar(chave) para recuperar o valor associado a uma chave.
# d.	Implemente o método remover(chave) para remover uma chave (e seu valor) da tabela.
# e.	Use listas para armazenar chaves e valores em cada posição da tabela para lidar com colisões (encadeamento separado).

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0 

    def hash(self, key):
        return hash(key) % self.capacity

    def inserir(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[index].append([key, value])
        self.size += 1

    def buscar(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remover(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return True
        return False

    def __str__(self):
        result = []
        for arr in self.table:
            for pair in arr:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"
    
tabela = HashTable(6)
tabela.inserir("0", "Value_0")
tabela.inserir("1", "Value_1")
tabela.inserir("2", "Value_2")
tabela.inserir("3", "Value_3")
tabela.inserir("4", "Value_4")
tabela.inserir("5", "Value_5")
print(tabela)