import pandas as pd
import numpy as np
from csv import writer as wt

csv_name = "Database/Result_ZigBee.csv"

table = []

data = pd.read_csv("Database/ZigBee/Modelo_04.csv")
data = data.replace("-", 25)


[row, col] = data.shape

for i in range(col):
    if i > 1 :
        temp = data.iloc[:, i].replace("-", 25)
        temp = temp.astype(float)
        table = table + list(temp)

stats = [1, round(np.mean(table), 2), round(np.std(table), 2), max(table) ]
print(table)

with open(csv_name, "a", newline="") as csvfile:
    input_csv = wt(csvfile, delimiter=',')
    input_csv.writerow(stats)