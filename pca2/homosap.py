import pandas as pd
data = pd.read_csv('homo_sapiens.csv')
data = data.ffill()
# Define the condition for filtering
mask = (data['Source Organism'] == 'Homo sapiens') & (data['Accession Code'] == 3)
# Apply the mask to get the required data
filtered_data = data[mask]