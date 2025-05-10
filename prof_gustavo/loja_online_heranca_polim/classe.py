class item_venda:
    def __init__(self, nome, preco_base):
        self.nome=nome
        self.preco_base=preco_base
        
    def calcular_preco_final(self):
        return self.preco_base
    
    def exibir_detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Preço base: R${self.preco_base:.2f}')
        
class produto_fisico:
    def __init__(self, nome, preco_base, peso, dimensao):
        super().__init__(nome, preco_base)
        self.peso=peso
        self.dimensao=dimensao
        
    def calcular_preco_final(self):
        custo_envio = self.preco * 0.5
        return self.preco_base + custo_envio

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Peso: {self.peso} kg')
        print(f'Dimensão { self.dimensao}')