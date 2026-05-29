import pandas as pd

# 1. Define the files (Change these paths if your file names are different)
raw_big_file = r"C:\Users\Md Shahriar\Desktop\project\public_passenger_dataset.csv"
output_small_file = r"C:\Users\Md Shahriar\Desktop\project\filtered_europe_data.csv"

# 2. List the 9 countries you want to keep
my_countries = [
    "denmark", "norway", "sweden", "finland", "france", 
    "united kingdom", "portugal", "latvia", "belgium"
]

print("Starting to filter... Please wait.")

# 3. Read and filter the data in small chunks (groups of 100,000 rows at a time)
is_first_chunk = True

for chunk in pd.read_csv(raw_big_file, chunksize=100000):
    # Clean up the country text (remove blank spaces and make it lowercase)
    chunk['country'] = chunk['country'].astype(str).str.strip().str.lower()
    
    # Keep only the rows matching our 9 countries
    filtered_chunk = chunk[chunk['country'].isin(my_countries)]
    
    # Save the filtered rows to a new CSV file
    if is_first_chunk:
        filtered_chunk.to_csv(output_small_file, index=False, mode='w')
        is_first_chunk = False
    else:
        filtered_chunk.to_csv(output_small_file, index=False, mode='a', header=False)

print(f"Done! Your clean, smaller dataset is saved at: {output_small_file}")