from tkinter import *
from tkinter import ttk

from cliente import Cliente

class Funcoes():
    def __init__(self, cod_cliente_entry, nome_entry, endereco_entry, CPF_entry, listaCli):
        self.cod_cliente_entry = cod_cliente_entry
        self.nome_entry = nome_entry
        self.endereco_entry = endereco_entry
        self.CPF_entry = CPF_entry
        self.listaCli = listaCli

    def limpa_cliente(self):
        self.cod_cliente_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.CPF_entry.delete(0, END)

    def select_lista(self):
        cliente = Cliente()
        lista = cliente.select_lista()

        self.listaCli.delete(*self.listaCli.get_children())

        for i in lista:
            self.listaCli.insert("", END, values=i)

    def OnDoubleClick(self, event):
        self.limpa_cliente()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.cod_cliente_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.endereco_entry.insert(END, col3)
            self.CPF_entry.insert(END, col4)

    def add_cliente(self):
        cliente = Cliente()

        cliente.nome =  self.nome_entry.get()
        cliente.endereco = self.endereco_entry.get()
        cliente.CPF = self.CPF_entry.get()

        cliente.cadastrarCliente()

        self.select_lista()
        self.limpa_cliente()

    def altera_cliente(self):
        cliente = Cliente()

        cliente.cod_cliente = self.cod_cliente_entry.get()
        cliente.nome =  self.nome_entry.get()
        cliente.endereco = self.endereco_entry.get()
        cliente.CPF = self.CPF_entry.get()
        
        cliente.altera_cliente()

        self.select_lista()
        self.limpa_cliente()

    def exclui_cliente(self):
        cliente = Cliente()

        cliente.cod_cliente = self.cod_cliente_entry.get()
        cliente.nome =  self.nome_entry.get()
        cliente.endereco = self.endereco_entry.get()
        cliente.CPF = self.CPF_entry.get()
        
        cliente.exclui_cliente()

        self.limpa_cliente()
        self.select_lista()

    def busca_cliente(self):
        self.listaCli.delete(*self.listaCli.get_children())

        cliente = Cliente()

        self.nome_entry.insert(END, '%')
        cliente.nome = self.nome_entry.get()

        buscaNomeCliente = cliente.busca_cliente()
        for i in buscaNomeCliente:
            self.listaCli.insert("", END, values=i)

        self.limpa_cliente()

class TelaCadastroCliente(Funcoes):
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
        self.top.title("Cadastro de Clientes")
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
                                , font = ('verdana', 8, 'bold'), command=self.limpa_cliente)
        self.bt_limpar.place(relx= 0.2, rely=0.85, relwidth=0.1, relheight= 0.15)
       
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao novo
        self.bt_cadastrar = Button(self.frame_1, text="Cadastrar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_cadastrar.place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.exclui_cliente)
        self.bt_excluir.place(relx=0.8, rely=0.85, relwidth=0.1, relheight=0.15)

        
        ## Criação da label e entrada do código
        self.lb_cod_cliente = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cod_cliente.place(relx= 0.05, rely= 0.0 )

        self.cod_cliente_entry = Entry(self.frame_1 )
        self.cod_cliente_entry.place(relx= 0.05, rely= 0.1, relwidth= 0.1)
        
        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx= 0.05, rely= 0.2 )

        self.nome_entry = Entry(self.frame_1 )
        self.nome_entry.place(relx= 0.05, rely= 0.3, relwidth= 0.6)

        # Criação da label e entrada CPF
        self.lb_CPF = Label(self.frame_1, text = "CPF", bg= '#dfe3ee', fg = '#107db2')
        self.lb_CPF.place(relx= 0.7, rely= 0.2 )

        self.CPF_entry = Entry(self.frame_1 )
        self.CPF_entry.place(relx= 0.7, rely= 0.3, relwidth= 0.2)

        ## Criação da label e entrada do endereço
        self.lb_endereco = Label(self.frame_1, text="Endereço", bg= '#dfe3ee', fg = '#107db2')
        self.lb_endereco.place(relx=0.05, rely=0.4)

        self.endereco_entry = Entry(self.frame_1)
        self.endereco_entry.place(relx=0.05, rely=0.5, relwidth=0.85)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Endereço")
        self.listaCli.heading("#4", text="CPF")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=30)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=150)
        self.listaCli.column("#4", width=60)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)