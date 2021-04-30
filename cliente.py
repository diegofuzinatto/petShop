from bancoDados import Banco 
import sqlite3

class Cliente:

    def __init__(self, cod_cliente = "", nome = "", endereco = "", CPF = ""):
        self.cod_cliente = cod_cliente
        self.nome = nome
        self.endereco = endereco
        self.CPF = CPF

    def cadastrarCliente(self):
        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "INSERT INTO Clientes (nome, endereco, CPF) VALUES (?, ?, ?)",
                (self.nome, self.endereco, self.CPF))

            banco.conexao.commit()
            cursor.close()

            return "Cliente cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do Cliente!"

    def select_lista(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "SELECT cod_cliente, nome, endereco, CPF FROM Clientes ORDER BY nome ASC")
                
            lista = cursor.fetchall()
            
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Ocorreu um erro na conexão com o banco de dados!"
        
    def altera_cliente(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("UPDATE Clientes SET nome = ?, endereco = ?, CPF = ? WHERE cod_cliente = ?", 
                (self.nome, self.endereco, self.CPF, self.cod_cliente))
            
            banco.conexao.commit()
            cursor.close()

            return "Cliente alterado com sucesso!"
        except:
            return "Ocorreu um erro ao alterar o cliente!"

    def exclui_cliente(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("DELETE FROM Clientes WHERE cod_cliente = ?", 
                (self.cod_cliente))

            banco.conexao.commit()
            cursor.close()

            return "Cliente excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o cliente!"

    def busca_cliente(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()


            cursor.execute("""SELECT cod_cliente, nome, endereco, CPF FROM Clientes
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % self.nome)

            lista = cursor.fetchall()
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"

    def lista_nomes_clientes(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "SELECT cod_cliente, nome FROM Clientes ORDER BY nome ASC")
                
            lista = cursor.fetchall()
            
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Ocorreu um erro na conexão com o banco de dados!"

    def busca_nome_cliente(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("SELECT nome FROM Clientes WHERE cod_cliente LIKE '%s'" % self.cod_cliente)
            
            nome_cliente = cursor.fetchall()
            nome_cliente = nome_cliente[0][0]
           
            banco.conexao.commit()
            cursor.close()

            return nome_cliente
        except:
            return "Erro de conexão com o banco de dados!"

        

    