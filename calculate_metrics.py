import pandas as pd

# Caminhos dos arquivos
bib_path = 'results2/resultados2_acm.csv' # MUDAR
scopus_path = 'results2/resultados2_scopus.csv' # MUDAR

# Carregar os dados
df_bib = pd.read_csv(bib_path)
df_scopus = pd.read_csv(scopus_path)

total_scopus = 886
selcionados_scopus = 27

total_acm = 120
selcionados_acm = 7

# Calcular métricas conforme a tabela da imagem
def calcular_metricas(df, total, selecionados):
    df['Selecionados/Total_revisao'] = df['Encontrados dos Selecionados da revisão'] / total

    df['Selecionados/Total_busca'] = df['Encontrados dos Selecionados da revisão'] / df['Total da pesquisa']
    df['Revisao/Total_busca'] = df['Encontrados do Total da revisão'] / df['Total da pesquisa']
    df['F1 Score'] = 2 * ( (df['Selecionados/Total_busca'] *  df['Revisao/Total_busca']) / (df['Selecionados/Total_busca'] +  df['Revisao/Total_busca']) )

    return df

df_bib = calcular_metricas(df_bib, total_scopus, selcionados_scopus)
#df_scopus = calcular_metricas(df_scopus, total_acm, selcionados_acm)

# Arredondar para 2 casas decimais
colunas_metricas = ['Selecionados/Total_revisao', 'Selecionados/Total_busca', 'Revisao/Total_busca']
df_bib[colunas_metricas] = (df_bib[colunas_metricas] * 100).round(4)
#df_scopus[colunas_metricas] = (df_scopus[colunas_metricas] * 100).round(4)

# Salvar resultados atualizados
df_bib.to_csv("results2/resultados_metricas2_acm.csv", index=False)
#df_scopus.to_csv("results2/resultados_metricas2_scopus.csv", index=False)
