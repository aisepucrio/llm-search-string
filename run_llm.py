import json
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

models = ['deepseek-r1:8b', 'llama3.1:8b']

def salvar_em_txt(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:  # 'w' para sobrescrever e salvar o JSON
        json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)
    print(f'Conteúdo salvo no arquivo "{nome_arquivo}".')

def limpar_resposta(resposta):
    # Remove o conteúdo dentro das tags <think> e as próprias tags
    resposta_limpa = re.sub(r'<think>.*?</think>', '', resposta, flags=re.DOTALL)
    # Remove espaços extras e quebras de linha
    return resposta_limpa.strip()

def run_llm(model, prompt_content, articleData):
    print("Iniciando o llm")
    print("prompt:\n")
    print(f'''{prompt_content}\n{articleData}''')
    print("\n")
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': f'''{prompt_content}\n{articleData}''',
        },
    ])
    print(response['message']['content'])
    return response.message.content

def main(models):
    resultados = {}

    for model in models:
        resultados[model] = []

        for prompt_name, prompt_content in prompts.items():
            for article in articles:
                inicio = time.time()
                answer = run_llm(model, prompt_content, article)
                fim = time.time()

                tempo_execucao = round(fim - inicio, 2)

                if model == 'deepseek-r1:8b':
                    print("Limpando resposta")
                    answer = limpar_resposta(answer)

                resultado = {
                    'prompt_name': prompt_name,
                    'prompt_content': prompt_content,
                    'article': article,
                    'answer': answer,
                    'execution_time': tempo_execucao
                }

                resultados[model].append(resultado)

    salvar_em_txt("resultados_llm.json", resultados)
            

    print("Classification completed.")
    winsound.Beep(500, 5000)

if __name__ == '__main__':
    winsound.Beep(500, 1000)
    main(models)
