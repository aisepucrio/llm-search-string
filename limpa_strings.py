import json

with open('resultados_novos.json', 'r', encoding='utf-8') as f:
    resultados_refinados = json.load(f)


i = 0
final = []
for chave, lista_execucoes in resultados_refinados.items():
    for execucao in lista_execucoes:
        string_suja = execucao["answer"]
        execucao["id"] = i
        print(string_suja) 
        string_limpa = string_suja.replace("\\", "")
        #string_limpa = string_suja.replace("\"", "\'")
        print(string_limpa)
        execucao["answer"] = string_limpa
        final.append(string_limpa + "\n")
        i = i + 1


with open('resultados_novos_refinados_limpos.txt', 'w', encoding='utf-8') as f:
    for el in final:
        f.write(el)
print(f"Foram um total de {i} execuções")