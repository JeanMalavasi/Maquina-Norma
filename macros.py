class Macros(object):
    valor = 0

    def __init__(self, valor):
        self.valor = valor

    def add(self):
        self.valor += 1

    def eqZero(self):
        return 1 if self.valor == 0 else 0

    def sub(self):
        if (self.eqZero()) != 1:
            self.valor -= 1
        else:
            self.valor = 0

    