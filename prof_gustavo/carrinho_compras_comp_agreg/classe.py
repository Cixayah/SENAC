class carrinho_compras:
    def __init__(self, data, nome, endereco):
        self.data=data
        self.cliente=Cliente(nome, endereco)
        self.produtos=[]
        
    def add_produto(self, descricao, preco):
        produto=Produto(descricao, preco)
        self.produtos.append(produto)
        
    def calcular_total(self):
        total=0
        for p in self.produtos:
            print(p.descricao, p.preco)
            total+=p.preco
        return total
    
class Cliente:
    def __init__(self, nome, endereco):
        self.nome=nome
        self.endereco=endereco
class Produto: 
    def __init__(self, descricao, preco):
        self.descricao=descricao
        self.preco=preco