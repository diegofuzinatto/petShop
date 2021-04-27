from bancoDados import Banco 

class Produto:

    def __init__(self, cod_produto = "", nome = "", classificacao = "", quantidade = "", valor = "", taxa_desconto=""):
        self.cod_produto = cod_produto
        self.nome = nome
        self.classificacao = classificacao
        self.quantidade = quantidade
        self.valor = valor
        self.taxa_desconto = taxa_desconto
    


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
      
            cursor.execute("""SELECT cod_produto, nome, classificacao, quantidade, valor FROM Produtos
            WHERE nome LIKE '%s' ORDER BY nome ASC""" % self.nome)

            lista = cursor.fetchall()
    
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"
        
    def busca_nome_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("SELECT nome FROM Produtos WHERE cod_produto LIKE '%s'" % self.cod_produto)
            
            nome_produto = cursor.fetchall()
            nome_produto = nome_produto[0][0]
           
            banco.conexao.commit()
            cursor.close()

            return nome_produto
        except:
            return "Erro de conexão com o banco de dados!"

    def busca_produto_classificacao(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            print(self.classificacao)
            cursor.execute("SELECT * FROM Produtos WHERE classificacao = '%s'" % self.classificacao)        
           
            lista = cursor.fetchall()
    
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"

    def promocao_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("UPDATE Produtos SET valor = (valor * ?) WHERE classificacao = ?", 
                (self.taxa_desconto, self.classificacao))
            banco.conexao.commit()

            cursor.close()

            return "Promoção cadastrada com sucesso!"
        except:
            return "Ocorreu um erro ao realizar a promoção!"


    