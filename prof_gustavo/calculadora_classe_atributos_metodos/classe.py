class Calculadora:
    def __init__(self, value_1, value_2):
        self.value_1=value_1
        self.value_2=value_2
    def soma(self):
        return self.value_1 + self.value_2
    def sub(self):
        return self.value_1 - self.value_2
    def mult(self):
        return self.value_1 * self.value_2
    def div(self):
        return self.value_1 / self.value_2
        