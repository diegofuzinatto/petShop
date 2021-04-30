from tkinter import *
from tkinter import ttk

from produto import Produto

class Funcoes():
    def __init__(self, cod_produto_entry, nome_entry, quantidade_entry, valor_entry, classificacaoChosen, 
        listaPro, classificacao_entry):
        self.cod_produto_entry = cod_produto_entry
        self.nome_entry = nome_entry
        self.quantidade_entry = quantidade_entry
        self.valor_entry = valor_entry
        self.classificacao_entry = classificacao_entry
        self.classificacaoChosen = classificacaoChosen
        self.listaPro = listaPro

    def limpa_produto(self):
        self.cod_produto_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.classificacaoChosen.current(1)

    def select_lista(self):
        produto = Produto()
        lista = produto.select_lista()

        self.listaPro.delete(*self.listaPro.get_children())

        for i in lista:
            self.listaPro.insert("", END, values=i)

    def OnDoubleClick(self, event):
        self.limpa_produto()

        for n in self.listaPro.selection():
            col1, col2, col3, col4, col5 = self.listaPro.item(n, 'values')
            self.cod_produto_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            for i, clas in enumerate(self.classificacaoChosen['values']):
                if (clas == col3):
                    self.classificacaoChosen.current(i)
            self.quantidade_entry.insert(END, col4)
            self.valor_entry.insert(END, col5)
    
    def add_produto(self):
        produto = Produto()

        produto.nome =  self.nome_entry.get()
        produto.classificacao = self.classificacao_entry.get()
        produto.quantidade = self.quantidade_entry.get()
        valor = float(self.valor_entry.get())
        valor = "{:.02f}".format(valor)
        produto.valor = valor

        produto.cadastrarProduto()

        self.select_lista()
        self.limpa_produto()

    def altera_produto(self):
        produto = Produto()

        produto.cod_produto = self.cod_produto_entry.get()
        produto.nome =  self.nome_entry.get()
        produto.classificacao = self.classificacao_entry.get()
        produto.quantidade = self.quantidade_entry.get()

        valor = float(self.valor_entry.get())
        produto.valor = "{:.02f}".format(valor)
        
        produto.altera_produto()

        self.select_lista()
        self.limpa_produto()

    def exclui_produto(self):
        produto = Produto()

        produto.cod_produto = self.cod_produto_entry.get()
        produto.nome =  self.nome_entry.get()
        produto.classificacao = self.classificacao_entry.get()
        produto.quantidade = self.quantidade_entry.get()
        produto.valor = self.valor_entry.get()
        
        produto.exclui_produto()

        self.limpa_produto()
        self.select_lista()

    def busca_produto(self):
        self.listaPro.delete(*self.listaPro.get_children())

        produto = Produto()

        self.nome_entry.insert(END, '%')
        produto.nome = self.nome_entry.get()

        buscaNomeProduto = produto.busca_produto()
        for i in buscaNomeProduto:
            self.listaPro.insert("", END, values=i)

        self.limpa_produto()

class TelaCadastroProduto(Funcoes):
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
        self.top.title("Cadastro de Produtos")
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
                                , font = ('verdana', 8, 'bold'), command=self.limpa_produto)
        self.bt_limpar.place(relx= 0.2, rely=0.85, relwidth=0.1, relheight= 0.15)
        
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.busca_produto)
        self.bt_buscar.place(relx=0.3, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao novo
        self.bt_cadastrar = Button(self.frame_1, text="Cadastrar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.add_produto)
        self.bt_cadastrar.place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.altera_produto)
        self.bt_alterar.place(relx=0.7, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.exclui_produto)
        self.bt_excluir.place(relx=0.8, rely=0.85, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do código
        self.lb_cod_produto = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cod_produto.place(relx= 0.05, rely= 0.0 )

        self.cod_produto_entry = Entry(self.frame_1 )
        self.cod_produto_entry.place(relx= 0.05, rely= 0.1, relwidth= 0.1)
        
        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx= 0.05, rely= 0.2 )

        self.nome_entry = Entry(self.frame_1 )
        self.nome_entry.place(relx= 0.05, rely= 0.3, relwidth= 0.6)

        # Criação da label e entrada classificação
        self.lb_classificacao = Label(self.frame_1, text = "Classificacao", bg= '#dfe3ee', fg = '#107db2')
        self.lb_classificacao.place(relx= 0.7, rely= 0.2 )

        self.classificacao_entry = StringVar(self.frame_1)                         # 2
        self.classificacaoChosen = ttk.Combobox(self.frame_1, width=12, textvariable=self.classificacao_entry) #3
        self.classificacaoChosen['values'] = ("Aves", "Cachorros", "Gatos", "Peixes", "Répteis")   
        self.classificacaoChosen.place(relx= 0.7, rely= 0.3, relwidth= 0.2)             # 5
        self.classificacaoChosen.current(1)    

        ## Criação da label e entrada do quantidade
        self.lb_quantidade = Label(self.frame_1, text="Quantidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_quantidade.place(relx=0.05, rely=0.4)

        self.quantidade_entry = Entry(self.frame_1)
        self.quantidade_entry.place(relx=0.05, rely=0.5, relwidth=0.3)

        ## Criação da label e entrada do valor
        self.lb_valor = Label(self.frame_1, text="Valor", bg= '#dfe3ee', fg = '#107db2')
        self.lb_valor.place(relx=0.05, rely=0.6)

        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.05, rely=0.7, relwidth=0.3)

    def lista_frame2(self):
        self.listaPro = ttk.Treeview(self.frame_2, height=3,
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
        self.listaPro.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaPro.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaPro.bind("<Double-1>", self.OnDoubleClick)
