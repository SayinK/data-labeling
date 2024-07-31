#while i < len(df_copy['Marker']):
    #if(pd.isna(df_copy['Marker'][i])):
    #print('in')
    #df_copy.at[i,'Marker'] = typeNames[typeNameCounter]
    #if df['Marker][i] is no longer na, then append new marker name, and change the typeNameCounter (add one)
    #if(pd.isna(df_copy['Marker'][i+1])==False):
        #typeNames.append(df_copy['Marker'][i+1]) 
        #typeNameCounter = typeNameCounter + 1
        #break
    #if(i == 2612):
        #break
    #i = i + 1

#! C:\Users\emily\Documents\dataLabeling\data-labeling\myenv\Scripts\python.exe
import pandas as pd

df = pd.read_csv('unsafe_data.csv')
print(df.columns)