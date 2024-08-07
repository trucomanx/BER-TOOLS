#!/usr/bin/python

import pandas as pd
import json
from collections import OrderedDict

def csv_to_json_summary(csv_path, json_path):
    # Lê o arquivo CSV
    df = pd.read_csv(csv_path)
    
    # Conta a quantidade de elementos por categoria
    category_counts = df['label'].value_counts().to_dict()
    
    # Ordena o dicionário por chave
    ordered_counts = OrderedDict(sorted(category_counts.items()))
    
    # Salva o resultado em um arquivo JSON
    with open(json_path, 'w') as json_file:
        json.dump(ordered_counts, json_file, indent=4)
    
    return dict(ordered_counts)


# SRC
csv_path = '../BER2024-SOURCE/test.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntest=sum(json_summary.values())
print(' SRC-test :',json_summary,Ntest)

csv_path = '../BER2024-SOURCE/train.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntrain=sum(json_summary.values())
print(' SRC-train:',json_summary,Ntrain)

print(Ntest+Ntrain)

# Body
csv_path = '../BER2024/BER2024-BODY/test.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntest=sum(json_summary.values())
print('BODY-test :',json_summary,Ntest)

csv_path = '../BER2024/BER2024-BODY/train.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntrain=sum(json_summary.values())
print('BODY-train:',json_summary,Ntrain)

print(Ntest+Ntrain)

# Face
csv_path = '../BER2024/BER2024-FACE/test.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntest=sum(json_summary.values())
print('FACE-test :',json_summary,Ntest)

csv_path = '../BER2024/BER2024-FACE/train.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntrain=sum(json_summary.values())
print('FACE-train:',json_summary,Ntrain)

print(Ntest+Ntrain)

# Skel
csv_path = '../BER2024/BER2024-SKELETON/test.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntest=sum(json_summary.values())
print('SKEL-test :',json_summary,Ntest)

csv_path = '../BER2024/BER2024-SKELETON/train.csv'
json_summary = csv_to_json_summary(csv_path, csv_path+'.json')
Ntrain=sum(json_summary.values())
print('SKEL-train:',json_summary,Ntrain)

print(Ntest+Ntrain)
