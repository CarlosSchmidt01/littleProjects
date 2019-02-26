class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        return self.dados.append(elemento)

    def desempilha(self):
        return self.dados.pop(len(self.dados) - 1)




p = Pilha()
p.empilha(50)
p.empilha(40)
p.empilha(30)
p.empilha(20)
p.empilha(10)
print(p.dados)
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())
