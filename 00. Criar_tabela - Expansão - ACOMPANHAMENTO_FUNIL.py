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
cur.execute('''CREATE TABLE Acompanhamento_funil (
               MEC VARCHAR(1000),
               NOME_ESCOLA VARCHAR(2000),
               NOME_FANTASIA VARCHAR(1000),
               LISTA_LINCE VARCHAR(10),
               LISTA_CLAUDETE VARCHAR(10),
               CLUSTER VARCHAR(300),
               ZONA VARCHAR(200),
               APPROACH VARCHAR(100),
               VISITADA VARCHAR(10),
               QTDE_VISITAS VARCHAR(100),
               DATA_PRIMEIRA_VISITA VARCHAR(100),
               DATA_ULTIMA_VISITA VARCHAR(100),
               STATUS_FUNIL VARCHAR(1000),
               MOTIVOS_DA_PERDA VARCHAR(2000),
               INTERESSE_MULTIVERSO VARCHAR(100),
               INTERESSE_ESCOLA VARCHAR(100),
               SCORE_LOCALIZACAO VARCHAR(100),
               SCORE_ALUNOS VARCHAR(100),
               SCORE_TICKET VARCHAR(100),
               SCORE_SAUDE_FINANCEIRA VARCHAR(100),
               SCORE_NECESSIDADE_DE_INFRA VARCHAR(100),
               SCORE_POTENCIAL_DE_CRESCIMENTO VARCHAR(100),
               SCORE_TOTAL VARCHAR(2000),
               BAIRRO VARCHAR(1000),
               PREDIO_ESCOLAR VARCHAR(100),
               SEGMENTOS VARCHAR(100),
               SALAS VARCHAR(100),
               SOCIOS VARCHAR(1000),
               REGIME_TRIBUTARIO VARCHAR(1000),
               CNPJ_ESCOLA VARCHAR(1000),
               CNPJ_MATRIZ VARCHAR(1000),
               ALUNOS_TOTAL VARCHAR(1000),
               ALUNOS_EI VARCHAR(500),
               ALUNOS_EF1 VARCHAR(500),
               ALUNOS_EF2 VARCHAR(500),
               ALUNOS_EM VARCHAR(500),
               CAGR VARCHAR(200),
               ALUNOS_2010 VARCHAR(500),
               TURMAS_EI VARCHAR(500),
               TURMAS_EF1 VARCHAR(500),
               TURMAS_EF2 VARCHAR(500),
               TURMAS_EM VARCHAR(500),
               ALUNOS_EI_TURMAS_EI VARCHAR(100),
               ALUNOS_EF1_TURMAS_EF1 VARCHAR(100),
               ALUNOS_EF2_TURMAS_EF2 VARCHAR(100),
               ALUNOS_EM_TURMAS_EM VARCHAR(100),
               PAIS_NIVEL_SUPERIOR_COMPLETO VARCHAR(100),
               PAIS_RENDA_FAMILIA_B2_E_C1 VARCHAR(100),
               ENEM_TOTAL_2019 VARCHAR(100),
               QUANTIDADE_DOCENTES VARCHAR(500),
               PISCINA VARCHAR(100),
               QUADRA_DESCOBERTA VARCHAR(100),
               QUADRA_COBERTA VARCHAR(100),
               TELEFONE VARCHAR(500),
               ENDEREÇO VARCHAR(1000),
               NUMERO VARCHAR(100),
               CEP VARCHAR(100),
               DATA_INSERT VARCHAR(100),
               POTENCIAL_DE_CRESCIMENTO VARCHAR(100),
               FATURAMENTO_ESTIMADO_GARANTIDORA VARCHAR(1000),
               FATURAMENTO_MEDIO_ANUAL VARCHAR(1000),
               FATURAMENTO_MEDIO_VALUATION VARCHAR(1000),
               CLUSTER_500 VARCHAR(1000),
               QTDE_DE_UNIDADES VARCHAR(500),
               QTDE_DE_ALUNOS_REGULAR VARCHAR(500),
               QTDE_DE_TURMAS VARCHAR(500),
               TICKET_MEDIO VARCHAR(2000),
               AVALIACAO_DO_IMOVEL VARCHAR(2000),
               AREA_CONTRUIDA VARCHAR(1000),
               VALOR_DA_PROPOSTA VARCHAR(2000),
               QTDE_DE_PROPOSTAS_REALIZADAS VARCHAR(100),
               AREA_TOTAL VARCHAR(2000),
               INTEGRAL_S_N VARCHAR(100),
               QTDE_DE_ALUNOS_INTEGRAL VARCHAR(500),
               VALOR_DO_M2 VARCHAR(1000),
               VALOR_DO_M2_CONSTRUIDO VARCHAR(1000),
               DIVIDA VARCHAR(2000),
               PROPOSTA_ACEITA_S_N VARCHAR(100),
               FATURAMENTO_SCORE_CARD VARCHAR(1000)
               );''')

# Commit e fechamento da conexão
conn.commit()
cur.close()
conn.close()