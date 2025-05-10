class item_venda:
    def __init__(self, nome, preco_base):
        self.nome=nome
        self.preco_base=preco_base
        
    def calcular_preco_final(self):
        return self.preco_base
    
    def exibir_detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Preço base: R${self.preco_base:.2f}')
        
class produto_fisico(item_venda):
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
        
    class livro_digital(item_venda):
        def __init__(self, nome, preco_base, formato):
            super().__init__(nome, preco_base)
            self.formato=formato
            
        def calcular_preco_final(self):
            desconto = self.preco_base * 0.10
            return self.preco_base - desconto
        
        def exibir_detalhes(self):
            super().exibir_detalhes()
            print(f'Formato{self.formato}')
            print('Entrega: Download imediato!')
            
class curso_online(item_venda):
    def __init__(self, nome, preco_base, duracao_horas):
        super().__init__(nome, preco_base)
        self.duracao_horas=duracao_horas
        
    def calcular_preco_final(self):
        if self.duracao_horas > 20:
            return self.preco_base * 0.95 #5% off
        return self.preco_base
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Duração: {self.duracao_horas} horas')
        print('Acesso: Plataforma online')