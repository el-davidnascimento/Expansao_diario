import psycopg2
import pandas as pd


################# TRAKING ###############################

# Caminho do arquivo Excel
caminho_arquivo = r'C:\Users\Public\Acompanhamento Funil.xlsx'

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansão",
    user="postgres",
    password="Multiverso@Educa"
)

# Ler os dados do arquivo Excel
dados_excel = pd.read_excel(caminho_arquivo)

# Cursor
cur = conn.cursor()

nome_tabela = 'Acompanhamento_funil'

# Iterar sobre as linhas do DataFrame e inserir os valores na tabela do PostgreSQL
for _, linha in dados_excel.iterrows():
    valores = tuple(linha)
    cur.execute("INSERT INTO acompanhamento_funil VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", valores)


# Executar o comando DELETE para remover registros duplicados
#cur.execute("""
#    DELETE FROM acompanhamento_funil
#    WHERE (mec, status_funil, data_insert) NOT IN (
#      SELECT mec, status_funil, MAX(data_insert)
#      FROM acompanhamento_funil
#      GROUP BY mec, status_funil, Setor
#    )
#""")


# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()