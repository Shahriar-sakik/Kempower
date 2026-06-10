import pandas as pd

chunks = []

for chunk in pd.read_csv(r"C:\Users\Md Shahriar\Documents\Kempower\public_passenger_dataset.csv", chunksize=100000):
    chunks.append(chunk[["country", "EVModel"]].value_counts())

result = pd.concat(chunks).groupby(level=[0, 1]).sum().sort_values(ascending=False)

for country in ["Norway", "Finland", "United Kingdom", "Sweden", "France", "Portugal", "Belgium", "Denmark", "Latvia"]:
    print("\n", country)
    print(result[country].head(5))
