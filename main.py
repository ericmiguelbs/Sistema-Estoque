from db.db import session
from sistema.estoque import SistemaEstoque


def main():
    sistema = SistemaEstoque()
    while True:

        print('''
                Bem vindo a consulta de estoque!     
                Selecione uma das ações abaixo.
                1. Cadastro
                2. Verificar estoque
                3. Atualizar estoque
                4. Atualizar preço
                5. Excluir item
                6. Listar itens
                7. Encerrar sessão
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
                sistema.atualizar_preco()    
            elif escolha == 5:
                sistema.excluir_item()
            elif escolha == 6:
                sistema.listar_itens()
            elif escolha == 7:
                session.close()
                print("Consulta encerrada!")
                break
            else:
                print('Opção Invalida')

        except ValueError:
            print('Valor invalido, tente novamente!')

if __name__ == "__main__":
    main()