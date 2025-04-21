from sqlalchemy import Column, Float, Integer, String
from .db import Base

class Item(Base):
    __tablename__ = 'itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cor = Column(String, nullable=True)
    _estoque = Column(Integer, nullable=False)
    _preco = Column(Float, nullable=False)

    def __init__(self, nome, estoque, preco, cor=None):
        self.nome = nome
        self.cor = cor
        self._estoque = estoque
        self._preco = preco

    def __repr__(self):
        return f'<Item(nome={self.nome}, estoque={self.estoque}, preço: R${self.preco})>'
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)) or novo_preco <= 0:
            raise ValueError('O preço deve ser um número positivo!')
        self._preco = novo_preco
            
    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        if not isinstance(novo_estoque, (int,float)) or novo_estoque < 0:
            raise ValueError('O estoque deve ser um valor positivo!')
        self._estoque = novo_estoque
        
    