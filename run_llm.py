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

models = ['gemma3:12b', 'mistral-nemo:latest', 'llama3.1:latest']

def salvar_em_txt(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo: 
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

    response: ChatResponse = chat(
        model=model,
        messages=[
            {
                'role': 'system',
                'content': (
                    "You are an expert in systematic literature reviews. Your task is to generate a single, precise, and comprehensive Boolean search string based on the title and abstract of a scientific article. "
                    "Use Boolean operators (AND, OR) to combine concepts, expand terms with synonyms and related expressions, and avoid any explanations or commentary. It's important to broaden the scope. "
                    "Return only the final search string in the expected format. You will have instructions."
                )
            },
            {
                'role': 'user',
                'content': f"{prompt_content}\n{articleData}"
            },
        ],
        options={
        "temperature": 0.2
    }
    )

    print(response['message']['content'])
    return response.message.content

def main(models):
    resultados = {}
    i = 0
    for model in models:
        resultados[model] = []

        for prompt_name, prompt_content in prompts.items():
            for article in new_articles:
                inicio = time.time()
                answer = run_llm(model, prompt_content, article)
                fim = time.time()

                tempo_execucao = round(fim - inicio, 2)

                resultado = {
                    'id': i,
                    'prompt_name': prompt_name,
                    'prompt_content': prompt_content,
                    'article': article,
                    'answer': answer,
                    'execution_time': tempo_execucao
                }

                resultados[model].append(resultado)
                i = i + 1

    salvar_em_txt("results2/resultados_llm.json", resultados) # mudar
            

    print("Classification completed.")
    winsound.Beep(500, 4000)

if __name__ == '__main__':
    winsound.Beep(500, 1000)
    main(models)
