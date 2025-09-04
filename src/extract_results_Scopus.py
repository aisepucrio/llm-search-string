import pandas as pd
import glob
import os

# 1️. Carregar base principal
try:
    df_primary_studies = pd.read_csv('primary-studies-Papers_Scopus.csv')
    df_primary_studies = df_primary_studies[['doi', 'title', 'Selected']]  
except Exception as e:
    raise RuntimeError(f"Erro ao carregar 'primary-studies-Papers_Scopus.csv': {e}")

# 2️. Filtrar artigos selecionados
selected_articles = []
for _, artigo in df_primary_studies.iterrows():
    if artigo["Selected"] == "YES":
        selected_articles.append(artigo[['doi', 'title']].to_dict())

df_selected_articles = pd.DataFrame(selected_articles)

# 3️. Iterar sobre arquivos de resultados
folder_path = 'results2/results_scopus'  # Ajuste conforme necessário
resultados = []

for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
    # Pular arquivo principal
    if 'primary-studies.csv' in file_path:
        continue  

    file_name = os.path.basename(file_path)
    try:
        df = pd.read_csv(file_path)

        # 🔹 Validar colunas obrigatórias
        colunas_necessarias = ['DOI', 'Title']
        if not all(col in df.columns for col in colunas_necessarias):
            print(f"[AVISO] Arquivo '{file_name}' ignorado: colunas obrigatórias ausentes ({colunas_necessarias})")
            continue

        # 🔹 Processar DOI e contagens
        dois_encontrados = df['DOI'].dropna().unique()
        i = sum(pd.Series(dois_encontrados).isin(df_selected_articles['doi']))
        j = sum(pd.Series(dois_encontrados).isin(df_primary_studies['doi']))

        resultados.append((file_name, i, j, len(dois_encontrados)))
        print(f"[OK] {file_name}: {i} DOIs encontrados no gabarito")
    
    except Exception as e:
        print(f"[ERRO] Falha ao processar '{file_name}': {e}")

# 4️. Gerar DataFrame final
df_resultados = pd.DataFrame(resultados, columns=[
    "arquivo",
    "Encontrados dos Selecionados da revisão",
    "Encontrados do Total da revisão",
    "Total da pesquisa"
])

# 5️. Salvar resultado final
os.makedirs("results2", exist_ok=True)
output_path = "results2/results2_scopus.csv"
df_resultados.to_csv(output_path, index=False)
print(f"\n[INFO] Resultados consolidados salvos em: {output_path}")
