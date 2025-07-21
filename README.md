# Supplementary Material — Comparing LLMs and Proposing an ML-Based Approach for Search String Generation in Systematic Literature Reviews

This repository contains the scripts, data, and notebooks used as supplementary material for the article that evaluates the use of Large Language Models (LLMs) for generating search strings in Systematic Literature Reviews (SLRs).

The purpose of this file is to explain the project structure and how to reproduce the study. It is important to note that the implementation was developed in stages, so the scripts must be executed in a specific sequence. Additionally, file names in the code may need to be adjusted to match your context. The proper execution order is described in the **How to Reproduce** section.

This artifact is available on Zenodo [zenodo.org/records/15984173](https://zenodo.org/records/15984173)

Access the full paper: [Comparing LLMs and Proposing an ML Based Approach for Search String Generation in Systematic Literature Reviews.pdf](https://github.com/user-attachments/files/21347421/Comparing.LLMs.and.Proposing.an.ML.Based.Approach.for.Search.String.Generation.in.Systematic.Literature.Reviews.pdf)


---

## 📁 Project Structure
```
├── pdf_reader/ # Scripts for reading and extracting content from PDF seed articles
├── results2/ # Results explicitly referenced in the article’s main table
│ ├── results_acm/ # Articles retrieved from ACM using LLM-generated search strings
│ ├── results_scopus/ # Raw results from Scopus, manually processed for the article’s final table (tabela.csv)
│ ├── metrics_acm/ # Processed ACM results for final table (dados_para_tabela.csv)
│ ├── metrics_scopus/ # Processed Scopus results for final table (dados_para_tabela.csv)
│
├── calculate_metrics.py # Script for computing evaluation metrics
├── extract_results_acm.py # Extracts results from 'results_acm/' folder
├── extract_results_Scopus.py# Extracts results from 'results_scopus/' folder
├── limpa_strings.py # Cleans LLM outputs and writes each search string line-by-line in a .txt file
├── merge_csv_json.py # Merges evaluation metrics with corresponding LLM metadata
├── plotMetrics.ipynb # Notebook to generate visual plots from the results
├── prompts.py # Contains all prompts (from both results1 and results2) and metadata of the articles used
├── run_llm.py # Runs LLMs using the prompts and seed articles defined in 'prompts.py'
```

---

## ▶️ How to Reproduce

1. **Run `pip install -r requirements.txt`

2. **Run `run_llm.py`**  
   This generates the file `resultados_llm.json`.
   
3. **Run `limpa_strings.py`**  
   It cleans and formats the LLM outputs from  `limpa_strings.py` into `resultados_llm_limpos.txt`, with each generated search string on a separate line. This makes the next manual step easier.

5. **Manually run the search queries**  
   Use the cleaned strings to manually query academic databases (ACM, Scopus). Save the resulting articles in:
   - `results_acm/`
   - `results_scopus/`
   You can export the results from a querry in those academic databases.

6. **Extract search results**  
   Run:
   `python extract_results_acm.py`
   `python extract_results_Scopus.py`

These generate:
    - `resultados2_acm.csv`
    - `resultados2_scopus.csv`
from the `results_acm/` and `results_scopus/`
   
5. **Compute evaluation metrics**
Run:
`python calculate_metrics.py`

This produces:
    - `resultados_metricas2_acm.csv`
    - `resultados_metricas2_scopus.csv`
from  `resultados2_acm.csv` and `resultados2_scopus.csv`

6. **Merge with LLM metadata for final table**
Run:
    - `python merge_csv_json.py`

This outputs the final completed results:
    - `tabela_completa2_acm.csv`
    - `tabela_completa2_scopus.csv`

📎 Citation
Comparing LLMs and Proposing an ML-Based Approach for Search String Generation in Systematic Literature Reviews
Authors anonymized
SBES-IIER 2025
