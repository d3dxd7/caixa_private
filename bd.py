import pyodbc

'''Host Name 
DESKTOP-MMITH5A
{}
'''
# Cores
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

# class banco_dados:
#     def dados_conexao(self):
#         self.dados_conect = (
#             "Driver = {SQL Server};"
#             "Server=DESKTOP-MMITH5A;"
#             "DataBase=PythonSQL;"
#         )
#     def conectar(self):
#         self.conexao = pyodbc.connect(self.dados_conexao())
#         self.cursor = self.conexao
#         print('Conexao bem sucedida')
#     def desconectar_banco(self):
#         self.cursor.close()
#
#     def montarTable(self):
#         self.conectar()
#         self.inserir_dados = """(
#         INSERT INTO Clientes(
#         id_usuario,
#         nome_usuario,
#         senha))"""
#         self.cursor.execute(self.inserir_dados)
#         self.cursor.commit()
#         self.desconectar_banco(); print(f'{GREEN}Banco de Dados Desconectado')




# conectar = banco_dados()
# print(conectar)

dados_conexao1 = (
            "Driver={SQL Server};"
            "Server=DESKTOP-MMITH5A;"
            "DataBase=PythonSQL;"
        )

conectar = pyodbc.connect(dados_conexao1)
print(f'{CYAN}Conectado com Sucesso!')

cursor = conectar.cursor()
comando_inserir = """
        INSERT INTO Clientes (id_usuario,  nome_usuario,senha)  
        VALUES (2, 'Teste2', 'senha123')"""
cursor.execute(comando_inserir); print(f'{GREEN}Dados Inseridos no Banco') # Executa os dados no banco
# cursor.commit() # Serve para validar Alterar Atualizar dados do Banco