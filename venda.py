from bancoDados import Banco 

class Venda:

    def __init__(self, cod_venda="", cod_produto="", cod_cliente="", quantidade="", data="", valor="", 
        nome_cliente="", nome_produto="", faturamento="", data_inicio="", data_fim=""):
        self.cod_venda = cod_venda
        self.cod_produto = cod_produto
        self.cod_cliente = cod_cliente
        self.quantidade = quantidade
        self.data = data
        self.valor = valor
        self.nome_produto = nome_produto
        self.nome_cliente = nome_cliente
        self.faturamento = faturamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    def select_lista(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(
                "SELECT cod_venda, cod_produto, cod_cliente, quantidade, data, valor FROM Vendas ORDER BY data ASC")
                
            lista = cursor.fetchall()
            
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Ocorreu um erro na conexão com o banco de dados!"
   

    def estorna_venda(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute("DELETE FROM Vendas WHERE cod_venda = ?", 
                (self.cod_venda))

            banco.conexao.commit()
            cursor.close()

            return "Produto excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o produto!"


    def busca_vendas(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute("""SELECT cod_venda, cod_produto, cod_cliente, quantidade, data, valor FROM Vendas
            WHERE data BETWEEN ? AND ? ORDER BY data ASC""", (self.data_inicio, self.data_fim))

            lista = cursor.fetchall()
            banco.conexao.commit()
            cursor.close()

            return lista
        except:
            return "Erro de conexão com o banco de dados!"
        

    