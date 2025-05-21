from classe import Produto
notebook = Produto('Notebook Dell i7', 5899 )
smartphone = Produto('iPhone 16', 13799 )
#input('Pressione qualquer tecla para ver as ofertas: ')
notebook.verProduto()
smartphone.verProduto()

user_product_name = input('Informe o nome do produto: ')
user_product_price = float(input('Informe o valor do produto: '))

user_product = Produto(user_product_name, user_product_price)
user_product.verProduto()


print()