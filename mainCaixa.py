from tkinter import *
from tkinter import ttk

import cadastroProduto
import cadastroCliente
import realizaVendas

root = Tk()

class Caixa():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Caixa")
        self.root.configure(background= '#1e3743')
        self.root.geometry("300x400")
        self.root.resizable(False, False)

    def cadastroCliente(self):
        cadastroCliente.TelaCadastroCliente()

    def cadastroProduto(self):
        cadastroProduto.TelaCadastroProduto()

    def realizaVendas(self):
        realizaVendas.TelaRealizaVendas()

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.05, rely=0.05, relwidth= 0.9, relheight= 0.9)

    def widgets_frame1(self):
        ### Criação do botao clientes
        self.bt_clientes = Button(self.frame_1, text= "Clientes", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.cadastroCliente)
        self.bt_clientes.place(relx= 0.05, rely=0.05, relwidth=0.9, relheight= 0.09)
        
        ### Criação do botao produtos
        self.bt_produtos = Button(self.frame_1, text="Produtos", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.cadastroProduto)
        self.bt_produtos.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.09)
        
        ### Criação do botao vendas
        self.bt_vendas = Button(self.frame_1, text="Vendas", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'),command=self.realizaVendas)
        self.bt_vendas.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.09)
        
        ### Criação do botao sair
        self.bt_sair = Button(self.frame_1, text="Sair", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'),)
        self.bt_sair.place(relx=0.05, rely=0.9, relwidth=0.9, relheight=0.09)
    
Caixa()