#!/usr/bin/python3

from collections import Counter
import pandas as pd
import json

def move_grouped_files(df1, df2):
    # Extrair prefixos dos nomes dos arquivos
    df1['prefix'] = df1['filename'].str.extract(r'(.*)_p[0-9]+\.png')
    df2['prefix'] = df2['filename'].str.extract(r'(.*)_p[0-9]+\.png')
    
    # Encontrar os prefixos presentes em ambos os DataFrames
    common_prefixes = set(df1['prefix']).intersection(set(df2['prefix']))
    
    # Para cada prefixo comum, mover as linhas de df2 para df1
    for prefix in common_prefixes:
        rows_to_move = df2[df2['prefix'] == prefix]
        df1 = pd.concat([df1, rows_to_move], ignore_index=True)
        df2 = df2[df2['prefix'] != prefix]
    
    # Remover a coluna auxiliar "prefix"
    df1.drop(columns=['prefix'], inplace=True)
    df2.drop(columns=['prefix'], inplace=True)
    
    return df1, df2

def salvar_contagem_json_pandas(df_base, coluna, caminho_arquivo):
    # Contar a frequência dos elementos na coluna 'label'
    contagem = Counter(df_base[coluna])
    #print(contagem)
    with open(caminho_arquivo, 'w') as json_file:
        json.dump(dict(contagem), json_file, indent=4, sort_keys=True)
    
    print(f"Contagem salva em {caminho_arquivo}")
    
    
    
arquivo1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train.csv'
arquivo2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/test.csv'


df1 = pd.read_csv(arquivo1)
df2 = pd.read_csv(arquivo2)

print(len(df1),len(df2),len(df1)+len(df2))

df1, df2 = move_grouped_files(df1, df2)

print(len(df1),len(df2),len(df1)+len(df2))


df1.to_csv('train_refface.csv', index=False)
df2.to_csv('test_refface.csv', index=False)

salvar_contagem_json_pandas(df1,'label', 'train_refface.csv.json')
salvar_contagem_json_pandas(df2,'label', 'test_refface.csv.json')

