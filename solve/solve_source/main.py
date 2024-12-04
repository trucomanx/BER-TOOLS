#!/usr/bin/python3

import pandas as pd
import re
import json
from collections import Counter


def processar_filename_del_p(filename):
    # Remover a extensão (tudo após o primeiro ponto)
    nome_sem_extensao = re.sub(r'\..*$', '', filename)
    # Remover o sufixo '_p*' (ex: '_p0', '_p1', etc.)
    nome_processado = re.sub(r'_p\d+$', '', nome_sem_extensao)
    return nome_processado
    
def carregar_data(arquivo1):
    df1 = pd.read_csv(arquivo1)

    filenames = df1['filename'].apply(processar_filename_del_p).to_list()
    
    resp = [ base+'.png' for base in filenames ]
    
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


FILE='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train_refface.csv'

BASE='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/labels.csv'


filenames=carregar_data(FILE)

df_base = pd.read_csv(BASE)

df_encontrados, df_nao_encontrados=dividir_dataframe_por_filenames(df_base, filenames)

print(len(df_encontrados))
print(len(df_nao_encontrados))


df_encontrados.to_csv('train_refface.csv', index=False)
df_nao_encontrados.to_csv('test_refface.csv', index=False)

salvar_contagem_json_pandas(df_encontrados,'label', 'train_refface.csv.json')
salvar_contagem_json_pandas(df_nao_encontrados,'label', 'test_refface.csv.json')


