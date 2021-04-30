from tkinter import *
from tkinter import ttk
import hashlib

import mainGerente
import mainCaixa

from funcionario import Funcionario


class Funcoes():
    def __init__(self, usuario="", senha="", funcao="", usuario_entry="", senha_entry="", lb_msg=""):
        self.usuario = usuario
        self.senha = senha
        self.funcao = funcao
        self.usuario_entry = usuario_entry
        self.senha_entry = senha_entry
        self.lb_msg = lb_msg

    def limpa_tela(self):
        self.usuario_entry.delete(0, END)
        self.senha_entry.delete(0, END)

    def valida_funcionario(self):
        funcionario = Funcionario()

        senhaMd5 = hashlib.md5(self.senha_entry.get().encode('utf-8'))

        self.senha = senhaMd5.hexdigest()
        self.usuario = self.usuario_entry.get()
        funcionario.CPF = self.usuario

        lista = funcionario.busca_funcionario_CPF()

        if (lista != []):
            funcionario.funcao = lista[0][0]
            funcionario.senha = lista[0][1]

            if (self.senha == funcionario.senha and funcionario.funcao == 'Gerente'):
                self.limpa_tela()
                mainGerente.Gerente()

            elif (self.senha == funcionario.senha and funcionario.funcao == 'Caixa'):
                self.limpa_tela()
                mainCaixa.Caixa()

            else:
                self.lb_msg.configure(text="Funcionário com função incorreta")    

        else:
            self.lb_msg.config(text="Usuário ou senha inválidos")

class Login(Funcoes):
    def __init__(self):
        root = Tk()
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Login")
        self.root.configure(background= '#1e3743')
        self.root.geometry("300x400")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.05, rely=0.05, relwidth= 0.9, relheight= 0.9)

    def widgets_frame1(self):
        ### Criação do botao login
        self.bt_login = Button(self.frame_1, text= "Login", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.valida_funcionario)
        self.bt_login.place(relx= 0.05, rely=0.4, relwidth=0.4, relheight= 0.1)
        

        ## Criação da label e entrada do usuário
        self.lb_usuario = Label(self.frame_1, text = "Usuário", bg= '#dfe3ee', fg = '#107db2')
        self.lb_usuario.place(relx= 0.05, rely= 0.0 )

        self.usuario_entry = Entry(self.frame_1)
        self.usuario_entry.place(relx= 0.05, rely= 0.1, relwidth= 0.5)
        
        
        ## Criação da label e entrada da senha
        self.lb_senha = Label(self.frame_1, text = "Senha", bg= '#dfe3ee', fg = '#107db2')
        self.lb_senha.place(relx= 0.05, rely= 0.2 )

        self.senha_entry = Entry(self.frame_1, show="*" )
        self.senha_entry.place(relx= 0.05, rely= 0.3, relwidth= 0.5)

        ## Criação da label e entrada da msg
        self.lb_msg = Label(self.frame_1, text="", bg='#dfe3ee', fg='#107db2')
        self.lb_msg.place(relx= 0.05, rely= 0.6 )

Login()
