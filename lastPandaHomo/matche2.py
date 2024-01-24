# import pandas as pd
# from itertools import combinations
# df = pd.read_csv('filtered_Homo_sapiens.csv')
import pandas as pd
df1 = pd.read_csv('filtered_Homo_sapiens.csv')
df2 = pd.read_csv('e_file2.csv', header=None, names=["Accession1", "Accession2"])
accession_set = set()
for _, row in df1.iterrows():
    accessions = set(row["Accession Code(s)"].split(','))
    accession_set.update(accessions)
matched_data = []
for _, row in df2.iterrows():
    if row["Accession1"] in accession_set and row["Accession2"] in accession_set:
        matched_data.append((row["Accession1"], row["Accession2"]))
matched_acc = pd.DataFrame(matched_data, columns=["Accession1", "Accession2"])
matched_acc.to_csv("matches_acc.csv", index=False, header=False)
num_lines = len(open("matches_acc.csv").readlines())
print(f"Number of lines in the new file: {num_lines}")