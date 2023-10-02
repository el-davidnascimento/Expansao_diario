import psycopg2
import pandas as pd
import datetime as date


################# ACOMPANHAMENTO DE FUNIL ###############################

# Caminho do arquivo Excel
caminho_arquivo = r'G:\Meu Drive\Dados\Expansão\BASE TRATADA\Tratamento_Acompanhamento_visita.xlsx'

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansao",
    user="postgres",
    password="Multiverso@Educa"
)

# Ler os dados do arquivo Excel
dados_excel = pd.read_excel(caminho_arquivo)

# Cursor
cur = conn.cursor()

nome_tabela = 'Acompanhamento_visitas'

cur.execute("DELETE FROM acompanhamento_visitas")

# Iterar sobre as linhas do DataFrame e inserir os valores na tabela do PostgreSQL
for _, linha in dados_excel.iterrows():
    valores = tuple(linha)
    cur.execute("INSERT INTO acompanhamento_visitas VALUES (%s, %s, %s, %s, %s)", valores)

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()