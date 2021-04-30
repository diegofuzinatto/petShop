from tkinter import *
from tkinter import ttk
import datetime

from produto import Produto
from cliente import Cliente
from venda import Venda

class Object():
    def __init__(self, codCliente="", nomeCliente="", dataAtual=""):
        self.codCliente = codCliente
        self.nomeCliente = nomeCliente
        self.dataAtual = dataAtual

class Funcoes():
    def __init__(self, cod_produto_entry, nome_entry, valor_entry, quantidade_entry, busca_produto_entry, listaPro, listaProVen, 
        total_entry, valor_recebido_entry, lb_troco_entry, pagamento_entry, nome_cliente_entry, lb_data_content):
        self.cod_produto_entry = cod_produto_entry
        self.nome_entry = nome_entry
        self.valor_entry = valor_entry
        self.quantidade_entry = quantidade_entry
        self.busca_produto_entry = busca_produto_entry
        self.listaPro = listaPro
        self.listaProVen = listaProVen
        self.total_entry_content = total_entry
        self.valor_recebido_entry = valor_recebido_entry
        self.lb_troco_entry = lb_troco_entry
        self.pagamento_entry = pagamento_entry
        self.nome_cliente_entry = nome_cliente_entry
        self.lb_data_content = lb_data_content

    def inicializa(self):
        self.listaVenda = []
        self.listasVendas = []

    def limpa_produto(self):
        self.cod_produto_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.busca_produto_entry.delete(0, END)

    def select_lista(self):
        produto = Produto()
        lista = produto.select_lista()

        self.listaPro.delete(*self.listaPro.get_children())

        for i in lista:
            self.listaPro.insert("", END, values=i)

    
    def add_produto(self):
        subtotal = int(self.quantidade_entry.get()) * float(self.valor_entry.get())
        subtotal = "{:.02f}".format(subtotal)
        total = float(self.total_entry_content.get()) + float(subtotal)
        total = "{:.02f}".format(total)

        self.total_entry_content.set(total)

        self.listaVenda = []
        for i in (self.cod_produto_entry.get(), self.nome_entry.get(), self.quantidade_entry.get(), self.valor_entry.get(), subtotal):
            self.listaVenda.append(i)

        self.listaProVen.insert("", END, values=(self.cod_produto_entry.get(), self.nome_entry.get(), self.quantidade_entry.get(), self.valor_entry.get(), subtotal))

        self.listasVendas.append(self.listaVenda)

        self.limpa_produto()

    def busca_produto(self):
        self.listaPro.delete(*self.listaPro.get_children())

        produto = Produto()

        self.busca_produto_entry.insert(END, '%')
        produto.nome = self.busca_produto_entry.get()

        buscaNomeProduto = produto.busca_produto()
        for i in buscaNomeProduto:
            self.listaPro.insert("", END, values=i)

        self.limpa_produto()

    def add_venda(self):
        venda = Venda()
        produto = Produto()

        for lista in self.listasVendas:
            venda.cod_produto = lista[0]
            venda.cod_cliente = self.codCliente
            venda.quantidade = lista[2]
            venda.data = self.dataAtual
            venda.valor = lista[4]

            produto.cod_produto = lista[0]
            produto.quantidade = lista[2]

            venda.cadastra_venda()
            produto.altera_quantidade()

            self.inicializa()
            self.listaProVen.delete(*self.listaProVen.get_children())

    def OnDoubleClick(self, event):
        self.limpa_produto()

        for n in self.listaPro.selection():
            col1, col2, col3, col4, col5 = self.listaPro.item(n, 'values')
            self.cod_produto_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.valor_entry.insert(END, col5)

    def onKeyPressing(self, event, entry, label):
        if (self.valor_recebido_entry.get() != self.lb_troco_entry.cget("text") and self.valor_recebido_entry.get() != ""):
            valor = float(self.valor_recebido_entry.get()) - float(self.total_entry_content.get())
            valor = "{:.02f}".format(valor)
            self.lb_troco_entry.config(text=valor)

    def onKeyPressingPagamento(self, e):
        if (self.pagamento_entry.get() != 'Dinheiro'):
            self.valor_recebido_entry.delete(0, END)
            self.valor_recebido_entry.insert(END, self.total_entry_content.get())
            self.valor_recebido_entry.config(state='disable')
        else:
            self.valor_recebido_entry.config(state='normal')

    def select_lista_nomes(self):    
        cliente = Cliente()

        self.listaNomesClientes = [""]
        self.tuplaNomesClientes = cliente.lista_nomes_clientes()
        for i, c in enumerate(self.tuplaNomesClientes):
            self.listaNomesClientes.insert(i+1, c[1])

    def seleciona_cliente(self): 
        for cli in self.tuplaNomesClientes:
            if (cli[1] == self.nome_cliente_entry.get()):
                self.codCliente = cli[0]
        self.nomeCliente = self.nome_cliente_entry.get()

    def data_atual(self):
        self.dataAtual = datetime.date.today()
        self.dataAtual = self.dataAtual.strftime('%d/%m/%Y')
        self.lb_data_content.config(text=self.dataAtual)
    
    
