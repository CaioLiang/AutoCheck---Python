from conexaoBD import *

conn = conecta_banco()
cursor = conn.cursor()

query = 'SELECT * from TB_ALUNO'
cursor.execute(query)
tabela = cursor.fetchall()