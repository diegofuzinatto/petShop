from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from venda import Venda
from produto import Produto
#from cliente import Cliente

class Funcoes():
    def limpa_tela(self):
        self.cod_venda_entry.delete(0, END)
        self.nome_produto_entry.delete(0, END)
        self.nome_cliente_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.data_inicio_entry.delete(0, END)
        self.data_fim_entry.delete(0, END)
        self.faturamento_entry.delete(0, END)

    def estorna_venda(self):
        venda = Venda()

        venda.cod_venda = self.cod_venda_entry.get()
        venda.estorna_venda()

        self.limpa_tela()
        self.select_lista()

    def busca_vendas(self):
        self.listaVen.delete(*self.listaVen.get_children())
        self.faturamento_entry.delete(0, END)

        venda = Venda()
        produto = Produto()

        venda.data_inicio = self.data_inicio_entry.get()
        venda.data_fim = self.data_fim_entry.get()

        buscaVendas = venda.busca_vendas()

        soma = 0
        for val in buscaVendas:
            soma += val[5]

            produto.cod_produto = val[1]
            nomeProduto = produto.busca_nome_produto()
            self.listaVen.insert("", END, values=(val[0], nomeProduto, val[2], val[3], val[4], val[5]))

        self.faturamento_entry.insert(END, soma)

    def select_lista(self):
        venda = Venda()
        produto = Produto()
        lista = venda.select_lista()

        self.listaVen.delete(*self.listaVen.get_children())

        for i in lista:
            produto.cod_produto = i[1]
            nomeProduto = produto.busca_nome_produto()
            self.listaVen.insert("", END, values=(i[0], nomeProduto, i[2], i[3], i[4], i[5]))

    def OnDoubleClick(self, event):
        self.limpa_tela()

        for n in self.listaVen.selection():
            col1, col2, col3, col4, col5, col6 = self.listaVen.item(n, 'values')
            self.cod_venda_entry.insert(END, col1)
            self.nome_produto_entry.insert(END, col2)
            self.nome_cliente_entry.insert(END, col3)
            self.quantidade_entry.insert(END, col4)
            self.data_entry.insert(END, col5)
            self.valor_entry.insert(END, col6)


class TelaRelatorioVendas(Funcoes):
    def __init__(self):
        top = Toplevel()
        self.top = top
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
        top.mainloop()

    def tela(self):
        self.top.title("Relatorio de Vendas")
        self.top.configure(background= '#1e3743')
        self.top.geometry("900x600")
        self.top.resizable(True, True)
        self.top.maxsize(width= 900, height= 600)
        self.top.minsize(width=500, height= 400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.top, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)
       
        self.frame_2 = Frame(self.top, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx= 0.3, rely=0.85, relwidth=0.1, relheight= 0.15)
        
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.busca_vendas)
        self.bt_buscar.place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao estornar
        self.bt_excluir = Button(self.frame_1, text="Estornar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.estorna_venda)
        self.bt_excluir.place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.15)

        
        ## Criação da label e entrada do código
        self.lb_cod_venda = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cod_venda.place(relx= 0.05, rely= 0.0 )

        self.cod_venda_entry = Entry(self.frame_1 )
        self.cod_venda_entry.place(relx= 0.05, rely= 0.1, relwidth= 0.1)
        
        ## Criação da label e entrada do nome do produto
        self.lb_nome_produto = Label(self.frame_1, text = "Nome do Produto", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome_produto.place(relx= 0.05, rely= 0.2 )

        self.nome_produto_entry = Entry(self.frame_1 )
        self.nome_produto_entry.place(relx= 0.05, rely= 0.3, relwidth= 0.4)

        # Criação da label e entrada nome do cliente
        self.lb_nome_cliente = Label(self.frame_1, text = "Nome do Cliente", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome_cliente.place(relx= 0.5, rely= 0.2 )

        self.nome_cliente_entry = Entry(self.frame_1 )
        self.nome_cliente_entry.place(relx= 0.5, rely= 0.3, relwidth= 0.4)

        ## Criação da label e entrada da data
        self.lb_data = Label(self.frame_1, text="Data", bg= '#dfe3ee', fg = '#107db2')
        self.lb_data.place(relx=0.05, rely=0.4)

        self.data_entry = Entry(self.frame_1)
        self.data_entry.place(relx=0.05, rely=0.5, relwidth=0.2)
        
        ## Criação da label e entrada do quantidade
        self.lb_quantidade = Label(self.frame_1, text="Quantidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_quantidade.place(relx=0.40, rely=0.4)

        self.quantidade_entry = Entry(self.frame_1)
        self.quantidade_entry.place(relx=0.40, rely=0.5, relwidth=0.2)
        
        ## Criação da label e entrada do valor
        self.lb_valor = Label(self.frame_1, text="Valor", bg= '#dfe3ee', fg = '#107db2')
        self.lb_valor.place(relx=0.70, rely=0.4)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.70, rely=0.5, relwidth=0.2)
        
        ## Criação da label e entrada da data do incio
        self.lb_data_inicio = Label(self.frame_1, text="Data Inicio", bg='#dfe3ee', fg ='#107db2')
        self.lb_data_inicio.place(relx= 0.05, rely= 0.6)
        
        self.data_inicio_entry = DateEntry(self.frame_1, width=12, background='#107db2', foreground='white', 
            borderwidth=2, locale='pt_BR')
        self.data_inicio_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.15)
        
        ## Criação da label e entrada da data do fim
        self.lb_data_fim = Label(self.frame_1, text="Data Fim", bg='#dfe3ee', fg='#107db2')
        self.lb_data_fim.place(relx= 0.25, rely= 0.6)

        self.data_fim_entry = DateEntry(self.frame_1, width=12, background='#107db2', foreground='white', 
            borderwidth=2, locale='pt_BR')
        self.data_fim_entry.place(relx= 0.25, rely= 0.7, relwidth= 0.15)
        
        ## Criação da label e entrada do faturamento
        self.lb_faturamento = Label(self.frame_1, text="Faturamento", bg= '#dfe3ee', fg = '#107db2')
        self.lb_faturamento.place(relx=0.8, rely=0.6)

        self.faturamento_entry = Entry(self.frame_1)
        self.faturamento_entry.place(relx=0.8, rely=0.7, relwidth=0.1)
        

    def lista_frame2(self):
        self.listaVen = ttk.Treeview(self.frame_2, height=3,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaVen.heading("#0", text="")
        self.listaVen.heading("#1", text="Código")
        self.listaVen.heading("#2", text="Produto")
        self.listaVen.heading("#3", text="Cliente")
        self.listaVen.heading("#4", text="Quantidade")
        self.listaVen.heading("#5", text="Data")
        self.listaVen.heading("#6", text="Valor")
        self.listaVen.column("#0", width=1)
        self.listaVen.column("#1", width=30)
        self.listaVen.column("#2", width=150)
        self.listaVen.column("#3", width=150)
        self.listaVen.column("#4", width=60)
        self.listaVen.column("#5", width=60)
        self.listaVen.column("#6", width=60)
        self.listaVen.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaVen.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaVen.bind("<Double-1>", self.OnDoubleClick)
