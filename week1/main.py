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

def run_main():
    print("You are now in run_main()")

if __name__ == "__main__":
    run_main()