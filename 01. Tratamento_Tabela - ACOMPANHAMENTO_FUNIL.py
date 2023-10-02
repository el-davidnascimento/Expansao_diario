import psycopg2
import pandas as pd
import datetime as date


################# ACOMPANHAMENTO DE FUNIL ###############################

# Caminho do arquivo Excel
caminho_arquivo = r'G:\Meu Drive\Dados\Expansão\BASE\Acompanhamento Funil.xlsx' ## alterar
nome_aba = 'Lista escolas'
dados_excel = pd.read_excel(caminho_arquivo, sheet_name=nome_aba)

# Obter a data atual
data_atual = date.datetime.today()

dados = {
    'MEC': dados_excel['MEC'],
    'NOME_ESCOLA': dados_excel['NOME ESCOLA'],
    'NOME_FANTASIA': dados_excel['NOME FANTASIA'],
    'LISTA_LINCE': dados_excel['Lista Lince'],
    'LISTA_CLAUDETE': dados_excel['Lista Claudete'],
    'CLUSTER': dados_excel['CLUSTER'],
    'ZONA': dados_excel['Zona'],
    'APPROACH': dados_excel['Approach'],
    'VISITADA': dados_excel['Visitada'],
    'QTDE_VISITAS': dados_excel['Qtd visitas'],
    'DATA_PRIMEIRA_VISITA': dados_excel['Data primeira visita'].fillna('nulo', inplace=True),
    'DATA_ULTIMA_VISITA': dados_excel['Data última visita'].fillna('nulo', inplace=True),
    'STATUS_FUNIL': dados_excel['Status funil'],
    'MOTIVOS_DA_PERDA': dados_excel['Motivos da perda'],
    'INTERESSE_MULTIVERSO': dados_excel['Interesse Multiverso'],
    'INTERESSE_ESCOLA': dados_excel['Interesse Escola'],
    'SCORE_LOCALIZACAO': dados_excel['Score Localização'],
    'SCORE_ALUNOS': dados_excel['Score Alunos'],
    'SCORE_TICKET': dados_excel['Score Ticket'],
    'SCORE_SAUDE_FINANCEIRA': dados_excel['Score Saúde Financeira'],
    'SCORE_NECESSIDADE_DE_INFRA': dados_excel['Score de Infra'],
    'SCORE_POTENCIAL_DE_CRESCIMENTO': dados_excel['Score Potencial de Crescimento'],
    'SCORE_TOTAL': dados_excel['Score Total'],
    'BAIRRO': dados_excel['BAIRRO'],
    'PREDIO_ESCOLAR': dados_excel['Prédio Escolar'],
    'SEGMENTOS': dados_excel['Segmentos'],
    'SALAS': dados_excel['# Salas'],
    'SOCIOS': dados_excel['Sócios'],
    'REGIME_TRIBUTARIO': dados_excel['Regime Tributário'],
    'CNPJ_ESCOLA': dados_excel['CNPJ Escola'],
    'CNPJ_MATRIZ': dados_excel['CNPJ Matriz'],
    'ALUNOS_TOTAL': dados_excel['ALUNOS TOTAL'],
    'ALUNOS_EI': dados_excel['Alunos EI'],
    'ALUNOS_EF1': dados_excel['Alunos EF1'],
    'ALUNOS_EF2': dados_excel['Alunos EF2'],
    'ALUNOS_EM': dados_excel['Alunos EM'],
    'CAGR': dados_excel['CAGR 10-22'],
    'ALUNOS_2010': dados_excel['Alunos 2010'],
    'TURMAS_EI': dados_excel['Turmas EI'],
    'TURMAS_EF1': dados_excel['Turmas EF1'],
    'TURMAS_EF2': dados_excel['Turmas EF2'],
    'TURMAS_EM': dados_excel['Turmas EM'],
    'ALUNOS_EI_TURMAS_EI': dados_excel['Alunos/Turma EI'],
    'ALUNOS_EF1_TURMAS_EF1': dados_excel['Alunos/Turma EF1'],
    'ALUNOS_EF2_TURMAS_EF2': dados_excel['Alunos/Turma EF2'],
    'ALUNOS_EM_TURMAS_EM': dados_excel['Alunos/Turma EM'],
    'PAIS_NIVEL_SUPERIOR_COMPLETO': dados_excel['% Pais Nível Super. Completo'],
    'PAIS_RENDA_FAMILIA_B2_E_C1': dados_excel['% Pais Renda Familiar B2 e C1'],
    'ENEM_TOTAL_2019': dados_excel['ENEM Total 2019'],
    'QUANTIDADE_DOCENTES': dados_excel['Quantidade Docentes'],
    'PISCINA': dados_excel['Piscina? (1= sim)'],
    'QUADRA_DESCOBERTA': dados_excel['Quadra Descoberta?'],
    'QUADRA_COBERTA': dados_excel['Quadra Coberta?'],
    'TELEFONE': dados_excel['Telefone'],
    'ENDEREÇO': dados_excel['Endereço'],
    'NUMERO': dados_excel['Número'],
    'CEP': dados_excel['CEP'],
    'DATA_INSERT': data_atual,
    'POTENCIAL_DE_CRESCIMENTO': dados_excel['% Potencial de crescimento'],
    'FATURAMENTO_ESTIMADO_GARANTIDORA': dados_excel['Faturamento estimado (Garantidora)'],
    'FATURAMENTO_MEDIO_ANUAL': dados_excel['Faturamento médio anual'],
    'FATURAMENTO_MEDIO_VALUATION': dados_excel['Faturamento médio Valuation'],
    'CLUSTER_500': dados_excel['Cluster 500'],
    'QTDE_DE_UNIDADES': dados_excel['Qtde de unidades'],
    'QTDE_DE_ALUNOS_REGULAR': dados_excel['Qtde de alunos regular'],
    'QTDE_DE_TURMAS': dados_excel['Qtde de turmas'],
    'TICKET_MEDIO': dados_excel['Ticket médio'],
    'AVALIACAO_DO_IMOVEL': dados_excel['Avaliação do imovel'],
    'AREA_CONTRUIDA': dados_excel['AREA CONSTRUIDA'],
    'VALOR_DA_PROPOSTA': dados_excel['VALOR DA PROPOSTA'],
    'QTDE_DE_PROPOSTAS_REALIZADAS': dados_excel['QTDE DE PROPOSTAS REALIZADAS'],
    'AREA_TOTAL': dados_excel['AREA TOTAL'],
    'INTEGRAL_S_N': dados_excel['INTEGRAL (S / N?)'],
    'QTDE_DE_ALUNOS_INTEGRAL': dados_excel['QTDE DE ALUNOS INTEGRAL'],
    'VALOR_DO_M2': dados_excel['VALOR DO M2'],
    'VALOR_DO_M2_CONSTRUIDO': dados_excel['VALOR DO M2 CONSTRUIDO'],
    'DIVIDA': dados_excel['DIVIDA'],
    'PROPOSTA_ACEITA_S_N': dados_excel['PROPOSTA ACEITA? (S /N)'],
    'FATURAMENTO_SCORE_CARD': dados_excel['Faturamento ScoreCard'],
}

# Criar o DataFrame
df = pd.DataFrame(dados)

Tratamento_Acompanhamento_Funil = r'G:\Meu Drive\Dados\Expansão\BASE TRATADA\Tratamento_Acompanhamento_Funil.xlsx'
df.to_excel(Tratamento_Acompanhamento_Funil,index=False)