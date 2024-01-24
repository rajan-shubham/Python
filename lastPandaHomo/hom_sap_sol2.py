import pandas as pd
from itertools import combinations
df = pd.read_csv('homo_sapiens.csv')
df['Entry ID'] = df['Entry ID'].fillna(method='ffill')
df['Accession Code(s)'] = df['Accession Code(s)'].apply(lambda x: str(x).split(',') if pd.notna(x) else [])
exploded_df = df.explode('Accession Code(s)').drop_duplicates()
filtered_df = exploded_df[exploded_df['Source Organism'] == 'Homo sapiens'].groupby(['Entry ID', 'Source Organism']).filter(lambda x: x['Accession Code(s)'].count() == 3)
result_df = filtered_df.groupby(['Entry ID', 'Source Organism'])['Accession Code(s)'].apply(lambda x: list(str(code) for code in x.dropna())).reset_index()
result_df.to_csv('filtered_Homo_sapience.csv', index=False)