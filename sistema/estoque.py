from db.item import Item
from db.db import session

class SistemaEstoque:
    def cadastro_item(self):
        nome = input('Nome: ')
        cor = input('Cor: ')
        try:
            estoque = int(input('Estoque: '))
            preco = float(input('Preço: '))

            item = Item(nome, estoque, preco, cor)
            session.add(item)
            session.commit()
            print('Item cadastrado com sucesso!')
        except ValueError as e:
            print(f'Erro {e}')
            session.rollback()

    def verificar_estoque(self):
        id = int(input('Digite o código do item: '))
        item = session.query(Item).filter_by(id=id).first()
        if item:
            print(f'ID: {item.id} | Nome: {item.nome} | Cor: {item.cor} | Estoque: {item.estoque} | Preço: {item.preco}')
        else:
            print('Item não encontrado!')

    def atualizar_estoque(self):
        id = int(input('Digite o código do item: '))
        item = session.query(Item).filter_by(id=id).first()
        if item:
            try:
                novo_estoque = int(input('Novo estoque:'))
                item.estoque= novo_estoque
                session.commit()
                print('Estoque Atualizado!')
            except ValueError:
                print('Entrada inválida!')
        else:
            print('Item não localizado!')
            session.rollback()

    def excluir_item(self):
        id = int(input('Digite o código do item: '))
        item = session.query(Item).filter_by(id=id).first()
        if item:
            session.delete(item)
            session.commit()
            print('Item removido com sucesso!')
        else:
            print('Item não localizado!')

    def listar_itens(self):
        itens = session.query(Item).all()
        if not itens:
            print("Estoque vazio.")
        else:
            for item in itens:
                print(f"ID: {item.id} | Nome: {item.nome} | Cor: {item.cor} | Estoque: {item.estoque} | Preço: {item.preco}")

    def atualizar_preco(self):
        id = int(input('Digite o código do item: '))
        item = session.query(Item).filter_by(id=id).first()
        if item:
            try:
                novo_preco = float(input('Novo preço: '))
                item.preco = novo_preco
                session.commit()
                print('Valor atualizado com sucesso!')
            except ValueError:
                print('Valor inválido!')
                session.rollback()