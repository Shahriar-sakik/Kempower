import pandas as pd

# read the file in chunks of 100000 rows at a time
chunks = []
for chunk in pd.read_csv(r"C:\Users\Md Shahriar\Documents\Kempower\public_passenger_dataset.csv", chunksize=100000):
    chunks.append(chunk["country"].value_counts())

# combine all chunks and add them up
sessions = pd.concat(chunks).groupby(level=0).sum()

print(sessions)
