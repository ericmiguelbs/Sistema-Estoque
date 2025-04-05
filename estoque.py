import time
import os

class Item():
    def __init__(self, nome, cor, estoque):
        self.nome = nome
        self.cor = cor
        self.estoque = estoque

class SistemaEstoque:
    def __init__(self):
        self.itens_estoque = {'1': Item('Garrafa', 'Azul', 50), 
                    '2': Item('Garrafa térmica', 'Preto', 100)}
        
    def cadastro_item(self):
        codigo = input('Digite o código do item: ')

        if codigo not in self.itens_estoque:
            nome = input('Digite o nome do item: ')
            cor = input('Digite a cor do item: ')
            estoque = int(input('Digite o estoque disponível do item: '))

            self.itens_estoque[codigo] = Item(nome,cor,estoque)
        else:
            print("Produto já possui cadastro!")
        
        time.sleep(3)
        limpar_terminal()


    def verificar_estoque(self):
        codigo = input('Digite o código do item: ')
        item = self.itens_estoque[codigo]
        if codigo in self.itens_estoque:
            print(f'Nome: {item.nome}')
            print(f'Cor: {item.cor}')
            print(f'Estoque disponível: {item.estoque}')
        
        else:
            print('Produto não localizado!')
        time.sleep(3)
        limpar_terminal()

    def atualizar_estoque(self):
        codigo = input('Digite o código do item: ')

        if codigo in self.itens_estoque:
            novo_estoque = int(input('Digite o estoque disponível do item: '))

            self.itens_estoque[codigo].estoque = novo_estoque
            print('Estoque atualizado com sucesso!')
        else:
            print('Produto não localizado!')
        time.sleep(3)
        limpar_terminal()

    def excluir_item(self):
        codigo = input('Digite o código do item: ')

        if codigo in self.itens_estoque:
            self.itens_estoque.pop(codigo)
            time.sleep(1.5)
            print('Item excluido com sucesso!')        
        else:
            print('Item não localizado!')
        time.sleep(3)
        limpar_terminal()

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    sistema = SistemaEstoque()
    while True:

        print('''
                Bem vindo a consulta de estoque!     
                Selecione uma das ações abaixo.
                1. Cadastro
                2. Verificar estoque
                3. Atualizar estoque
                4. Excluir item
                5. Encerrar ação  
        ''')
        try:

            escolha = int(input('Digite o número da ação desejada: '))

            if escolha ==1:
                sistema.cadastro_item()

            elif escolha ==2:
                sistema.verificar_estoque()
        
            elif escolha == 3:
                sistema.atualizar_estoque()
                
            elif escolha == 4:
                sistema.excluir_item()
            elif escolha == 5:
                print("Consulta encerrada!")
                break
            else:
                print('Opção Invalida')

        except ValueError:
            print('Valor invalido, tente novamente!')

if __name__ == "__main__":
    main()
