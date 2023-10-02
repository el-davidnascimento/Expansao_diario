import psycopg2
import pandas as pd
import datetime as date


################# ACOMPANHAMENTO DE FUNIL ###############################

# Caminho do arquivo Excel
caminho_arquivo = r'G:\Meu Drive\Dados\Expansão\BASE\Acompanhamento Funil.xlsx' ## alterar
nome_aba = 'Acompanhamento visitas'
dados_excel = pd.read_excel(caminho_arquivo, sheet_name=nome_aba)

# Obter a data atual
data_atual = date.datetime.today()

dados = {
    'DATA_VISITA': dados_excel['Data visita'],
    'MEC': dados_excel['MEC Escola'],
    'NOME_ESCOLA': dados_excel['Nome da Escola'],
    'RESPONSAVEL_VISITA': dados_excel['Responsável Visita'],
    'OBSERVACOES': dados_excel['Observações'],
}

# Criar o DataFrame
df = pd.DataFrame(dados)

Tratamento_Acompanhamento_Funil = r'G:\Meu Drive\Dados\Expansão\BASE TRATADA\Tratamento_Acompanhamento_visita.xlsx'
df.to_excel(Tratamento_Acompanhamento_Funil,index=False)