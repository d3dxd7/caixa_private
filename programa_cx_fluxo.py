import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import base64
import mysql.connector
from mysql.connector import Error
# Cores
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
class telaTkinter:
    #Banco de Dados
    def banco_connect(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1234567',
            database='pythonsql',
            auth_plugin='mysql_native_password',
            autocommit=True
        )
        self.cursor = self.con.cursor()
        print(f'{GREEN}Conected')
    def banco_desconecta(self):
        self.con.close();print(f'{RED}Desconected')

    # Funcao Do Login
    def login(self):
        self.nome_usuario = self.user_input_user_log.get()
        self.senha = self.user_input_pass_log.get()
        sql = "select * from clientes where nome_usuario = %s and senha = %s "  # Comando para Puxar os Dados do Cadastro
        self.banco_connect()
        self.cursor.execute(sql, [(self.nome_usuario), (self.senha)])
        resultado = self.cursor.fetchall()
        sucess =f'{GREEN}Usuario Logado com Sucesso!'
        print(f'{RED}''#' * len(sucess)) # Insere '#' multiplicado * len= tamanho(string)
        print(sucess)
        print(f'{RED}''#' * len(sucess))
        if resultado:
            self.tela_menus() # Abri Proxima tela
            self.tela.destroy() # Fecha a tela de Login
        else:
            messagebox.showerror("","Usuario ou Senha Invalido")

    def truncate_table_admin(self):
        self.banco_connect()
        self.vqueryTRUNCATE = "truncate table pythonsql.funcionario"
        self.cursor.execute(self.vqueryTRUNCATE)
        self.con.commit()
        if self.truncate_table_admin :
            messagebox.showinfo(title=f'TRUNCATE TABLE', message='Tabela Truncada Sucesso')
        else:
            messagebox.showinfo(title=f'Error Table Truncate', message='Nao Foi Possivel Truncar a Tabela')

    def open_popup(self):
        msg_pop=Toplevel()
        msg_pop.geometry('600x300+600+153')
        msg_pop.title('Bem Vindo')
        Label(msg_pop, text=f'Bem Vindo! {self.nome_usuario}',font=('Mistral 18 bold'))
        Label.place(x=150, y=80)

    def registrar(self):
        nome_email = self.user_input_user.get()
        senha = self.user_input_pass.get()
        confirma_senha = self.user_input_pass_confirmar.get()
        # admin = self.is_checked.get()
        # self.admin = admin
        self.dados = '\'' + nome_email + '\',''\'' + senha + '\',' '\'' + confirma_senha + '\'' ')'
        self.declaracao = """INSERT INTO pythonsql.Clientes(
        nome_usuario, senha, confirma_senha)
        VALUES("""  # , admin
        self.sql = self.declaracao + self.dados
        print(self.sql)
        # Tentar conexao com Banco de Dados!
        try:
            if (nome_email == "" and senha == "" and confirma_senha == ""):
                messagebox.showerror(title='Erro de Registro', message='Campos Nao Preencidos, '
                                                                       f'Cadastro Invalido!')
            elif (senha != confirma_senha):
                messagebox.showwarning(title='Erro Senha Invalida', message='As Senhas Nao Conferem')
            elif (nome_email == 'admin'):
                messagebox.showwarning(title='Contate Suporte', message='Usuario Admin nao Pode ser Registrado')
                messagebox.showwarning(title='Contate Suporte', message='Insira um Usuario valido')
            else:
                self.banco_connect()
                inserirdados = self.sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                messagebox.showinfo(title="Informacoes do Registro", message="Registrado com Sucesso!")
                self.tela_2.destroy()
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
                self.tela_2.destroy()
    def inserir_cx_pego_laranja(self):
        ncx_pego = self.bt_cx_hj_entry.get()
        posicao_cx = self.btn_posicao_entry.get()
        try:
            if (ncx_pego == "" and posicao_cx == ""):
                messagebox.showwarning(title="ERROR AO INSERIR DADOS", message="Coloque ID do Funcionario, Coloque Quantidade de Caixa que Pegou Hoje")
            else:
                sql = """UPDATE pythonsql.funcionario 
                 SET qtd_laranja = """ + ncx_pego + """
                 WHERE posicao = """ +posicao_cx+ """;"""
                print(f'{BLUE}{sql}')
                # Comando para Puxar os Dados do Cadastro
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                # messagebox.showinfo(title="Informacoes Caixa Inserido", message="!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def inserir_cx_pego_limao(self):
        ncx_pego = self.bt_cx_hj_entry.get()
        posicao_cx = self.btn_posicao_entry.get()
        try:
            if (ncx_pego == "" and posicao_cx == ""):
                messagebox.showwarning(title="ERROR AO INSERIR DADOS", message="Coloque ID do Funcionario, Coloque Quantidade de Caixa que Pegou Hoje")
            else:
                sql = """UPDATE pythonsql.funcionario 
                 SET qtd_limao = """ + ncx_pego + """
                 WHERE posicao = """ +posicao_cx+ """;"""
                print(f'{BLUE}{sql}')
                # Comando para Puxar os Dados do Cadastro
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                # messagebox.showinfo(title="Informacoes Caixa Inserido", message="!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def inserir_cx_pego_tomate(self):
        ncx_pego = self.bt_cx_hj_entry.get()
        posicao_cx = self.btn_posicao_entry.get()
        try:
            if (ncx_pego == "" and posicao_cx == ""):
                messagebox.showwarning(title="ERROR AO INSERIR DADOS", message="Coloque ID do Funcionario, Coloque Quantidade de Caixa que Pegou Hoje")
            else:
                sql = """UPDATE pythonsql.funcionario  
                 SET qtd_tomate = """ + ncx_pego + """
                 WHERE id_funcionario = """ +posicao_cx+ """;"""
                print(f'{BLUE}{sql}')
                # Comando para Puxar os Dados do Cadastro
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                # messagebox.showinfo(title="Informacoes Caixa Inserido", message="!")

        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def registrar_fun_bd(self):
        nome_func = self.user_input_func.get()
        data_nasc = self.user_input_nascimento.get()
        cx_laranja = self.label_zerado.get()
        cx_limao = self.label_zerado.get()
        cx_tomate = self.label_zerado.get()
        # admin = self.is_checked.get()
        # self.admin = admin # ''\'' + data_nasc + '\''
        self.dados = '\'' + nome_func + '\',''\'' + data_nasc + '\',' + cx_laranja + ',' + cx_limao + ',' + cx_tomate + ')'
        self.declaracao = """INSERT INTO pythonsql.funcionario(
        nome_funcionario, data_nascimento, qtd_laranja, qtd_limao, qtd_tomate)
        VALUES("""  # , admin
        sql = self.declaracao + self.dados
        print(sql)
        # Tentar conexao com Banco de Dados!
        try:
            if (nome_func == "" and data_nasc == ""):
                messagebox.showerror(title='Erro de Registro Funcionario', message='Campos Nao Preencidos, '
                                                                       f'Cadastro Invalido!')
            else:
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                messagebox.showinfo(title="Informacoes do Registro", message="Funcionario Registrado com Sucesso!")
                # Label(self.registro_fun, text=f'Funcionario {self.bt_cx_nfuncionario_entry.get().upper()} Cadastrado!',
                #       bg='GREEN'). \
                #     place(relx=0.025, rely=0.42, relheight=0.03, relwidth=0.25)
        except Error as erro:
            print(f'{RED}',"Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close(); print(f'{RED}Descontado')

    #Frames
    def frames(self):
        #Frame Esquerdo
        self.left_Frame = Frame(self.programa, width=198, height=300, bg='MIDNIGHTBLUE', relief='raised')
        self.left_Frame.pack(side=LEFT)
        #Frame Direito
        self.right_Frame = Frame(self.programa, width=400, height=300, bg='MIDNIGHTBLUE', relief='raised')
        self.right_Frame.pack(side=RIGHT)
    # Config da tela 1
    def main_win(self, tela_tk):
        self.tela = tela_tk
        self.tela.resizable(False, False)
        self.tela.geometry('600x300+600+153')
        self.tela.configure(bg='white')
        self.tela.title('Fluxo de Caixa')

        #Variaveis de imagens code64_Base64

        left_Frame = Frame(self.tela, width=198, height=300, bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        left_Frame.pack(side=LEFT)
        right_Frame = Frame(self.tela, width=400, height=300, bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        right_Frame.pack(side=RIGHT)
        # ========= Bem Vindo ========
        bemvindo_Label = Label(right_Frame, text='Tela Login', font=('Century Gothic', 30, 'italic', 'bold',),bg='#dfe3ee',highlightthickness=0, highlightbackground="#107db2",
                               fg='#107db2')
        bemvindo_Label.place(x=100, y=15)

        # ======== Logo Base64 ==========
        #  ======== Base 64 Brasao =========
        logo_base64_banner = PhotoImage(data=base64.b64decode(logoBanner))
        logo_base64_banner = logo_base64_banner.subsample(2, 2)
        logo_base64_1 = Label(left_Frame, image=logo_base64_banner, bg='#dfe3ee')
        logo_base64_1.place(x=50, y=53, )

        # ========= Input Usuario =======
        #    ========= Usuario ========
        userLabel_user = Label(right_Frame, text='Usuario/email', font=('Century Gothic', 13), bg='#dfe3ee',highlightthickness=0, highlightbackground="#107db2",
                               fg='#107db2')
        userLabel_user.place(x=1, y=86)
        # Posicao
        self.user_input_user_log = Entry(right_Frame, width=30)
        self.user_input_user_log.place(x=135, y=92)

        #    ========= Senha ========
        userLabel_pass = Label(right_Frame, text='Senha', font=('Century Gothic', 15), bg='#dfe3ee',highlightthickness=0, highlightbackground="#107db2",
                               fg='#107db2')
        userLabel_pass.place(x=27, y=137)
        # Posicao
        self.user_input_pass_log = Entry(right_Frame, width=30, show='*')
        self.user_input_pass_log.place(x=135, y=142)


    # Config dos Botoes IMAGEN E FUNCOES
        #  ======== Base 64 Frase =========
        logo_base64_frase = PhotoImage(data=base64.b64decode(logoFrase))
        logo_base64_frase = logo_base64_frase.subsample(2, 2)
        logo_base64_2 = Label(left_Frame, image=logo_base64_frase, bg='#dfe3ee')
        logo_base64_2.place(x=7, y=155, )

        # ======== Base 64 Botao Entrar =========
        entrar_btn = PhotoImage(data=base64.b64decode(btn_entrar_img))
        entrar_btn = entrar_btn.subsample(7, 5)

        # ======== Base 64 Botao Cadastro =========
        register_btn = PhotoImage(data=base64.b64decode(btn_register_img))
        register_btn = register_btn.subsample(5, 4)

        # ======== Button ==========
        btn_login = Button(right_Frame, text='Entrar',font=('Arial', 10, 'italic', 'bold'),bd=3, fg='white', bg='#107db2', command=self.login)
        btn_login.place(x=130, y=200, width=70, height=30)

        btn_senha = Button(right_Frame,text='Cadastrar', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.tela_registro)
        btn_senha.place(x=210, y=200, width=100, height=30)

        mainloop()
    # Config da tela 2
    def tela_registro(self, tela_2 = None):
        self.tela_2 = Toplevel()
        self.tela_2.geometry('600x300+600+153')
        self.tela_2.resizable(False,False)
        self.tela_2.title('Registro Novo Usuario')
        self.tela_2.transient(self.tela)

        # ======== widgets ==========
        left_Frame = Frame(self.tela_2, width=198, height=300, bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        left_Frame.pack(side=LEFT)
        right_Frame = Frame(self.tela_2, width=400, height=300, bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        right_Frame.pack(side=RIGHT)

        # ======== Logo Base64 ==========
        #  ======== Base 64 Brasao =========
        logo_base64_banner = PhotoImage(data=base64.b64decode(logoBanner))
        logo_base64_banner = logo_base64_banner.subsample(2, 2)
        logo_base64_1 = Label(left_Frame, image=logo_base64_banner, bg='#dfe3ee')
        logo_base64_1.place(x=50, y=53, )

        #  ======== Base 64 Frase =========
        logo_base64_frase = PhotoImage(data=base64.b64decode(logoFrase))
        logo_base64_frase = logo_base64_frase.subsample(2, 2)
        logo_base64_2 = Label(left_Frame, image=logo_base64_frase, bg='#dfe3ee')
        logo_base64_2.place(x=10, y=155, )

        # ========= Tela Registro ========
        bemvindo_Label = Label(right_Frame, text='Tela Registro', font=('Century Gothic', 30), bg='MIDNIGHTBLUE',
                               fg='white')
        bemvindo_Label.place(x=100, y=10)
        #  ======== Mensagem Registro Frame 1 Left =========
        msg_registro = Label(left_Frame, font=('Century Gothic', 20), text='Informaçoes:', bg='MIDNIGHTBLUE',
                             fg='white')
        msg_registro.place(x=15, y=70)
        # ======== Mensagem Abaixo da Informacao Frame 1 Left =========
        msg_registro_info = Label(left_Frame, font=('Century Gothic', 10), text='voce ira efetuar registro\n'
                                                                                 'seus dados estao protegidos'
                                  , bg='MIDNIGHTBLUE', fg='white')
        msg_registro_info.place(x=15, y=110)
        msg_registro_LTDA = Label(left_Frame, font=('Century Gothic', 7), text='LTDA Fluxo de Caixa', bg='GREEN',
                                  fg='WHITE')
        msg_registro_LTDA.place(x=100, y=285)


        # ======== Input Usuario/Email NOME_USUARIO =========
        self.userLabel_user = Label(right_Frame, text='Usuario/email', font=('Century Gothic', 15), bg='MIDNIGHTBLUE',
                               fg='white')
        self.userLabel_user.place(x=1, y=92)
        # Posicao
        self.user_input_user = Entry(right_Frame, width=30)
        self.user_input_user.place(x=138, y=98)


        #    ========= Senha SENHA ========
        self.userLabel_pass = Label(right_Frame, text='Senha', font=('Century Gothic', 15), bg='MIDNIGHTBLUE', fg='white')
        self.userLabel_pass.place(x=27, y=137)
        # Posicao
        self.user_input_pass = Entry(right_Frame, width=30, show='*')
        self.user_input_pass.place(x=138, y=142)
        #    ========= Confirmar Senha ========
        self.userLabel_pass_c = Label(right_Frame, text='Confirmar Senha', font=('Century Gothic', 12), bg='MIDNIGHTBLUE',
                               fg='white')
        self.userLabel_pass_c.place(x=3, y=176)
        # Posicao
        self.user_input_pass_confirmar = Entry(right_Frame, width=30, show='*')
        self.user_input_pass_confirmar.place(x=138, y=180)

        # ======== Button =========
        # ======== Button Confirmar register =========
        self.btn_confirmar = Button(right_Frame, text='Confirmar Registro', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.registrar)
        self.btn_confirmar.place(x=145, y=230, width=130, height=30)

        # ======== Button Voltar =========
        self.btn_voltar = Button(right_Frame, text='Voltar', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.tela_2.destroy)
        self.btn_voltar.place(x=173, y=268, width=70, height=30)

        # # ======== Button CheckBox ==========
        # self.is_checked = tkinter.IntVar()

        # def check_checkbox():
        #     if self.is_checked.get() == 1:
        #         print(f'{GREEN}E UM ADM')                                  , variable=self.is_checked
        self.checkbox_admin = tkinter.Checkbutton(right_Frame, onvalue=1, offvalue=0, command="check_checkbox",bg='MIDNIGHTBLUE')
        self.checkbox_admin.place(x=138, y=200)
        self.msg_check_admin = Label(right_Frame, text='E ADM?', font=('Century Gothic', 10), bg='MIDNIGHTBLUE',
                               fg='white')
        self.msg_check_admin.place(x=30, y=200)
    # Tela Programa
    def tela_menus(self, tela_programa = None):   # TELA QUANDO LOGADO
        self.programa = Tk()
        self.programa.geometry('600x300+600+153')
        self.programa.resizable(False,False)
        self.programa.title(f'Nome Usuario:[ {self.nome_usuario} ] Programa de Caixa Fluxo ')
        left_Frame_programa = Frame(self.programa, width=198, height=300, bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        left_Frame_programa.pack(side=LEFT)
        self.right_Frame_programa = Frame(self.programa, width=400, height=300, bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        self.right_Frame_programa.pack(side=RIGHT)
        tamanho_nome_usuario = len(self.nome_usuario)
        # ========= Tela Quando o Usuario esta Logado Programa ========
        msg_programa_bemvindo = Label(self.right_Frame_programa, text=f'Sistema Fluxo Caixa', font=('Century Gothic', 30), bg='#dfe3ee',fg='#107db2')
        msg_programa_bemvindo.place(x=1, y=1)
        msg_programa_modulo = Label(self.right_Frame_programa, text=f'Modulos de Acesso', font=('Century Gothic', 15), bg='#dfe3ee', fg='#107db2')
        msg_programa_modulo.place(x=85, y=53,width=200, height=40)
        msg_programa__ = Label(self.right_Frame_programa, text=(f'--'*100), font=('Century Gothic', 30),bg='#dfe3ee', fg='#107db2')
        msg_programa__.place(x=1, y=80, width=500, height=20)
        msg_programa = Label(left_Frame_programa, text=f'User: ', font=('Century Gothic', 20), bg='#dfe3ee',fg='#107db2')
        msg_programa.place(x=1, y=38)
        msg_programa_usuario = Label(left_Frame_programa, text=f'{self.nome_usuario}',bg='#dfe3ee', font=('Arial', 10, 'italic', 'bold'), bd=2, fg='GREEN',highlightthickness=2, highlightbackground="#107db2")
        msg_programa_usuario.place(x=68, y=48)
        msg_programa_usuario = Label(left_Frame_programa, text=f'Status ON',bg='#dfe3ee', font=('Arial', 15, 'italic', 'bold'), bd=2, fg='GREEN',highlightthickness=2, highlightbackground="GREEN")
        msg_programa_usuario.place(x=30, y=5)

        # ======== Base 64 Botao Entrar =========
        btn_confirmar = PhotoImage(data=base64.b64decode(btn_confirmar_img))
        btn_confirmar = btn_confirmar.subsample(5, 3)

        btn_menu_reg_fun = Button(self.right_Frame_programa, text='Registro Geral',font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.programaFinal)
        btn_menu_reg_fun.place(x=150, y=100)  # , width=500, height=20

        # ======== Button MENUS Cadastrar Funcionario =========
        btn_menu_reg_fun = Button(self.right_Frame_programa, text='Registrar Funcionario',font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.menu_registro_funcionario)
        btn_menu_reg_fun.place(x=125, y=135)#, width=500, height=20

        # ======== Button MENUS Apagar Registro Funcionario=========
        btn_menu_reg_fun = Button(self.right_Frame_programa, text='Apagar Funcionario',font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.menu_registro_funcioniario_apagar_func)
        btn_menu_reg_fun.place(x=135, y=170)  # , width=500, height=20

        # ======== Button MENUS Valores Caixa =========
        btn_menu_reg_fun = Button(self.right_Frame_programa, text='Valor Produto',font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                                  command=self.menu_valores)
        btn_menu_reg_fun.place(x=150, y=200)  # , width=500, height=20


        # BTN PARA INSERIR ID E DELETAR APENAS PARA TESTE
        btn_colocar_id_msg = Label(left_Frame_programa, text='CLEAR ID', bg='RED',font=('Arial', 8, 'italic', 'bold'), bd=3, fg='white')
        btn_colocar_id_msg.place(x=5, y=273, height=19)
        self.btn_colocar_id_input = Entry(left_Frame_programa,width=5 )
        self.btn_colocar_id_input.place(x=65, y=273)
        btn_colocar_id_click = Button(left_Frame_programa,bg='RED',text='Confirmar' ,font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white',command=self.deletar_id)
        btn_colocar_id_click.place(x=90, y=273, height=21)

    def tela_somar_resultado_funcionario(self):
        self.root_delete = Tk()
        self.root_delete.geometry('700x500+200+153')
        self.root_delete.title("TreeView Banco De Dados Text")
        self.root_delete.configure(bg="#003153")

        # =====Frames=====
        # Frame Esquerdo
        self.left_Frame_delete = Frame(self.root_delete, width=100, height=200, bg='#C0C0C0', relief='raised', highlightthickness=2,
                           highlightbackground="#0fe3ee")
        self.left_Frame_delete.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)

        # Frame Direito
        self.right_Frame_delete = Frame(self.root_delete, width=400, height=300, bg='#C0C0C0', relief='raised', highlightthickness=2,
                            highlightbackground="#0fe3ee")
        self.right_Frame_delete.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.45)

        ############# RESULTADO A PAGAR #############
        resultado_soma_lb = Label(self.left_Frame_delete, text=f'Resultado a Pagar: ', font=('Arial', 9, 'italic', 'bold'),
                                  fg='#107db2',
                                  bg='#dfe3ee', highlightthickness=1, highlightbackground="#759fe6", anchor=W)
        resultado_soma_lb.place(relx=0.05, rely=0.8, relheight=0.07, relwidth=0.17)

        self.resultado_soma_lb_entry_pagamento = Entry(self.left_Frame_delete, fg='BLUE', bg='#dfe3ee')
        self.resultado_soma_lb_entry_pagamento.place(relx=0.22, rely=0.8, relheight=0.07, relwidth=0.3)
        #############################################

        ############ BOTOES DA TELA ##################
        btn_novo_msg = Button(self.root_delete, text="Limpar Dados da Tela", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white',
                              bg='#107db2',
                              command=self.limpar_tela_pagamento)
        btn_novo_msg.place(relx=0.025, rely=0.04, relheight=0.05, relwidth=0.215)

        btn_novo_msg = Button(self.root_delete, text="Buscar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.buscar_todos_pagamento)
        btn_novo_msg.place(relx=0.8, rely=0.04, relheight=0.05, relwidth=0.074)

        btn_novo_msg = Button(self.root_delete, text="Voltar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.root_delete.destroy)
        btn_novo_msg.place(relx=0.9, rely=0.04, relheight=0.05, relwidth=0.074)
        #############################################

        # NUMERO DA POSICAO FUNCIONARIO
        label_cx_hj_lebel = Label(self.root_delete, text="Nº Registro FUNCIONARIO", font=('Arial', 9, 'italic', 'bold'), fg='#107db2',
                                  bg='#dfe3ee', highlightthickness=1, highlightbackground="#759fe6")
        label_cx_hj_lebel.place(relx=0.15, rely=0.234, relheight=0.035, relwidth=0.23)
        self.btn_posicao_entry_pagamento = Entry(self.left_Frame_delete, font=('Arial', 10, 'italic'))
        self.btn_posicao_entry_pagamento.place(relx=0.05, rely=0.45, relheight=0.08, relwidth=0.08)

        bt_cx_lebel = Label(self.root_delete, text="QUANTAS CAIXAS TOTAL", font=('Arial', 9, 'italic', 'bold'), fg='#107db2',
                            bg='#dfe3ee',
                            highlightthickness=1, highlightbackground="#759fe6")
        bt_cx_lebel.place(relx=0.15, rely=0.30, relheight=0.035, relwidth=0.23)
        self.bt_cx_hj_entry_pagamento = Entry(self.left_Frame_delete, font=('Arial', 10, 'italic'))
        self.bt_cx_hj_entry_pagamento.place(relx=0.05, rely=0.6, relheight=0.08, relwidth=0.08)

        btn_cx_laranja_btn_mais_1 = Button(self.left_Frame_delete, text="SOMAR LARANJA", font=('Arial', 7, 'italic', 'bold'), bd=3,
                                           fg='white',
                                           bg='#107db2', command=self.Somar_Laranja)
        btn_cx_laranja_btn_mais_1.place(relx=0.05, rely=0.7, relheight=0.08, relwidth=0.15)

        btn_cx_limao_mais_1 = Button(self.left_Frame_delete, text="SOMAR LIMAO", font=('Arial', 7, 'italic', 'bold'), bd=3,
                                     fg='white',
                                     bg='#107db2', command='self.inserir_cx_pego_limao')
        btn_cx_limao_mais_1.place(relx=0.2, rely=0.7, relheight=0.08, relwidth=0.15)

        btn_cx_tomate_mais_1 = Button(self.left_Frame_delete, text="SOMAR TOMATE", font=('Arial', 7, 'italic', 'bold'), bd=3,
                                      fg='white',
                                      bg='#107db2', command=self.Somar_Tomate)
        btn_cx_tomate_mais_1.place(relx=0.35, rely=0.7, relheight=0.08, relwidth=0.15)

        btn_trazer_valores_cx_laranja = Button(self.left_Frame_delete, text='Mostrar Valores R$',
                                               font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                                               command=self.valores_cx_atuais_bd_pagamento)
        btn_trazer_valores_cx_laranja.place(relx=0.604, rely=0.31, relheight=0.09, relwidth=0.25)
        # BTN VOLTAR
        btn_novo_msg = Button(text="Voltar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.destroy_programa_final)
        btn_novo_msg.place(relx=0.9, rely=0.04, relheight=0.05, relwidth=0.074)

        # Tela Exibir Apenas os Valores das Caixas produtos
        self.tv_pagamento = ttk.Treeview(self.left_Frame_delete, columns=["col1", "col2", "col3"], show='headings')
        self.tv_pagamento.place(relx=0.55, rely=0.40, relheight=0.22, relwidth=0.4)
        self.tv_pagamento.heading("#1", text="Caixa Laranja", anchor=W)
        self.tv_pagamento.heading("#2", text="Caixa Limao", anchor=W)
        self.tv_pagamento.heading("#3", text="Caixa Tomate", anchor=W)
        self.tv_pagamento.column("#1", width=90, stretch=False)  # Caixa Laranja
        self.tv_pagamento.column("#2", width=90, stretch=False)  # Caixa Limao
        self.tv_pagamento.column("#3", width=85, stretch=False)  # Caixa Tomate

        self.tree_pagamento = ttk.Treeview(self.right_Frame_delete, columns=["col1", "col2", "col3", "col4", "col5", "col6"], show='headings')
        barra_rolagem = Scrollbar(self.right_Frame_delete, orient='vertical')
        self.tree_pagamento.configure(yscrollcommand=barra_rolagem.set)
        barra_rolagem.place(relx=0.967, rely=0.1, relwidth=0.03, relheight=0.88)

        self.tree_pagamento.place(width=668, height=220)  # (relx=-0.040, rely=-0.015, relheight=1, relwidth=1.2,height=3)
        self.tree_pagamento.heading("#1", text="Nº Registro", anchor=W)
        self.tree_pagamento.heading("#2", text="Nome Funcionario", anchor=W)
        self.tree_pagamento.heading("#3", text="Data Nascimento", anchor=W)
        self.tree_pagamento.heading("#4", text="QTD Laranja", anchor=W)
        self.tree_pagamento.heading("#5", text="QTD Limao", anchor=W)
        self.tree_pagamento.heading("#6", text="QTD Tomate", anchor=W)
        self.tree_pagamento.column("#1", width=5)  # Nome Funcionario
        self.tree_pagamento.column("#2", width=50)  # Data Nascimento
        self.tree_pagamento.column("#3", width=50)  # Laranja
        self.tree_pagamento.column("#4", width=50)  # Limao
        self.tree_pagamento.column("#5", width=50)  # Tomate
        self.tree_pagamento.column("#6", width=20)  # POSICAO

        self.root_delete.mainloop()

    def Somar_Laranja(self):
        qtd_caixa_total = self.bt_cx_hj_entry.get()
        valor_cx_atuai = self.linhas.fetchone()[1]
        resultado = valor_cx_atuai * qtd_caixa_total
        n_funcionario_bd = 'testeaaaaaaaaaa'
        result_valor = Label(self.left_Frame_delete, text=f'{n_funcionario_bd} {resultado}0 R$', fg='GREEN', bg='#dfe3ee',
                             anchor=W)
        result_valor.place(relx=0.22, rely=0.81, relheight=0.05, relwidth=0.3)

    def Somar_Limao(self):
        qtd_caixa_total = self.bt_cx_hj_entry_pagamento.getint()
        self.banco_connect()
        result_sql = "select * from python.valores WHERE caixa_laranja"
        self.cursor.execute(result_sql)
        valor_cx_atuai = 2.5  # Puxar valor da caixa do Banco de Dados
        resultado = valor_cx_atuai * qtd_caixa_total

    def Somar_Tomate(self):
        qtd_caixa_total = self.bt_cx_hj_entry.get()
        self.banco_connect()
        sql_tomate = "SELECT SUM(caixa_tomate) FROM python.valores WHERE id_valores=1"
        self.cursor.execute(sql_tomate)
        dados = self.cursor.fetchone()[0]
        print(dados)
        valor_cx_atuai = dados
        resultado = valor_cx_atuai * qtd_caixa_total
        n_funcionario_bd = self.nome_usuario
        result_valor = Label(self.left_Frame_delete, text=f'{n_funcionario_bd} {resultado}0 R$', fg='GREEN', bg='#dfe3ee',
                             anchor=W)
        result_valor.place(relx=0.22, rely=0.81, relheight=0.05, relwidth=0.3)

    # Funcao da Tela Programa Final
    def pesquisar(self):
        self.tree.delete(*self.tree.get_children())
        nome_recebe = self.bt_cx_nfuncionario_entry.get()
        sql = "SELECT * FROM funcionario WHERE nome_funcionario = %s"
        self.cursor.execute(sql, [(nome_recebe)])
        mostrar = self.cursor.fetchall()
        for exibir in mostrar:
            self.tree.insert("", "end", values=exibir)
    def limpar_programaFinal(self):
        self.bt_cx_hj_entry.delete(0, END)
        self.bt_cx_nfuncionario_entry.delete(0, END)
        self.btn_posicao_entry.delete(0, END)
        self.btn_novo_msg.delete(0, END)

    def limpar_tela_pagamento(self):
        self.bt_cx_hj_entry_pagamento.delete(0, END)
        self.resultado_soma_lb_entry_pagamento.delete(0, END)
        self.btn_posicao_entry_pagamento.delete(0, END)

    def valores_cx_atuais_bd(self):
        self.banco_connect()
        sql = "SELECT caixa_laranja, caixa_limao, caixa_tomate FROM valores"
        self.cursor.execute(sql)
        mostra = self.cursor.fetchall()
        for exibir in mostra:
            self.tv.insert("", "end", values=exibir)

    def valores_cx_atuais_bd_pagamento(self):
        self.banco_connect()
        sql = "SELECT caixa_laranja, caixa_limao, caixa_tomate FROM valores"
        self.cursor.execute(sql)
        mostra = self.cursor.fetchall()
        for exibir in mostra:
            self.tv_pagamento.insert("", "end", values=exibir)

    def qtd_cx_atuais_por_func(self):
        self.banco_connect()
        sql = "SELECT qtd_laranja, qtd_limao, qtd_tomate FROM valores"
        self.cursor.execute(sql)
        mostra = self.cursor.fetchall()
        for exibir in mostra:
            self.tv.insert("", "end", values=exibir)
    def buscar_todos(self):
        self.banco_connect()
        self.tree.delete(*self.tree.get_children())
        sql = "SELECT id_funcionario,nome_funcionario, data_nascimento, qtd_laranja, qtd_limao, qtd_tomate FROM funcionario"
        self.cursor.execute(sql)
        mostrar = self.cursor.fetchall()
        for exibir in mostrar:
            self.tree.insert("", "end", values=exibir)

    def buscar_todos_pagamento(self):
        self.banco_connect()
        self.tree.delete(*self.tree.get_children())
        sql = "SELECT id_funcionario,nome_funcionario, data_nascimento, qtd_laranja, qtd_limao, qtd_tomate FROM funcionario"
        self.cursor.execute(sql)
        mostrar = self.cursor.fetchall()
        for exibir in mostrar:
            self.tree_pagamento.insert("", "end", values=exibir)


    def programaFinal(self):
        self.root = Tk()
        self.root.geometry('700x500+600+153')
        self.root.configure(bg="#003153")
        self.root.resizable(False, False)
        self.root.title(f' TreeView Banco De Dados - Usuario:[ {self.nome_usuario} ]')
        # =====Frames=====
        # Frame Esquerdo
        left_Frame = Frame(self.root, width=100, height=200, bg='#dfe3ee', relief='raised', highlightthickness=2,
                           highlightbackground="#759fe6")
        left_Frame.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)
        # Frame Direito
        right_Frame = Frame(self.root, width=400, height=300, bg='#dfe3ee', relief='raised', highlightthickness=2,
                            highlightbackground="#759fe6")
        right_Frame.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.45)

        btn_novo_msg = Button(text="Limpar Dados da Tela", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.limpar_programaFinal)
        btn_novo_msg.place(relx=0.025, rely=0.04, relheight=0.05, relwidth=0.2)

        btn_novo_msg = Button(text="Excluir Funcionario", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.deletar_nome_func)
        btn_novo_msg.place(relx=0.25, rely=0.04, relheight=0.05, relwidth=0.2)
        self.btn_novo_msg = Entry()
        self.btn_novo_msg.place(relx=0.46, rely=0.045, relheight=0.04, relwidth=0.2)

        btn_novo_msg = Button(text="Pagamento", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.tela_somar_resultado_funcionario)
        btn_novo_msg.place(relx=0.67, rely=0.04, relheight=0.05, relwidth=0.12)

        btn_novo_msg = Button(text="Buscar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
                              command=self.buscar_todos)
        btn_novo_msg.place(relx=0.8, rely=0.04, relheight=0.05, relwidth=0.074)

        # btn_novo_msg = Button(text="Pesquisar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',
        #                       command=self.pesquisar)
        # btn_novo_msg.place(relx=0.7, rely=0.04, relheight=0.05, relwidth=0.095)

        btn_trazer_valores_cx_laranja = Button(left_Frame, text='Mostrar Valores R$',
                                               font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',command=self.valores_cx_atuais_bd)
        btn_trazer_valores_cx_laranja.place(relx=0.604, rely=0.31, relheight=0.09, relwidth=0.25)
        btn_nfuncionario_btn = Button(text="Filtrar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white',
                                      bg='#107db2', command=self.pesquisar)
        btn_nfuncionario_btn.place(relx=0.55, rely=0.40, relheight=0.05, relwidth=0.15)

        #Funcao Usuario Administrador
        if self.nome_usuario == 'admin' and self.senha == '123':
            truncate_table = Button(self.root, text='Limpar Tabela Funcionarios',font=('Arial', 8, 'italic', 'bold'), bd=3, fg='white',
                                      bg='#107db2',command=self.truncate_table_admin)
            truncate_table.place(relx=0.35, rely=0.485, relheight=0.033, relwidth=0.3)
        # Nome Funcionario
        bt_nfuncionario_lebel = Label(text="FILTRAR PELO NOME DO FUNCIONARIO", font=('Arial', 8, 'italic', 'bold'), fg='#107db2',bg='#dfe3ee', highlightthickness=2, highlightbackground="#759fe6")
        bt_nfuncionario_lebel.place(relx=0.553, rely=0.32, relheight=0.03, relwidth=0.33)
        self.bt_cx_nfuncionario_entry = Entry(left_Frame, font=('Arial', 10, 'italic'))
        self.bt_cx_nfuncionario_entry.place(relx=0.555, rely=0.72, relheight=0.08, relwidth=0.3)

        # NUMERO CX PEGO HOJE
        bt_cx_lebel = Label(text="PEGOU QUANTAS CAIXAS HOJE",  font=('Arial', 9, 'italic', 'bold'), fg='#107db2',bg='#dfe3ee', highlightthickness=2, highlightbackground="#759fe6")
        bt_cx_lebel.place(relx=0.15, rely=0.30, relheight=0.035, relwidth=0.3)
        self.bt_cx_hj_entry = Entry(left_Frame, font=('Arial', 10, 'italic'))
        self.bt_cx_hj_entry.place(relx=0.05, rely=0.6, relheight=0.08, relwidth=0.08)

        # NUMERO DA POSICAO FUNCIONARIO
        label_cx_hj_lebel = Label(text="Nº Registro FUNCIONARIO",  font=('Arial', 9, 'italic', 'bold'), fg='#107db2',bg='#dfe3ee', highlightthickness=2, highlightbackground="#759fe6")
        label_cx_hj_lebel.place(relx=0.15, rely=0.234, relheight=0.035, relwidth=0.23)
        self.btn_posicao_entry = Entry(left_Frame, font=('Arial', 10, 'italic'))
        self.btn_posicao_entry.place(relx=0.05, rely=0.45, relheight=0.08, relwidth=0.08)

        # BOTAO INSERIR + 1 CAIXA PARA FUNCIONARIO = POSICAO DECLARADA
        btn_cx_laranja_btn_mais_1=Button(left_Frame, text="CX LARANJA",font=('Arial', 7, 'italic', 'bold'), bd=3, fg='white',bg='#107db2',command=self.inserir_cx_pego_laranja)
        btn_cx_laranja_btn_mais_1.place(relx=0.05, rely=0.7, relheight=0.08, relwidth=0.13)

        btn_cx_limao_mais_1=Button(left_Frame, text="CX LIMAO",font=('Arial', 7, 'italic', 'bold'), bd=3, fg='white',bg='#107db2',command=self.inserir_cx_pego_limao)
        btn_cx_limao_mais_1.place(relx=0.18, rely=0.7, relheight=0.08, relwidth=0.13)

        btn_cx_tomate_mais_1 = Button(left_Frame, text="CX TOMATE",font=('Arial', 7, 'italic', 'bold'), bd=3, fg='white',bg='#107db2',command=self.inserir_cx_pego_tomate)
        btn_cx_tomate_mais_1.place(relx=0.31, rely=0.7, relheight=0.08, relwidth=0.13)
        #
        #BTN VOLTAR
        btn_novo_msg = Button(text="Voltar", font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2',command=self.destroy_programa_final)
        btn_novo_msg.place(relx=0.9, rely=0.04, relheight=0.05, relwidth=0.074)

        # Tela Exibir Apenas os Valores das Caixas produtos
        self.tv = ttk.Treeview(left_Frame, columns=["col1","col2","col3"], show='headings')
        self.tv.place(relx=0.55, rely=0.40, relheight=0.22, relwidth=0.4)
        self.tv.heading("#1", text="Caixa Laranja",anchor=W)
        self.tv.heading("#2", text="Caixa Limao",anchor=W)
        self.tv.heading("#3", text="Caixa Tomate",anchor=W)
        self.tv.column("#1", width=90, stretch=False) # Caixa Laranja
        self.tv.column("#2", width=90, stretch=False)  # Caixa Limao
        self.tv.column("#3", width=85, stretch=False)  # Caixa Tomate

        # Tela Exibir tudo Abaixo Tree View
        self.tree = ttk.Treeview(right_Frame, columns=["col1", "col2", "col3", "col4","col5","col6"], show='headings')
        # Barra Rolagem
        barra_rolagem = Scrollbar(right_Frame, orient='vertical')
        self.tree.configure(yscrollcommand=barra_rolagem.set)
        barra_rolagem.place(relx=0.967, rely=0.1, relwidth=0.03, relheight=0.88)

        self.tree.place(width=668, height=220)  # (relx=-0.040, rely=-0.015, relheight=1, relwidth=1.2,height=3)
        self.tree.heading("#1", text="Nº Registro",anchor=W)
        self.tree.heading("#2", text="Nome Funcionario",anchor=W)
        self.tree.heading("#3", text="Data Nascimento",anchor=W)
        self.tree.heading("#4", text="QTD Laranja",anchor=W)
        self.tree.heading("#5", text="QTD Limao",anchor=W)
        self.tree.heading("#6", text="QTD Tomate",anchor=W)
        self.tree.column("#1", width=5)  # Nome Funcionario
        self.tree.column("#2", width=50)  # Data Nascimento
        self.tree.column("#3", width=50)  # Laranja
        self.tree.column("#4", width=50)  # Limao
        self.tree.column("#5", width=50)  # Tomate
        self.tree.column("#6", width=20) # POSICAO
        self.root.mainloop()
        self.tree.pack()
        self.buscar_todos()

    # Telas do Menu
    def menu_registro_funcionario(self):
        self.registro_fun = Tk()
        self.registro_fun.title('Registrar Funcionario')
        self.registro_fun.resizable(False, False)
        self.registro_fun.geometry('600x300+600+153')

        # Frames
        # Frame Esquerdo
        left_Frame = Frame(self.registro_fun, width=198, height=300,bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        left_Frame.pack(side=LEFT)
        right_Frame = Frame(self.registro_fun, width=400, height=300,bg='#dfe3ee', relief='raised',highlightthickness=3, highlightbackground="#107db2")
        right_Frame.pack(side=RIGHT)

        msg_dados_fun = Label(right_Frame, text='Insira os Dados \n Funcionario', font=('Century Gothic', 20),bg='#dfe3ee',fg='#107db2')
        msg_dados_fun.place(x=100, y=1)

        #  ======== Mensagem Registro Frame 1 Left =========
        msg_registro_fun_esquerda = Label(left_Frame, font=('Century Gothic', 20,'italic'), text='Registro \nFuncionarios',bg='#dfe3ee',fg='#107db2')
        msg_registro_fun_esquerda.place(x=20, y=1)
        # ======== Mensagem Abaixo da Informacao Frame 1 Left =========
        msg_registro_info_esquerda = Label(left_Frame, font=('Century Gothic', 9), text='- voce ira efetuar registro\n'
                                                                                         '- seus Funcionarios\n'
                                                                                         '- seus dados estao protegidos'
                                           , bg='#dfe3ee', fg='#107db2', anchor=W)
        msg_registro_info_esquerda.place(x=7, y=110)
        msg_registro_LTDA_esquerda = Label(left_Frame, font=('Century Gothic', 7), text='LTDA Fluxo de Caixa',bg='GREEN',fg='WHITE')
        msg_registro_LTDA_esquerda.place(x=99.3, y=277)

        # ========= Input Nome Funcionario ========
        userLabel_user = Label(right_Frame, text='Nome Funcionario', font=('Century Gothic', 9), bg='#dfe3ee', fg='#107db2')
        userLabel_user.place(x=1, y=92)
        # Posicao
        self.user_input_func = Entry(right_Frame, width=30)
        self.user_input_func.place(x=138, y=98)

        #    ========= Input Data Nascimento ========
        userLabel_nascimento = Label(right_Frame, text='Data Nascimento', font=('Century Gothic', 9), bg='#dfe3ee', fg='#107db2')
        userLabel_nascimento.place(x=1, y=137)
        # Posicao
        self.user_input_nascimento = Entry(right_Frame, width=30)
        self.user_input_nascimento.place(x=138, y=141, width=70)

        self.label_zerado = Entry(right_Frame)
        self.label_zerado.insert(0,"0")

        #Botao Confirmar Registro de Funcionario Banco de Dados
        btn_confirmar_reg = Button(right_Frame, text='Confirmar Registro', font=('Century Gothic', 10), bd=3, fg='white', bg='#107db2', command=self.registrar_fun_bd)
        btn_confirmar_reg.place(x=145, y=225, width=130, height=30)

        # ======== Button Voltar =========
        btn_voltar = Button(right_Frame, text='Voltar', font=('Century Gothic', 10), bd=3, fg='white', bg='#107db2', command=self.destroy_tela_registro_func)
        btn_voltar.place(x=173, y=260, width=70, height=30)
    def menu_registro_funcioniario_apagar_func(self):
        self.registro_fun_apagar = Tk()
        self.registro_fun_apagar.title('Apagar Registro de Funcionario')
        self.registro_fun_apagar.resizable(False, False)
        self.registro_fun_apagar.geometry('600x300+600+153')

        # Frames
        # Frame Esquerdo
        left_Frame = Frame(self.registro_fun_apagar, width=198, height=300, bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        left_Frame.pack(side=LEFT)
        right_Frame = Frame(self.registro_fun_apagar, width=400, height=300,bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        right_Frame.pack(side=RIGHT)

        msg_dados_fun = Label(right_Frame, text='Insira os Dados do \n Funcionario', font=('Century Gothic', 25,'italic'),bg='#dfe3ee',fg='#107db2')
        msg_dados_fun.place(x=20, y=1)

        #  ======== Mensagem Registro Frame 1 Left =========
        msg_registro_fun_esquerda = Label(left_Frame, font=('Century Gothic', 13), text='Apagar Registro \nFuncionarios',bg='#dfe3ee',fg='blue')
        msg_registro_fun_esquerda.place(x=20, y=1)
        # ======== Mensagem Abaixo da Informacao Frame 1 Left =========
        msg_registro_info_esquerda = Label(left_Frame, font=('Century Gothic', 9), text='- voce ira apagar registro\n'
                                                                                         '- de seus Funcionarios\n'
                                                                                         '- seus dados estao protegidos'
                                           , bg='#dfe3ee', fg='#107db2')
        msg_registro_info_esquerda.place(x=1, y=110)
        msg_registro_LTDA_esquerda = Label(left_Frame, font=('Century Gothic', 7), text='LTDA Fluxo de Caixa',bg='GREEN',fg='WHITE')
        msg_registro_LTDA_esquerda.place(x=99.3, y=277)

        # ========= Input Nome Funcionario ========
        userLabel_user = Label(right_Frame, text='Nome Funcionario', font=('Century Gothic', 12), bg='#dfe3ee', fg='#107db2')
        userLabel_user.place(x=1, y=92)
        # Posicao
        self.user_input_func = Entry(right_Frame, width=30)
        self.user_input_func.place(x=147, y=98)


        #Botao Confirmar Registro de Funcionario Banco de Dados
        btn_confirmar_reg = Button(right_Frame, text='Apagar', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.deletar_nome_func)
        btn_confirmar_reg.place(x=145, y=230, width=130, height=30)

        # ======== Button Voltar =========
        btn_voltar = Button(right_Frame, text='Voltar', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.destroy_tela_apagar_func)
        btn_voltar.place(x=173, y=265, width=70, height=30)
    def menu_valores(self):
        self.valores = Tk()
        self.valores.title('Valores a Registrar')
        self.valores.resizable(False, False)
        self.valores.geometry('600x300+600+153')

        # =====Frames=====
        # Frame Esquerdo
        left_Frame = Frame(self.valores, width=198, height=300, bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        left_Frame.pack(side=LEFT)
        # Frame Direito
        right_Frame = Frame(self.valores, width=400, height=300, bg='#dfe3ee', relief='raised',highlightthickness=2, highlightbackground="#107db2")
        right_Frame.pack(side=RIGHT)

        msg_dados_fun = Label(right_Frame, text='Insira Valores das Caixa', font=('Century Gothic', 25,'italic', 'bold'),
                              bg='#dfe3ee', fg='#107db2')
        msg_dados_fun.place(x=1, y=1)

        #  ======== Mensagem Registro Frame 1 Left =========
        msg_registro_fun_esquerda = Label(left_Frame, font=('Century Gothic', 17, 'italic','bold'), text='Registro Valores',
                                          bg='#dfe3ee',
                                          fg='#107db2')
        msg_registro_fun_esquerda.place(x=1, y=1)
        # ======== Mensagem Abaixo da Informacao Frame 1 Left =========
        msg_registro_info_esquerda = Label(left_Frame, font=('Century Gothic', 9), text='Voce ira inserir VALORES\n'
                                                                                         'das CAIXAS do seu produto\n'
                                                                                         'todos os dados sao EDITAVEIS'
                                           , bg='#dfe3ee', fg='#107db2')
        msg_registro_info_esquerda.place(x=1, y=80)
        msg_registro_LTDA_esquerda = Label(left_Frame, font=('Century Gothic', 7), text='LTDA Fluxo de Caixa',
                                           bg='GREEN',
                                           fg='WHITE')
        msg_registro_LTDA_esquerda.place(x=99.3, y=277)

        # MSG VALORES E ENTRY E BTN VALRES, R$
        msg_reais_laranja = Label(right_Frame, font=('Century Gothic', 10), text='R$', bg='#dfe3ee', fg='blue')
        msg_reais_laranja.place(x=207, y=80)

        msg_reais_limao = Label(right_Frame, font=('Century Gothic', 10), text='R$', bg='#dfe3ee', fg='blue')
        msg_reais_limao.place(x=207, y=115)

        msg_reais_tomate = Label(right_Frame, font=('Century Gothic', 10), text='R$', bg='#dfe3ee', fg='blue')
        msg_reais_tomate.place(x=207, y=150)

        # Caixa Laranja
        caixa_laranja = Label(right_Frame, font=('Century Gothic', 10), text='Caixa LARANJA:', bg='#dfe3ee', fg='#107db2')
        caixa_laranja.place(x=1, y=80)
        self.caixa_laranja_input = Entry(right_Frame, width=15)
        self.caixa_laranja_input.place(x=110, y=80)

        # # ======== Button Salvar LARANJA =========
        # btn_laranja_salvar = Button(right_Frame, text='Salvar', font=('Century Gothic', 10), command=self.salvar_laranja)
        # btn_laranja_salvar.place(x=230, y=80, width=70, height=20)

        # ======== Button Atualizar Valores CX LARANJA =========
        btn_laranja_update = Button(right_Frame, text='Inserir R$', font=('Century Gothic', 10, 'italic'), bd=3, fg='white', bg='#107db2', command=self.alterar_preco_laranja)
        btn_laranja_update.place(x=230, y=80, width=70, height=20)

        # Caixa Limao
        caixa_limao = Label(right_Frame, font=('Century Gothic', 10), text='Caixa LIMAO:', bg='#dfe3ee', fg='#107db2')
        caixa_limao.place(x=1, y=115)
        self.caixa_limao_input = Entry(right_Frame, width=15)
        self.caixa_limao_input.place(x=110, y=115)

        # ======== Button Salvar LIMAO =========
        # btn_limao_salvar = Button(right_Frame, text='Salvar', font=('Century Gothic', 10), command=self.salvar_limao)
        # btn_limao_salvar.place(x=230, y=115, width=70, height=20)

        # ======== Button Atualizar Valores CX LIMAO =========
        btn_limao_update = Button(right_Frame, text='Inserir R$', font=('Century Gothic', 10, 'italic'), bd=3, fg='white', bg='#107db2', command=self.alterar_preco_limao)
        btn_limao_update.place(x=230, y=115, width=70, height=20)


        # Caixa Tomate
        caixa_tomate = Label(right_Frame, font=('Century Gothic', 10), text='Caixa TOMATE:', bg='#dfe3ee', fg='#107db2')
        caixa_tomate.place(x=1, y=150)
        self.caixa_tomate_input = Entry(right_Frame, width=15)
        self.caixa_tomate_input.place(x=110, y=150)

        # ======== Button Salvar TOMATE =========
        # btn_tomate_salvar = Button(right_Frame, text='Salvar', font=('Century Gothic', 10), command=self.salvar_tomate)
        # btn_tomate_salvar.place(x=230, y=150, width=70, height=20)

        # ======== Button Atualizar Valores CX TOMATE =========
        btn_tomate_update = Button(right_Frame, text='Inserir R$', font=('Arial', 10, 'italic'), bd=3, fg='white', bg='#107db2', command=self.alterar_preco_tomate)
        btn_tomate_update.place(x=230, y=150, width=70, height=20)

        # ======== Button Mostrar Valores das Caixa =========
        btn_voltar = Button(right_Frame, text='Valores das Caixas', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.exibir_valores_atuais_cx)
        btn_voltar.place(x=165, y=180, width=115, height=30)
        # ======== Button Voltar =========
        btn_voltar = Button(right_Frame, text='Voltar', font=('Arial', 10, 'italic', 'bold'), bd=3, fg='white', bg='#107db2', command=self.destroy_tela_valores)
        btn_voltar.place(x=173, y=268, width=70, height=30)

    def consulta_valores_bd(self):
        try:
            self.banco_connect()
            consulta_sql = "select * from pythonsql.valores;"
            self.cursor.execute(consulta_sql)
            self.linhas = self.cursor.fetchall()
            print("Número total de registros retornados: ", self.cursor.rowcount)
            print("\nMostrando os Registros cadastrados")
            for linha in self.linhas:
                print("Caixa Laranja:", linha[1])
                print("Caixa Limao:", linha[2])
                print("Caixa Tomate:", linha[3], "\n")
        except Error as erro:
            print(f'{RED}', "Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
                print(f'{RED}Descontado')
    def exibir_valores_atuais_cx(self):
        app = Tk()
        app.title('Valores das Caixas Anteriores')
        app.geometry('390x90+1200+153')
        app.resizable(False, False)
        tv = ttk.Treeview(app, columns=('R$ Caixa Laranja', 'R$ Caixa Limao', 'R$ Caixa Tomate'), show='headings')  # Visualizar valores Anteriores

        result_laranja = StringVar()
        tv_caixa_laranja = Label(app,bg='yellow', textvariable=result_laranja)
        result_laranja.set(str(self.linhas[1]))
        tv_caixa_laranja_lb = Label(app, text='R$ Caixa Laranja')
        tv_caixa_laranja.grid(column=0, row=1,pady=10,sticky='w')
        tv_caixa_laranja_lb.grid(column=0, row=0,sticky='w')


        tv_caixa_limao = Label(app, bg='yellow')
        tv_caixa_limao.grid(column=1, row=1,sticky='w')
        tv_caixa_limao_lb = Label(app, text="R$ Caixa Limao")
        tv_caixa_limao_lb.grid(column=1, row=0,sticky='w')

        tv_caixa_tomate = Label(app,bg='yellow')
        tv_caixa_tomate.grid(column=3, row=1,sticky='w')
        tv_caixa_tomate_lb = Label(app, text="R$ Caixa Tomate")
        tv_caixa_tomate_lb.grid(column=3, row=0,sticky='w')


        tv.column('R$ Caixa Laranja', minwidth=0, width=130)
        tv.column('R$ Caixa Limao', minwidth=0, width=130)
        tv.column('R$ Caixa Tomate', minwidth=0, width=130)
        tv.heading('R$ Caixa Laranja', text='R$ Caixa Laranja')
        tv.heading('R$ Caixa Limao', text='R$ Caixa Limao')
        tv.heading('R$ Caixa Tomate', text='R$ Caixa Tomate')
        btn = Button(app, text='Atualizar Todos Valores', bg='GREEN', command=self.consulta_valores_bd)
        btn.place(x=130, y=63)
    # ======== BOTOES DE TODAS AS TELAS ========
    def select_sql_table_valores(self):
        caixa_laranja = self.caixa_laranja_input.get()
        caixa_limao = self.caixa_limao_input.get()
        caixa_tomate = self.caixa_tomate_input.get()
        sql = "select * from valores where caixa_laranja = %s and caixa_limao = %s and caixa_tomate = %s "  # Comando para Puxar os Dados do Cadastro
        self.banco_connect()
        self.cursor.execute(sql, [(caixa_laranja), (caixa_limao), (caixa_tomate)])
        resultado = self.cursor.fetchall()
        sucess =f'{GREEN}Valores Atuais Atualizados!'
        print(f'{RED}''#' * len(sucess)) # Insere '#' multiplicado * len= tamanho(string)
        print(sucess)
        print(f'{RED}''#' * len(sucess))
        if resultado:
            messagebox.showinfo(f'{self.nome_usuario}','Valores Atuais Atualizados!')
        else:
            messagebox.showerror("","Usuario ou Senha Invalido")
    # Tela de POPUP ID DELETADO
    def tela_popup_deletar_id(self):
        top = Toplevel(self.programa)
        top.geometry('200x30+600+153')
        top.title('DELECTED')
        top.resizable(False, False)
        Label(self.root, text=f'ID=: {self.btn_colocar_id_input.get()} , DELETADO COM SUCESSO!', bg='GREEN').place(x=1, y=1)
        print(f'{RED} Dados Deletados', self.cursor.rowcount, "Mostrar Deletado")
    def tela_popup_deletar_nome_func(self):
        # top = Toplevel(self.root)
        # top.geometry('200x45+600+153')
        # top.title('DELECTED')
        # top.resizable(False, False)
        Label(self.root, text=f'Funcionario {self.bt_cx_nfuncionario_entry.get().upper()} Excluido!', bg='GREEN'). \
            place(relx=0.025, rely=0.42, relheight=0.03, relwidth=0.25)
        messagebox.showinfo(title='Funcionario Deletado', message='Funcionario Deletado')
        print(f'{RED} Dados Deletados', self.cursor.rowcount, "Mostrar Deletado")
    #Funcao DELETAR ID Table Clientes
    def deletar_id(self):# Funcao Deletar Nome_Funcionario Table MYSQL funcionario
        self.banco_connect()
        id = self.btn_colocar_id_input.get()
        inteiro_id = int(id)
        self.con.cursor()
        deletar = """DELETE FROM pythonsql.clientes WHERE
           id_usuario = %s"""
        sql_delete = deletar
        self.cursor.execute(sql_delete, ([inteiro_id]))
        self.con.commit()
        #Tela do POPUP
        self.tela_popup_deletar_id()
        # Tela Funcoes


        #Button CheckBox
        # self.btn_voltar = Button(self.programa, text='Voltar', font=('Century Gothic', 10), command="")
        # self.btn_voltar.place(x=173, y=268, width=70, height=30) # Funcao Deletar Nome_Funcionario Table MYSQL funcionario
    def deletar_nome_func(self):
        self.banco_connect()
        nome_funcionario = self.btn_novo_msg.get()
        # inteiro_id = int(id)
        self.con.cursor()
        deletar = """DELETE FROM pythonsql.funcionario WHERE
                   nome_funcionario = %s"""
        sql_delete = deletar
        self.cursor.execute(sql_delete, ([nome_funcionario]))
        self.con.commit()
        # Tela do POPUP
        self.tela_popup_deletar_nome_func()
    #Funcao BTN _ VOLTAR
    def destroy_tela_registro_func(self):
        self.registro_fun.destroy()
    def destroy_tela_apagar_func(self):
        self.registro_fun_apagar.destroy()
    def destroy_tela_valores(self):
        self.valores.destroy()
    def destroy_programa_final(self):
        self.root.destroy()
    # Botao Salvar Valores Produto INSERT INTO
    def salvar_laranja(self):
        salvar_laranja = self.caixa_laranja_input.get()
        # salvar_limao = self.caixa_limao_input.get()
        # salvar_tomate = self.caixa_tomate_input.get()
        dados = salvar_laranja + ')'
        inserir = """INSERT INTO Valores(
        caixa_laranja)
        VALUES("""
        sql = inserir + dados
        print(sql)
        try:
            if (salvar_laranja == ""):
                messagebox.showerror(title='Erro de Valores', message='Insira '"0"' aos valores, '
                                                                       f'Em Branco Antes Salvar!')
            else:
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                messagebox.showinfo(title="Informacoes do Registro", message="Valor Inserido CX Laranja!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def salvar_limao(self):
        #salvar_laranja = self.caixa_laranja_input.get()
        salvar_limao = self.caixa_limao_input.get()
        #salvar_tomate = self.caixa_tomate_input.get()
        dados =  salvar_limao + ')'
        inserir = """INSERT INTO Valores(
        caixa_limao)
        VALUES("""
        sql = inserir + dados
        print(sql)
        try:
            if (salvar_limao == ""):
                messagebox.showerror(title='Erro de Valores', message='Insira '"0"' aos valores, '
                                                                       f'Em Branco Antes Salvar!')
            else:
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                messagebox.showinfo(title="Informacoes do Registro", message="Valor Inserido CX Limao!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def salvar_tomate(self):
        #salvar_laranja = self.caixa_laranja_input.get()
        #salvar_limao = self.caixa_limao_input.get()
        salvar_tomate = self.caixa_tomate_input.get()
        dados =  salvar_tomate + ')'
        inserir = """INSERT INTO Valores(
        caixa_tomate)
        VALUES("""
        sql = inserir + dados
        print(sql)
        try:
            if (salvar_tomate == ""):
                messagebox.showerror(title='Erro de Valores', message='Insira '"0"' aos valores, '
                                                                       f'Em Branco Antes Salvar!')
            else:
                self.banco_connect()
                inserirdados = sql
                self.cursor.execute(inserirdados)  # self.admin
                self.con.commit()
                print(self.cursor.rowcount, f'{CYAN}')
                self.banco_desconecta()
                messagebox.showinfo(title="Informacoes do Registro", message="Valor Inserido CX Tomate!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()

    def update(self):
        salvar_laranja = self.caixa_laranja_input.get()
        salvar_limao = self.caixa_limao_input.get()
        salvar_tomate = self.caixa_tomate_input.get()
        dados = salvar_laranja + ',' + salvar_limao + ',' + salvar_tomate + ')'
        sql = "UPDATE valores SET caixa_laranja = %s and caixa_limao = %s and caixa_tomate = %s WHERE id_valores = 1;"
        inserir = sql + dados
        print(inserir)
        self.banco_connect()
        self.cursor.execute(inserir)
        self.con.commit()

        # resultado = self.cursor.fetchall()
        sucess = f'{GREEN}Valor Alterado com Sucesso!'
        print(f'{RED}''#' * len(sucess))  # Insere '#' multiplicado * len= tamanho(string)
        print(sucess)
        print(f'{RED}''#' * len(sucess))
        # if resultado:
        #     messagebox.showinfo(f'{self.nome_usuario}', 'Valor Alterado com Sucesso!!')
        #     self.tela_menus()  # Abri Proxima tela
        #     self.tela.destroy()  # Fecha a tela de Login
        # else:
        #     messagebox.showerror("", "Digite valor a ser alterado antes de Clicar")

    #Atualizar Dados da Tabela de Cada Caixa UPDATE ? SET ? WHERE ?
    def alterar_preco_laranja(self):
        salvar_laranja = self.caixa_laranja_input.get()
        # salvar_limao = self.caixa_limao_input.get()
        # salvar_tomate = self.caixa_tomate_input.get()
        try:
            sql = """UPDATE pythonsql.valores 
            SET caixa_laranja = """+salvar_laranja+"""
            WHERE id_Valores = 1;"""
            print(f'{BLUE}{sql}')
            # Comando para Puxar os Dados do Cadastro
            self.banco_connect()
            inserirdados = sql
            self.cursor.execute(inserirdados)  # self.admin
            self.con.commit()
            print(self.cursor.rowcount, f'{CYAN}')
            self.banco_desconecta()
            messagebox.showinfo(title="Informacoes do Novo Valor", message="Valor Alterado!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def alterar_preco_limao(self):
        #salvar_laranja = self.caixa_laranja_input.get()
        salvar_limao = self.caixa_limao_input.get()
        # salvar_tomate = self.caixa_tomate_input.get()
        try:
            sql = """UPDATE pythonsql.valores 
            SET caixa_limao = """+salvar_limao+"""
            WHERE id_Valores = 1;"""
            print(f'{BLUE}{sql}')
            # Comando para Puxar os Dados do Cadastro
            self.banco_connect()
            inserirdados = sql
            self.cursor.execute(inserirdados)  # self.admin
            self.con.commit()
            print(self.cursor.rowcount, f'{CYAN}')
            self.banco_desconecta()
            messagebox.showinfo(title="Informacoes do Novo Valor", message="Valor Alterado!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()
    def alterar_preco_tomate(self):
        # salvar_laranja = self.caixa_laranja_input.get()
        #salvar_limao = self.caixa_limao_input.get()
        salvar_tomate = self.caixa_tomate_input.get()
        try:
            sql = """UPDATE pythonsql.valores 
             SET caixa_limao = """ + salvar_tomate + """
             WHERE id_Valores = 1;"""
            print(f'{BLUE}{sql}')
            # Comando para Puxar os Dados do Cadastro
            self.banco_connect()
            inserirdados = sql
            self.cursor.execute(inserirdados)  # self.admin
            self.con.commit()
            print(self.cursor.rowcount, f'{CYAN}')
            self.banco_desconecta()
            messagebox.showinfo(title="Informacoes do Novo Valor", message="Valor Alterado!")
        except Error as erro:
            print("Falha de Dados MySQL:".format(erro))
        finally:
            if (self.con.is_connected()):
                self.con.close()


# Base 64 Imagens Global
btn_confirmar_img = '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'
btn_entrar_img = entrar_btn = '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'
btn_register_img = register_btn = 'iVBORw0KGgoAAAANSUhEUgAAAfYAAADoCAYAAAAdQMbjAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAABs5klEQVR4Xu2dB5wcxZX/nzbnvNpd5bjKAiGQEDmIaGNjjIkOh+1z4LDP2D7/nc/2+ew7ZxwO54ANGBuDyWByRgiBQDnnLG3O8V+vuqanurqqp7une3bB76vPaGeq5tfvVU1P/6Y6VI8ZZsAop7NvGLYeHoIth4ZgM/u77fAgHOscho7eYejqA2jvGYZW9hhSWzLG0LQx4q8OXhewS5hmWKdJGQdRdL40iE9d2hpE0vnWSATSiFhey1Ow+z5wbkwXpQYxLk/qQ5VINfifQRelRhBovXeUK7ooNYhJF6sGEbpAGkFgjdIfKiZNmNy8dJFqGKG222E0+J9bN4aVl+dmQ2lOFhSLR21+DkwvyYPG0nz+mFmSz8tHK6PS2A+1DcMzmwfgafZ4ZusA7Dg6BK4sQ3xgoTSISSfKw23cwmgQRRebBpF0sWoQoTNpEKUupaEjpliBNYy3mjnb5RqdSYOwusz+kA2jQSRdrBpE6GLXoCqFTlseRoMwXWANY4TNOR6N1PeMGczcz6gthrNqS/ijriBH1Iw8o8bYNx4cgttf7ocH3ujnz98MG8R/akNHTLrYNahiuoAaHiuwhpEpQ0dG+Qbxn8LQEZPOVe4jlrZc6AJowhk6wnQZ0TCiXH8RzxwCxgqtkfpeRtHMLSuAtzeUwbWTKmE2G9WPJCNq7C1dw3DXa/1w24p+eGn7oFX4FvmQbRzlis6kQey6MBpE0sWqQYQudg2qmC6ghscKrEE8dJFqGKPc0BHXeu9D44rlS4P41KWtQSRdrBpE6AJoRo2hI8blSf2hEqkG/zPoItdIfS+TQoPMYcb+XmbwH5hcxXfjZ5oRMfZdx4bgp0/2we+f74PuflEYuvMDahCTLoUm0IeM2HWKLjYNIuli1SBCF0aDmHSa8nAbtzAahOkCaxij3pwDxhLl4TZuYTSIootNg0i6WDWI0Jk0iFKXcp1HTLECaxhvUXPW6kwahNVFta3Pyx4D7xlfAV+cVcd33WeKjBo7Hiv/4aN9cMuLfTAwJAqRUb5BfOsaOuJDF4kGEboAmnCGjjBdRjSMKNdfxDOHgLFCa6S+l0mh0cZKqUEUXZQaxKTzrUGELnYNqpguoIbHCqxhhFoXQ2iQKL8rKduq0aXQxLWtz2Kv3zWuAr46uw5mlxaI0vjIiLE3dQ7Df97bC394oc955voo/5AR1wftQxMolqPcZ6y0NYiki1WDCF0ATSyGjmjrwmgYYTZuoTT4n0HnqUE0uhSacIaOKDqTBrHrwmgQSRerBhG62DWoYrqAGh4rsAbx0EWqYfyzbOtTaNDgPzS5Gr4xpwGq8rJFRfTEauy4ZDwh7ot398DRDilMlB8YYtKF1mg+ZCSFRhsrpQZRdLFpEEkXpQYx6QJoUho6oq1jusAaxqg354AaxKRLoQm0ziN2naKLTYNIulg1iNCF0SAmnaY85XpvzIHpMqJhjHpzDhhLlI/Eth5N/Uuz6uH6qbXc7KMmNmPffGgIPn5rN6xInBSHjOYNoigf/YaOSDqTBjHF8q1BhC52DaqYLqCGxwqsYWTK0JFRvkF80xk6YtK5yiVdrBpE6AJo3tSGjhiXF0aD/xl0kWukvpdJodHGSqlBFJ2oO6WqGH5x/CRojPj4eyzG/ueV/fDvf+6Bzl6x6Ix+yIhGl0Lzptu4xapBhC52DaqYLqAmZSzj8jxiRaphjHJDR1zrvQ9NoFiOcp+x0tYgki5WDSJ0ATSxGDqirQujYYx6Q0c0uhSacIaOKDqTBrHrUmtKcrLgpwsnwtUTKkVJ+kRq7D39AF+5pwdufqrPKuCNMCze1ClhNIhJl0JDhi7+2vjQRaJBldAF0FgwXUY0jJE2Z8Qz7zAaqe9lUmi0sVJqEEUXmwaRdFFqEJMukAZVTBdQw2MF1jBGvTkH1CAmXQrNaN/WXzuhCn6ycAIUZ6c/o11kxo6XsF3+8y7YcECc7j7SG8QUmsx+yIikC6NBTDpXuY9YkWgQoQugeVMbOmJcXhgN/mfQRa6R+l4mhUYbK6UGUXS+NIikM2kQUyzfGkToYtegiukCaniswBpGmHXRK5ZnDoZYkWvwP40uhWa0G7qFpZtfVgh3L5kGkwrz+OuwRGLs6/YPwaU/64QDrWxRMX1ghbljYP64LJhVlw0zx2axRzaMLR0DRXljoLRgDJSzBz8JwSsOoSHtj18PfQ6jA/ocIiTcd4Wr6HMYHfj4HIaYJbb1D0HbwCB0DAzBkd4B2NzRC1vYY1NHD7zR2gPdg4kBrPXHQlk/TLFSaMYV5ML9S2fAvDQui0vb2F/cNshH6q098oXpEl4dyev04cdkAZw4KRvOnZ0LZ8zIgSVTsqGAmTtBEARBjBQ9g8OworkTnjraAY8dboeV7LnDxUw25Sj3/hFQmZsNd500nZ9cF4a0jP2RdQPw3t90QXe/YRGeDdRrptZkwdUn5cHVJ+bx5wRBEAQxWtnW2Qu37WmGW/c2wQ683agOk6mbPJJRmJMFfz5hKlw4tkyU+Ce0sb/ARurv/Fmn3tRDGPrSqTnw2fPy4cK5ufy2eQRBEATxZgGd7cGDbfC/Ww7xET0nhKHLdYXZWfDAkulwalWJKPFHKGNfu28QLripE1q7FalnsvowJ0/Lga9cXABnzhw9t7wjCIIgiLA8ebQdvrbxILzEDT64oVtYOtwt//iyRphXWshf+yGwse88NgTLf9ABB9v8JqtffGXxGPjCBQXwsTPyY5l5hyAIgiBGCnQ+3D3/+fX7+Al4Rp80GLoNq28oyIWnl82CyT7Plg9k7DjhzBnf64BNeL90xNPQ8T/Noln5tUvy4H8uLYTKIq8FEARBEMSbm6b+QfiPdXvhT8zkXTgs0G3oMnNLCuD5U2dDkY/r3AOdnXbjX3pSmzqW81G629QL88bAT68qgl9cU0SmThAEQbzlqcrNht8cPxl+yx44yxyH+6T11ELyS1edxfqOHvjU+j3ilTe+R+x/fKmPz/2uC8jh5YZFsbo59dlw63VF0FgX3x1tCIIgCGK0spGZ85WrdvC/Foqhm5DqfrNwCrx3fJV4pceXsW84MAhnfr8Tuvo0b01h6MhJk7Phzo+UQHWxV+YEQRAE8damuX8Q3v3KNni+qcMqSGWLSn1x9hh4/pQ5MKfEPIFNyl3xeP/062/rNpg6lhnMXiRz0bxceODfyNQJgiAIAs9yf2jpTLi0ocLb1CUftbD8tnNwCD60Zgf3ZhMpjf03z/XByl3SrVcRNHTd2e5KIhczU7/9Q8V82leCIAiCIADys8bArYumwsVjy0WJhMHQOaJuVWsX/HbvUatMg+eu+MPtw3DCf7dDS5e0UNMIXWHJlBy47/piKCZTJwiCIAgXOOf821duhedwt7zLKiWv1dhoVW4OvHH6PKjNc88B4zli//I9PZap40K9drsrzG3Ihrs/SqZOEARBECZwZrm/Lp4Gcxw3fJG8lnuv9VSlqX8AvrR5r3jlxGjsr+8dhNtf6fM2dE3AkoIxcPsHi6G8kEydIAiCILzAkfdfTpgGJdnomZLXelmo8N9b9h2DNe3dVpmE0di/+2gPaPfSiwVqYeU3vacQptemPHRPEARBEASjsbgAfr5givUihcfKdXiv+e/sOCBeJdE68KZDg3Dv6/3ilSBlsGG4blkeXLk4vRvEEwRBEMQ/G+9pqITrJtaIVwou/03uSf/boWbY0pW4Lt5Ca+zfe7Q3eSq9D0PHAHWlWfDNS/xPUk8QBEEQRJLvzJ4A9fm54hVD67/SnnRWNzg8DN/dcVAUWLiMfV/LEPx1lbinrA9DT4Bzv9NxdYIgCIIIR1lONnxr1njhsVZZEslzlfrb9h+D/b3Je8G7jP3Pr/TBAGp1Hs0X5jR0BG+5+p4TaBc8QRAEQaTDNeOq4fRK+f7rZkNP0M9G7bcfSN5kxmXsd6xSjq0j9sKchs5h5V+5iHbBEwRBEES6oNV+s3EC+z+1oXNE3R/ZqD2Bw9hX7R6E9QfUWebwPylAArEwHK2fPNV9gTxBEARBEME5uaKYjdpLbZ/VItWhO6/v7IbX2rr4a4ex8+vWE3CR2dATfG45jdYJgiAIIko+P71BPNMgGbrl0NazWw9Y08w6jP3+N/p9GzqCM8zhiJ0gCIIgiOhYXl0Gc0qUgbPwYdXQOaz8nqMt/Klt7NuODMHeVtwNrxg6ohh6gmtOpBPmCIIgCCIOrm2otp4IQ0d0hp6o29XdCzvYwzb2p7Z4nTSnwMqymJLOhCcIgiCIeLh2XBVkZ1kmnLRyt6HLPNnUljT2Z7YOiGcMg4DDynEauzNm5sD4cseefIIgCIIgImJcfh6cVlkiGTp7ePkz48lm2dhxxJ7K0MegpVshljdKs+MQBEEQBBE5eKzdMUo3Ifz76eZ2y9gPtg3BkU4hVBFvThh6AjppjiAIgiDi5exKZuzCh7UodQf7+i1j33x4iBc4EG+2xuhOUy8vGgMLx5GxEwRBEEScnFBWBBU52eKVhGLoFujVw5axbzkiTUrjYeiJupMm5UA2HV4nCIIgiFjJHjMGTiwrFq8YwoedWIbOYXXWiP0QM3bxZi9DTzBrrObXA0EQBEEQkYP3a+dIPmzhNPREPTf2bUeHhJ17G3qCmbVk7ARBEASRCRqLCw2mztD4NDf2o53KMXaDoXNYeeNY2g9PEARBEJmgsUiM2DlilO7h09yh23vNzm9j1w1DfRkZO0EQBEFkgvo8vLw8taEn6rhDd6Cxp3ijvVBGcZ7pzQRBEARBRElpDrNq24sNSHXWiL3PMmwH9kKShp6gNN9r6QRBEARBREVptsd5bbZXJ+HG3pnYFZ/AfpOmnD2KydgJgiAIIiOUhbmOfSBx7pz9RmWUriwA9woQBEEQBBE/OWMkA1b82EJ4tqizLNp+o7ehEwRBEAQxAmj9WPJsqU6MvRVDR0yGTkZPEARBECOMZOiKL7t3qmvexDGVEwRBEASRIcRA3MOTk8ZuepOjXDOyJwiCIAgiZlIbeqIueYxdh11Ohk4QBEEQI4YwbS1KnXtXPGK/STF0RUwQBEEQxAii8WSnsTuMWxmhk6ETBEEQxOjA4dcJrMF4cle8w9BplE4QBEEQow6tJwvfFnXSiN2noevKCIIgCIKID60nOw09gTB2H4aOmMoJgiAIgsggbkNPkByxpzJ0u076EUAQBEEQRAaRRukGksfYdbgMnUydIAiCIDKPZOgpPFs6xi7hECqGblogQRAEQRDx4PBlBaXOaeyOSo2hS0KCIAiCIEYQgy8nd8U7KsnQCYIgCGLUovVla0Cu7IqXRulk6ARBEAQxutB6s/BuUSeM3aehe9URBEEQBBEPWv91GnoC9zF2HdoFEgRBEAQxMrgNPYHhGLvAVS6N7AmCIAiCyDBo6MLUDSjH2AVehu6xMIIgCIIg4kD4sJcHC+92G7uXoXstkCAIgiCIePDyYKUuaeyOCjJ0giAIghjVGPw5eYydIxk6QoZOEARBEKMLg6EnPFzaFa8Yuk5kXBhBEARBELHjYegJjxbGLkzdZNymcoIgCIIg4sfow0lDT5DcFa8VMFzl0sieIAiCIIgRAA1dmLoCN/YcaYe8jcvs0dCHITfHekUQBEEQRKYxGzqHlXNLH1eWzV9zDIaeKB8vv5cgCIIgiAyQwtARUTdmmPGJe9rht690WyU2aOgCaUEfOqkQfnxJmXjlj3WHBmD9kQFo7x0SJQa8EtZQUTAGSvKzYFplNkypyNHvecgA/UPDsOpAP+xpwzbK/SY994vPPshi76styoYlDXn872gAW7uzdQD2dQxAW/8QtLHPGz/xCvYZVbIH/p1RkQu5mPwooLl3EF481AMtLM+6wmxYVl8IRTmZy613cBg2t/XBga4BONozCANsPSrOzYIStiLPLM+DySW5kB1BOhtae2Ftcy//TAIRZv31QrQln33+E4tz4eSaIv48CO0DQ/DKsS440DMA3YMB24OwcEFbhetrQ0EOnFJdzD8bvwwOD8MrLV2wraMPuhK5+m6uvB0RfwXZrKAsNxuq2GN6cT5MLMzzv9gMgdmvbuuCXd297DPOghPLi6E2b3Ts7j3Y1w+7e3qhKDsLZhcVQs6Y0dZ7evJeeEE806A0gRv7tqZBOOknTdA7gB+HeYUqYBu9lTdUw7Qqf0by7M4++OxDbbCWGbtuzRtOxDL1q7G/mU6T29IJeXDO1Hy4Yn4hTC6P3+yOdQ/B/77QBn9c0wWt8o8Wrw2iZ1sNOg8Nbvgvn1UE3zmrMuMGj0b0woFeeHBHF6w42Avrj/VBW5/cD+Kv1K58lvCC2jxYXJsPp44rgIumFEEJM7NM0spy/MJLR+FPm9v5jzKLYZ7HDQsq4IsnVMX242PV0R64c0c7PHuwC95o6oU+O76ECI19tbS2EM4bXwyXTCqB2czsg7DiSDfc+PJBeLWpR5QoGJvIcjLVeXWLab03aCrysuE/5tbAjbNq+A9VLza398LX1x6G+/e1QS8zTO13xTM364+9zUngQ5OIVciM4KPTquHrcxqgIMUvrtv2NMOXN+yHfd39ooRhkjjKg+dXlpMNp7MfHefXlsHlDZVQM8IG+peDTfDlLfu4qSdg3g7vqK2E78+aCBMKgq3HUfFEcxv85/Y9sKKtw+67ctZ3H2wYC1+eMh5Ks0f33mitsRvWD27s+OSO13vgX+9qBf7DUvNmtk7Dry4rhysXFogSb/66tgc+fFcL2/izF8ryUho6oq1jOh8a/IMG/9lTS+DMyflWYcSs3N8HV959DA52DIoSBo+vfDETmPIOo0EU3aSyHHj8ynoYXxr/yrmOGfjNb7TB37Z08tGuCztvpV2a9uAI+eKpxXBlYwlcPLko5QY+XZrYyHj5fftgQ3OfKBE5SnGXTyiCuy4YF5m548j8li1t8KO1TbCNjdCNn6sxHMuR1Z1eVwQfm10J75pcmrKf7t/TDtc8s8/zh4OWgObMCaXB/yzdeyaVwx9Onmhs0607W+D6V/aZDR0xxRLlLkNHUmi0sVgdjtwfPGUaN3odX994EL616aB4xUgZB1FimTSIhy6P/eC4rL4SPje9DuaVForSzPFf2/bDN9nDRsoVMx3LfnTct6gRFpUVWYUZ4qd7D8Jnt+7iexB1zGIj94eOmw0T8kfmR4cfHMZuXD9YL7M629iRp7f3wacfaIeNR9gIW2LO2Bz4wdtK4Yyp/hq9HfcA/N9R6GEbNBX+BfO90iYIo2GwDc7yaQXwg/PLYUZVdL9i1x/ph3NuPcJ3NduMwAbRASs/bXwB/OOKOlEQPc/t64H/frkFntqrHrYR2Hkr+aVsj8Xsylz44omV8O4ZJbEZ/BX/OAD37exkz6QcNbE+d3wVfP2kavEqPHdsa4fPrzzMd7cb+8HYVpajpu6E6gL4zklj4TRm9Dr2s1gL79kGHfxXtYRXn5rWRcSYdxgN/ufWfXdRA3yi0d3ff93TCu9/aQ9TGGJ5xsFIGl0KjS4/VfOxaTVw08Lx4lWSRw61wTte2m69SBkngRTPpEEC6PDlv0yshm/OGp+xEfyDR1rhXa9tsV5I+SSztJ5VsXweOmEWLCrNjLnjSP3iNzaA7jcuR+Q6tSAfHj9+7qg1d27srnUgAWucVOcw9gRvHByA9bj7nDG3LgcW1gdbMf79gTb49Std4pVFaENHTDqfjcTd9N87rxw+uKhYlIQHf6ss/d0hbu6ciM3ZiE/NI++pg9Mn+Nur4pdtLf3wpeeb4Z7taIgaHDkoOZra5KGZW50H3zu1Bs6eEO2IY21TH5x05y7xiuGRG+5J2HXttNCHCQ4yc/3ocwfhkb2sz3z1gQzrD2Mdg9VhNY7ev714rGu38BdWHYYfrj8mXglMyxthQ+ewutr8HNj5jlmQLR3vPNA9APMf3gydA9JesQSecTCSJpZJg9h1is6gwb05Oy6Yy/OWOevZLfBis+F7gjiWJ8XylVsC/zo8rv3746bA8ppg50WF4ZSXNsCq9mTbk1mKZ1KuVbmZM/fTX11n7X5X0fTdaDb3vBdNx9hZ/ypt0W610MivOq6AP4KaOvLo1uSxFfyCeZo6lmvrhEZX56lxx+oZGIYbHm6B6x9stg4NpMHfNnRZps7jsIeKMTcGr0ONQacjoObRnYbjqSHAiL9Z2w5Lbt+nN3Wem/XUereUo6NOwodmPTPgt923H254+gh0BD3hy4PH0GQRRw4KoryLrTPPHTTsmUjByiM9cMq9u+CRfUFNnfWFZv21wXJRh71288ZmOOPBnbC3UzqOy3h0v7QRkzQOTOsvYtTgI6xGo5M0R3oH4LVm57r7vU2H3aZuioOwcnt7I5NCY9UpOabQ9LPx0BNH2kWBRUv/IKxoMZi6Y3lSrBRxnHU+dYioO9I3AJe8shV+uOOQVRATGOdVYerJLJV8JZr6B+CiVzfBa+3OAWDU4IlyL6umbuy7YdjR0wPnvr4O9vYmDtWNZljfGrYX4YYjKdjfNshCii+YqRM9OteUbLqa37/eBdfefUw6YSo4f9vEVkSvjZsOngNqNDopPwchNfs7nYdRwnK4axAuvfcg3PDkUW5yDhzxlRxNuSGOcm8N1v5mfRss/eteeO1I8odiOuzDvvHKTclvb4i+fJSZ+XkP7Yb9bLSpRdNW3lrT+otoNQymeaOlB85+ZBc/uz4Bj23SJGLpMGoYQddFJKBmv3SiGX5F/7anVbxieMZhUVisTBh6sm4Y9vc4f1AdZK9dmxZF44qlw6FBfOoQjXaI/Qj5/Ma98JXN+0RZ9OxnRog/wa0spXxd+SRpGmDm/lq85o5nv0s9Z8hF5Cty3cE0o9vcMVeRrw5WHoux8xN2RCdp0ZanTtZNcM19m3v4yJ2pQvHqQc2HjXF0OfByjKSJ5qnBJ8E1uGGrLEj/I93Q1A9n/HU//GOXZsRqx1faZcoNcdRJOh+a7W39cN49++CBXYaRUAA0p3xochD5sbKgPwCfOdgFVzy+T3tuiTsOkoylRatBUJOMsYeN2Jczc98tRu6V+boTKIVGtzxjHAbXJGPZeGrwEVxTlZfM+wAzyYM9Xj9QGKLOZehICo3d9zIpNUhSV6kcu8ZRvI1Bw3HUKTjKA+pMWlH3ne0HYxu549nluphapDo+cmfmvjomc8dL2jjafES+mrrRae6Yq8hXBysfxgd7GouxewV216VOVlsXWjMMt67tgh+/7NyN5pfDnfIJc+KhA2PxLlbw1OB/Gl0KjTVWsTR4Al06PLuvB865cz/salNGnHYOSn4pckvWSbqAms6BIbjykQPwq/XSCC5dXDko+QVke3s/vIeZerdq6q44Cdj7THWeGqFTONw7AB958QB/fupY5bil6btijMMQ3xUXnhp8oMag0yE0hdlj4ISq5DkVhxKmroNrMEpyvbcRdS7sck1+KTWIomPlp1VrztlJoUnWKUSiQyStRvfFzXvh0aNt4lV0TC7Mh/F4GZsmpo22bpiZez9cuHpjLOaO16mX56o/dEUfpch1Ry8z9zdGkbmbcmUkDD1BPMauou1A7FjRuTq0GkTodATQfPWpNnhNN/pOAR/FGeMweJs0+Xlq8IEaRZdCo+5+nFaeAxdNDX/C2fP7e+Cd9x50XsLmyEGTnw6XRtL50iBODfrlJ589Av+3Nk1zd8VBRCxtXWpwhH7Nk/v49fE2xmWxWHwdES9lwmgQUf7UwU5Y3dQD/za70rqqgGvYQ4dxWWE0+ECNRsfrrKcOFM2HplUlR1eMAfc5vfayRtrQ8XFxXRnMKPa6lNat0eKqS0cntB463Hxdt2YHPyYeJRjuhkmGK3K0+TjzxZF7HOaOk898sH6seIWwmNp8JKQ6PnIfTeauwnJFU1eJ19i1HSg+UE0yHK0GQY1BZ9QwDBrcbXbDIy363bNeGOPgQ7Mwz9zwgRpFl1KDCqemMGcM/O6iWn4daxjeONoHl99/CLoTx9MdOSg5Ouok0tYgkk6j+ezzR+C2LeH2trgRsTRxgvC/rx+D1cek8wC0y8I4IpaOsBql7plDXXBcZQF89bhaUaKg0XB4OYulI6VGo/PU4JOkZkF5AXxtforLNJkmkKEjdnlYjaSTNA0FufDThROtFy4kXao4jroIdIhJhwgtmvqX2Mg9aj7JjP3MylLxSuDKx9xOvls+BnPHyWdmFeGeTBbXlY+Eko+FdULd8jWjzNxZnuoo3QLb6LgfuwVeg/6dZzrgQ3e18sd3n+2E7c2ay0280HYQIjpWV+epMXwgRg2Da9hDRdLgiP2O9WmuRHx5GMcQS0doDSrcG7dZVbnwj8vrYUl9uMl49rQPwNv+LkbqIo6FkqOjTiJtDSLpTBoGrszXP3MYntof7ox1CxHLI46xXGFXRz+feIajXR7GEbF0aDWMkJpjYiT2+fk18OMlDVCWuFzPqMGH6A8VkwYJpcH/nLrLJpTDP86aZp6qlWkye2Kct+b06hJ45vSZML4wV5RoUDQOXHVSPC8d4qoL2rYEw3DLvqPwesQGmstGx387biYsLS8x5JO6nccGBuD81c7L5tIFZ5R7aOEcmMbNXYMxH5avqNvOzP2sN9bCTjaCH1FYLl6GnmiHfR07zjj3tSfa4ccvdLpmi8NtwydPKYb/PKfU19zVRf9lHetLkgzogpV/cJHhWkaPWDgPMx7vXnekH3a3yrO/uZtso1ne7OpceOVDdb4nRCn67h7rCX+/IZa0rA8uZCt5Ai+NCY+8aoqyYFlDAZw7qQByQs7ogrOinfu3A7DqsLzCKjl6LdpRN8xfTivPhZkVuVCen8X6dQw09wzyM8w3NPVZe0gUjY3vOABVBVmw8t2TYFyx/8sxP/3CYbh5fYvvOD84eSx8fG6FeKXnw88ehD9t0x0eYO3yEQf/zKnI59PF4jXzR3sGYGNbH2xv14wOjMtLxvrRSfXwscYq6wWjuW8Q7t/bDmtaevm5Cg48vit/39sGx3p114/rNZdOLINq00QoPLekDnePTijKhQsbSvloXcfLTV1w+pNbxSsJQx/gJCyXjjdcq23sN4ajTt82XIfr83Pg7NpSOKXKPBfGmrZuOPGZjeKVgiuHYT4V7BXjKq2XXjkq9A0NwSG8vKy1E46wUa4RTUwbVndZXSXcftx0URAdbQOD8LbVm2FFa+IyMxHXq41KXQXrm4eOnw2LS9OfeyQBjriXv7EetneLyyqN+bB8DXWT8vPhsQXzYEpBPDOaepG74nnxTEHznbSN/Yb72uB3q8QvOKVRiV/LH1xcBD99ezl/7kXS2M0dxBF1XV8aZz0JyasH+uDbL7TDA1tSzYimwMuH4YEra+Hsyf5OOiv6Hhq7uyM5mjhdn5kkno1O8HK236xL7NpW2uXjs0Oy2Ir1tinFcPmMErhgUhE3dB3t/UPw3P4euH1LO9y/s8O529+Eqy6pOWtcETxw8XjfP8o+/aIwdh2aZfzg5Fpm7GLDq+Fw9wDMvHM7/3GUJEWbRDnOk3797Er46KwKqCt0G+I6ZsS/2NQMv93SAgOm9Q1RvtRvXDIDGsvSn1zj5Ee2wWr5unKetyYP0Z6XzpsBx1emd+KmzApm7Geoxu7RpydUFMKLZ88UBSOD0dgdeSf7EG/gsv6seeJVcPB4+TNN7fD1rfvhhWZl7gIX0mcn6vEH1vYzFkJdvsfeh5C0MnN/++pNlrmbPrcEhnwtc58Tj7mzEbgb1kc+cuXmPj/z5u42dnO+fAuME8pwU8c3KW/kpi7Kf/tqFzy+3c+uCNR4dJImTjqc0JAHf313Nfzq7VV8ljkbrzh8g4gPgD+vC7JLytI4iLg9meKhnV3C1JN9wfHsN/Hgf4bhqsZiWH31JPjLRfVwxcwSo6kjpWxEetHkIrhleR1suGYKfGx+ufmcAFcOUo6i/Kn9XfCjN5qtF2FxxcEoYtevUq7y682tblPXLI8jleNUsK9cMgW+enyN1tSReWwU/+Ol9fDS26fC1BLNhpd/v+TYAO+aVBaJqTvgeWMcZyyOrp1xIPWdA7vckN9I48pbylHXnoDgD9qzqkvhiaWz4Oszx1k/cF3LlfpGqccTFO84KA4jRQxe/nb/8bNgCe6WN+GVLytvGRyEi16Pdrc8zij32MK5MK1A/hGajGlEynV3by8sX7tuBHfLY64e+bJyvhX+5Uph6hJ806YR/wLfmwqPgMa6CLh2fhH8/h1VwH6IeuQgOkXikR09/KMNjGccfIRaakZo7xuCf38apx1VcvRsj/UUNVPKcuDhd46D3zGTxt3uQakryoYfnlYLz102EeZXSWbkiINgfiJHVx3A1185BptbQ5zUolmWw9CVOh337pL2dJi+aMqyLp5QAg+eNxEmFPvrs/nM4J+9cCqcVCOudtCsvwga+s+WNIhXEcDzxjjuWGqbYsMUx1GuyW+kceUt9aOrLn1wcZ+f3gD/1SjPXe8v5iPHIryEVAHN/QE09zLF3LX5iHyVuhY28o/P3HHE7Y7pwFC3u7cHlq/DY+7RzfSZGsxV5KtDypUb+4q9yRmUHBs3DSv2RbMRtRCJRsg7Ggvhw4s0vxING0TMC2dZ23TMOYuUJ8b2MHgdxom2XVHzjRXNsKddarOpTY5yq13nTyqCF94zAc4Yn/5c7guq8+BZZu7XzipV4kt96JFbHxt1fGd1wFG7sizHOq+LowFnsXsdb4ea6osmMZOZ7y1njIO8gOdD1BRkw8PLJ/Fd96oWd3i8d3oFPHPBVKjSTkwTFtH3Mhhal7qpPA7sONL6gWQqfioceUg5ZqCPPju1Hs5lI3hfMUXdCy0dzol1IsZh7tp8RB9p6yz4yP2NOMx9HkwrDHNCnZUvH7mvw5F7hszd0D+6XLmxN3UNsXRTbNxE+VF5gpZUmJYldU4cfPHUUn4vaw6Pwx46pPjrjvo0dlPOWM7jGGKNIna09cMv1ohJKnje1lMHjvJku3B3+98urodKj13uQcGbmPzqrDr49HGJ49miD025IVL5Q7t9fuE1ywtq6AmeP9zFz07VYlje95eMNZ/9nYJipvvBifWw892NcPvpE/gZ77ecNgG2vasRfn3yOH7MPja8+oeXJ9eP2LBzUGJ55TZiaHLMEN+YyUbtXn0i1WGGnYNDsK0rXmPSj9xFH3nliog6HLlf/MbG6M19ATN3ebe8MR8pX4mEue9if0cEQ9/xrQzaurFBSjk2zxfagBjH3TlRU1ecDadPxlmQDNkqbUK2NIWcsMFeliZWzO0MyzfZaJ3/Sjfl5yhPtuvS6cV813vYM/C9wCX+99Jq+Pi8cuuFV26OumFo6h1wz2efAv4z1mtdNJULNrRovsiu3BIMw/zKPDh/nMfxRp/gtKt4LP0jMyvhisllUG84Rh8JxvYweB32ebB+D4ydgyaWKbcRRcrRzl2DV10anFheDNOKDCd1iXjJnrSebe2K35S4uR+H5o4nwok+8mq/pn+aB/r57VdjM3dtPqK3NPkk2N3XC+euW5tZczfmg7kmrmM3JGwUpkKny4Chy5w8XrNyY3xtbgBNPQGv1Uf4ssQHL2OKMwrY2NwPd2xR7naUwJG31C5WtrguH357rv/LAsPy3VNq4e2TU03ViSTzy2UjfvXWpSas/VJMZ3q7K46eTfJxfaMG41ixLp2kTNwx2jH1AW9rsu9jheegicVzsJ6OSrzyy0DuyyrMx7StnpT6lJUf87pkLkIsc59tnVBn6gMp1yQiX1bePDgAF6/ZAK92xDxy51gx/eSKI/eMmLtnPiJfhn6/oFaMoqTQN1zDHjq0caKhvlhqmlccsZHq6DPkqIMvz9I5iLE9UXHzG63u2fYceSvtYuV4ffXv2UgdZ7eLG/TnX59VDxNLxEjUkVsCkZ+oW1ZX6OsHB1dpl8cwlRtoxuljjRoWSfmunFAd7b3lMw5vK/ag6HuZAP0WDCWWqb9N5ZnGKw9XnaEvI6AuT5yYKcVMRhMxpbr2wRCDmpBwc1/IzD2NE+qa8a5wbOQeubnPT5g7xhRxdWhztU6oO3f9mvjM3ZiPyFfCaezahFHg0Ugj7mA22jjR0tYrcjbF4XXJ/HwfouQapV0ZaE8U4HXkf96sXO9q5620S6r74ek1MKM8+mtdTZTnZcGvmLlnuX52ihwdeUPKSWQ8UZaVRMQx0KG9sT9q9LqxhTEeA48Tu3+w7xXsupjxipOJ+Ongyh37UdOXEdKBRi1iJqOJZ6582LaPX0aUORzmrsnHQp9rAm7ucYzc588NcUIdYuXLR+5xmrsM39bg5+omuStem7B35xoxbNxCLSskW1sMu5d4DtgZzg4pC3symKk9GWyrX+5gpt7mGmkqfaHkvay+wDpjPcOc2VAInz8+MYOayFHJDblqehm8c0rIY9fKsiwwjojlgWsPgZeGlbPfVG8+eHtE38tguamtUeIVx67T5DdacOUu5enVtjTZ3GVdvmtFk/rHEK+UGW2mSZj7SaXqd1fk69U3ou/iMfd8eGyeZre8MR/M1Zlv/OYuYppguRjczJ2sjbGBHqDGpPNKMCQ4I9Mj25VZ6HgOGEsTj9VNLg94EpKpTaLcPpY7ivgLHlt35CzlZ2jPd0+t0RVnhK8sroZvL62xDgEoSeAJfJ+YXwm/OqMueH4ocIlYX5jWeQ2ViV08XGP4nKU4OztG0Q0kfKO0S9tvGcbOAXOT8hvpvGRc/STl6qqLFpzx7fkW3CvnMyYrnzwC06MiaO4P2uYu8k2Rq1pnmfv6+MzdmA/mKvLVwE+o2xC1uXvHlHNVjN2HMCjGZYlYMfDXjV2wr10cN+KNxTiaWLzOetpY5XNXs6RxIMpHo6EjR7sH4YUDictapP4wtYdx3qQiWDx2ZL70CT61oBLWXzEVvntyLXygsRze31gG3zypBl6/fAp8Z2ltsDP0tW0VfRFgMUhNAfvqmNZfTZxnDwWZ3XCUoe03gVddlDjiKP2eifh+ceQi1i3EkX98/GT3IT6XPMcrplTXWGzY9ZwBbHNP7JbXYWwHfm+HAU+ou2htDOZuH3OXsWJ65Zq4SQuaeqTm7hFTrRPGnjpZY50Jk4bHwWbHw5GuQfjK02I+cB5HE0vJDac1PaEujak42bK0hq5r/wjxwM4ufuMcuz+UPnAg6j51XBrHriOkvigHbphXCT8/vQ5+cXo9fGZhFUwrjeKYP+sLUz+Y+kYwtyLAVReMu/a0QZf2uPwox9QPoq3a9T5KHH0qrb+Io240IeXplWPEuW/o7IYf7DyQOqZUN7OoAGpyY7xk0gfc3BfMce+WN7ZD9K9Ux0fuUZt7nrxbHuM5Y6ro7rpmmfsb7G8McwUY+0cYe57pbGeN0Nf9vrVvER0TI809Q3DF3Udhb8eAPpamPcjShjwozvXRLhUmCXxLyRHiH7ulEaMpNynvyaU5cFYEM8uNTsS6qOsHqQ+8OL5K+iXvpeFxhqGlbxBu2hjPvNyxYGqTKCdDNyHyTJVjxPnv6u6Fy17fAh2J0bqKNp9hOKdqdFyG6TJ3bf+I9UDbFsvcL1m/AdZ0Rrd3zDZ30wl1CMtFP1kV5joMu3C3/EYcuUdk7ob2W1gxubFPLFdOnjAKh2FyhbL3PiVWIO3yPBMMxlO7e+CMPx2CFQc0uz284rDyd8823DbWhFiedsNmijPCrDjEViqRtwtX+TBcNbMk9mvWM4/HuogEaO+S2kLr2nnjskQsif9dewRWHUvnPvIjCLaTPbSGHqDfgoFxpFgih1GPV44RtwF7585DTbDs5fWwzTTRjCtesl8vH5u8xe9IY5u7eilcIl+vvhN1R/r74cJ166M397nztSfU+bk3OsJH7lGYu7RMF1JM7tIXzRC7FbFQK0wmeuEMj18uKkrjbJQ4rx3s8/c45Hw8vrMHblrZDufefhgu/sth2NaimRZW2x4Gz2EYcOKuy2cFuC0g0xk3bqZYIwzuwcC5zV24csY2We3C27D+02D67Dw+T5wadrluJjm+zivrhqBnaBje9fQeWKubtW40w/oh8+u8FMsrTqw5hMB3nsPQy0bXr7Z1hXh0wkNHW+Gb2/fD4pfWwjVrtsFR3SQz2r4R/crKpxblw+kVhnvYjxBo7g/Ml8+Wx+8T++Nqh0BTZ5n7OljbFZO5s3h+DV0m7ZG7Ybm6bQ6/H/v+9kE44ReHrWu/HTiTLMsfA699tA4aSrwvjyj6n73imQav5EwYNfifQedTc/2iUvje2f5/tRb+aKd4JvCMA9D9ySnWkxHk79s74epHDopXAkfeUh+y8uqCbNj9/qlvuRH7jSsOwc0bpRvGGD87qz9+uKQePj7LfD/223e0wnXP7xevmMa4PPFXgD8KvnNCHfzL9MpR28cnP7YVVrd2s1Zpvl+anFecMxOOr4ju0M2K5k4445ktPvt0GE4oL4IXz5glXo8Ma9q74cTn14tXAlf+zu+aJ6I+qfCp1dYJrVT301lT4CPjx4pXo4uWgQF427oNsLLdY5ZMLcl21ubmwiPz5sH8ooB7ZD3Yw8x5+Ya17vu5e/kXIuU7mf1IeHz2ApicH2CQzMhd9ax4JvCIyUfs40qz4Y/vqpJmFmMCFEnJFOWO4e9JZepGcFnS8mx4uSHBlBqNzlODT5Ka0rws+MxJ5eJVQExxELvc0K4Ms7nFNP2p1IdS+dK6grfgbngJRx/IsL5I9QWVePfkMhhflGNpdMszxMHJba5fuR9OeHAr/GjjMVjT0sPvjT2qYHn7NfXYSNmnmN8o67cEjjwTSLnq2pZAaJOtk9qpXa5AWye0St3Uwnx4f0ONeDX6qMjJgQfmzYETS3R7xcRfF8524sj9gohH7hNx5D5H3i2PMcVno0Ppd8QauadxQh3f3njH5CN28RLWHOqHLzzRCk/u6E2sRnwDf9aUfPifc8th/lh/ZyI7RuxKo2x4uSE5kwYxNchTg/+5dd86sxI+tTjYrqjCm5QRu4ydgxIrZW5IcE1tYTacXJ8PH1tQDudMMI+Wrn/qCPxuo7ibG8c71pcWV8GXTxw9x96i4saXlRG7DesPTX+nGrEjP9pwDD7/6iHxSuD52bnXwwTFuVlQm58Dc8rzYXFVIZxbXwxLqgshO8MzgyFLH98Cq1uk8wFMKYjyFWfHMGJ/lo3YEzjih/l+JZC0PnXY//Xsc8Fbot44rQ7mlujbaY/YI4hpKYLrknhr717YCG+rGR1XvXiBI/eL126AVzrUOThkWFs9+qc2j43c58Yxcl8D203m7Pl5WZ8NH7nPWuh75J676pkUyxV/GY4z4RbU5cL9V9fAtk/Ww0PX1vAHPscyv6Zug0FMSfCGSSteglQa3UbRU4MPTSxWftqEArhhUUTHl+wclFh2uQZHnTs/LYrmSPcA3LejE95273745DNH+MQ8OnbK9133kd+cqjQu/XtTwfqCr1fiZQg+1lgFM0ql/jIty7T+IuJz6GQj+Z2dffDQ/nb45trDcPbjO2DavZvg86sP8vIRQeTmwlFuaFdUOOJLsUy5Ia461AltQN3g8BDs6+mDW/Ydg5Oe3wA/331E1GlIM2ZS4UOHuOpSx7xuXO2bwtQRPnKfPwcWlerO+WHt9Pr+ivbzkfv6dbA+4pH7o3MWwFTVlA19zlG2AThyP3/zGtjL/voiRTtltKe415dkw5mT8/kDb4EaGJ8Ns9EkZsPrwmr0Ojyc8IeLayDkrbGT2DloYnnmZj116Rx1Ej40v1rXBt9Yqb+cyjpxTtI5lichyiclbsDyloX1A18XxUsVU/9owDPjf3RSvVnDy6XPSyalZhgO9QzAjzYdhQUPboGPvLwPDrAfcxnBlBtil1s5xoYjBylWqtwcdT51iKtOapvQ4iGTT63fDX8/JObK0BI816RCPPPSIa765BK8tMeXFsEPZ04Wr94cVDJzf2jeXFhUkjB37B/RRyaUOjT3d27cwC+Ji4pJfLf8ApiC5u7R53a+GnDEf9m29dAX5lCcR8x0rc0f/EMwJG7qDJ40ajS6sBr2KM/PgnveNTb8uQKIWJYVR4ll1yk4yhVdRJofvtYCu9rdK25HYqJyjcZGKh9f/BY2dr4uiucqXv3jwfKGEvi3WZpDFynWRS0GDd4//5adzXDcw5vhF1ubdEuNHztvJUev9qSNFMsrjqtOk6MJL62rzqr5zIY9/DNxY9bZSHXJSMlnRh2iXa6/mFMK8+Ge42ZBUXZmNvtRUmWbe5G5jYixD/B68h74/v594nU0oLk/njB3F+xz8bG9ea2rA357VDm52QtjGxk8XuJ+7HEhgmgxJcfLUaPReWrwibdmbFE2PHR5HcyvSW+WOQsllhTHhUMj6XxpEH8a/NV31zb3WaS4i9czjhILb9P61kSzfiDGPjW8X8P/LKqD08aKY3im9d4Yh+FT08Z+pP37q/vhqud38+cZwc4B85NyVHKLHiWWDlcOAXL00qbQ7e3tg+eaNGdse+kQUZeM5D+mu05ofehmFRXA44vmQEPilq5vQixznweLijW75Y19gP0j+ohx21GPwygh4eY+WzZ3Z0wXmlxvazosnnmg0TmQth/xbMF5AskgDkzJ2RqNzqRBeLlGp2hwytinrqqH48eme/xYiZUqN14XRoNIOp+a9c3u4zVdA1LsBK7liVisrCgD910fFbj6QMK0/hrIzRoDd54xEU6q0fxy94yDDz+fjwQrv2d/K5zz5DbY362ZuyEq7BzEuiFjyi1q7Bw0OMqVHFPpTNoAuvUdASYbkrRWpHAxLYTWS4eIuguqyuGpE+bCxII3/7kzaO54CZt9tryxD7B/RB9J4PHsthjuP4/m/gQz92l4Qx3TZ2LMFWBdj+GyPj/wduI6kSSmoZkzCMejUVZSQTX40OgUDW5wP3tSOTx+ZT1MCXoHNy9S5oZPlPx8aRCNTodrecPspenNAo3GjpVC+pbB1QcSmi+JXyrysuHesybDSdXSWdPGOPiQ+l7Gp2Ztaw9c9PQOONYbw3F3noMmP56D9TR2PPvBemoh5eiVn1YntF46xFU37O+SUGm5yWg+YmrrlHxNCG1JdjZ8Z8YkuPe4WVA9wvPBRw2fwlXbB6x/+HdYvNTgURUPxlwRK9+sMFnxdor1QSH+fa5ejTIl5qnBB2oUnaLBL92lM4tgxfsa4BunVUC+nznu/WJalCMHTX46XBpJ56iTcJUndXM0d6njI3APjVqnHeG/VXD0gYTHlyQIeDvXR8+dCh+YXqmPxfta6nsZ5XOwscvdmk0dvXDp87ugZzD93J0oyzPlhpjKo8aVg9SPqfIz6RCTDvHQzjFc9saRdEmFeOZapoKrLrkET62oyx0zBj7QUAtrli6AT02sN779zUjTwACcv34drMLL31yIvjXB6ibm50Mp+8ETNXib1nM2veG+/M0zn2S+cwsDXIrnta3C5bGHy9hfPdgH/+/xFnjnX47yBz7H6VwDIwJo4XUeiemwNRqdpBlfks2vTX/l/ePgtrfXwmy/t2P1iy4/npv11PElRBx1EmlrEEnHyvEGPZdNc0/oUJwnf8xOjS6OfbLdWw1NW1N+SUKAZ8r/Ysk4+N3J46G2QIyUeF9LfS9j+Bw4vFyjkzQrm7rg06sTM+BFTKrceJ2h/6LClYPUH646BVedlKuX1lXnjDmxMA9OrTRMniJ0SYVTa0TSJpF0Jq2om1KQD1+aMg42nLwQfjV7KozPf/PvepdBU7+QmfrqTvUObqyP+PdYvFRh5YkpYK+uqbXKIoTfe52Z+k7Z1MVnokWzzbmm0scMgBqdAymevcXvZb/4r3+oGU7//WH4ycoOeHR7D3/85JUOOO0Ph+H6h5v5e3xhbBA+cBma5Zg6QqPBO7EtqsuDpePy4YJphfCx40vhx+dWwSpm5lv+dQJ864zK6A1dhyNnpV2e7bGeWvjQIC6N0EmaTx9fCZM1tzNNngzn1rhg5dp55d9qeH1JvPonAFdPqYA1F8+AG2ZVQZFuj5FXHF4nfc4JDJrf7miC+w/IkxBFgGdu+ESTX5S42qrEM+WHeGlddRI+dPjn+7Mn8pGxA/EyqXBrtWjrhFapw9HmjKICOKG0GC6oLoePT6iDn82aAmuXLoTNy46D/5w6ASbhcd63GHpTx/4RfaSDlctzuuPJbZ8dN168igaXqSuflwPDNueEohK4rqZBvAqBJibf4mOoD93XBL9/vdPuBPnNWIZ1H74/5G0n+bJwKe5G6ZLi2OVuTTf7gfHlZRXw5FX1cPelY+EHZ1fBhxeWwpzqDJ7xaeestMvUHsRRLulSaew6s+Yjc8vhK4bZ4sbzuQiYTtE4kOp2421vYwbvTb6rox92tId/7Onshz7TrDxGsB8MGq/+CQked//eogbYcsks+M8FdTCzVJxcY4rD6zA/JceUGoBPrd5nXQERF44cgvZ7QBxtVfrDkYeCq07SBtIhSkxGDjPzm+ZMhneO1c9IaCnSjckeHro7F8yEl06aB/cdNwtuapwM/zpuLDQys3+r4jZ17B/RRzpYuXqTFpw3/p5Zc6AiO7pzDdDUlydM3ePzsnKVs0kyraAQ/jZ9HuSFmV3SIyafUvbezd1w1V3HRIn1xwUvH4Y73lUDl8z0njqy6Lt7rCdCo8UUBzHpJA3O845nuWfUzBmFP90hnin5pWxPAkmXpmZsYTaf1/3j8yvgbI97p//bM4fht5taxSsFVw7D8MVF1fCVxdXidXRgK+7Y3gY/Wd8Mrx7tEa1i/5v6wdg/SQ2eS3F6XRF8Zl41nK+725rEja8chJs3aX6cGuL88MR6+Hhj9FPrbmjrhUcPdsDq5m54o6UHNrf3igkqrB5xkaJ/5Dndv7WgAT7TmP7uxqVPbuY3geE44is5iroVZ86C48u9twtBWNHSCWc8v0m8Epj6AXHVSXkG0iFOLU4p25CfC+dWl8GNk+uMx9bXdHTB4hfXWS/CxvTSIax+JjPx5xfPg4qc6I8VjzZwStmLNqwXx9RZH6XoH35SnQKa+j9m45Sy0d2xkk8pi8fU+wxTyiKmAYQAp5J9fOZCmJzn70dZ7uqnrSdefSBicmN/xx1H4bGd/hI8f1oB/P1y7w0HN3ZTozyTwv80OoNmZmUuPHN1PZ90JlNYxi7lmKI93ddPEy9Gju+uboKvrhQ/3BJo87baddGkYrjr/Gh3WeFRnA8/ewBuZ8ZuwQpMfWfsU2/NjXOr4dsnmI9VaY3duLxh+OHihliMXWWQmTpek46zzD16qB1+s70JNjLzT9U/upu04DH9rRfOse4Vnwbc2Nvky7mUWMriYzV2r6aIOn53t1NmWy9GCG7sLwlj16Fth9SvPtqZ4Lyqcrh3YeOI3EcgUyRNvd0qSNE/7m8DmnoOM/X50Zv6Zs2JcjYe2ymE1aGZBzF1JPd1Yew6eLxkD3BHfMV0chyas2LQrxzwcSKdztQxsKGxZ05ijeMaReehwfItLf3wLw8f4aaROaRgHrkZ60aAxgrpJBptbqLvRd2Kwz2R9+nXXj0iTB3jiFg6tOX+ND9cfwx+sVl3kxcNqNEtj8dhjwyCG2c8m352WT58YmYNvHp+I9x84ngoVuc8FjmjobtMXdQd6R2Au/cb9s4Ewe4bjCPFEnEyglcsV11mP7PAuNoxDJMK8vhscMHaiQzDo00t8JUdYs/oWxCHqafoH3W3u8XwyJh6qu0Ue4QxdU/49srZA3zL0dqjHJczbdxYUs3qe/3g2dBhuO2SGphWoRz78NRgM6x/D+/ohv983ufGPCpEDi4c5e7OHilOqhUrkCtnkaPSnqbeQVh1xGMPTkD2dw3ATevYSNnHSu8ioObrq494H2c2xsHH6Pi88PDCdVOr4Kmzp0N1fvKs+sQ670DTnlt3R/F9wDhSLE0cG1N5XLjijY7PTYu236x8y3Oz4d7jGqFMt0vdqGMPUfe93QfgDwejn0ltpLFMfR2s6hSmroOVmwwdv8fW7vcMmjrfTrmz4YjPC4nU1D1i2ifPcVIlxzDU6pEa5ICX45KspVUWZMFf3zkWyvCyLE8NKtwbt++vaoU7NqmXQMSELjfEUR6ol2JnXHEOTHDc2EX0vehTHQ/sSWMmJIX72bKMNzkw5ZBqXdTmPQxN/QPw9KGA64K0Ljow9E2mWFBeAHefOhnY9p9lp+Rn7AOAZ452QOdgRCfRecTxrIsDVzzD5zYa0PaNyFeqm11cCL+dMy052Y2XDlHqPrF5J6xsi+67OtIkTd3QJtZ+vaEz+DYDoDYng6YeYDsVman7iGnt6+Mv/CXnC5PGLnfHwpPgfnVRtT4UK9QZenJ5AB979CisOuTz9ndRIuVgtUvk6CgfefAkOzs/r9xE3Z+3tRtvAxuUbW2awzfGHDA/Q+BUGlG3td3nvAumL4gxTuZZUlUE/z5TOafFlJvIu3doCF46FsEP3RRxLLD/NH0YJY54iBTTVTfCaPMR+RpyfUdtJXxpynhDO7zb2cM+68vXbYb9vSHmGhlleJo6a7vR0HnfWjUZM3XTtiOB8llFYupeMZX1QxzE07xZeWPa8GVhHCWWFOOS6UXwhZPLxSsGqxtmDfEzWsGZt95z32E40Bn9PMBaHDlI7dLkNhq4YIJY0U25KXnv7uiHJ/dHsxcEJ86xUeIkYf3HV1zxUsaoYWg0eEmSJ6YviFecEeRzs2qt4+2m/OxybJPVLvuM9rB4xkGSsWLDEQ+RYrrqRiMiXx+5fnnqeLh8rHyipg+tqDvQ1w9Xrd/Cf9C9WfEy9ZSGLvonM6YuYpoQn4lMZCN1HZp4iDB2CcMbOaYNohd8eahRdIY4X1pWAe+eZd2az4+h27DyA12DcPWDh/xPpBMGRw5Ku0y5jQIunlQM2rs1OtpjYf2UGoYfrI3m3IWFVV4nCLH+k76cLozlQqfhuErDF8hDY4wzCijLzYZLxpWJVxKOPnW2a1N7xHuvHP0jxXLkEBcYT4k5qpHy9cpVqsOnv5w9FRbwS+mYFgtMWk3dS20d8PHNiUtx31wYTZ21EU3dDfaP6CNB/KbujukAyzV1sZu6geSm3pAYh9exRgXB1mh0Hglh1c3nVcO8GuX6dM/c8IkVa8WBXrjhiaNYECNKu+wcFEw5jwDVBdlwar0yH7GSX8LQE+15nI3YV0ZwEt3FE0pgbGJqVRuMI2LpEDm44Bqp72XY+8cW5sDS2gCXXRnj4H+GOCPAsmplg2XnjDlKeYr2HIrqxjBieRZSLEd5nLjbpiUjufjBR/8Y6vCmLXcvaIRa061Vjcu0Ppc/HT4CP9sX4L7eowCtqbM2ep0Yp/ZB7KYeZjvFmJyfH4+pe8S06hL3Y0/xJl0Xe2LSeCUkgVOg3vmOsVBTmG3W2OXuWH/a2AE3vxHx9Jo2UqyUuY0urphWaj3R5CcbusxnXz6s9G5wcDfyD5bUJRcd5ovCNYZMJM0Vk8tS74pHTHGQMOt8zEwvFpcs2nkrOSrtae1P85CUY3lSLCVOvPiImdF8fJBmrjgd7B3zZ0Keeus4rU58LtJyP7t9FzzS1GK9GOW4TJ21IYihI9zU58Rk6n3dVlwdUp+7YBpu6jOOi9bUPWPiA3O18tXtnHW9yYFpwV6YEjKVMyaX5cCf317Lb7vqwKFR8pPqPvdsEzy1N83jjCYcOSg4yjX9N4JcOb3UuvJAgo/RDV8aZMWRbrhlS/rXRV8+pRR+fko9uAbuCYx9irkZ+lGjed+0CvHMgDEOg/fD6PrMEvCseN74TMrR0B71axMOTSwdhhzSxmu5ccWMA22uSt9KnFZeCv87fZL1wkurqcPJjj6wcSts605/T1ucOEydtcF4HN1j22SbemHEpr5FmLoOTZ87YPny3e9Rm7oJno9YHyScW3nDmzipGqTDS8PKrR2/mliCU8cXwLdPl+Zktpel5KiJMzA0DNc8dBi2t/aLkojwaI8xv1EC7gm5dqZ1rNbuex/twVE7zs2eLh+YUQFr3jkd/mN+NSwbWwjTSvNgammu9ShJPuoLE9duG/KTcpM5bWyR+fi6F3x5ms9LF9tAU98gPHGoA/6+r43fJz3qT7+pD3etK0s15cfKXT+IAyPF4v1jPXWRbpigaHPBXKPu8YjQ9o/I1aPv/m18PXx4nDqLomintg8ErLxpcADetX4TtA1m6ETigNim3tVhNnTeTn0Nwq9Tj8vUez1M3QTfVmXa1LF/9H0kHWM3vMlrJTLhpWHl2jPdDfzb8WXwwQWlYnlKjiniNPcOweUPHIK2vhjPFnXloOQ3yvjYnAo2mmM5uvIWaMrb+4fgvU/v4zduSZeJxbnwX4vGwpMXTIH1l06HDZfOcDzWvnOGONlOs36YckbY+z8xO+D0r3x5yjqVwBRH4XDPAHzw5T0w+b4NcPGzO+CqF3fBiY9ugXkPb4K/7olgBjjBiuYu8Yxh6gepfFzix1E6mOIgrjpNH0aNKxfpszPlOVK4+gcR+Wrr3Nw0cwqcUYE/xH3qpLqNXd1w3aatMNrOk3eYuihzgu0UbdXByu3JZzJl6l79znO1WpIxU5diuhC5imPsmjd5NSYMYnkuQ/cR40dnVcFp45VbEZp0Io7FMGxo6oMPP3bEsBKlgSMOghFEFFfd6KGxPA+uniFdUpjAmDNrE1s/Vh3rgX959kCs0/fiom9ceQD+sd99yYuxP8VKvrCiAC4ZrzlzXAdvK0bTNMbYD262dfTB0se2wm27W6BfmYBnO6t738u74WvrDomS8AywZd+L08R65WaXW+2aUqR8X4LiFcdRZ+jHKPGK6aobYbT5iHwD5oq3hb11zgyYUJDnrTPEvO9YE/z37tEz7Sw39Y3r4BWtqWP/iD7SIdponyiXCVPX9qtAbHcSZMTUlZgOlFzdx9g9G4MPw4JNiOVZY3RFa4qjgLsVb71oLEwoZaMQsTwXjnKMk4x1345O+PbKiKaddcWXYrnqRidfXVQN+eq15S5Ym/iKJF4y7t3dDlc9uTeWywlxiZ995SD8covyOZn6lJcn8/j6cWNTH1e2NZr8TXEMoNle89IuONBjOETBloXr+7c3HoK79qU3cv/r3hbY6xHHytvZrkUV0d2QhePqHymeozxCUsWMK25kiHzTyLUuLxfumjcLirLcm2r9cp0xv7l7L9x5VLkB1AjQMjgAF6Kpu65Tx1xFvjqkNmbM1KWYLniu2MdJMjZS12HI1X2MXQcXY2OcDfJEBDQauimWgbFF2XDn2+ugKEcROpal5CjVffPlZrhra5TTzkqxHDmMfiaV5MJHZ1cY8mZt8vii3be3Ay57Yi8c643u+F3HwBBc++xe+Jl85zWvPlXWxXPqi+GiceKM/6B4xfHgvv1t8HqL5gQltiz1UNP1r+6F3V3hZgbDm7r8x9r94pWEnbezL7AMLwpYWqlc2hgWO04Cd7z4kWK68hmNiHwjyvX4kmL47ewZyUUZl+uOiZl8ZMs2WNMpHcrJMNzU1UvaEI/tDEeqy4ipK33ngNdhbzoZMVP3ypUhdsWLh4pd7m6QJ0wTlaHLHFebBz87p0a8YtjLwjhSLE0crP3oE0dg7bF0p16UYnm1x6tuFPDVRTUwmRl8EtEuH+15/EAnnHz/TniS/U2XlUe74fSHd8Bdu8XliV79xjcEou8F+WyYftOJ48SrAHjGwYczjspDB8StJBOI5enW+eb+Qbj25d3QEvAStLaBQbh8xU5u7jYijoU7FnIiM/W6fMO10EGw4yAYS4rnyCNORMxU8TKSix+kfE2kaouGy2qq4DMT2Xqu1bGYHibZMTgI79qwEY70R3wisQ/0pi7yNaH0T+ymrsRzwXN15zuipm6CtyVxHbsOLtY0yGuhgkCG7mN5MlfNKoEbF5fr80sRB0eGlz94EI71RHmNr4JX3SgCz5D/ybI68Yr1oSlvQ/mezj646LHd8IFn98Gm1uA/lnZ39sMNLx+AM/+xAza0inuP6+IjfKOlrFMIe//n59fCzFLptrSp8IyDD2WdMrC3S2wkxfKMP2QFLzd1welPbYUtHf5mhNvY3gPnP7cNXmoSP55EHAslR0cdM4GGFJf8BcI7VryIuF7xMpqPD7zySTPXb06dBG+rkq4SSnw2XssUMXf39sIVGzeZb8YUA25Tx1w98hW5ymTE1E2YtjuMyfkjYOqa/rHhdZirla/hGHvyDTZeCzXhpbHr9B3nxTeXVcFFU6RjiL7iIMOwq70f3vePQ/xyuFD4ioNo+nCUcf74YvjI7MSPJAVXexKwNklfzjt2tsGi+7bBZU/ugdt3tPLLvkzg2fV/39MG1zy7F+bduxV+vaXZutGMNg7D44uFmtNqi+Bzc6U9OGHhbcU4hlgaEnciNBq6pk2bmakvfnwz3LB6L2w1GDwa/6fX7IOlT22G11rU0YSSoyZOQVYWvH9SwKsDjHjHsjGVp0uqmKJO6ZXRh7YdwbPGjfUts2fAnCI0E6bVLlegqXu+rR0+t2OneBUvTlPHXEW+OgztiNXU+eQzolAlxXaHm/r0ETqmrsL7DnN15jtmmFH0/d3WG3QrmqbxXTdOFs/0FP6IrTzGThN/pVjdn5wqnvkHL2E76879sKHZMFp0xFfaxepuWFgO3z01uCkU/mKreCZwtVOKxeo+hMap4tIgQqetc5OTNQZqC7P59eBnNhSBfC5cEPBEuOUP7+a7xG1M+XnFkOrwWvTGsnyoYOaH89M3M7Pf0dEPm9t6nXeMMy3P9KVChKa2IAdePH8aTCjyv8v5xlcPwM1bpROJ7PiaeKzuh8ePg4/PqBYFTn685Sj8xxvKsW9TexBNrPqCXDiuogBKcrKhrX8Q1rX1wH75JDlTfh5xPjylGn62cKJ4FZ6lz26E1W1dPtsEsOLU2XB8WUTH9RkrWjvhjBUbxCsJKWayV4ahJjcHLq2TR7MavNriQQH7co3Lz4NzK8tgUanZZNZ0dMHiV9aIVwxjPCvzBSVFsGrxQv48CFu6e+DU19fws8xdeMUUdf83fTp8uC6xty56kqbucT91xKOuln2e/5i1IHpT36qcKCfjY7vDd7+PkKnnrntSPGPwfPT5Yqll7D/YZZWoGDo+pbHfpPlVaC/LnUwYY0c2t/TDGXfug9Ze6WpNR85KLKU9PzuzFj441+clUgLb2F19I8Uy9BvHpAukQRXTifI5FXnwy9Ma4KTacCvb3s5+WHY/Hss1jLZ9rPAuQmnwP4NO0uBx9YfPmQLLaoIZicPYTbGkOF7Gfoz9WJn78EbruLmpPYhdp8SKQVPEfkWtP2cONLAfDOmy9Dlh7CaUXGI3dileslek/knRN26ENqDuvKoy+PXsadDAjF7FYew+Yi4oDmfsyKMtLfCOdRv5THMcYztYvVKHl9E9NG8enFEWbNvnB8vU1/Lr1I0Yc0WGrevUM2nqXtsqROQ7kqaO2MZuyJeXilz1x9ixUtf5pnIvbA2GVRIKszyJxopc+N150mVOjmVJsQxxPv3cUVh5OMTUi65liViGOBxXneiPQBpUsH/4wUrlG1r64PyHdsNLhw2/RFMwoTgX7j9vIhthZ4sSAY8j2qZizDuMhsE1Gp2iwc/6l0vHBzZ1G748TSwlTiqqWV99c0G9WWMvT4nlFcdRF1zz1Vn1kZi6J65cNH0ZNSJeMpIU05WPhLZOaEPqHm1qhdNeWwcH+1JdfijjI2ZAzquogP+aPMljmVJMBZxz4dpNm+BAX7T3cO8eGoK3bWIj9VCmjrlapv5oxKZ+ZKAfzgtj6lLfTssrhCdnHD+yu995Pu58+Sct5Yo4jV2ptBHl1tFEj45QsZelaExxQnDR5CL4xrIqJZaI5xWHlfcODcN1jx+GviDH2x3LE7FSxElfgwrR9wZNN2vDB545EPoa8+OqCuDecydACd73m8cxLMeYt9Do6owaBtdoYmk0+PInJ46DKydrDm/4gcdRYnnmJv4a+PDUajijRtkA2cszxNJhaxBF51NzcmURfHJarXgdA454iJSnKcd0ETGTkZSYprjaOqH10iHaOmfMPT19cIPuFqkurc+YIfnshHFwVa3ucGKKmKz8EDO7T+zYLgqi4Vv798DLHcrVIgmM+WCuVr54TB1NfV6Epo58fPdm2Kaaumm7gyi5TmVm/tiM42BibpqTPqWNM198pRp6AsvYDZUcVm6bil/s5fHQ+MTCK04afHpRBVwxE1cGEcsrjqNuGLa19sE92/1ftoXHth3t8hUnQXCN3ffa5TGk8l0d/XD3LsMXywdLagvhvuUToapAGbkjpviI+GK6SKkR/SFj0OAkRb8+eTx8aHqK46hBMOYmHinAt9y6dDJMxOP8tgbbpLTLtDxHuaILoBmbnwO3nTgVsv3c1S4orjykPF110ZGYrsKK5DOmtk5ovXRIQO29R5thR7fpCgcfMb3qAvCLGdNhcUmJeIUxRVwdSsz7mppge080N4vBvQA3HzogXkl4tVPKNS5T39jTBfe0yufViD7SockVTf1xNlIfeVNPgtmbDJ3DyvW74hFWqZ3T3bQwBzy09RRJkUS64CJ+fvZYWFSLc4xbZS5cOSTze3Kf/8kbxhaKLnMtT6AtF/0RQBPE0GWePZjeRBR4Mt5TF07hJ8DZ6OIjqb4kOkJoSnOz4O4zJsG1UyK6jMvQd4lyu+99gKZ617KpUMqdSNGkiGOBGkln0iCOcktTlpMNdy+ZDuOj3gXvykOTZ4zgjGtWNBHTlY+Etk7K1ytXL622TsDKn2nV3Ro6hQ7xqgtIYVYW3DlnFtTniVk5dRjywVY+1x7N7a3XdHVC66BpvgUFZRsQl6kjj7eLmSxTbXc0uY5KU/fqV4TX6a5jF0Lths1rgRKOO0uZNCJO+nehsihkG9a/XFTPjFc9TiweNtgu0TZRdzTAde2Lagw/HlxxEBFLWydQym1TCaCxQM2w5+Vmfmksy4NnL5oKF09gIwFdrBBfEqs8uOa4ynx44fxpsLw+MSoJD9/boouDsHK77wXqJIcmFpYXwMOnTYdq3LgiqPOIY4FxpP5IpdHoynOz4e9Lp8GJFdGdtJYg2XZ/eUb1PU6AZ6HbZuW1aFedlK+XVlsntD51x/qdZ6XjSWlGHSJpEf7+CBiflwd3zJ4NebrlGUNgO9n2QndmfQiaE6autNGBZrsRp6kjhwf6XTFtPHIdtaZugrcF22m1NWnsopHqxo0j6vwyroSZq0njKB+GCfjeiJhQkgN/vrAe8hIbcEf8ZKPVumrdrmcD756umbrUEQcRsVw5SGjqeL8H1FhxhI5h3/I0TWpYn/zt7Inw4yX1UJi4lk7zxbTR5sbg5ajR6EwaBh7q/9Ssanh6+XSYWRrNl2tcoWZUy+Kb9kxNLPI/8Q3O9vb4GdNhaolBY7dV6Qu7XIOjTtKxsqnF+fD0qY1walX6P3h0jMcbj/jME/0EjThK8Cv8rnqPwy7afJL9Y8rVrGMPLx2i1DUos/s1MIPV7gI1LHd8hH22rLQUfjJtmnjFMLYF2ynaymjIjWZPz7hc1hZtPETEVIjb1JHqHMP20Jgr+27xyWdGl6kb4Z8z9q2zf631kFVamzal87nIehqE8ycbbkBhLyuZyHmTor1ZxbL6AvjRGfIJJVKjDe05e7z/HN4zrQRmV4gvpGt5IpYhDkdTx3te+rK50C4P3+/WLB8X3ZcEF/2RxkpYfcl0uHxKqT49bW4CzQrHSaFZUlMIz543Df7n+Hp+DXFUnC+P+tlijYea2AMvHTtNPTEuBXNKC2Dl2bPg2omSIYnlWWhi6XBpJB0rf3dDBbxw+iweLy7OqxU/YB25KIi6JRXFUJkb3Q/0BJ+b0sB3NTvQ5iP6SFsn8NIhJh2i0eJqeXaF8yTO8pxsWFom/fDX6Cww12G4oCrKGQIBrqurg39raPCMKdfhHoMzy0OeiKowu7CIT9zixB0zQSZMHTmrROlj42fCYLlyU5/+JjB13g7Wt4n1V4bV8W9NIEM3lUvceEKFc4NsL8+ZSGHuGP7eqLluThl8bH7iPsYMO76b6eW58M6p/kc9uDv3D+fWQ3GuvMGR2mWIo8vBshWmC6CxY2k0x1cVwEW4+zxicE75P502AZ44fwqc21BshdbmJuBfZtEfMp4aa7f7X0+bBM8snwaLKiO+OxljXlkBvBNv7cpiudZ5RMrtkzNrxBUCwShlmt8ungR3nTwVZrN4FuIzS2DqB0e5W9NYmg/3LJkOty2eClUxGKnMe8dVwyTTHgsl/y9NZ2YSAziivXnOFOuFEtNC9JG2TkJbJ/rWS6uts2Je11AL9Xnu0e4XJ433WGYy30n5+fC+sdFfxfDdKVPgbIdZYzwrpsoHx9ZBPY60IwAX/6WGxMRI5phI4pK2uE0dWVhYAueVsh/amIshn8T2ampe4eg3dd4Oli9flxSkNjq3XJ6NFw/dAhWmlufAr86rhRw0d1sj6VgZ1v3ynFqYUhbNrmOV75xSAxdPZisOj6+BlZflZ8EtzKQdtzD1wcKqfLj3wnF85je7XbgI3WI05Q5D96mxMGswlz+eOS71rUvTYFltETxwzmR4jY3gPzqzEqrzFXMRXxAthrzwB9IVk8vg8XOmwIoLZvi/p3pI/m/xBGa4yhdX6dPldaXw5dnpzcz1tvoyWHV2I/xq0UQ4KXGnNSWOjaMc+0/qQ1Z+QkUR/GHRFHjtzDlw4dh4+ydBYXYW3LFoOlSoPyCU/D8/rR4uqIlm1KfjmoZq+PncKdbhNRupj5R8HGCdq15otXWCFLrFZcXwnWn6SbpwFP7lSRPEqwTOmDiyv2NOo3tvRATksFH47Y2zYGExW+f491FUKCwtKYVvTxI/miLiuto6+CB7mGJiOR6ueLQxM6ae4JeTZsF4nVnzzwM/G4AZ+W8SU+frkgalz/nMc9qZ4hLYguQC/c4U99z+HvjMM0fhjaPSRAhseQtr8uD7p9fAaePivdgfr0//xsom+NmaFuhJXN8t2rO4Nh9uPrMOFlSF/8V6uHsQvvXaMfjTljboHJBmv0OUjkbsUaKmjmMqT2wUDFw8sQRuWloHE4sjPjM6BdilK452wQP72uEl9ndtSy+0qncwU/LGDc/8inw4hf1IOKuuGM6rL+Emkkkwxy+sOQC37G6GfmkOAxyh//vMWvjCrLGRnwz2Rls33HOgFZ462g4vN3cl505whLHK8DAA/hg4q6aU39BldsnITYqxpbMHbtywBx495jx7Gs/C/+/G8XA1M95MsK6jG76ybS88fKyF3wvf6/ugr9P1t4KxzoqHu64/3DAWvjV1MhSnWGf/fPgofHHnLtjby7Z90nJxYpkfTp8CjYXR75GSaR1k6/iunXDLkUOOG7/gvQRwOtlvTJgMJdnR7/XBSD8/vB/+a/9uPjFMAvw6XVZZA9+fON06Hp9h9vX3wkf2bIZ/tItbQ0sDkHeX18JPxzdCTU5mt59Bydn4uHgmYVhnzcZuC5IdkCDoFLDrm/pgvbhd6tzqPJibhpmGAc96f3xvF+ztGIBCtvFeMjYfThwb3cYSfzS8dKgb9nYOWBPEuDrb3YcuDB+QF3iHNrw8bVKGDd2LXZ39sK+rn5tna/8Qv9kO9jnO1IY/PCYV5UZummHB26muONYFx/oG+Ixty6qLMvIjA019T3cf7Orq4zkgOE1uGRsdTynKgwkFebHueQnDbpbv6vYu6BgYhBnFBWzUivcnyHySTf0D8FJbBxzq7YdBP98rP/hoxti8HDitvAyqTCdjacCf+qvaO2BLdzf7IZANi0qK+S74TIK3an2hvY2bbAMz1GWlwdoQFryu/eXOdtjR2wPlrO1LikuhbgQMXWVtTyc82dHM+wN/YCwvqeKj9TcDDmP3WmdZndvYbYHmSyPquj8Rbm53giAIgiCCw409haFbyNexY6HJ1B11BEEQBEFkFC8P5nXo25Z3W8buMHTJ1MnQCYIgCGJ0wj1a8W2GGLEHMHQyeoIgCIIYOQyGzmF17jOFvAydTJ0gCIIgRoYUhp7waMMxdglHuWGBBEEQBEHEB/dhb0NPoBxjl3C8mQydIAiCIEYOg6lrcO+KR0yG7jB7giAIgiAyjpcXs3KnsdtvJkMnCIIgiFGFlxfbdYnr2B1vVob7poUQBEEQBJEZTF5s+3dyQC6N2H2O0k0LJwiCIAgicyiGnkAYu09DJ1MnCIIgiJGF+7Hb0DmsLjli9zJuR7lmQQRBEARBxEsKQ094dfIYuw7pjdaCyNQJgiAIIuNwL/Y29ATSMXYJk6FrFkAQBEEQRNwopu7hx05jd7xRMnSEDJ0gCIIgRh4vP2Z1yV3xXobutRCCIAiCIOLHy4/tOvl+7GToBEEQBDE68WHoCQ8Xxu7T0L3qCIIgCILIDLYfK4NyRnLE7mXajjrnAgiCIAiCyCAGQ+ewuuQxdh0OQ0fI1AmCIAhiRLA9WW/oCb+WjrFLSG+wkH4ZOMoJgiAIgogd7r2SFydw+bVq7K43KIauiAmCIAiCyASpDT2B8xi7DRk6QRAEQYw6Unkyq1OOsZOhEwRBEMSoJIWhW/X2dew+Dd2rjiAIgiCIeEjpy0kfdx9j12ELCYIgCIIYcTSGniC5K15n3K5y9wIIgiAIgsgQti9r/FjUOUfsMiZDd5QTBEEQBBE7wrQtNANsyZu5sedkSSUOMSIZuigfGNIslCAIgiCIyBkYTngu/lX81+XZwtiLc1ipq1IsQCPqHFAWTBAEQRBELLQND7D/Uxt6Am7spfnyHnlh6IhB1NE/JJ4RBEEQBBEnbUNo7AIPQ0/UWcaei38UQ9cJRXk7GTtBEARBZIQONHaTLyew68R17CW5osQkVMoPdkm/HgiCIAiCiI2DQ33imQbbn5ODc27sNYXZekNHXOXDsLnVIwhBEARBEJGxqb9TPJPQGHoCbuzTy3L5Cwe2KIEQs7Itrf1WEUEQBEEQseIwdg9DT9RxY59VkYd/LGxRAkksyjfRiJ0gCIIgMgI3doc36w09ATf2meXM2JUKC8nQpbqXD3fDoLJcgiAIgiCiZZD58Kr+VvFKGmgncPm2PWJXd8ULsdbsAVr7h+CNYz3iFUEQBEEQcbCqrw1ahvDwt8bQNf6McGOvL8qBWjyBLoWhc0T5Uwe6rScEQRAEQcTCEz3HxDNBCn+uz8m3jB05s6EwpUCue2yf5iw9giAIgiAi49Geo9YTn/58Vn6lZOzjisQzBc3Chtm/Jw92wr5Oup6dIAiCIOJg32APPNfbbDZ0xK6z9rifnV+dNPazxrERu4zB0PEfluN9YO7Y3iZqCIIgCIKIkj927ucnz2mxPdoydOt/gHPya5LGPqMsDyYU56Q0dLnu1m1k7ARBEAQRB7d27RfPJBw+nDR0ZEpOIUxlD9vYkXdMKRHPLEyGnmBdcy88daBLvCIIgiAIIgr+0XMUNvR3iFcMxdATps4RdZcW1vGXDmO/ZkaZeCYkjgUpiLr/eUM5Y48gCIIgiLT4Vts264nDh5OGzk3dUQfw3qLx/K/D2BfXFMDcyjwYHiNMXYeyIByxv3iYLn0jCIIgiCh4prcJnuuTT5pTDB1RPHpuTgksyrUG5w5jR66anhy1O1AM3cIK87XXjiSDEQRBEAQRCvTSr7RtsV4Ij7X+F2i9GOD9xdZoHXEZ+zXM2HOyJJVhITyMqHv6YBedIU8QBEEQafLHrn3wPBux+zV0JJd59jWF48QrjbGPL86BK6eVeiwEDV2YusTnXjkMLX2D4hVBEARBEEFoHRqAL7Vu8m3oibprC8fD+OwCq4zhMnbkcwurQR60W+gNPcHhngH4wqoj4hVBEARBEEH4TOsG2D/Ya70Qpq1FqsPJ4P9fyTTrhUBr7LPK8+DSyWzUzvE2dDnA77a0wO20S54gCIIgAnFH1wH4Xedeh6dqcdQNw+WFDdCYUyxeW2iNHfl/C6tgTICz4xN8csUB2NpO92snCIIgCD/g9eofaV6T2tDteubN7IEvv1AynZfIGI39uKoCuHZ6uXgl4Vi4jDWybx8Ygiuf2gvNdLydIAiCIDxpGuqH9zS9Bh1g8EyNoSf4l+IJsCA3sXc9idHYkW+fOBYq83APPiOFoct161p64Z2P74FOZvIEQRAEQbjpHh6ES4+tgg0D0gxzCTwMHcursnPh26WzRYETT2OvLciGr59Q6zDtJG5Dl3n5WDd84Ln9MDAsJUMQBEEQBPQzb7yyaTU8jxPRyHgZOiLqvlU6C2qz8qwXCp7Gjny4sQJOqlHv/GY2dDmp+/e2wxVP7YUuGrkTBEEQBKeLjdQva1oFD/QcFiWCVIYu6k/KLYcPFU20XmhIaex42dsvTqmHohz2Vm7oSrAEUlCZB/e3wwWP7YJjvXTMnSAIgvjnpnmoHy48uhIe7JEuD3f4p9nQkeIx2fC7iuOYeWsMV5DS2JG5Fflw01LrrjEulKBJkj8CVh7rhnMf3QkbW8X1eQRBEATxT8a6/g449ciLyd3vDv9Ev5RM3eCt/1c+H+bkOO/EquLL2JH3TS+H98pnyRuCcjS76tHUlz28HX63rUWUEARBEMQ/BzhV7LIjL8CmgU7FP/0ZOvLBoonw3sLknPAmxgwzxPOU4Fnupz20EzaYRt6m3fSIlOh7p1XAd06og6rEGfcEQRAE8Rbk2FA/3Ni6Hm7t2q8YtuKXBjNPMD+3FF6sPgWKxqT2zUDGjuzt6oezHt7F/9r4NHSZqvws+OL8Wri+UTd9LUEQBEG8eUFX/BMbpf9H60Y4MixP2qbxSy8PZHXjsgrgueplMDlbOZHdQGBjR9Y098J5j+6Clv4BUaLBlCgvT4ZcWlMEX1s4Fs6uc06JRxDEW5cxY8ZAiE0PQbwpeKz3KHy1bQus6GtRvFBZ51MYOlKZlQtPVZ0M83PcE9GYCGXsyHOHu+CSJ3ZB92CQRA2hmGZJdSF8fl4tXDSu1HMRBEG8uUFTT0DmTrxVwDUZL1/7Vvu2SAwdKRyTBQ9XLoHT8qpEiT9CGzvy0L4OuObZPZa5eyZqCKHRTC3Jg2unlMPVUypgOntOEMRbDxqxE28Vtg508V3ut3bvh+3seRSGjrrCMdnw14oT4KL8saLMP2kZO/LCkS5499N79HPDBzB0G15nTW5/IhvFL68rgbPYY2l1ERRkewkJgiAIIl56hofgpb5meKL3GDzaexRe7mu1KhRjdpDS82SG+e73eypOglPzKkVZMNI2dmRtSy9c8uQuONAtjrmHOJnOKjf/ECjMzoL5Ffkwu7QAGsvyYGZJPtQV5EBJbhaU5mRBeW4EZ9h7dT4RIz5WQfps3lzQ5zVKMW9jiSQtQwPQPmw9Dg/2waaBDtg80MkvVVvd38bN3cbRd0r/pupXjXZCdgE8WLkE5gU4pq4SibEjuzv74bJndjOT7xElCqYG8vKAK5tdrtGZNAirGw6hsVB0sWkQSedbg/jUIWG1EeiSCvHMS4dEEDOJj5jGurDaNGN66ZCwWlYnMlNIrTOThjbMgAAJq0NCx8T/DNqQOl4aW0xEo/XSIZmO6aVDYo2JWFp7CQF1DkJoF+aUwT2VJ8Ikn2e/m4jM2JGewWH40upD8LPNx0QJw7NxhtApOyR4J5KhC8JqI9AlFWFjIkIbhw6JNCbCtGF1SEwxxdIVwuaKpKGNw9CRWGLifwatlw4xxOSlccS068JqI47pS4eE1aYf016Clw7RaG0CxkyAE8/cXLbA13XqqYjU2BPcvrMFPvHKAegw3fwlg4aOuEzdhyaqD8uoS1uDhM0RkbRx6BBRn1SEjYkIbVgdkrGYCNN66ZBMx2R1Um84CW2SqWMaCWuuSGhjDqvD/6LV8pKwMb10SFhtWjpEo/XSIWG1aesQS+tYQkCtTUhdaVYON/SrC8aJkvSJxdiRze298JEV++Glo12ihMEbpwmXskMMKZp0ojzQKN0uD6NBFF2UGiQSHSJpA+mQYNrkuyOI6aVDwmoj1SFpamPSiaw0xBfTSOgfEYxMGzoS8Y8BXhJCx0mZK/4XQmvXabRhdUisMRFF66VDlJgOdRwxXXVOLV7G9qvyhdCYHe08LrEZO4ILvo2N3j//+iE40iPNVCdj6hRebkjNU4MqjS6FRhsrpQZRdFFqEFedpI1Dh0QQM6kQz3zqkoRtJ5JmzMA6JE1tHDqE1YvMFMLGZIQ2yRGIyevCaqONyUu8dIhXviFiclLqEI3WS4eE1aatQ9KL6VCHjemlQzy0Vdm58JXimXBD0RTPu7SFJVZjT9DUNwhffv0g/H5HMwwlopnaYpdr0kqhCWfoiKIzaRC7LowGkXS+NUgEOiTmmEmFeOalQyKImcRHTGMd03rpkEzH9MwntVZkppBGTC+jQ8Jq49AhmY7J6/Ta4ZS54n+GuCFjptYhEWvj0CFpx0QUhwigcxFSmzVmDPxr4ST475JZ/JK2uMiIsSfY0dEH39t4FG7Z2Qz9tsNL8A4J3omBDB2x6xRdbBpE0vnWID51SFhtBLqkImxMRGgzpkNGKKaXDgmrZXUiM4XUOjNpaOMwVySWmPifQRtSx0tji4lotF46JNMxvXRIrDERS2svwUuHRBgzQS4z9CsLxsEXimfA7BS3XI2CjBp7gt1d/XDTpqPw2+3N0D04JDokeCf+0xg6ElYbsy6pCBsTEdo4dEikMRGmDatDYooplu4mtEmGbScjDnNFMh3TS4cYYvLSOGLadWG1Ecf00iFhtWnrEEtrL8FLh2i0NgFjJsjLyoIr8hvgyyUzYWbEx9G9GBFjT4Cz1d21txX+tKuZn2Tn6wMQdS5T99XxmqaadI5yn7HCaJBIdIikDaRDhNZLh4j6ZKSYY3rpkIzFRJjWS4dkOiark3pDIbVWT1gdI6y5IqGNOawO/4tWy0vCxvTSIWG1dp1GG1aHZDqmLx1iaR1LCKi1Cambm1sC7yuYAP9SOBHGZmV+avQRNXaZjW29cBsz+PsPtMP6Ns0kN6ITwx1HD6NBfH7IYTRIJDpE0gbSIcG1liKCmF46JKw2Uh2SpjYOHcN83DZsTEYc5orEEhP/M2i9dEjEMXlJ2FyRsNqUOkSj9dIhmY7pqFO0XjpEielQxxHTVWdNgT43pxTekV/Hr0fPxO52L0aNscsc7hmAJ490wFOHO+GZox2wvaMPhtSOR0ydb5eH0SA+P2RXuaQzaZBM65AIYiYV4plPXZKw7UTSjOmlQyKNiTBtWB2SQivepRA2JiOs0Y1ETF4XVhttTF7ipUO88g0Rk5NSh0SsjVWHpKd1qMPG9NIhUv3M7CI4M78azsmrhrPYoy4rX9SMPKPS2FU6B4ZgS0cvvzZ+M/u7lT2O9g1Cx8AgtPcPQcfgELQmbkJjd3yADywtDSLpfGuQCHRIzDGVaN46LWHbiQhtYB0SVptmzFA6JLVWZKaQZkwvPJfroY1Dh2Q6Jq/Ta3lpSG1qXQhsXToxNdo4dEjaMRFLay8hoM6BVF8xJhdKxmRDSVYO/1ubnQczsovZSLwYGrNLoJH9LY5ghrh4APj/EnSQ5Rs3D7EAAAAASUVORK5CYII='
logoFrase = logo_base64_frase = 'iVBORw0KGgoAAAANSUhEUgAAAWoAAAD8CAYAAABekO4JAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyNpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ4IDc5LjE2NDAzNiwgMjAxOS8wOC8xMy0wMTowNjo1NyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RTVGMUZFQjg3RjZBMTFFQkEyODg5NDE0QzBCMTFGNDUiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RTVGMUZFQjc3RjZBMTFFQkEyODg5NDE0QzBCMTFGNDUiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIxLjAgKFdpbmRvd3MpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NTEzNEE0MzU1Q0Q0MTFFQkE3MUE4NDlDNEEyQzlCMDAiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NTEzNEE0MzY1Q0Q0MTFFQkE3MUE4NDlDNEEyQzlCMDAiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7I1NyXAAAlEElEQVR42uydB5gU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'
logoBanner = logo_base64_banner = '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'
icone_login = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABHNCSVQICAgIfAhkiAAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAudJREFUSEutls1LFHEYx7+zs7rr+pKlJIUKUrnUdoiCXoQgiMJuXYIoCDx06BhI+Bd0iILOQVCXoEvhoYhArEOpRBAJSkupRazpurW+tOvuujN9n53fTNrOzK7kB8R9nn18vr/fM8/zjJpJUA2fXwFzkzBWksimk9BbuhCMnkKw47AK8Key0PIP4PVdQK8FgrUwDAOZ1Cw0mDDzGQSa2xE5f1MFexNQv93JrQDDt4FQA1AT5rGscE3ToOk1CNRtg8kbZp4OlPx++AuN3APCTY6AGxoPYC4mUIiztD54Z8guWmULBJXDh1A9CuPPlOGOt9DPaeu5VIGm6TDS35XljrdQMS8ZlFEBiasQ6y0U2QG2mDL8kcaV5vDDW6h1L4UKkkU5fODt9c4jynDHW0joPgNwVvyQ25hsnNCJPuVxx18oSiEOJPK/XW9msrTm8jzCp69DCzcqrzvVraCJ51xBwxzaEIyiyc2QoEoRGjdF+OwN6Du7VaA3nkIzKWBqAYjtBtrsw85+5A2SKOSyTL4Pelu05J7kuI3MAEc7gYOMd6NMaGkVGBgE0lmgVgcy7PJzMaDvuAr4h2uPgQejQBM3VJa9094MjPZb9no2CMmnSw8ZFOL+pIjtW13j2uPPyT1AVwvwhTd99w148gFoZGyEc22PkcQt8pC/blm2zQahO0Mswxw3isvWkag1jtVSDng5CTRQIMw4tzldYUzvfuD+ZeUgTtcVmWTsq1UuNyShfFfP00tZ6jifXstAYh69V4bCEXo7zRL4/PFmkBxy48Fx5SCOUHyeO9R/qjaF3H6Mh7dxUifSWysUZK54UhnESS1tHdiCstlIriRf0DaOUKG6RV018pzybHUbR0g6yXAa/f+RLm7lvxo2jlBPlzXZW4U8iguHlEEcod4D1k5bZoCc5u8YV09pqIvAAp9NbBdw5Zj6gpTtuhcTwJspIMU3g7B+ruRjlnUf+lS+PewsHduBi3wHXu2xbAvgD0mA+eG/SDvrAAAAAElFTkSuQmCC'
icone_senha = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAN5QTFRFAAAAD2rhDmrgAGfjDWrgBZP/DmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgDmrgANH/Cn3uDW/kCYDwBJX/AMr/BZP/BZP/BZL+Bo/8BZL/BZP/BZL+BZP/BZT/BZP/BZL/BZP/BZP/BZP/BZP/BZP/BZP/BZP/BZP/BZP/BZP/DmrgBZP/BpD8CIT0DHHmCIX0DmnfBpD9DHLmDmngDmzhBo77DW7jBZH9C3jqC3jrBpH9////ITpVHAAAADh0Uk5TAAAAAAAABhoFPajcpjs+4Ozt3jqlLi+jBNsxHuMBMuY5HQEZjdr85ODbjgGLARfW1R7hARjXAx+0FZH4AAAAAWJLR0RJhwXkfAAAAAlwSFlzAADsOAAA7DgBcSvKOAAAANhJREFUOMvV0VsTgUAYBuAsK3LMWaUcc0oUOkkJ4f//IjNxYbS73fJe7F68z+zOfktRf5dUlqZzAFsDkGcKhWIpncGBcsWqslatjjkD5Bir0WwxVruDFoDushwAHNulMYAXBB68VlQPe6Ik9QeDviSJQ4joR+OJLE9ns6kszxejmIDLsf0RZfUtoLr+BBs1BjQ9ahwn2nQNAw6ueyQBx/U81ycA/xQEJ594xflMvMK+XK8XIghv95AI7EeIe2bioLYJo6bgTlnr7+yVHeo7DdXUopiqgeh/OU+fvzby6QEVmgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOS0xMC0wOFQwOTozMzo0OCswMTowMDg/SRQAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTktMTAtMDhUMDk6MzM6NDgrMDE6MDBJYvGoAAAARnRFWHRzb2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjcuOC05IDIwMTktMDItMDEgUTE2IGh0dHA6Ly93d3cuaW1hZ2VtYWdpY2sub3JnQXviyAAAABh0RVh0VGh1bWI6OkRvY3VtZW50OjpQYWdlcwAxp/+7LwAAABh0RVh0VGh1bWI6OkltYWdlOjpoZWlnaHQANTEywNBQUQAAABd0RVh0VGh1bWI6OkltYWdlOjpXaWR0aAA1MTIcfAPcAAAAGXRFWHRUaHVtYjo6TWltZXR5cGUAaW1hZ2UvcG5nP7JWTgAAABd0RVh0VGh1bWI6Ok1UaW1lADE1NzA1MjM2Mjgxn7GAAAAAEnRFWHRUaHVtYjo6U2l6ZQA3LjdLQkId0Ly7AAAAcXRFWHRUaHVtYjo6VVJJAGZpbGU6Ly8uL3VwbG9hZHMvNTYvakljRnI0Ni8yMDcyL2ludGVybmV0X2xvY2tfbG9ja2VkX3BhZGxvY2tfcGFzc3dvcmRfc2VjdXJlX3NlY3VyaXR5X2ljb25fMTI3MDc4LnBuZwTjYQgAAAAASUVORK5CYII='


#####################
#  Telas do Tkinter #
#####################
# Inicio da Main_win
main_screen = telaTkinter()  # Nesta classe
tela = Tk()
main_screen.main_win(tela)  # Acessa este atributo da caracteristica telaTkinter()
