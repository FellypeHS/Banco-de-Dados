from funcoesGerais import geraData, gera_id
import pyodbc

# Classes
class Cliente:
    def __init__(self, nome, telefone, endereco, email):
        self.id_cliente = gera_id()
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return f"ID: {self.id_cliente}, Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}, Email: {self.email}"

class Produto:
    def __init__(self, nome, categoria, preco, quantidade):
        self.id_produto = gera_id()
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"ID: {self.id_produto}, Nome: {self.nome}, Categoria: {self.categoria}, Preço: {self.preco}, Quantidade: {self.quantidade}"

class Vendedor:
    def __init__(self, nome, telefone, cargo, email):
        self.id_vendedor = gera_id()
        self.nome = nome
        self.telefone = telefone
        self.cargo = cargo
        self.email = email

    def __str__(self):
        return f"ID: {self.id_vendedor}, Nome: {self.nome}, Telefone: {self.telefone}, Cargo: {self.cargo}, Email: {self.email}"

class Venda:
    def __init__(self, cliente, vendedor):
        self.id_venda = gera_id()
        self.cliente = cliente
        self.vendedor = vendedor
        self.data_venda = geraData()
        self.itens_venda = []
        self.total = 0

    def calcular_total(self):
        self.total = sum(item.subtotal for item in self.itens_venda)
        return self.total

    def __str__(self):
        return f"ID: {self.id_venda}, Cliente: {self.cliente.nome}, Vendedor: {self.vendedor.nome}, Total: {self.total}, Data: {self.data_venda}"

