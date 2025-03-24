import random
from datetime import datetime
import os

# Funções utilitárias
def geraData():
    return datetime.now().strftime("%d/%m/%Y")

def gera_id():
    return random.randint(1000, 9999)

def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

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

class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade

    def __str__(self):
        return f"Produto: {self.produto.nome}, Quantidade: {self.quantidade}, Subtotal: {self.subtotal}"

# Classe Gerenciadora
class Gerenciador:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.vendedores = []
        self.vendas = []

    # Métodos para Clientes
    def cadastrar_cliente(self, nome, telefone, endereco, email):
        cliente = Cliente(nome, telefone, endereco, email)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado!")
        else:
            for cliente in self.clientes:
                print(cliente)

    def buscar_cliente_por_id(self, id_cliente):
        return next((c for c in self.clientes if c.id_cliente == id_cliente), None)

    def editar_cliente(self, id_cliente, nome=None, telefone=None, endereco=None, email=None):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente:
            if nome:
                cliente.nome = nome
            if telefone:
                cliente.telefone = telefone
            if endereco:
                cliente.endereco = endereco
            if email:
                cliente.email = email
            print("Cliente editado com sucesso!")
        else:
            print("Cliente não encontrado!")

    def remover_cliente(self, id_cliente):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado!")

    # Métodos para Produtos
    def cadastrar_produto(self, nome, categoria, preco, quantidade):
        produto = Produto(nome, categoria, preco, quantidade)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado!")
        else:
            for produto in self.produtos:
                print(produto)

    def buscar_produto_por_id(self, id_produto):
        return next((p for p in self.produtos if p.id_produto == id_produto), None)

    def editar_produto(self, id_produto, nome=None, categoria=None, preco=None, quantidade=None):
        produto = self.buscar_produto_por_id(id_produto)
        if produto:
            if nome:
                produto.nome = nome
            if categoria:
                produto.categoria = categoria
            if preco:
                produto.preco = preco
            if quantidade:
                produto.quantidade = quantidade
            print("Produto editado com sucesso!")
        else:
            print("Produto não encontrado!")

    def remover_produto(self, id_produto):
        produto = self.buscar_produto_por_id(id_produto)
        if produto:
            self.produtos.remove(produto)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado!")

    # Métodos para Vendedores
    def cadastrar_vendedor(self, nome, telefone, cargo, email):
        vendedor = Vendedor(nome, telefone, cargo, email)
        self.vendedores.append(vendedor)
        print("Vendedor cadastrado com sucesso!")

    def listar_vendedores(self):
        if not self.vendedores:
            print("Nenhum vendedor cadastrado!")
        else:
            for vendedor in self.vendedores:
                print(vendedor)

    def buscar_vendedor_por_id(self, id_vendedor):
        return next((v for v in self.vendedores if v.id_vendedor == id_vendedor), None)

    def editar_vendedor(self, id_vendedor, nome=None, telefone=None, cargo=None, email=None):
        vendedor = self.buscar_vendedor_por_id(id_vendedor)
        if vendedor:
            if nome:
                vendedor.nome = nome
            if telefone:
                vendedor.telefone = telefone
            if cargo:
                vendedor.cargo = cargo
            if email:
                vendedor.email = email
            print("Vendedor editado com sucesso!")
        else:
            print("Vendedor não encontrado!")

    def remover_vendedor(self, id_vendedor):
        vendedor = self.buscar_vendedor_por_id(id_vendedor)
        if vendedor:
            self.vendedores.remove(vendedor)
            print("Vendedor removido com sucesso!")
        else:
            print("Vendedor não encontrado!")

    # Métodos para Vendas
    def registrar_venda(self, id_cliente, id_vendedor, itens):
        cliente = self.buscar_cliente_por_id(id_cliente)
        vendedor = self.buscar_vendedor_por_id(id_vendedor)
        if not cliente or not vendedor:
            print("Cliente ou vendedor não encontrado!")
            return

        venda = Venda(cliente, vendedor)
        for item in itens:
            produto = self.buscar_produto_por_id(item["id_produto"])
            if produto and produto.quantidade >= item["quantidade"]:
                venda.itens_venda.append(ItemVenda(produto, item["quantidade"]))
                produto.quantidade -= item["quantidade"]
            else:
                print(f"Produto {produto.nome if produto else 'ID inválido'} não disponível em estoque!")
        self.vendas.append(venda)
        print(f"Venda registrada com sucesso! Total: R${venda.calcular_total():.2f}")

    def listar_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada!")
        else:
            for venda in self.vendas:
                print(venda)

    def buscar_venda_por_id(self, id_venda):
        return next((v for v in self.vendas if v.id_venda == id_venda), None)

    def remover_venda(self, id_venda):
        venda = self.buscar_venda_por_id(id_venda)
        if venda:
            self.vendas.remove(venda)
            print("Venda removida com sucesso!")
        else:
            print("Venda não encontrada!")

    # Relatórios
    def relatorio_clientes(self):
        print("="*40)
        print("RELATÓRIO DE CLIENTES")
        print("="*40)
        print(f"Total de clientes cadastrados: {len(self.clientes)}")
        for cliente in self.clientes:
            print(cliente)

    def relatorio_produtos(self):
        print("="*40)
        print("RELATÓRIO DE PRODUTOS")
        print("="*40)
        print(f"Total de produtos cadastrados: {len(self.produtos)}")
        valor_total_estoque = sum(p.preco * p.quantidade for p in self.produtos)
        print(f"Valor total em estoque: R${valor_total_estoque:.2f}")
        for produto in self.produtos:
            print(produto)

    def relatorio_vendas(self):
        print("="*40)
        print("RELATÓRIO DE VENDAS")
        print("="*40)
        print(f"Total de vendas registradas: {len(self.vendas)}")
        valor_total_vendas = sum(v.calcular_total() for v in self.vendas)
        print(f"Valor total em vendas: R${valor_total_vendas:.2f}")
        for venda in self.vendas:
            print(venda)