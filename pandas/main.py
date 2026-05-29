from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def run():
    df = pd.read_csv(f"{DATA_DIR}/students.csv")
    print(df)

    name_series = df["Name"]
    print(name_series)

    print(df["Score"].mean())

if __name__ == "__main__":
    run()