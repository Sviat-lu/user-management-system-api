import pandas as pd
import csv

xlsx_file = "userdata.xlsx"

df = pd.read_excel(xlsx_file)
csv_file = "userdata.csv"

df.to_csv(csv_file, index=False, quoting=csv.QUOTE_MINIMAL)

with open(csv_file, "r") as file:
    data = file.read()

data = data.replace('"', "")

with open(csv_file, "w") as file:
    file.write(data)
