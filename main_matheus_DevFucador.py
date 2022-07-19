from tkinter import *
from tkinter import ttk
import sqlite3
from time import sleep

root = Tk()

class Functions():
    def limpar_dados(self):
        self.input_num.delete(0, END)
        self.input_nome.delete(0, END)
        self.input_sobrenome.delete(0, END)
        self.input_email.delete(0, END)
        self.input_tel.delete(0, END)

    def conexao_db(self):
        self.conn = sqlite3.connect("CadUser.db")
        self.cursor = self.conn.cursor()
        print(f"Conectado ao Banco de Dados!"); sleep(1)

    def desconect_db(self):
        self.conn.close();

    def criar_tabela(self):
        self.conexao_db()
        self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS Users(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome CHAR(40) NOT NULL,
            Sobrenome CHAR(40) NOT NULL,
            Email TEXT,
            Telefone INTEGER(20)
        );""")
        self.conn.commit(); 
        print(f"Tabela criada com sucesso!!!"); sleep(2)
        self.desconect_db()
        print(f"A Conexão com Banco de Dados foi encerrada!"); sleep(2)

    def variaveis_db(self):
        self.num = self.input_num.get()
        self.nome = self.input_nome.get()
        self.sobrenome = self.input_sobrenome.get()
        self.email = self.input_email.get()
        self.tel = self.input_tel.get()

    def adicionar_novo(self):
        self.variaveis_db()
        self.conexao_db()
        self.cursor.execute(""" INSERT INTO Users (Nome, Sobrenome, Email, Telefone ) VALUES ( ?, ?, ?, ?) """, (self.nome, self.sobrenome, self.email, self.tel))
        self.conn.commit()
        self.desconect_db()
        self.selecionar_item()
        self.limpar_dados()

    def selecionar_item(self):
        self.listaExibir.delete(*self.listaExibir.get_children())
        self.conexao_db()
        lista = self.cursor.execute("""SELECT Id, Nome, Sobrenome, Email, Telefone FROM Users ORDER BY Nome ASC; """)
        for l in lista:
            self.listaExibir.insert("", END, values=l) 
        self.desconect_db()
      
    def duplo_click(self, event):#  EVENTO BIND
        self.limpar_dados()
        self.listaExibir.selection()
        for n in self.listaExibir.selection():
            col1, col2,col3,col4,col5 = self.listaExibir.item(n, 'values')
            self.input_num.insert(END, col1)
            self.input_nome.insert(END, col2)
            self.input_sobrenome.insert(END, col3)
            self.input_email.insert(END, col4)
            self.input_tel.insert(END, col5)

    def deletar_item(self):
        self.variaveis_db()
        self.conexao_db()
        self.cursor.execute(""" DELETE FROM Users WHERE Id = ? """, [self.num])
        self.conn.commit()
        self.desconect_db()
        self.limpar_dados()
        self.selecionar_item()

    def atualizar_dados(self):
        self.variaveis_db()
        self.conexao_db()
        self.cursor.execute(""" UPDATE Users SET Nome = ?, Sobrenome = ?, Email = ?, Telefone = ? WHERE Id = ? """, [self.nome, self.sobrenome,self.email, self.tel, self.num])
        self.conn.commit()
        self.desconect_db()
        self.selecionar_item()
        self.limpar_dados()

    def buscar_dados(self):
        self.conexao_db()
        self.listaExibir.delete(*self.listaExibir.get_children())
        self.input_nome.insert(END, "%")
        nome = self.input_nome.get()
        self.cursor.execute( """ SELECT Id, Nome, Sobrenome, Email, Telefone FROM Users WHERE Nome LIKE '%s' ORDER BY Nome ASC """ % nome)
        buscarnomeBD = self.cursor.fetchall()
        for n in buscarnomeBD:
            self.listaExibir.insert("", END, value = n)
        self.limpar_dados()
        self.desconect_db()

class App(Functions):
    def __init__(self):
        self.root = root
        self.tela_principal()
        self.frames_telaprincipal()
        self.criar_btn()
        self.lista_exibir()
        self.criar_tabela()
        self.selecionar_item()
        self.Menus()

        #LOOP DA JANELA PRINCIPAL 
        root.mainloop()

    #FUNÇÃO QUE CRIA A TELA PRINCIPAL
    def tela_principal(self):
        self.root.title("//DevFuçador TkinterApp")
        self.root.configure(bg="#DCDCDC")
        self.root.geometry("620x420")
        self.root.resizable(True,True)
        # self.root.maxsize(width=780, height=540)
        self.root.minsize(width=520, height=400)
    
    #FUNÇÃO QUE CRIA OS FRAMES DA TELA PRINCIPAL
    def frames_telaprincipal(self):
        #FRAM DO CABEÇALHO
        self.frame_head = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#eee9e5")
        self.frame_head.place(relx=0.11, rely=0.01, relwidth=0.88, relheight=0.08)

        #MAIN FRAME SUPERIOR
        self.frame_sup = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#d0d2e3")
        self.frame_sup.place(relx=0.11, rely=0.10, relwidth=0.88, relheight=0.39)

        #MAIN FRAME INFERIOR 
        self.frame_inf = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#d0d2e3")
        self.frame_inf.place(relx=0.11, rely=0.5, relwidth=0.88, relheight=0.38)

        #BARRA DE TÍTULO NO FRAMA SUPERIOR PRINCIPAL
        self.frame_titulo = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#d0d2e3")
        self.frame_titulo.place(relx=0.11, rely=0.10, relwidth=0.88, relheight=0.07)

        #FRAME BARRA INFERIOR
        self.frame_barra_inf = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#d0d2e3")
        self.frame_barra_inf.place(relx=0.11, rely=0.89, relwidth=0.88, relheight=0.10)

        #FRAME MENU LATERAL
        self.frame_menu_lat = Frame(self.root, bd=4, bg="#A9A9A9", highlightthickness=2, highlightbackground="#d0d2e3")
        self.frame_menu_lat.place(relx=0.01, rely=0.01, relwidth=0.09, relheight=0.98)

    #FUNÇÃO QUE CRIA OS BOTÕES E AS LABELS
    def criar_btn(self):
        #BOTÔES     
        self.bt_novo = Button(self.frame_head, text="NOVO", bg="#00b34c", command=self.adicionar_novo)
        self.bt_novo.place(relx=0.01, rely=0.05, relwidth=0.11, relheight= 0.90)

        self.bt_editar = Button(self.frame_head, text="EDITAR", bg="#0074b4", command=self.atualizar_dados)
        self.bt_editar.place(relx=0.15, rely=0.05, relwidth=0.11, relheight= 0.90) 

        self.bt_limpar = Button(self.frame_head, text="LIMPAR", bg="#ffd41f", command = self.limpar_dados)
        self.bt_limpar.place(relx=0.60, rely=0.05, relwidth=0.11, relheight= 0.90)

        self.bt_deletar = Button(self.frame_head, text="DELETAR", bg="#02fcf3", command=self.deletar_item)
        self.bt_deletar.place(relx=0.75, rely=0.05, relwidth=0.11, relheight= 0.90)
 
        self.bt_buscar = Button(self.frame_head, text="BUSCAR", bg="#de4f15", command=self.buscar_dados)
        self.bt_buscar.place(relx=0.89, rely=0.05, relwidth=0.11, relheight= 0.90)

        self.bt_login = Button(self.frame_barra_inf, text="ENTRAR", bg="#f2e5f9")
        self.bt_login.place(relx=0.01, rely=0.1, relwidth=0.15, relheight= 0.80)

        self.bt_cadastrar = Button(self.frame_barra_inf, text="CADASTRE-SE", bg="#f2e5f9")
        self.bt_cadastrar.place(relx=0.40, rely=0.1, relwidth=0.20, relheight= 0.80)

        self.bt_sair = Button(self.frame_barra_inf, text="SAIR", bg="#f2e5f9")
        self.bt_sair.place(relx=0.84, rely=0.1, relwidth=0.15, relheight= 0.80)

##########>>>>>>>>>>>>>>LABELS>>>>>>>>>>>>>>>>>>>############********************>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #LABELS
        self.lb_titulo = Label(self.frame_titulo, text=("CRUD TKinter By //DevFuçador - INSCREVA-SE NO YOUTUBE! OBRIGADO!"), bg="#ffd41f", font=('verdana', 10 , 'bold'))
        self.lb_titulo.place(relx=0.0, rely=0.0, relwidth=1.00, relheight= 1.00)#LARGURA X ALTURA
        
        #LABEL ID NUM
        self.lb_num = Label(self.frame_menu_lat, text="ID", font=('verdana', 8 , 'bold'))
        self.lb_num.place(relx=0.01, rely=0.01, relwidth=0.95, relheight= 0.05)

        #LABEL NOME
        self.lb_nome = Label(self.frame_sup, text="NOME", font=('verdana', 8 , 'bold'))
        self.lb_nome.place(relx=0.01, rely=0.2, relwidth=0.25, relheight= 0.12)

        #LABEL SOBRENOME
        self.lb_sobrenome = Label(self.frame_sup, text="SOBRENOME", font=('verdana', 8 , 'bold'))
        self.lb_sobrenome.place(relx=0.01, rely=0.4, relwidth=0.25, relheight= 0.12)

        #LABEL EMAIL
        self.lb_email = Label(self.frame_sup, text="EMAIL", font=('verdana', 8 , 'bold'))
        self.lb_email.place(relx=0.01, rely=0.6, relwidth=0.25, relheight= 0.12)

        #LABEL TELEFONE
        self.lb_tel = Label(self.frame_sup, text="TEL", font=('verdana', 8 , 'bold'))
        self.lb_tel.place(relx=0.01, rely=0.8, relwidth=0.25, relheight= 0.12)

        #INPUTS
        #ID_N°
        self.input_num = Entry(self.frame_menu_lat , font=('verdana', 9 ))
        self.input_num.place(relx=0.01, rely=0.09, relwidth=0.95, relheight= 0.05)

        #NOME
        self.input_nome = Entry(self.frame_sup, font=('verdana', 9 ))
        self.input_nome.place(relx=0.35, rely=0.2, relwidth=0.65, relheight= 0.12)

        #SOBRENOME
        self.input_sobrenome = Entry(self.frame_sup, font=('verdana', 9 ))
        self.input_sobrenome.place(relx=0.35, rely=0.4, relwidth=0.65, relheight= 0.12)

        #EMAIL
        self.input_email = Entry(self.frame_sup, font=('verdana', 9 ))
        self.input_email.place(relx=0.35, rely=0.6, relwidth=0.65, relheight= 0.12)

        #TELEFONE
        self.input_tel = Entry(self.frame_sup, font=('verdana', 9 ))
        self.input_tel.place(relx=0.35, rely=0.8, relwidth=0.65, relheight= 0.12)

    #FUNÇÃO QUE EXIBE OS DADOS NA TREEVIEW
    def lista_exibir(self):
        #CABEÇALHO DAS COLUNAS
        self.listaExibir = ttk.Treeview(self.frame_inf, height=3, columns=("col1","col2","col3","col4","col5"))
        self.listaExibir.heading("#0", text="")
        self.listaExibir.heading("#1", text="Id")
        self.listaExibir.heading("#2", text="Nome")
        self.listaExibir.heading("#3", text="Sobrenome")
        self.listaExibir.heading("#4", text="Email")
        self.listaExibir.heading("#5", text="Telefone")

        #COLUNAS
        self.listaExibir.column("#0",  width=1)
        self.listaExibir.column("#1",  width=10)
        self.listaExibir.column("#2",  width=90)
        self.listaExibir.column("#3",  width=100)
        self.listaExibir.column("#4",  width=100)
        self.listaExibir.column("#5",  width=100)
        self.listaExibir.place(relx=0.011, rely=0.011, relwidth=0.98, relheight= 0.95)

        #BARRA DE ROLAGEM
        self.barra_rolagem = Scrollbar(self.frame_inf, orient='vertical')
        self.listaExibir.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.98, rely=0.011, relwidth=0.020, relheight= 0.951)
        self.listaExibir.bind("<Double-1>", self.duplo_click)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        def Sair(): self.root.destroy()
        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)
        filemenu.add_command(label="Sair", command=Sair)
        filemenu2.add_command(label="Limpar Dados", command=self.limpar_dados)






App()   