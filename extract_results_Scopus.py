import pandas as pd
import glob
import os

df_primary_studies = pd.read_csv('results1/results1_scopus/primary-studies.csv') # Manter
df_primary_studies = df_primary_studies[['doi', 'title', 'Selected']]  

selected_articles = []

for _, artigo in df_primary_studies.iterrows():
    if artigo["Selected"] == "YES":
        selected_articles.append(artigo[['doi', 'title']].to_dict())

df_selected_articles = pd.DataFrame(selected_articles)


folder_path = 'results2/results2_scopus'  # Mudar
resultados = []
jota = []
for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
    i=0
    j=0
    if 'primary-studies.csv' in file_path:
        continue  
    
    try:
        df = pd.read_csv(file_path)
        df = df[['DOI', 'Title']] 

        dois_encontrados = df['DOI'].dropna().unique()
        i = sum(pd.Series(dois_encontrados).isin(df_selected_articles['doi']))
        j = sum(pd.Series(dois_encontrados).isin(df_primary_studies['doi']))
        resultados.append((os.path.basename(file_path), i, j, len(dois_encontrados)))
    except Exception as e:
        print(f'Erro ao processar {file_path}: {e}')

data = [[]]
for nome_arquivo, i, j, total in resultados:
    print(f'{nome_arquivo}: {i} encontrados no gabarito')
    data.append((nome_arquivo, i, j, total))

df = pd.DataFrame(data, columns=["arquivo", "Encontrados dos Selecionados da revisão", "Encontrados do Total da revisão", "Total da pesquisa"])

df.to_csv("results2/resultados2_scopus.csv", index=False)

