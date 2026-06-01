import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import seaborn as sns
import joblib
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# Some constants so we can find our directories where files are stored.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = BASE_DIR / "models"

# Create any missing directories, just to make sure they do exist if / when  we need them
MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)


# entry point of the python file, this will run if this file is main()
def run():
    pass

if __name__ == "__main__":
    run()