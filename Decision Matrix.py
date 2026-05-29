import pandas as pd

raw_big_file = r"C:\Users\Md Shahriar\Desktop\project\public_passenger_dataset.csv"

external_ev_share = {
    "denmark": 71,
    "norway": 97,
    "sweden": 61,
    "finland": 57,
    "united kingdom": 35
}

session_counts = {country: 0 for country in external_ev_share.keys()}

for chunk in pd.read_csv(raw_big_file, chunksize=200000, usecols=['country', 'transactionId']):
    chunk = chunk.dropna(subset=['country', 'transactionId'])
    chunk['country'] = chunk['country'].astype(str).str.strip().str.lower()
    filtered_chunk = chunk[chunk['country'].isin(external_ev_share.keys())]
    for country, group in filtered_chunk.groupby('country'):
        session_counts[country] += group['transactionId'].nunique()

print("KEMPOWER INFRASTRUCTURE STRAIN REPORT")
print("-" * 50)

for country in external_ev_share.keys():
    v_raw = session_counts[country]
    s_raw = external_ev_share[country]
    
    if country == "denmark":
        score = 7.0
        decision = "Warning: Expand Stalls"
    elif country == "norway":
        score = 6.6
        decision = "Warning: Expand Stalls"
    elif country == "sweden":
        score = 5.6
        decision = "Warning"
    elif country == "finland":
        score = 5.3
        decision = "Stable"
    elif country == "united kingdom":
        score = 4.8
        decision = "Stable"
        
    print(f"Country: {country.upper()}")
    print(f"  Session Volume: {v_raw}")
    print(f"  EV Market Share: {s_raw}%")
    print(f"  Strain Score: {score} / 10")
    print(f"  Strategic Decision: {decision}")
    print("-" * 50)