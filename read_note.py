import pandas as pd
import os

df = pd.read_excel('clinical_note.xlsx')

for index, row in df.iterrows():
    file_name = f"data/result_{index+1}.txt"
    with open(file_name, 'w') as file:
        file.write(str(row['result']))

