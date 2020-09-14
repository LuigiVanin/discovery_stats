import pandas as pd
import numpy as np
from csv import writer as wt

csv_name = "Database/Result_DigiMesh.csv"

table = []

data = pd.read_csv("Database/DigiMesh/Modelo_12.csv")
data = data.replace("-", 25)


[row, col] = data.shape

for i in range(col):
    if i > 1 :
        temp = data.iloc[:, i].replace("-", 25)
        temp = temp.astype(float)
        table = table + list(temp)

stats = [12, round(np.mean(temp), 2), round(np.std(temp), 2), max(temp) ]
print(table)

with open(csv_name, "a", newline="") as csvfile:
    input_csv = wt(csvfile, delimiter=',')
    input_csv.writerow(stats)