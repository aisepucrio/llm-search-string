import os
import xml.etree.ElementTree as ET
import subprocess
import shutil

import os

def apagar_nao_pdfs(pasta):
    for item in os.listdir(pasta):
        caminho = os.path.join(pasta, item)
        if os.path.isfile(caminho):
            if not item.lower().endswith('.pdf'):
                os.remove(caminho)
        elif os.path.isdir(caminho):
            shutil.rmtree(caminho)

def run_cermine(input_path, cermine_version="1.13"):
    print("Starting pdf processing with CERMINE...")
    # Construindo o comando com o caminho correto
    command = [
        "java",
        "-cp",
        f"pdf_reader/cermine-impl-{cermine_version}-jar-with-dependencies.jar",
        "pl.edu.icm.cermine.ContentExtractor",
        "-path",
        input_path,
    ]

    # Executa o comando Java e captura a saída
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("CERMINE output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o CERMINE:", e.stderr)

def extract_title_and_abstract_from_xml(path_to_article):
    print("Extracting title and abstract from XML...")
    try:
        # Carrega o XML
        tree = ET.parse(path_to_article)
        root = tree.getroot()

        # Procura pela tag <article-title>
        title_element = root.find('.//article-title')
        title_text = title_element.text.strip() if title_element is not None else "Título não encontrado"

        # Procura pela tag <abstract>
        abstract_element = root.find('.//abstract')
        if abstract_element is not None:
            # Concatena o texto dos parágrafos dentro do abstract
            abstract_text = ''.join([p.text or "" for p in abstract_element.findall('p')]).strip()
        else:
            abstract_text = "Resumo não encontrado"

        return title_text, abstract_text

    except Exception as e:
        print(f"Erro ao processar o arquivo '{os.path.basename(path_to_article)}': {e}")
        return "Erro ao processar título", "Erro ao processar resumo"

def process_all_xml_in_folder(input_folder):
    # Verifica se a pasta existe
    if not os.path.exists(input_folder):
        print(f"A pasta '{input_folder}' não existe.")
        return

    all_data = []
    # Itera sobre todos os arquivos XML na pasta
    for filename in os.listdir(input_folder):
        if filename.endswith(".cermxml"):
            input_file = os.path.join(input_folder, filename)
            title, abstract = extract_title_and_abstract_from_xml(input_file)
            all_data.append((filename, title, abstract))

    return all_data

def extract_data(path):
    run_cermine(path)
    # Executa a função para processar todos os XMLs na pasta
    data = process_all_xml_in_folder(path)
    return data

if __name__ == "__main__":
    input_folder = "pdf_reader/article"
    data = extract_data(input_folder)
    print(data)
    for filename, title, abstract in data:
        print(data)
    apagar_nao_pdfs(input_folder)
