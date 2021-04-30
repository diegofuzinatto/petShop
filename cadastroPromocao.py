from tkinter import *
from tkinter import ttk

from produto import Produto

class Funcoes():
    def __init__(self, taxa_desconto_entry, classificacao_entry, listaPro):
        self.taxa_desconto_entry = taxa_desconto_entry
        self.classificacao_entry = classificacao_entry
        self.listaPro = listaPro

    def limpa_tela(self):
        self.taxa_desconto_entry.delete(0, END)

    def promocao_produto(self):
        produto = Produto()

        #produto.taxa_desconto = (100 - int(self.taxa_desconto_entry.get())) / 100
        taxa_desconto = (100 - int(self.taxa_desconto_entry.get())) / 100
        produto.classificacao = self.classificacao_entry.get()

        lista = produto.busca_produto_classificacao()

        for pro in lista:
            valor = pro[4] * taxa_desconto
            produto.valor = "{:.02f}".format(valor)
            produto.cod_produto = pro[0]
            produto.cadastra_promocao_produto()
        
        #produto.promocao_produto()

        self.busca_produto_classificacao()

    def busca_produto_classificacao(self):
        self.listaPro.delete(*self.listaPro.get_children())

        produto = Produto()

        produto.classificacao = self.classificacao_entry.get()

        buscaProdutoClassificacao = produto.busca_produto_classificacao()
        for i in buscaProdutoClassificacao:
            self.listaPro.insert("", END, values=i)

class TelaCadastroPromocao(Funcoes):
    def __init__(self):
        top = Toplevel()
        self.top = top
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.busca_produto_classificacao()
        top.mainloop()

    def tela(self):
        self.top.title("Cadastro de Promoção")
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
                                , font = ('verdana', 8, 'bold'), command=self.busca_produto_classificacao)
        self.bt_buscar.place(relx=0.4, rely=0.85, relwidth=0.1, relheight=0.15)
        
        ### Criação do botao cadastrar promocao
        self.bt_cadastrar_promocao = Button(self.frame_1, text="Cadastrar Promoção", bd=2, bg ='#107db2', fg='white'
                                , font = ('verdana', 8, 'bold'), command=self.promocao_produto)
        self.bt_cadastrar_promocao.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.15)
       

        # Criação da label e entrada classificação
        self.lb_classificacao = Label(self.frame_1, text = "Classificacao", bg='#dfe3ee', fg='#107db2')
        self.lb_classificacao.place(relx= 0.05, rely= 0.1 )

        
        self.classificacao_entry = StringVar(self.frame_1)                         
        self.classificacaoChosen = ttk.Combobox(self.frame_1, width=12, textvariable=self.classificacao_entry) 
        self.classificacaoChosen['values'] = ("Aves", "Cachorros", "Gatos", "Peixes", "Répteis")   
        self.classificacaoChosen.place(relx= 0.05, rely= 0.2, relwidth= 0.2)             
        self.classificacaoChosen.current(1)                         

        ## Criação da label e entrada da taxa de desconto
        self.lb_taxa_desconto = Label(self.frame_1, text="Taxa de Desconto", bg='#dfe3ee', fg='#107db2')
        self.lb_taxa_desconto.place(relx=0.05, rely=0.4)

        self.taxa_desconto_entry = Entry(self.frame_1)
        self.taxa_desconto_entry.place(relx=0.05, rely=0.5, relwidth=0.05)

        self.lb_taxa_desconto = Label(self.frame_1, text="%", bg='#dfe3ee', fg='#107db2')
        self.lb_taxa_desconto.place(relx=0.1, rely=0.5)


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
    