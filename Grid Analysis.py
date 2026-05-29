import pandas as pd

raw_big_file = r"C:\Users\Md Shahriar\Desktop\project\public_passenger_dataset.csv"

my_countries = [
    "denmark", "norway", "sweden", "finland", "france", 
    "united kingdom", "portugal", "latvia", "belgium"
]

country_data = {c: {"power_sum": 0.0, "peak_power": 0.0, "rows": 0} for c in my_countries}

for chunk in pd.read_csv(raw_big_file, chunksize=200000, usecols=["country", "avgCurrentA", "avgVoltageV"]):
    chunk = chunk.dropna(subset=["country", "avgCurrentA", "avgVoltageV"])
    chunk["country"] = chunk["country"].astype(str).str.strip().str.lower()
    
    filtered_chunk = chunk[chunk["country"].isin(my_countries)]
    filtered_chunk["kw"] = (filtered_chunk["avgVoltageV"] * filtered_chunk["avgCurrentA"]) / 1000.0
    
    for country, group in filtered_chunk.groupby("country"):
        country_data[country]["power_sum"] += group["kw"].sum()
        country_data[country]["rows"] += len(group)
        
        local_max = group["kw"].max()
        if local_max > country_data[country]["peak_power"]:
            country_data[country]["peak_power"] = local_max

print("GRID TELEMETRY ANALYSIS")
print("-" * 50)

for country in my_countries:
    stats = country_data[country]
    if stats["rows"] > 0:
        avg_kw = stats["power_sum"] / stats["rows"]
        peak_kw = stats["peak_power"]
        total_mwh = (stats["power_sum"] * 10) / 3600 / 1000
        
        print(f"Country: {country.upper()}")
        print(f"  Average Delivery: {avg_kw:.2f} kW")
        print(f"  Peak Load: {peak_kw:.2f} kW")
        print(f"  Total Energy: {total_mwh:.2f} MWh")
        print("-" * 50)