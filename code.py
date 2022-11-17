# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:16:14 2022

@author: gcangemi
"""
import pandas as pd
dt_rettificato = pd.read_excel(r"C:\Project\AAA\RwoH.xlsx")
#dt_rettificato.columns = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

print(len(dt_rettificato.columns)) #output: 15 (15 colonne - da "a" -> "o")
len_df = len(dt_rettificato.columns)

df_alf = pd.read_excel(r"C:\Project\AAA\array.xlsx")
print(len(df_alf))
len_alf = len(df_alf)
        
letters = list()        
for i, row in df_alf.iterrows():
    if i+1 <= len_df:
        letters.append(row["list"])  
        
dt_rettificato.columns = letters    





















