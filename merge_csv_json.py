import pandas as pd
import json, re

# Caminhos dos arquivos # MUDAR 
json_path = 'results2/resultados_llm.json'
csv_path = 'results2/resultados_metricas2_scopus.csv'
saida_path = 'results2/tabela_completa2_scopus.csv'

# Carregar JSON
with open(json_path, 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

# Transformar o JSON em uma lista tabular
registros = []
for modelo, entradas in dados_json.items():
    for entrada in entradas:
        registro = {
            'modelo': modelo,
            'id': entrada['id'],
            'prompt_name': entrada['prompt_name'],
            'prompt_content': entrada['prompt_content'],
            'article': entrada['article'],
            'answer': entrada['answer'],
            'execution_time': entrada['execution_time']
        }
        registros.append(registro)

df_json = pd.DataFrame(registros)

# Carregar CSV
df_csv = pd.read_csv(csv_path)

# Extrair o ID do nome do arquivo
df_csv['id'] = df_csv['arquivo'].str.extract(r'(\d+)')
df_csv['id'] = df_csv['id'].astype('Int64')
# Mesclar os dados pelo campo 'id'
df_merged = pd.merge(df_csv, df_json, on='id', how='inner')

# Reordenar colunas para melhor organização (opcional)
colunas_ordenadas = [
    'modelo', 'id', 'prompt_name', 'prompt_content', 'article', 'answer', 'execution_time',
    'arquivo', 'Encontrados dos Selecionados da revisão', 'Encontrados do Total da revisão',
    'Total da pesquisa', 'Selecionados/Total_revisao', 'Selecionados/Total_busca', 'Revisao/Total_busca', 'F1 Score'
]
df_merged = df_merged[colunas_ordenadas]
df_merged = df_merged.drop('prompt_content', axis=1)

def extract_title(text):
    match = re.search(r'title:\s*(.*?)(?:\n|$)', text)
    return match.group(1).strip() if match else ''

df_merged['article'] = df_merged['article'].apply(extract_title)

df_merged = df_merged[[
    'id',
    'arquivo',
    'modelo',
    'prompt_name',
    'Encontrados dos Selecionados da revisão',
    'Encontrados do Total da revisão',
    'Total da pesquisa',
    'Selecionados/Total_revisao',
    'Selecionados/Total_busca',
    'Revisao/Total_busca',
    'F1 Score',
    'article',
    'answer',
    'execution_time'
]]
# Salvar o resultado final
df_merged.to_csv(saida_path, index=False)
