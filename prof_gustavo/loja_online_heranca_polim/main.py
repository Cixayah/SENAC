from classe import *

teclado = produto_fisico('Teclado mecânico', 150.00, 0.8, '30x15x5cm')
python_book = livro_digital('Python fluente', 80, 'PDF')
web_course = curso_online('Desenvolvimento Web Completo', 400, 30)
data_course = curso_online('Análises de Dados com Python', 250.00, 15)

#Demonstrando herança e polimorfismo
itens = [teclado, python_book, web_course, data_course]

for item in itens:
    item.exibir_detalhes()
    preco_final = item.calcular_preco_final() #polimorfismo em ação
    print(f'Preço final: R$ {preco_final:.2f}')
    print('-' * 30)