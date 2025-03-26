from classes import Gerenciador
from funcoesGerais import limpartela

# Instância do gerenciador
gerenciador = Gerenciador()



# Menus
def menu_principal():
    while True:
        limpartela()
        print("="*40)
        print("MENU PRINCIPAL")
        print("="*40)
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Vendedores")
        print("4 - Vendas")
        print("5 - Relatórios")
        print("0 - Sair")
        print("="*40)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_vendedores()
        elif opcao == "4":
            menu_vendas()
        elif opcao == "5":
            gerenciador.gerar_relatorio_geral()
            #menu_relatorios()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Pressione Enter para continuar.")
            input()




def menu_clientes():
    while True:
        limpartela()
        print("="*40)
        print("MENU - CLIENTES")
        print("="*40)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Todos os Clientes")
        print("3 - Listar um Cliente Específico")
        print("4 - Editar Cliente")
        print("5 - Remover Cliente")
        print("0 - Voltar")
        print("="*40)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            
            nome = input("Digite o nome do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            email = input("Digite o email do cliente: ")
            gerenciador.cadastrar_cliente(nome, telefone, endereco, email)
        
        elif opcao == "2":
            gerenciador.listar_clientes()
        
        elif opcao == "3":
            id_cliente = int(input("Digite o ID do cliente: "))
            cliente = gerenciador.buscar_cliente_por_id(id_cliente)
            if cliente:
                print(cliente)

            else:
                print("Cliente não encontrado!")
                
        elif opcao == "4":
            id_cliente = int(input("Digite o ID do cliente que deseja editar: "))
            nome = input("Digite o novo nome (ou deixe em branco para não alterar): ")
            telefone = input("Digite o novo telefone (ou deixe em branco para não alterar): ")
            endereco = input("Digite o novo endereço (ou deixe em branco para não alterar): ")
            email = input("Digite o novo email (ou deixe em branco para não alterar): ")
            gerenciador.editar_cliente(id_cliente, nome or None, telefone or None, endereco or None, email or None)
        elif opcao == "5":
            id_cliente = int(input("Digite o ID do cliente que deseja remover: "))
            gerenciador.remover_cliente(id_cliente)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Pressione Enter para continuar.")
        input()




def menu_produtos():
    while True:
        limpartela()
        print("="*40)
        print("MENU - PRODUTOS")
        print("="*40)
        print("1 - Cadastrar Produto")
        print("2 - Listar Todos os Produtos")
        print("3 - Listar um Produto Específico")
        print("4 - Editar Produto")
        print("5 - Remover Produto")
        print("0 - Voltar")
        print("="*40)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            categoria = input("Digite a categoria do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            gerenciador.cadastrar_produto(nome, categoria, preco, quantidade)
        elif opcao == "2":
            gerenciador.listar_produtos()
        elif opcao == "3":
            id_produto = int(input("Digite o ID do produto: "))
            produto = gerenciador.buscar_produto_por_id(id_produto)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado!")
        elif opcao == "4":
            id_produto = int(input("Digite o ID do produto que deseja editar: "))
            nome = input("Digite o novo nome (ou deixe em branco para não alterar): ")
            categoria = input("Digite a nova categoria (ou deixe em branco para não alterar): ")
            preco = input("Digite o novo preço (ou deixe em branco para não alterar): ")
            quantidade = input("Digite a nova quantidade (ou deixe em branco para não alterar): ")
            gerenciador.editar_produto(id_produto, nome or None, categoria or None, float(preco) if preco else None, int(quantidade) if quantidade else None)
        elif opcao == "5":
            id_produto = int(input("Digite o ID do produto que deseja remover: "))
            gerenciador.remover_produto(id_produto)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Pressione Enter para continuar.")
        input()




def menu_vendedores():
    while True:
        limpartela()
        print("="*40)
        print("MENU - VENDEDORES")
        print("="*40)
        print("1 - Cadastrar Vendedor")
        print("2 - Listar Todos os Vendedores")
        print("3 - Listar um Vendedor Específico")
        print("4 - Editar Vendedor")
        print("5 - Remover Vendedor")
        print("0 - Voltar")
        print("="*40)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do vendedor: ")
            telefone = input("Digite o telefone do vendedor: ")
            cargo = input("Digite o cargo do vendedor: ")
            email = input("Digite o email do vendedor: ")
            gerenciador.cadastrar_vendedor(nome, telefone, cargo, email)
        elif opcao == "2":
            gerenciador.listar_vendedores()
        elif opcao == "3":
            id_vendedor = int(input("Digite o ID do vendedor: "))
            vendedor = gerenciador.buscar_vendedor_por_id(id_vendedor)
            if vendedor:
                print(vendedor)
            else:
                print("Vendedor não encontrado!")
        elif opcao == "4":
            id_vendedor = int(input("Digite o ID do vendedor que deseja editar: "))
            nome = input("Digite o novo nome (ou deixe em branco para não alterar): ")
            telefone = input("Digite o novo telefone (ou deixe em branco para não alterar): ")
            cargo = input("Digite o novo cargo (ou deixe em branco para não alterar): ")
            email = input("Digite o novo email (ou deixe em branco para não alterar): ")
            gerenciador.editar_vendedor(id_vendedor, nome or None, telefone or None, cargo or None, email or None)
        elif opcao == "5":
            id_vendedor = int(input("Digite o ID do vendedor que deseja remover: "))
            gerenciador.remover_vendedor(id_vendedor)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Pressione Enter para continuar.")
        input()



def menu_vendas():
    while True:
        limpartela()
        print("="*40)
        print("MENU - VENDAS")
        print("="*40)
        print("1 - Registrar Venda")
        print("2 - Listar Todas as Vendas")
        print("3 - Listar uma Venda Específica")
        print("4 - Remover Venda")
        print("0 - Voltar")
        print("="*40)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Clientes disponíveis:")
            gerenciador.listar_clientes()
            id_cliente = int(input("Digite o ID do cliente: "))
            print("Vendedores disponíveis:")
            gerenciador.listar_vendedores()
            id_vendedor = int(input("Digite o ID do vendedor: "))
            itens = []
            while True:
                print("Produtos disponíveis:")
                gerenciador.listar_produtos()
                id_produto = int(input("Digite o ID do produto (ou 0 para finalizar): "))
                if id_produto == 0:
                    break
                quantidade = int(input("Digite a quantidade: "))
                itens.append({"id_produto": id_produto, "quantidade": quantidade})
            gerenciador.registrar_venda()
        elif opcao == "2":
            gerenciador.listar_vendas()
        elif opcao == "3":
            id_venda = int(input("Digite o ID da venda: "))
            venda = gerenciador.buscar_venda_por_id(id_venda)
            if venda:
                print(venda)
            else:
                print("Venda não encontrada!")
        elif opcao == "4":
            id_venda = int(input("Digite o ID da venda que deseja remover: "))
            gerenciador.remover_venda(id_venda)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Pressione Enter para continuar.")
        input()

