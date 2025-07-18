import pandas as pd

# Caminhos dos arquivos
bib_path = 'results2/resultados2_acm_new.csv' # MUDAR
scopus_path = 'results2/resultados2_scopus.csv' # MUDAR

# Carregar os dados
#df_bib = pd.read_csv(bib_path)
df_scopus = pd.read_csv(scopus_path)

total_scopus = 886
selcionados_scopus = 27

total_acm = 120
selcionados_acm = 7

# Calcular métricas conforme a tabela da imagem
def calcular_metricas(df, total, selecionados):
    
    df['Selecionados/Total_revisao'] = df['Encontrados dos Selecionados da revisão'] / selecionados # Relativo

    df['Selecionados/Total_busca'] = df['Encontrados dos Selecionados da revisão'] / df['Total da pesquisa'] # Precision
    df['Revisao/Total_busca'] = df['Encontrados do Total da revisão'] / df['Total da pesquisa'] # Coverage
    df['F1 Score'] = 2 * ( (df['Selecionados/Total_busca'] *  df['Revisao/Total_busca']) / (df['Selecionados/Total_busca'] +  df['Revisao/Total_busca']) )
    
    return df

#df_bib = calcular_metricas(df_bib, total_acm, selcionados_acm)
df_scopus = calcular_metricas(df_scopus, total_acm, selcionados_scopus)

# Arredondar para 2 casas decimais

#df_bib = df_bib.round(5)
df_scopus = df_scopus.round(5)

# Salvar resultados atualizados
#df_bib.to_csv("results2/resultados_metricas2_acm_new.csv", index=False)
df_scopus.to_csv("results2/resultados_metricas2_scopus.csv", index=False)
