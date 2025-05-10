from classe import Calculadora
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor:'))
calc = Calculadora(n1, n2)
print(f'Soma: {calc.soma()}\n')
print(f'Subtração: {calc.sub()}\n')
print(f'Multiplicação: {calc.mult()}\n')
print(f'Divisão: {calc.div()}\n')