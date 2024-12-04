#!/usr/bin/python3

import pandas as pd
import re
import json
from collections import Counter


def carregar_data(arquivo1):
    df1 = pd.read_csv(arquivo1)

    resp = df1['filename'].to_list()
    
    return resp

def dividir_dataframe_por_filenames(df_base, filenames):
    # Cria uma máscara booleana onde True representa os valores em 'filename' que estão em 'filenames'
    mascara = df_base['filename'].isin(filenames)
    
    # DataFrame com os elementos encontrados em filenames
    df_encontrados = df_base[mascara].reset_index(drop=True)
    
    # DataFrame com os elementos que não estão em filenames
    df_nao_encontrados = df_base[~mascara].reset_index(drop=True)
    
    # Exibe os resultados
    print(f"DataFrame com elementos encontrados em 'filenames' ({len(df_encontrados)} linhas):")
    #print(df_encontrados)
    
    print(f"DataFrame com elementos não encontrados em 'filenames' ({len(df_nao_encontrados)} linhas):")
    #print(df_nao_encontrados)
    
    # Retorna os dois DataFrames com índices reiniciados
    return df_encontrados, df_nao_encontrados

def salvar_contagem_json_pandas(df_base, coluna, caminho_arquivo):
    # Contar a frequência dos elementos na coluna 'label'
    contagem = Counter(df_base[coluna])
    #print(contagem)
    with open(caminho_arquivo, 'w') as json_file:
        json.dump(dict(contagem), json_file, indent=4, sort_keys=True)
    
    print(f"Contagem salva em {caminho_arquivo}")

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

FILE='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train_refface.csv'

BASE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/train.csv'
BASE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/test.csv'

filenames=carregar_data(FILE)

df_base1 = pd.read_csv(BASE1)
df_base2 = pd.read_csv(BASE2)
df_base = pd.concat([df_base1, df_base2], ignore_index=True)
df_base = df_base.reset_index(drop=True)


df_encontrados, df_nao_encontrados=dividir_dataframe_por_filenames(df_base, filenames)


print(len(df_encontrados))
print(len(df_nao_encontrados))


df_encontrados, df_nao_encontrados = move_grouped_files(df_encontrados, df_nao_encontrados)

print(len(df_encontrados))
print(len(df_nao_encontrados))


df_encontrados.to_csv('train_refface.csv', index=False)
df_nao_encontrados.to_csv('test_refface.csv', index=False)

salvar_contagem_json_pandas(df_encontrados,'label', 'train_refface.csv.json')
salvar_contagem_json_pandas(df_nao_encontrados,'label', 'test_refface.csv.json')


