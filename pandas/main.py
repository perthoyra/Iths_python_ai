from pathlib import Path
import pandas as pd

def set_globals():

    globals()["BASE_DIR"] = Path(__file__).resolve().parent
    globals()["DATA_DIR"] = BASE_DIR / "data"
    globals()["OUTPUTS_DIR"] = BASE_DIR / "outputs"
    globals()["MODELS_DIR"] = BASE_DIR / "models"



def more_complex():
    df = pd.read_csv(f"{DATA_DIR}/test_results.csv")

    # Inspect your data, should show 2 columns with missing values in this case
    print(f"\nColumns:\n{list(df.columns)}")
    print(f"\nMissing before:\n{df.isna().sum()}")

    # Clean your data
    df["Test1"] = df["Test1"].fillna(0).astype(int)
    df["Test2"] = df["Test2"].fillna(0).astype(int)
    print(f"\nMissing after:\n{df.isna().sum()}")
    
    # Transform the data
    # add a derived column ( just as an example of transformed data )
    df["Total"] = df["Test1"] + df["Test2"]

    print(df["Total"])
    print(f"\nMissing after transformation:\n{df.isna().sum()}")

    # Create a sneak peek of the cleaned data
    # NOTE: Our derived column is now included in the in memory copy of the transformed dataframe
    print(f"\nPreview:\n{df.head()}")
    print(f"\nSummary statistics (float):\n{df.describe()}")
    print(f"\nSummary statistics (int):\n{df.describe().astype(int)}")

    # Save the cleaned and transformed data for future use
    print(f"Saving result to:\n{DATA_DIR}/clean_test_results.csv")
    df.to_csv(f"{DATA_DIR}/clean_test_results.csv", index=False)

def simple_exampel():
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
                print(f"Missing value found: {col_value}")

    # replace value in the in menory Copy of the data
    # NOTE: fillna() casts int as floats
    df["Score"] = df["Score"].fillna(0)
    df["Score"] = df["Score"].astype(int)

    print(df["Score"])
    print(df.isna().sum())

    # Save the cleaned and transformed data for future use
    df.to_csv(f"{DATA_DIR}/clean_data.csv", index=False)        

def run():
    # simple_exampel()
    more_complex()

if __name__ == "__main__":
    set_globals()
    run()