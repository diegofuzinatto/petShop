import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('petshop.db')

        #cursor = self.conexao.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Funcionarios (
        #     cod_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        #     nome varchar(50) NOT NULL,
        #     endereco varchar(120) NOT NULL,
        #     CPF numeric(11) UNIQUE NOT NULL,
        #     funcao varchar(20) NOT NULL,
        #     salario decimal(7,2) NOT NULL
        # )""")
        # self.conexao.commit()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes (
        #     cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        #     nome varchar(50) NOT NULL,
        #     endereco varchar(120) NOT NULL,
        #     CPF numeric(11) UNIQUE NOT NULL)""")
        # self.conexao.commit()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos (
        #     cod_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        #     nome varchar(50) NOT NULL,
        #     classificacao varchar(120) NOT NULL,
        #     quantidade int NOT NULL,
        #     valor decimal(7,2) NOT NULL
        # )""")
        # self.conexao.commit()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Vendas (
        #     cod_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        #     cod_produto smallint NOT NULL,
        #     cod_cliente smallint NOT NULL,
        #     quantidade int NOT NULL,
        #     data date NOT NULL,
        #     valor decimal(7,2) NOT NULL,
        #     FOREIGN KEY (cod_produto) REFERENCES Produtos(cod_produto),
        #     FOREIGN KEY (cod_cliente) REFERENCES Clientes(cod_cliente)
        # )""")
        # self.conexao.commit()

        #cursor.execute("insert into Vendas values (1, 3, 4, 10, '08/01/2021', ")
       
        #cursor.close()


#Banco()



