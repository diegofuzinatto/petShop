import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('petshop.db')

        # cursor = self.conexao.cursor()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Funcionarios (
        #     cod_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        #     nome varchar(50) NOT NULL,
        #     endereco varchar(120) NOT NULL,
        #     CPF numeric(11) UNIQUE NOT NULL,
        #     funcao varchar(20) NOT NULL,
        #     salario numeric(7,2) NOT NULL
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
        #     valor numeric(7,2) NOT NULL
        # )""")
        # self.conexao.commit()

        # cursor.execute("""CREATE TABLE IF NOT EXISTS Vendas (
        #     cod_vendas INTEGER PRIMARY KEY AUTOINCREMENT,
        #     cod_produto smallint NOT NULL,
        #     cod_cliente smallint NOT NULL,
        #     quantidade int NOT NULL,
        #     data date NOT NULL,
        #     valor numeric(7,2) NOT NULL,
        #     FOREIGN KEY (cod_produto) REFERENCES Produtos(cod_produto),
        #     FOREIGN KEY (cod_cliente) REFERENCES Clientes(cod_cliente)
        # )""")
        # self.conexao.commit()

        # cursor.execute(
        #     "alter table Vendas rename column cod_vendas to cod_venda")

        # cursor.execute(
		# 	"insert into Vendas (cod_venda, cod_produto, cod_cliente, quantidade, data, valor) values (4, 1, 1, 100, '2021-04-15', 50.25)")
#         # cursor.execute(
#         #     "INSERT INTO Clientes (cod_cliente, nome, endereco, CPF) VALUES (2, 'Maria', 'Rua 8, 35', 23156854215)")
#
        # data_inicio = '01-04-2023'
        # data_fim = '30-04-2023'
        # cursor.execute("""SELECT cod_venda, cod_produto, cod_cliente, quantidade, data, valor FROM Vendas
        #     WHERE data BETWEEN ? AND ? ORDER BY data ASC""", (data_inicio, data_fim))

#         self.conexao.commit()
#         lista = cursor.fetchall()
#         print(lista)

#         cursor.close()


# Banco()


# p 1 4 5