# Classe Gerenciadora
class Gerenciador:
    
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.vendedores = []
        self.vendas = []

        ## conexão com BD
        dados_conexao = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=FELLYPE;"
            "DATABASE=Papelaria;"
            "Trusted_Connection=yes;"
            )

        self.conn = pyodbc.connect(dados_conexao)

        self.cursor = self.conn.cursor() 



    # Métodos para Clientes
    def cadastrar_cliente(self, nome, telefone, endereco, email): 
        
        cliente = Cliente(nome, telefone, endereco, email)
        self.cursor.execute("""
            INSERT INTO clientes(id_cliente, nome,telefone, endereco, email )
                VALUES (?, ?, ?, ?, ?)
                """, (cliente.id_cliente, nome, telefone, endereco, email))
        self.conn.commit()
        print("Cliente cadastrado com sucesso!")


    def listar_clientes(self): 
        self.cursor.execute("SELECT * FROM clientes")
        clientes = []

        for row in self.cursor.fetchall():
            print(row)  
            clientes.append(Cliente(
            nome=row[1],
            telefone=row[2],
            endereco=(row[3]),  
            email=(row[4])
            ))

            if not clientes:
                print("Nenhum produto cadastrado!")
        return clientes


    def buscar_cliente_por_id(self, id_cliente): 
        
        self.cursor.execute("SELECT * FROM clientes WHERE id_cliente = ?", (id_cliente,))
        cliente = self.cursor.fetchone()  
        
        if cliente:
            # Retorna o objeto com os dados encontrados
            return Cliente(
                nome=cliente[1],
                email=cliente[2],
                telefone=cliente[3],
                endereco=cliente[4]
            )
        else:
            return None  


    def editar_cliente(self, id_cliente, nome=None, telefone=None, endereco=None, email=None):  
       
        # Busca o cliente no BD
        cliente = self.buscar_cliente_por_id(id_cliente)
        
        if not cliente:
            print("Cliente não encontrado!")
            return
        
        # Exibe os dados atuais do cliente
        print(f"Dados atuais do cliente: {cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}")
        
        # Exibe as opções 
        print("\nEscolha o campo que deseja editar:")
        print("1. Nome")
        print("2. Email")
        print("3. Telefone")
        print("4. Endereço")
        print("5. Cancelar")
        
        opcao = input("Digite o número da opção: ")
        
        
        if opcao == '1':
            novo_nome = input(f"Novo nome (atual: {cliente.nome}): ") or cliente.nome
            self.cursor.execute("""
                UPDATE clientes 
                SET nome = ? 
                WHERE id_cliente = ?
            """, (novo_nome, id_cliente))
            print(f"Nome atualizado para {novo_nome}!")


        elif opcao == '2':
            novo_email = input(f"Novo email (atual: {cliente.email}): ") or cliente.email
            self.cursor.execute("""
                UPDATE clientes 
                SET email = ? 
                WHERE id_cliente = ?
            """, (novo_email, id_cliente))
            print(f"Email atualizado para {novo_email}!")


        elif opcao == '3':
            novo_telefone = input(f"Novo telefone (atual: {cliente.telefone}): ") or cliente.telefone
            self.cursor.execute("""
                UPDATE clientes 
                SET telefone = ? 
                WHERE id_cliente = ?
            """, (novo_telefone, id_cliente))
            print(f"Telefone atualizado para {novo_telefone}!")


        elif opcao == '4':
            novo_endereco = input(f"Novo endereço (atual: {cliente.endereco}): ") or cliente.endereco
            self.cursor.execute("""
                UPDATE clientes 
                SET endereco = ? 
                WHERE id_cliente = ?
            """, (novo_endereco, id_cliente))
            print(f"Endereço atualizado para {novo_endereco}!")


        elif opcao == '5':
            print("Edição cancelada.")
            return
        else:
            print("Opção inválida!")

        # Confirma a atualização no banco de dados
        self.conn.commit()

    def remover_cliente(self, id_cliente):  
        
        # Verifica se o cliente existe
        self.cursor.execute("SELECT id_cliente FROM clientes WHERE id_cliente = ?", (id_cliente,))
        if not self.cursor.fetchone():
            print("Cliente não encontrado!")
            return False
        
        # Executa a remoção
        self.cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))
        
        # Confirma a operação
        self.conn.commit()
        
        # Verifica se realmente removeu
        if self.cursor.rowcount > 0:
            print(f"Cliente {id_cliente} removido com sucesso!")
            return True
        
        print("Nenhum cliente foi removido")
        return False

    
    
    
    
    # Métodos para Produtos
    def cadastrar_produto(self, nome, categoria, preco, quantidade): 
        
        produto = Produto(nome, categoria, preco, quantidade)
        produto = Produto(nome, categoria, float(preco), int(quantidade))
        self.cursor.execute("""
            INSERT INTO produtos(id_produto, nome,categoria, preco, quantidade )
                VALUES (?, ?, ?, ?, ?)
                """, (produto.id_produto, nome, categoria, preco, quantidade))
        self.conn.commit()
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self): 
        self.cursor.execute("SELECT * FROM produtos")
        produtos = []

        for row in self.cursor.fetchall():
            print(row)  
            produtos.append(Produto(
            nome=row[1],
            categoria=row[2],
            preco=float(row[3]),  
            quantidade=int(row[4])
            ))
            
        if not produtos:
            print("Nenhum produto cadastrado!")
        return produtos


    def buscar_produto_por_id(self, id_produto): 
        self.cursor.execute("SELECT * FROM produtos WHERE id_produto = ?", (id_produto,))
        produto = self.cursor.fetchone()
        if produto:
            return Produto( nome = produto[1], 
                           categoria=produto[2], preco=produto[3], 
                           quantidade=produto[4])
        else:
            return None




    def editar_produto(self, id_produto, nome=None, categoria=None, preco=None, quantidade=None): 

        produto = self.buscar_produto_por_id(id_produto)
        
        if not produto:
            print("Produto não encontrado!")
            return

        
        if nome:
            produto.nome = nome
        if categoria:
            produto.categoria = categoria
        if preco is not None:
            produto.preco = preco
        if quantidade is not None:
            produto.quantidade = quantidade

       
        self.cursor.execute("""
            UPDATE produtos 
            SET nome = ?, categoria = ?, preco = ?, quantidade = ?
            WHERE id_produto = ?
        """, (produto.nome, produto.categoria, produto.preco, produto.quantidade, id_produto))
        
        self.conn.commit()
        print(f"Produto {id_produto} editado com sucesso!")

    def remover_produto(self, id_produto): 
    
        #  Verifica se o produto existe
        self.cursor.execute("SELECT nome FROM produtos WHERE id_produto = ?", (id_produto,))
        produto = self.cursor.fetchone()
        
        if not produto:
            print("Produto não encontrado!")
            return False

        #  Remove o produto
        self.cursor.execute("DELETE FROM produtos WHERE id_produto = ?", (id_produto,))
        
        #  Confirma
        self.conn.commit()
        
        # Verifica se foi removido
        if self.cursor.rowcount > 0:
            print(f"Produto '{produto[0]}' removido com sucesso!")
            return True
        
        print("Nenhum produto foi removido")
        return False
    



    # Métodos para Vendedores
    def cadastrar_vendedor(self, nome, telefone, cargo, email): 
        vendedor = Vendedor(nome, telefone, cargo, email)
        self.cursor.execute("""
                INSERT INTO vendedores (id_vendedor, nome, telefone, cargo, email)
                VALUES (?, ?, ?, ?, ?)
            """, (vendedor.id_vendedor, nome, telefone, cargo, email))
        self.conn.commit()
        print("Vendedor cadastrado com sucesso!")

    def listar_vendedores(self): 
        self.cursor.execute("SELECT * FROM vendedores")
        vendedores = []

        for row in self.cursor.fetchall():
            print(row)  
            vendedores.append(Vendedor(
            nome=row[1],
            telefone=row[2],
            cargo=(row[3]),  
            email=(row[4])
            ))
            
        if not vendedores:
            print("Nenhum vendedor cadastrado!")
        return vendedores

    def buscar_vendedor_por_id(self, id_vendedor): 
        
        self.cursor.execute("SELECT * FROM vendedores WHERE id_vendedor = ?", (id_vendedor,))
        vendedor = self.cursor.fetchone()
        
        if vendedor:
            
            return Vendedor(
                nome=vendedor[1],
                telefone=vendedor[2],
                cargo=vendedor[3],
                email=vendedor[4]
            )
        return None  


    def editar_vendedor(self, id_vendedor, nome=None, telefone=None, cargo=None, email=None): 
       
        vendedor = self.buscar_vendedor_por_id(id_vendedor)
        
        if not vendedor:
            print("Produto não encontrado!")
            return

        # Atualiza os campos que foram passados
        if nome:
            vendedor.nome = nome
        if telefone:
            vendedor.telefone = telefone
        if cargo :
            vendedor.cargo = cargo
        if email:
            vendedor.email = email

        # Atualizando no banco de dados
        self.cursor.execute("""
            UPDATE vendedores 
            SET nome = ?, telefone = ?, cargo = ?, email = ?
            WHERE id_vendedor = ?
        """, (vendedor.nome, vendedor.telefone, vendedor.cargo, vendedor.email, id_vendedor))
        
        self.conn.commit()
        print(f"Vendedor {id_vendedor} editado com sucesso!")


    def remover_vendedor(self, id_vendedor):  
        
        # Verifica se o cliente existe
        self.cursor.execute("SELECT id_vendedor FROM vendedores WHERE id_vendedor = ?", (id_vendedor,))
        if not self.cursor.fetchone():
            print("vendedor não encontrado!")
            return False
        
        # Executa a remoção
        self.cursor.execute("DELETE FROM vendedores WHERE id_vendedor = ?", (id_vendedor,))
        
        # Confirma a operação
        self.conn.commit()
        
        # Verifica se realmente removeu
        if self.cursor.rowcount > 0:
            print(f"vendedor {id_vendedor} removido com sucesso!")
            return True
        
        print("Nenhum vendedor foi removido")
        return False

    def registrar_venda(self):
        
        print("\n=== REGISTRO RÁPIDO DE VENDA ===")
        
        # 1. Coleta básica
        id_cliente = input("ID do cliente: ")
        id_vendedor = input("ID do vendedor: ")
        
        # 2. Adição de produtos
        itens = []
        while True:
            id_produto = input("\nID do produto (ou 0 para finalizar): ")
            if id_produto == '0':
                break
                
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço unitário: "))  
            
            itens.append({
                'id_produto': id_produto,
                'quantidade': quantidade,
                'preco': preco
            })
        
        #  Cálculo do total
        total = sum(item['quantidade'] * item['preco'] for item in itens)
        
        #  Registro no banco (transação direta)
        try:
            self.cursor.execute("""
                INSERT INTO venda (id_cliente, id_vendedor, total)
                VALUES (?, ?, ?)
                """, (id_cliente, id_vendedor, total))
            
            self.conn.commit()
            print(f"\nVenda concluída! Total: R${total:.2f}")
            
        except Exception as e:
            print(f"\nErro: {e}")
            self.conn.rollback()

    def listar_vendas(self):
        
        print("\n=== LISTA DE VENDAS ===")
        
        try:
            self.cursor.execute("""
                SELECT v.id_venda, c.nome AS cliente, vd.nome AS vendedor, 
                    v.data_venda, v.total
                FROM venda v
                JOIN clientes c ON v.id_cliente = c.id_cliente
                JOIN vendedores vd ON v.id_vendedor = vd.id_vendedor
                ORDER BY v.data_venda DESC
            """)
            
            vendas = self.cursor.fetchall()
            
            if not vendas:
                print("Nenhuma venda registrada.")
                return
                
            for venda in vendas:
                print(f"\nID: {venda.id_venda}")
                print(f"Data: {venda.data_venda}")
                print(f"Cliente: {venda.cliente}")
                print(f"Vendedor: {venda.vendedor}")
                print(f"Total: R${venda.total:.2f}")
                print("-" * 30)
                
        except Exception as e:
            print(f"Erro ao listar vendas: {str(e)}")
    
    
    def buscar_venda(self, id_venda):
    
        self.cursor.execute("SELECT * FROM venda WHERE id_venda = ?", (id_venda,))
        venda = self.cursor.fetchone()
        
        if venda:
            print(f"\nID: {venda.id_venda}")
            print(f"Cliente: {venda.id_cliente}")
            print(f"Vendedor: {venda.id_vendedor}")
            print(f"Total: R${venda.total:.2f}")
        else:
            print("Venda não encontrada!")
        
        return venda
    
    
    def remover_venda(self, id_venda):
        
        try:
            # Verifica se a venda existe
            self.cursor.execute("SELECT 1 FROM venda WHERE id_venda = ?", (id_venda,))
            if not self.cursor.fetchone():
                print(f" Venda {id_venda} não encontrada!")
                return False

            # Remove do banco de dados
            self.cursor.execute("DELETE FROM venda WHERE id_venda = ?", (id_venda,))
            self.conn.commit()
            print(f"✅ Venda {id_venda} removida com sucesso!")
            return True
            
        except Exception as e:
            self.conn.rollback()
            print(f" Erro ao remover venda: {str(e)}")
            return False

    # Relatórios
    def gerar_relatorio_geral(self):
        
        print("\n" + "="*50)
        print("RELATÓRIO GERAL".center(50))
        print("="*50)
        
        try:
            #  Dados de Clientes
            self.cursor.execute("SELECT COUNT(*) FROM clientes")
            total_clientes = self.cursor.fetchone()[0]
            
            #  Dados de Vendedores
            self.cursor.execute("SELECT COUNT(*) FROM vendedores")
            total_vendedores = self.cursor.fetchone()[0]
            
            #  Dados de Produtos 
            self.cursor.execute("SELECT COUNT(*), ISNULL(SUM(quantidade), 0) FROM produtos")
            prod_data = self.cursor.fetchone()
            total_produtos = prod_data[0]
            estoque_total = prod_data[1] if prod_data[1] is not None else 0
            
            #  Dados de Vendas
            self.cursor.execute("""
                SELECT COUNT(*), ISNULL(SUM(total), 0), 
                    MIN(data_venda), MAX(data_venda) 
                FROM venda
            """)
            vendas_data = self.cursor.fetchone()
            total_vendas = vendas_data[0]
            faturamento = vendas_data[1] if vendas_data[1] is not None else 0
            primeira_venda = vendas_data[2]
            ultima_venda = vendas_data[3]
            
            # Exibição 
            print(f"\n CLIENTES: {total_clientes} cadastrados")
            print(f" VENDEDORES: {total_vendedores} cadastrados")
            print(f" PRODUTOS: {total_produtos} tipos | Estoque total: {estoque_total} unidades")
            print(f"\n VENDAS: {total_vendas}")
            print(f" Período: {primeira_venda.strftime('%d/%m/%Y') if primeira_venda else 'N/A'} a "
                f"{ultima_venda.strftime('%d/%m/%Y') if ultima_venda else 'N/A'}")
            print(f" Faturamento total: R${faturamento:.2f}")
            
            #  Top produtos
            print("\n PRODUTOS:")
            self.cursor.execute("""
                SELECT TOP 3 
                    p.nome, 
                    ISNULL(SUM(iv.quantidade), 0) as total_vendido
                FROM produtos p
                LEFT JOIN itens_venda iv ON p.id_produto = iv.id_produto
                GROUP BY p.nome
                ORDER BY total_vendido DESC
            """)
            
            top_produtos = self.cursor.fetchall()
            if top_produtos:
                for i, (nome, qtd) in enumerate(top_produtos, 1):
                    print(f"{i} {nome}")
            else:
                print("Nenhum dado de vendas disponível")
                
        except Exception as e:
            print(f"\n Erro ao gerar relatório: {str(e)}")
            import traceback
            traceback.print_exc()  
        
        print("\n" + "="*50)
        input("Press enter p continuar...")
    
    