from tkinter import *
from tkinter import ttk

from funcionario import Funcionario

class Funcoes():
    def limpa_funcionario(self):
        self.cod_funcionario_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.CPF_entry.delete(0, END)
        self.funcao_entry.delete(0, END)
        self.salario_entry.delete(0, END)


    def select_lista(self):
        funcionario = Funcionario()
        lista = funcionario.select_lista()

        self.listaFun.delete(*self.listaFun.get_children())

        for i in lista:
            self.listaFun.insert("", END, values=i)

    def OnDoubleClick(self, event):
        self.limpa_funcionario()

        for n in self.listaFun.selection():
            col1, col2, col3, col4, col5, col6 = self.listaFun.item(n, 'values')
            self.cod_funcionario_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.endereco_entry.insert(END, col3)
            self.CPF_entry.insert(END, col4)
            self.funcao_entry.insert(END, col5)
            self.salario_entry.insert(END, col6)

    def add_funcionario(self):
        funcionario = Funcionario()

        funcionario.nome =  self.nome_entry.get()
        funcionario.endereco = self.endereco_entry.get()
        funcionario.CPF = self.CPF_entry.get()
        funcionario.funcao = self.funcao_entry.get()
        funcionario.salario = self.salario_entry.get()

        funcionario.cadastrarFuncionario()

        self.select_lista()
        self.limpa_funcionario()

    def altera_funcionario(self):
        funcionario = Funcionario()

        funcionario.cod_funcionario = self.cod_funcionario_entry.get()
        funcionario.nome =  self.nome_entry.get()
        funcionario.endereco = self.endereco_entry.get()
        funcionario.CPF = self.CPF_entry.get()
        funcionario.funcao = self.funcao_entry.get()
        funcionario.salario = self.salario_entry.get()
        
        funcionario.altera_funcionario()

        self.select_lista()
        self.limpa_funcionario()

    def exclui_funcionario(self):
        funcionario = Funcionario()

        funcionario.cod_funcionario = self.cod_funcionario_entry.get()
        funcionario.nome =  self.nome_entry.get()
        funcionario.endereco = self.endereco_entry.get()
        funcionario.CPF = self.CPF_entry.get()
        funcionario.funcao = self.funcao_entry.get()
        funcionario.salario = self.salario_entry.get()
        
        funcionario.exclui_funcionario()

        self.limpa_funcionario()
        self.select_lista()

    def busca_funcionario(self):
        self.listaFun.delete(*self.listaFun.get_children())

        funcionario = Funcionario()

        self.nome_entry.insert(END, '%')
        print(self.nome_entry.get())
        funcionario.nome = self.nome_entry.get()

        buscaNomeFuncionario = funcionario.busca_funcionario()
        for i in buscaNomeFuncionario:
            self.listaFun.insert("", END, values=i)

        self.limpa_funcionario()

class TelaCadastroFuncionario(Funcoes):
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
        self.top.title("Cadastro de Funcionários")
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
                                , font = ('verdana', 8, 'bold'), command=self.limpa_funcionario)
        self.bt_limpar.place(relx= 0.2, rely=0.85, relwidth=0.1, relheight= 0.15)
       
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.busca_funcionario)
        self.bt_buscar.place(relx=0.3, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao novo
        self.bt_cadastrar = Button(self.frame_1, text="Cadastrar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.add_funcionario)
        self.bt_cadastrar.place(relx=0.6, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.altera_funcionario)
        self.bt_alterar.place(relx=0.7, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao excluir
        self.bt_excluir = Button(self.frame_1, text="Excluir", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.exclui_funcionario)
        self.bt_excluir.place(relx=0.8, rely=0.85, relwidth=0.1, relheight=0.15)

        
        ## Criação da label e entrada do código
        self.lb_cod_funcionario = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_cod_funcionario.place(relx= 0.05, rely= 0.0 )

        self.cod_funcionario_entry = Entry(self.frame_1 )
        self.cod_funcionario_entry.place(relx= 0.05, rely= 0.1, relwidth= 0.1)
        
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

        ## Criação da label e entrada da função
        self.lb_funcao = Label(self.frame_1, text="Função", bg= '#dfe3ee', fg = '#107db2')
        self.lb_funcao.place(relx=0.05, rely=0.6)

        self.funcao_entry = Entry(self.frame_1)
        self.funcao_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada do salário
        self.lb_salario = Label(self.frame_1, text="Salário", bg= '#dfe3ee', fg = '#107db2')
        self.lb_salario.place(relx=0.5, rely=0.6)

        self.salario_entry = Entry(self.frame_1)
        self.salario_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listaFun = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaFun.heading("#0", text="")
        self.listaFun.heading("#1", text="Codigo")
        self.listaFun.heading("#2", text="Nome")
        self.listaFun.heading("#3", text="Endereço")
        self.listaFun.heading("#4", text="CPF")
        self.listaFun.heading("#5", text="Função")
        self.listaFun.heading("#6", text="Salário")
        self.listaFun.column("#0", width=1)
        self.listaFun.column("#1", width=30)
        self.listaFun.column("#2", width=150)
        self.listaFun.column("#3", width=150)
        self.listaFun.column("#4", width=60)
        self.listaFun.column("#5", width=60)
        self.listaFun.column("#6", width=60)
        self.listaFun.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaFun.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.listaFun.bind("<Double-1>", self.OnDoubleClick)

