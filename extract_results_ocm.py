# Recarregando bibliotecas e reexecutando o código após o reset do ambiente
import pandas as pd
import glob
import os
import bibtexparser

# Caminho para os arquivos .bib
folder_path = 'results2/results2_acm'  # MUDAR

# Lê o gabarito
gabarito_path = 'results1/results1_ocm/primary-studies_Papers_ACM.csv' # Pode manter
df_primary_studies = pd.read_csv(gabarito_path)
df_primary_studies = df_primary_studies[['doi', 'title', 'Selected']]

# Seleciona apenas os artigos marcados como "YES"
selected_articles = []
for _, artigo in df_primary_studies.iterrows():
    if artigo["Selected"] == "YES":
        selected_articles.append(artigo[['doi', 'title']].to_dict())

df_selected_articles = pd.DataFrame(selected_articles)

# Processa os arquivos .bib
resultados = []

for file_path in glob.glob(os.path.join(folder_path, '*.bib')):
    i = 0
    j = 0
    dois_encontrados = []

    try:
        with open(file_path, 'r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)

        for entry in bib_database.entries:
            doi = entry.get('doi')
            if doi:
                dois_encontrados.append(doi)

        # Remove duplicatas e valores nulos
        dois_encontrados = pd.Series(list(set(dois_encontrados))).dropna()

        i = sum(dois_encontrados.isin(df_selected_articles['doi']))
        j = sum(dois_encontrados.isin(df_primary_studies['doi']))
        resultados.append((os.path.basename(file_path), i, j, len(dois_encontrados)))

    except Exception as e:
        print(f'Erro ao processar {file_path}: {e}')

# Monta o DataFrame final
data = []
for nome_arquivo, i, j, total in resultados:
    print(f'{nome_arquivo}: {i} encontrados no gabarito')
    data.append((nome_arquivo, i, j, total))

df_result = pd.DataFrame(data, columns=["arquivo", "Encontrados dos Selecionados da revisão", "Encontrados do Total da revisão", "Total da pesquisa"])
output_path = "results2/resultados2_acm.csv"
df_result.to_csv(output_path, index=False)

df_result.head()
