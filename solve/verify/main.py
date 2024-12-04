#!/usr/bin/python3

import pandas as pd
import re

# Função para remover a extensão e o sufixo '_p*' do nome
def processar_filename_basic(filename):
    # Remover a extensão (tudo após o primeiro ponto)
    nome_sem_extensao = re.sub(r'\..*$', '', filename)
    return nome_sem_extensao

def processar_filename_del_p(filename):
    # Remover a extensão (tudo após o primeiro ponto)
    nome_sem_extensao = re.sub(r'\..*$', '', filename)
    # Remover o sufixo '_p*' (ex: '_p0', '_p1', etc.)
    nome_processado = re.sub(r'_p\d+$', '', nome_sem_extensao)
    return nome_processado
    
def comparar_csvs_same(arquivo1, arquivo2):
    # Carregar os arquivos CSV
    df1 = pd.read_csv(arquivo1)
    df2 = pd.read_csv(arquivo2)
    

    
    # Processar os filenames dos dois arquivos
    filenames1 = set(df1['filename'].apply(processar_filename_basic))
    filenames2 = set(df2['filename'].apply(processar_filename_basic))
    
    # Calcular a interseção entre os dois sets
    comum = filenames1 & filenames2
    
    # Resultados
    print(f"Quantidade de elementos únicos no arquivo 1: {len(filenames1)}")
    print(f"Quantidade de elementos únicos no arquivo 2: {len(filenames2)}")
    print(f"Quantidade de elementos em comum: {len(comum)}")
    return filenames1, filenames2, comum
    
def comparar_csvs_source_vs_basic(arquivo1, arquivo2):
    # Carregar os arquivos CSV
    df1 = pd.read_csv(arquivo1)
    df2 = pd.read_csv(arquivo2)
    

    
    # Processar os filenames dos dois arquivos
    filenames1 = set(df1['filename'].apply(processar_filename_basic))
    filenames2 = set(df2['filename'].apply(processar_filename_del_p))
    
    # Calcular a interseção entre os dois sets
    comum = filenames1 & filenames2
    
    # Resultados
    print(f"Quantidade de elementos únicos no arquivo 1: {len(filenames1)}")
    print(f"Quantidade de elementos únicos no arquivo 2: {len(filenames2)}")
    print(f"Quantidade de elementos em comum: {len(comum)}")
    return filenames1, filenames2, comum

################################################################################

FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/test_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train_refface.csv'
set1,set2,comum = comparar_csvs_same(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/test_refface.csv'
set1,set2,comum = comparar_csvs_same(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/test_refface.csv'
set1,set2,comum = comparar_csvs_same(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/test_refface.csv'
set1,set2,comum = comparar_csvs_same(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/test_refface.csv'
set1,set2,comum = comparar_csvs_same(FILE1,FILE2)
print(len(comum)/len(set1|set2))


################################################################################

FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/test_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/train_refface.csv'
set1,set2,comum = comparar_csvs_source_vs_basic(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/test_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/train_refface.csv'
set1,set2,comum = comparar_csvs_source_vs_basic(FILE1,FILE2)
print(len(comum)/len(set1|set2))


FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-BODY/test_refface.csv'
set1,set2,comum = comparar_csvs_source_vs_basic(FILE1,FILE2)
print(len(comum)/len(set1|set2))
print(comum)

FILE1='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024-SOURCE/train_refface.csv'
FILE2='/mnt/8811f502-ae19-4dd8-8371-f1915178f581/Fernando/DATASET/TESE/BER/BER2024/BER2024-FACE/test_refface.csv'
set1,set2,comum = comparar_csvs_source_vs_basic(FILE1,FILE2)
print(len(comum)/len(set1|set2))
print(comum)





