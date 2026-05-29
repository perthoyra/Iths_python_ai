# %%

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).cwd()
## BASE_DIR = Path(__file__).resolve().parent <- Does not work with jupytr notebooks
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = BASE_DIR / "models"

# BASE_DIR has to exists or the application is missing
# DATA_DIR has to exist or the raw data can not be found
MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)

# %%

df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

plt.plot(df["day"], df["cups_sold"] )
plt.tile("Cups sold per day")
plt.show()

# %%
