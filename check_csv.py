import pandas as pd

files = [
    "data/tenant1.csv",
    "data/tenant2.csv",
    "data/tenant3.csv"
]

for file in files:
    print(f"\nChecking {file}")
    data = pd.read_csv(file)
    print(data.head())
    print("Rows:", len(data))