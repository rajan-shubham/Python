import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./homo_sapiens.csv')

df['Entry ID'] = df['Entry ID'].fillna(method='ffill')

# Uncomment the next line if you want to print the filtered dataframe
# print(df)

homo_df = df[df['Species'] == 'Homo sapiens']
print(homo_df)

mydict = {
    'Entry_ID': homo_df['Entry ID'],
    'Species': homo_df['Species'],
    'Accession_Codes': homo_df['Accession Codes']
}

print(mydict)

# or we can write this
# mydict = {
#     'Entry_ID': homo_df['Entry ID'].tolist(),
#     'Species': homo_df['Species'].tolist(),
#     'Accession_Codes': homo_df['Accession Codes'].tolist()
# }