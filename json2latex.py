#!/usr/bin/python

import json

def json_to_latex_table(json_path,caption='Resumo da base de dados',label='tab:dataset_summary'):
    # Lê o arquivo JSON
    with open(json_path, 'r') as file:
        data = json.load(file)
    TOTAL=sum(data.values());
    
    # Cria o cabeçalho da tabela
    latex_table  = "\\begin{table}[h!]\n"
    latex_table += "\\centering\n"
    latex_table += "\\begin{tabular}{r|l|l}\n"
    latex_table += "\\hline\n"
    latex_table += "Categoria & Quantidade & Porcentagem \\\\\n"
    latex_table += "\\hline\n"
    latex_table += "\\hline\n"
    
    # Adiciona as linhas da tabela
    for category, count in data.items():
        percent= 100*float(count)/TOTAL;
        str_p=f"{percent:.2f}\\%";
        latex_table += category+" & "+str(count)+" & "+str_p+" \\\\\n"
        latex_table += "\\hline\n"
    latex_table += "\\hline\n"
    latex_table += "Total & "+str(TOTAL)+" & 100\\% \\\\\n"
    
    # Finaliza a tabela
    latex_table += "\\end{tabular}\n"
    latex_table += "\\caption{"+caption+"}\n"
    latex_table += "\\label{"+label+"}\n"
    latex_table += "\\end{table}"
    
    return latex_table

################################################################################

# Source
json_path = '../BER2024-SOURCE/labels.csv.json'
latex_table = json_to_latex_table(  json_path,
                                    caption='Resumo da base de dados BER2024',
                                    label='tab:BER2024:source')
print('\n')
print(latex_table)
print('\n')

for dname in ['Body', 'Face', 'Skeleton']:
    for mtype in ['train', 'test']:
        json_path = '../BER2024/BER2024-'+dname.upper()+'/'+mtype+'.csv.json'
        latex_table = json_to_latex_table(  json_path,
                                            caption='Resumo da base de dados BER2024-'+dname+' '+mtype,
                                            label='tab:BER2024-'+dname.upper()+':'+mtype)
        print('\n')
        print(latex_table)
