from bancoDados import Banco 

class Produto:

    def __init__(self, cod_produto = "", nome = "", classificacao = "", quantidade = "", valor = ""):
        self.cod_produto = cod_produto
        self.nome = nome
        self.classificacao = classificacao
        self.quantidade = quantidade
        self.valor = valor
    


    def cadastrarProduto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "INSERT INTO Produtos (nome, classificacao, quantidade, valor) VALUES (?, ?, ?, ?)",
                (self.nome, self.classificacao, self.quantidade, self.valor))

            banco.conexao.commit()
            cursor.close()

            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro no cadastro do produto!"

    def select_lista(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "SELECT cod_produto, nome, classificacao, quantidade, valor FROM Produtos ORDER BY nome ASC")
                
            lista = cursor.fetchall()
            
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Ocorreu um erro na conexão com o banco de dados!"
        
    def altera_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("UPDATE Produtos SET nome = ?, classificacao = ?, quantidade = ?, valor = ? WHERE cod_produto = ?", 
                (self.nome, self.classificacao, self.quantidade, self.valor, self.cod_produto))
            
            banco.conexao.commit()
            cursor.close()

            return "Produto alterado com sucesso!"
        except:
            return "Ocorreu um erro ao alterar o produto!"

    def exclui_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("DELETE FROM Produtos WHERE cod_produto = ?", 
                (self.cod_produto))

            banco.conexao.commit()
            cursor.close()

            return "Produto excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o produto!"

    def busca_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            print(self.nome)
            cursor.execute("""SELECT cod_produto, nome, classificacao, quantidade, valor FROM Produtos
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % self.nome)

            lista = cursor.fetchall()
            print(lista)
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"
        

    