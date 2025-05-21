class Produto:
    def __init__(self, descricao, preco_custo, preco_venda):
        self.descricao=descricao
        self.preco_custo=preco_custo
        self.__preco_venda=preco_venda
        if (preco_custo >= preco_venda):
            self.__preco_venda=preco_custo
        else:
            self.__preco_venda=preco_venda
            
    @property
    def preco_venda(self):
        return(self.__preco_venda)
    @preco_venda.setter
    def preco_venda(self,valor):
        if(valor>=self.preco_custo):
            self.__preco_venda=valor
            print(f'Preço de venda alterado para R${valor}')
        else:
            print(f'O preço de venda não pode ser alterado.\n')
            
            
