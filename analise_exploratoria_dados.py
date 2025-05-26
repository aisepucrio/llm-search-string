import pandas as pd

# Lê o arquivo CSV original
df = pd.read_csv("results2/tabela_completa2_scopus.csv")

# Seleção das colunas necessárias
colunas = ["modelo", "prompt_name", "Encontrados dos Selecionados da revisão", "Selecionados/Total_revisao", "F1 Score", "Selecionados/Total_busca", "Revisao/Total_busca", "article"]
df_filtrado = df[colunas].copy()

# Remover valores ausentes
df_filtrado.dropna(subset=["Selecionados/Total_revisao", "F1 Score"], inplace=True)

# Top 10 por 'F1 Score'
top10_f1 = df_filtrado.sort_values(by="F1 Score", ascending=False)
top10_f1.to_csv("results2/metrics_scopus/scopus_top10_f1_score.csv", index=False)

# Bottom 10 por 'F1 Score'
bottom10_f1 = df_filtrado.sort_values(by="F1 Score", ascending=True)
bottom10_f1.to_csv("results2/metrics_scopus/scopus_bottom10_f1_score.csv", index=False)
