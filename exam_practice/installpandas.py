import pandas as pd
print("hello")
df = pd.read_csv('homo_sapiens.csv')
print(df.head())
print(type(df))
print(df.shape)
print(df.columns)
source_organism = df['Source Organism']
print(source_organism.head())
subset = df[['Entry ID', 'Source Organism', 'Accession Code(s)']]
print(subset.head())
print(subset.tail())
print(df.loc[0])
print(df.loc[99])
#print(df.loc[-1]) # ValueError: -1 is not in range
print(df.tail(n=1))
subset_loc = df.loc[0]
subset_head = df.head(n=1)
print(type(subset_loc))
print(type(subset_head))
print(subset_loc)
print(subset_head)
print(df.loc[[0, 99, 999]])
print(df.iloc[0])