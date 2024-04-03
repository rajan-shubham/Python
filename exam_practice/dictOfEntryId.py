#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./homo_sapiens.csv')
df['Entry ID'] = df['Entry ID'].fillna(method= 'ffill')
#df['Entry ID'] = df['Entry ID'].ffill

homo_df = df[df['Source Organism'] == 'Homo sapiens']
print(homo_df)

mydict = {'Entry ID':homo_df['Entry ID'],
          'Species':homo_df['Source Organism'],
          'Accession Code(s)':homo_df['Accession Code(s)']}

# mydict = {
#     'Entry_ID': homo_df['Entry ID'].tolist(),
#     'Species': homo_df['Source Organism'].tolist(),
#     'Accession_Codes': homo_df['Accession Code(s)'].tolist()
# }

print(mydict)