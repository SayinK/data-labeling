#! C:\Users\emily\Documents\dataLabeling\data-labeling\myenv\Scripts\python.exe

# pip installing all the needed packages 
import pandas as pd

df = pd.read_csv('unsafe_data.csv', skiprows = lambda x: x in [0, 1, 2]) #skipping the first 3 rows
pd.options.mode.copy_on_write = True
typeNames = [] #store the used type names

df_copy = df.copy() 

i = 0
count = 0
while i < len(df_copy['Marker']):
    if(pd.isna(df_copy['Marker'][i]) or df_copy['Marker'][i] in typeNames): #checking if the row at Marker is nan
        count = count + 1
    else:
        typeNames.append(df_copy['Marker'][i]) 
        break
        #df.Marker[df.Marker == 'nan'] = typeNames[0]
        #df_copy['Marker'].replace(df_copy['Marker'][i], typeNames[0], inplace=True)
    i = i + 1

print(typeNames)
print(i)

deletingIndex = i 
#print(deletingIndex)
i = i +1

typeNameCounter = 0
while i < len(df_copy['Marker']):
    #if(pd.isna(df_copy['Marker'][i])):
    if(pd.isna(df_copy['Marker'][i])==False):
        typeNames.append(df_copy['Marker'][i]) 
        typeNameCounter = typeNameCounter + 1
        #break
    #print('in')
    df_copy.at[i,'Marker'] = typeNames[typeNameCounter]
    i = i + 1

print('i value after loop: ',i)
#print(df_copy['Marker'][i])
#print('before marker', df_copy['Marker'][i-1])
print(typeNames)
print("deleting index:",deletingIndex)
df_copy.drop(df.index[:deletingIndex], inplace=True) #delete all previous rows

print(df_copy.Marker)
print(df_copy)

#delete everything before hand
#add back in the first 3 columns (have to delete it first: tested it out)






