from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def run():
    df = pd.read_csv(f"{DATA_DIR}/students.csv")
    print(df)

    name_series = df["Name"]
    print(name_series)
    
    # use df.notna() to get the opposite result, shows where a value is missing but harder to read
    missing_values = df.isna().sum()

    print(missing_values)

    # test to see if we can get the invalid/missing value
    for col_value in missing_values:
        if col_value != 0:
                print(col_value)

    # replace value in the in menory Copy of the data
    # NOTE: fillna() casts int as floats
    df["Score"] = df["Score"].fillna(0)
    df["Score"] = df["Score"].astype(int)

    print(df["Score"])
    print(df.isna().sum())

    df.to_csv(f"{DATA_DIR}/clean_data.csv", index=False)


if __name__ == "__main__":
    run()