import psycopg2


# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="Multiverso - Expansao",
    user="postgres",
    password="Multiverso@Educa"
)

# Cursor
cur = conn.cursor()

################# ACOMPANHAMENTO DE FUNIL ###############################


# Se a tabela não existe, cria
cur.execute('''CREATE TABLE Acompanhamento_visitas (
               DATA_VISITA VARCHAR(100),
               MEC VARCHAR(500),
               NOME_ESCOLA VARCHAR(1000),
               RESPONSAVEL_VISITA VARCHAR(1000),
               OBSERVACOES VARCHAR(5000)
               );''')

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()