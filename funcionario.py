from bancoDados import Banco 
import sqlite3

class Funcionario:

    def __init__(self, cod_funcionario="", nome="", endereco="", CPF="", funcao="", salario="", senha=""):
        self.cod_funcionario = cod_funcionario
        self.nome = nome
        self.endereco = endereco
        self.CPF = CPF
        self.funcao = funcao
        self.salario = salario
        self.senha = senha

    def cadastrarFuncionario(self):
        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "INSERT INTO Funcionarios (nome, endereco, CPF, funcao, salario, senha) VALUES (?, ?, ?, ?, ?, ?)",
                (self.nome, self.endereco, self.CPF, self.funcao, self.salario, self.senha))

            banco.conexao.commit()
            cursor.close()

            return print("Funcionário cadastrado com sucesso!")
        except:
            return print("Ocorreu um erro na inserção do funcionário!")

    def select_lista(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "SELECT cod_funcionario, nome, endereco, CPF, funcao, salario FROM Funcionarios ORDER BY nome ASC")
                
            lista = cursor.fetchall()
            
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Ocorreu um erro na conexão com o banco de dados!"
        
    def altera_funcionario(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("UPDATE Funcionarios SET nome = ?, endereco = ?, CPF = ?, funcao = ?, salario = ?, senha = ? WHERE cod_funcionario = ?", 
                (self.nome, self.endereco, self.CPF, self.funcao, self.salario, self.senha, self.cod_funcionario))
            
            banco.conexao.commit()
            cursor.close()

            return "Funcionário alterado com sucesso!"
        except:
            return "Ocorreu um erro ao alterar o funcionário!"

    def exclui_funcionario(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("DELETE FROM Funcionarios WHERE cod_funcionario = ?", 
                (self.cod_funcionario))

            banco.conexao.commit()
            cursor.close()

            return "Funcionário excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o funcionário!"

    def busca_funcionario(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()


            cursor.execute("""SELECT cod_funcionario, nome, endereco, CPF, funcao, salario FROM Funcionarios
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % self.nome)

            lista = cursor.fetchall()
         
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"
    
    def busca_funcionario_CPF(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
    
            cursor.execute("""SELECT funcao, senha FROM Funcionarios
            WHERE CPF LIKE '%s' """ % self.CPF)

            lista = cursor.fetchall()

            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"
        

    