class TelaRealizaVendas(Funcoes):
    def __init__(self):
        top = Toplevel()
        self.top = top
        self.inicializa()
        self.tela()
        self.select_lista_nomes()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame3()
        self.widgets_frame2()
        self.lista_frame4()
        self.select_lista()
        self.data_atual()
        top.mainloop()

    def tela(self):
        self.top.title("Caixa")
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
        
        self.frame_3 = Frame(self.frame_1, bd=4, bg='#dfe3ee')
        self.frame_3.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)
        
        self.frame_4 = Frame(self.frame_2, bd=4, bg='#dfe3ee')
        self.frame_4.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.5)

    def widgets_frame1(self):
        ### Criação do botao buscar cliente
        self.bt_busca_cliente = Button(self.frame_1, text= "Ok", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.seleciona_cliente)
        self.bt_busca_cliente.place(relx= 0.23, rely=0.1, relwidth=0.1)
        
        ### Criação do botao buscar produto
        self.bt_busca_produto = Button(self.frame_1, text= "Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.busca_produto)
        self.bt_busca_produto.place(relx= 0.23, rely=0.3, relwidth=0.1)
        
        ### Criação do botao buscar limpar
        self.bt_limpa_produto = Button(self.frame_1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.limpa_produto)
        self.bt_limpa_produto.place(relx= 0.7, rely=0.3, relwidth=0.1)
        
        ### Criação do botao adicionar
        self.bt_adiciona_produto = Button(self.frame_1, text= "Adicionar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.add_produto)
        self.bt_adiciona_produto.place(relx= 0.85, rely=0.3, relwidth=0.1)

       
        ## Criação da label e entrada do nome do cliente
        self.lb_nome_cliente = Label(self.frame_1, text="Nome do Cliente", bg='#dfe3ee', fg='#107db2')
        self.lb_nome_cliente.place(relx= 0.05, rely= 0.0 )

        self.nome_cliente_entry = StringVar(self.frame_1)                         
        self.clienteChosen = ttk.Combobox(self.frame_1, width=12, textvariable=self.nome_cliente_entry)  
        self.clienteChosen['values'] = self.listaNomesClientes
        self.clienteChosen.place(relx= 0.05, rely= 0.1, relwidth= 0.15)             
        self.clienteChosen.current(0) 
        
        ## Criação da label e entrada do busca do produto
        self.lb_busca_produto = Label(self.frame_1, text="Nome do Produto", bg='#dfe3ee', fg='#107db2')
        self.lb_busca_produto.place(relx= 0.05, rely= 0.2 )

        self.busca_produto_entry = Entry(self.frame_1 )
        self.busca_produto_entry.place(relx=0.05, rely=0.3, relwidth=0.15)
        
        ## Criação da label e entrada do codigo do produto
        self.lb_cod_produto = Label(self.frame_1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.lb_cod_produto.place(relx= 0.45, rely= 0.0)

        self.cod_produto_entry = Entry(self.frame_1 )
        self.cod_produto_entry.place(relx=0.45, rely=0.1, relwidth=0.1)
        
        ## Criação da label e entrada do nome do produto
        self.lb_nome = Label(self.frame_1, text="Nome do Produto", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx= 0.6, rely= 0.0 )

        self.nome_entry = Entry(self.frame_1 )
        self.nome_entry.place(relx=0.6, rely=0.1, relwidth=0.2)
       
        ## Criação da label e entrada do valor do produto
        self.lb_valor = Label(self.frame_1, text="Valor do Produto", bg='#dfe3ee', fg='#107db2')
        self.lb_valor.place(relx= 0.85, rely= 0.0 )

        self.valor_entry = Entry(self.frame_1 )
        self.valor_entry.place(relx=0.85, rely=0.1, relwidth=0.1)
        
        ## Criação da label e entrada da quantidade
        self.lb_quantidade = Label(self.frame_1, text="Quantidade", bg='#dfe3ee', fg='#107db2')
        self.lb_quantidade.place(relx= 0.45, rely= 0.2 )

        self.quantidade_entry = Entry(self.frame_1 )
        self.quantidade_entry.place(relx=0.45, rely=0.3, relwidth=0.1)
    

    def widgets_frame2(self):
        ### Criação do botao para cancelar a venda
        self.bt_cancela_venda = Button(self.frame_2, text= "Cancelar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'),)
        self.bt_cancela_venda.place(relx= 0.74, rely=0.77, relwidth=0.1)
        
        ### Criação do botao para finalizar a venda
        self.bt_finaliza_venda = Button(self.frame_2, text= "Finalizar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.add_venda)
        self.bt_finaliza_venda.place(relx= 0.85, rely=0.77, relwidth=0.1)

        #Criação da label e entrada da data
        self.lb_total = Label(self.frame_2, text="Data", bg='#dfe3ee', fg='#107db2')
        self.lb_total.place(relx= 0.85, rely= 0.47 )

        self.lb_data_content = Label(self.frame_2)
        self.lb_data_content.place(relx=0.85, rely=0.57, relwidth=0.1)

        ## Criação da label e entrada do total da compra
        self.lb_total = Label(self.frame_2, text="Total a Pagar", bg='#dfe3ee', fg='#107db2')
        self.lb_total.place(relx= 0.05, rely= 0.67 )

        self.total_entry_content = DoubleVar()
        self.total_entry = Label(self.frame_2, textvariable=self.total_entry_content)
        self.total_entry.place(relx=0.05, rely=0.77, relwidth=0.1)
        
        ## Criação da label e entrada da forma de pagamento
        self.lb_pagamento = Label(self.frame_2, text="Forma de Pagamento", bg='#dfe3ee', fg='#107db2')
        self.lb_pagamento.place(relx= 0.2, rely= 0.67 )

        self.pagamento_entry = StringVar(self.frame_2)                         
        self.pagamentoChosen = ttk.Combobox(self.frame_2, width=12, textvariable=self.pagamento_entry) 
        self.pagamentoChosen['values'] = ("Cartão de Crédito", "Cartão de Débito", "Dinheiro")   
        self.pagamentoChosen.place(relx= 0.2, rely= 0.77, relwidth= 0.15)             
        self.pagamentoChosen.current(2) 
        self.pagamentoChosen.bind("<<ComboboxSelected>>", self.onKeyPressingPagamento)

        
        ## Criação da label e entrada do valor recebido
        self.lb_valor_recebido = Label(self.frame_2, text="Valor Recebido", bg='#dfe3ee', fg='#107db2')
        self.lb_valor_recebido.place(relx= 0.4, rely= 0.67)

        self.valor_recebido_entry_content = DoubleVar()
        self.valor_recebido_entry = Entry(self.frame_2, textvariable=self.valor_recebido_entry_content)
        self.valor_recebido_entry.place(relx=0.4, rely=0.77, relwidth=0.1)
        self.valor_recebido_entry.bind("<KeyRelease>", lambda e: self.onKeyPressing(e, self.valor_recebido_entry, self.lb_troco_entry))
        
        ## Criação da label e entrada do troco
        self.lb_troco = Label(self.frame_2, text="Troco", bg='#dfe3ee', fg='#107db2')
        self.lb_troco.place(relx= 0.55, rely= 0.67)

        
        self.troco = self.valor_recebido_entry_content.get()
        self.lb_troco_entry = Label(self.frame_2, text="0.00", bg='white')
        self.lb_troco_entry.place(relx= 0.55, rely= 0.77, relwidth=0.1)

    def lista_frame3(self):
        self.listaPro = ttk.Treeview(self.frame_3, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5"))
        self.listaPro.heading("#0", text="")
        self.listaPro.heading("#1", text="Código")
        self.listaPro.heading("#2", text="Nome")
        self.listaPro.heading("#3", text="Classificação")
        self.listaPro.heading("#4", text="Quantidade")
        self.listaPro.heading("#5", text="Valor")
        self.listaPro.column("#0", width=1)
        self.listaPro.column("#1", width=30)
        self.listaPro.column("#2", width=150)
        self.listaPro.column("#3", width=150)
        self.listaPro.column("#4", width=60)
        self.listaPro.column("#5", width=60)
        self.listaPro.place(relx=0.00, rely=0.0, relwidth=0.97, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_3, orient='vertical')
        self.listaPro.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.00, relwidth=0.03, relheight=0.85)
        self.listaPro.bind("<Double-1>", self.OnDoubleClick)
    
    def lista_frame4(self):
        self.listaProVen = ttk.Treeview(self.frame_4, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5"))
        self.listaProVen.heading("#0", text="")
        self.listaProVen.heading("#1", text="Código")
        self.listaProVen.heading("#2", text="Nome")
        self.listaProVen.heading("#3", text="Quantidade")
        self.listaProVen.heading("#4", text="Valor Unitário")
        self.listaProVen.heading("#5", text="Subtotal")
        self.listaProVen.column("#0", width=1)
        self.listaProVen.column("#1", width=30)
        self.listaProVen.column("#2", width=150)
        self.listaProVen.column("#3", width=60)
        self.listaProVen.column("#4", width=60)
        self.listaProVen.column("#5", width=60)
        self.listaProVen.place(relx=0.00, rely=0.00, relwidth=0.97, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_4, orient='vertical')
        self.listaProVen.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.00, relwidth=0.03, relheight=0.85)
