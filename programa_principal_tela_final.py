from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x500+200+153')
root.title("TreeView Banco De Dados Text")
root.configure(bg="#003153")

# =====Frames=====
# Frame Esquerdo
left_Frame = Frame(root, width=100, height=200, bg='#C0C0C0', relief='raised', highlightthickness=2, highlightbackground="#0fe3ee")
left_Frame.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)
# Frame Direito
right_Frame = Frame(root, width=400, height=300, bg='#C0C0C0', relief='raised', highlightthickness=2, highlightbackground="#0fe3ee")
right_Frame.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.45)

btn_novo_msg = Button(text="Limpar",font=('Arial',10,'italic', 'bold'),command="")
btn_novo_msg.place(relx=0.1, rely=0.04, relheight=0.05, relwidth=0.074)
btn_novo_msg = Button(text="Deletar",font=('Arial',10,'italic', 'bold'),command="")
btn_novo_msg.place(relx=0.2, rely=0.04, relheight=0.05, relwidth=0.074)
btn_novo_msg = Button(text="Alterar",font=('Arial',10,'italic', 'bold'),command="")
btn_novo_msg.place(relx=0.5, rely=0.04, relheight=0.05, relwidth=0.074)
btn_novo_msg = Button(text="Buscar",font=('Arial',10,'italic', 'bold'),command="")
btn_novo_msg.place(relx=0.6, rely=0.04, relheight=0.05, relwidth=0.074)

bt_nfuncionario_lebel = Label(text="NOME FUNCIONARIO",font=('Arial',10,'italic', 'bold'),bg="#C0C0C0", highlightthickness=2, highlightbackground="#003153")
bt_nfuncionario_lebel.place(relx=0.07, rely=0.22, relheight=0.03, relwidth=0.2)

btn_nfuncionario_btn = Button(text="Adicionar",font=('Arial',10,'italic', 'bold'),command="")
btn_nfuncionario_btn.place(relx=0.068, rely=0.37, relheight=0.05, relwidth=0.1)

bt_nfuncionario_lebel = Entry(left_Frame,font=('Arial',10,'italic'))
bt_nfuncionario_lebel.place(relx=0.05, rely=0.50, relheight=0.08, relwidth=0.3)
# DATA
bt_data_lebel = Label(text="DATA NASCIMENTO",bg="#C0C0C0",font=('Arial',10,'italic', 'bold'),highlightthickness=2, highlightbackground="#003153")
bt_data_lebel.place(relx=0.07, rely=0.30, relheight=0.03, relwidth=0.2)

bt_data_lebel = Entry(left_Frame,font=('Arial',10,'italic'))
bt_data_lebel.place(relx=0.05, rely=0.67, relheight=0.08, relwidth=0.2)


btn_trazer_valores_cx_laranja = Button(left_Frame, text='Mostrar Valores R$')
btn_trazer_valores_cx_laranja.place(relx=0.604, rely=0.31, relheight=0.09, relwidth=0.25)
#CX_LARANJA LABEL
bt_cx_laranja_lebel_recebe_valor = Label(left_Frame,font=('Arial',8,'italic'))
bt_cx_laranja_lebel_recebe_valor.place(relx=0.83, rely=0.42, relheight=0.07, relwidth=0.1)
# CX_LARANJA_LABEL
bt_cx_laranja = Label(text="VALOR CX LARANJA",bg="#C0C0C0",font=('Arial',8,'italic', 'bold'),highlightthickness=2, highlightbackground="#003153")
bt_cx_laranja.place(relx=0.6, rely=0.22, relheight=0.03, relwidth=0.2)

#CX_LIMAO LABEL
bt_cx_limao_lebel_recebe_valor = Label(left_Frame,font=('Arial',8,'italic'))
bt_cx_limao_lebel_recebe_valor.place(relx=0.83, rely=0.51, relheight=0.07, relwidth=0.1)
# CX_LIMAO_LABEL
bt_cx_limao = Label(text="VALOR CX LIMAO",bg="#C0C0C0",font=('Arial',8,'italic', 'bold'),highlightthickness=2, highlightbackground="#003153")
bt_cx_limao.place(relx=0.6, rely=0.26, relheight=0.03, relwidth=0.2)

#CX_TOMATE LABEL
bt_cx_tomate_lebel_recebe_valor = Label(left_Frame,font=('Arial',8,'italic'))
bt_cx_tomate_lebel_recebe_valor.place(relx=0.83, rely=0.60, relheight=0.07, relwidth=0.1)
# CX_TOMATE_LABEL
bt_cx_tomate = Label(text="VALOR CX TOMATE",bg="#C0C0C0",font=('Arial',8,'italic', 'bold'),highlightthickness=2, highlightbackground="#003153")
bt_cx_tomate.place(relx=0.6, rely=0.30, relheight=0.03, relwidth=0.2)
# btn_novo_btn
# btn_novo_btn




tree = ttk.Treeview(right_Frame, height=2, columns=["col1", "col2", "col3","col4","col5"])
tree.place(width=668, height=220) # (relx=-0.040, rely=-0.015, relheight=1, relwidth=1.2,height=3)
tree.heading("#0", text="ID")
tree.heading("#1", text="Nome Funcionario")
tree.heading("#2", text="Data Nascimento")
tree.heading("#3", text="CX Laranja")
tree.heading("#4", text="CX Limao")
tree.heading("#5", text="CX Tomate")
tree.column("#0", width=1)
tree.column("1", width=125) # Nome Funcionario
tree.column("2", width=25) # Data Nascimento
tree.column("#3", width=25) # Laranja
tree.column("#4", width=25) # Limao
tree.column("#5", width=25) # Tomate



root.mainloop()