import json
import ollama
from tqdm.auto import tqdm
from prompts import *
import winsound
import time
from pdf_reader.pdf_reader_service import extract_data
from ollama import chat
from ollama import ChatResponse

ollama_client = ollama.Client(timeout=60)
print("iniciamos cliente")

models = ['deepseek-r1:14b']

#inicioExtraction = time.time()
#data = extract_data("pdf_reader/article")          
#fimExtraction = time.time()
#print(f"Tempo de execução llama: {fimExtraction - inicioExtraction:.2f} segundos")

#titulo = data[0][1]
#resumo = data[0][2]

def salvar_em_txt(nome_arquivo, conteudo):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(conteudo + '\n')  # adiciona uma quebra de linha no final
    print(f'Conteúdo adicionado ao arquivo "{nome_arquivo}".')

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
    print(response.message.content)
    return response.message.content


def main(models):
    for model in models:
        for prompt, prompt_content in prompts.items():
            for article in articles:
                inicio = time.time()
                answer = run_llm(model, prompt_content, article)
                fim = time.time()
                print(f"Tempo de execução llama: {fim - inicio:.2f} segundos")
                save = prompt_content + '\n' + article + '\n' + "Answer:" + answer + '\n' + f"Tempo de execução llama: {fim - inicio:.2f} segundos" + "\n"
                salvar_em_txt("log_deepseek14b.txt", save)
                

    print("Classification completed.")
    winsound.Beep(500, 5000)  

if __name__ == '__main__':
    winsound.Beep(500, 1000)  
    main(models)
