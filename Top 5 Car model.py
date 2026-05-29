import pandas as pd

# 1. Location of the main datasheet 
raw_big_file = r"C:\Users\Md Shahriar\Desktop\project\public_passenger_dataset.csv"

# 2. List of the country
my_countries = [
    "denmark", "norway", "sweden", "finland", "france", 
    "united kingdom", "portugal", "latvia", "belgium"
]

print("Scanning the dataset to aggregate car frequencies by country...")

country_fleet_counts = {country: {} for country in my_countries}

for chunk in pd.read_csv(raw_big_file, chunksize=200000, usecols=['country', 'evModel']):

    chunk = chunk.dropna(subset=['country', 'evModel'])
    
    chunk['country'] = chunk['country'].astype(str).str.strip().str.lower()
    chunk['evModel'] = chunk['evModel'].astype(str).str.strip()
    
    filtered_chunk = chunk[chunk['country'].isin(my_countries)]
    
    for country, group in filtered_chunk.groupby('country'):
        for model, row_count in group['evModel'].value_counts().items():
            # Add the chunk counts to the master accumulator dictionary
            country_fleet_counts[country][model] = country_fleet_counts[country].get(model, 0) + row_count

print("\n" + "="*60)
print("             TOP 5 EV MODELS BY COUNTRY WITH COUNTS")
print("="*60)

for country in my_countries:
    print(f"\nCountry: {country.upper()}")
    
    sorted_fleet = sorted(country_fleet_counts[country].items(), key=lambda x: x[1], reverse=True)
    
    # Extract only the top 5 models
    top_5_models = sorted_fleet[:5]
    
    for rank, (model, total_count) in enumerate(top_5_models, 1):
        print(f"  [{rank}] {model:<30} -> Count: {total_count:,} rows")
        
    print("-" * 60)

print("\nFleet analysis task complete.")