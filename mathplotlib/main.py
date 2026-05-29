# %%
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# BASE_DIR = Path(__file__).cwd()
BASE_DIR = Path(__file__).resolve().parent # <- Does not work with jupytr notebooks
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = BASE_DIR / "models"

# BASE_DIR has to exists or the application is missing
# DATA_DIR has to exist or the raw data can not be found
MODELS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)

# %%

# Here we are doing a lot of validation and verifying our data
# ......
# we do not do this since we have perfect data in this case :)

#set up the graf plot
df = pd.read_csv(DATA_DIR / "coffee_sales.csv")

x_values = df["day"]
y_values = df["cups_sold"]

fig, ax = plt.subplots(figsize=(7,4))

#setup the plot, values and labels
ax.plot(x_values, y_values, marker="o")
ax.set_title("Cups sold per day")
ax.set_xlabel("Day")
ax.set_ylabel("Number of cups")

# create the fig ( picture )
fig.tight_layout()

# remember fig and ax are references to objects in plt, created on row 30
# plt.show()
fig.savefig(OUTPUTS_DIR / "coffe_figure.png")
plt.close(fig)

# %%

fig, ax = plt.subplots(figsize=(7,4))

#setup the plot, values and labels
ax.bar(x_values, y_values, color="#4C78A8")
ax.set_title("Cups sold per day")
ax.set_xlabel("Day")
ax.set_ylabel("Number of cups")

# create the fig ( picture )
fig.tight_layout()

# remember fig and ax are references to objects in plt, created on row 30
# plt.show()
fig.savefig(OUTPUTS_DIR / "coffe_bars.png")
plt.close(fig)

# %%

fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(x_values, y_values, marker="o")
axes[0].set_title("Cups sold per day")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Number of cups")

#setup the plot, values and labels
axes[1].bar(x_values, y_values, color="#4C78A8")
axes[1].set_title("Cups sold per day")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Number of cups")

# create the fig ( picture )
fig.tight_layout()

# remember fig and ax are references to objects in plt, created on row 30
# plt.show()
fig.savefig(OUTPUTS_DIR / "coffe_combined.png")
plt.close(fig)