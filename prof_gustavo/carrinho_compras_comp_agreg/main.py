from classe import *
data='30/04/2022'
nome='Joaquim da Silva'
endereco='Rua dos Pombos, 000'
carrinho=carrinho_compras(data, nome, endereco)
carrinho.add_produto('Notebook Dell i7', 5800)
carrinho.add_produto('SmartPhone', 2800)
carrinho.add_produto('Xbox', 3400)
print(f'Carrinho: {carrinho.data}')
print('Cliente', carrinho.cliente.nome)
print('Endereço', carrinho.cliente.endereco)
print('-----')
total = carrinho.calcular_total()
print(f'Total R${total}')
print('-----')
