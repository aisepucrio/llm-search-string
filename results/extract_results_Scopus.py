import pandas as pd
import bibtexparser

# Incluir base e ano

# 1. Lê o CSV do Scopus
df_Scopus = pd.read_csv('results/scopus.csv')
df1 = df_Scopus[['DOI', 'Title']]

# 2. Lê o arquivo .bib da ACM
with open('results/acm.bib', encoding='utf-8') as bib_file:
    bib_database = bibtexparser.load(bib_file)

# Extrai DOI e Title dos registros BibTeX
acm_entries = bib_database.entries
acm_data = [{'DOI': entry.get('ID'), 'Title': entry.get('title')} for entry in acm_entries]

# Cria o DataFrame do ACM
df2 = pd.DataFrame(acm_data)

# 3. Junta os dois DataFrames
df_combined = pd.concat([df1, df2], ignore_index=True)

# 4. Remove duplicatas por DOI
df_combined = df_combined.drop_duplicates(subset='DOI')

# 5. Salva o resultado
df_combined.to_csv('combined_result.csv', index=False)
