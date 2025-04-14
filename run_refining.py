import json
import os
import ollama
from tqdm.auto import tqdm
from prompts import *
import winsound
import time
from pdf_reader.pdf_reader_service import extract_data
from ollama import chat
from ollama import ChatResponse
import re
ollama_client = ollama.Client(timeout=60)
print("iniciamos cliente")

def salvar_em_txt(nome_arquivo, modelo, novo_item):
    # Verifica se o arquivo já existe e carrega o conteúdo atual
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            try:
                conteudo = json.load(arquivo)
            except json.JSONDecodeError:
                conteudo = {}
    else:
        conteudo = {}

    # Garante que o modelo tenha uma lista
    if modelo not in conteudo or not isinstance(conteudo[modelo], list):
        conteudo[modelo] = []

    # Adiciona o novo item
    conteudo[modelo].append(novo_item)

    # Salva tudo novamente
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)

    print(f'Item adicionado ao modelo "{modelo}" no arquivo "{nome_arquivo}".')

def limpar_resposta(resposta):
    # Remove o conteúdo dentro das tags <think> e as próprias tags
    resposta_limpa = re.sub(r'<think>.*?</think>', '', resposta, flags=re.DOTALL)
    # Remove espaços extras e quebras de linha
    return resposta_limpa.strip()

def run_llm(model, prompt_content):
    #print("Iniciando o llm")
    #print("prompt:\n")
    #print(f'''{prompt_content}''')
    #print("\n")
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': f'''{prompt_content}''',
        },
    ])
    #print(response['message']['content'])
    return response.message.content

# Carrega o arquivo JSON com os resultados anteriores
with open("resultados_novos.json", "r", encoding="utf-8") as f:
    resultados = json.load(f)

novo_prompt = (
    "You should enhance the provided keywords to find relevant scientific topics related to them. Focus on expand the context broaden the thematic coverage without losing the connection to the original keywords. Remove keywords that are unimportant or too specific. The string doesn't need to be long to have quality. In the answer, I want just end only the final search string, with no additional answer. The provided keywords are: "
)

# Para cada modelo, cria lista de chamadas ao modelo com novo prompt
entrada_para_llm = {}

for modelo, resultados_modelo in resultados.items():
    entrada_para_llm[modelo] = []

    for item in resultados_modelo:
        entrada_para_llm[modelo].append({
            "novo_prompt": novo_prompt + item["answer"],
            "old_answer": item["answer"],
            "article": item["article"]
        })


resultados_gerais = {}

for modelo, lista_de_entradas in entrada_para_llm.items():
    print("iniciou para o modelo:")
    print(modelo)

    resultados_gerais[modelo] = []

    for el in lista_de_entradas:
        print("prompt:")
        print(el["novo_prompt"])

        inicio = time.time()
        answer = run_llm(modelo, el["novo_prompt"])
        fim = time.time()

        if modelo in ('deepseek-r1:8b', 'deepseek-r1:14b'):
            print("Limpando resposta")
            answer = limpar_resposta(answer)

        tempo_execucao = round(fim - inicio, 2)

        resultado = {
            'article': el['article'],
            'new_prompt': el["novo_prompt"],
            'old_answer': el["old_answer"],
            'new_answer': answer,
            'execution_time': tempo_execucao
        }

        resultados_gerais[modelo].append(resultado)
        salvar_em_txt("resultados_novos_refinados.json", modelo, resultado)
        print("Finalizou um prompt")

    print("Finalizou o modelo")
                

print("Classification completed.")
winsound.Beep(500, 4000)


