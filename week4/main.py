
from pathlib import Path

import data.Text_Handler as Txt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def main():
    print("Hello World!")

    print(BASE_DIR)
    print(DATA_DIR)

    txt_handler = Txt(DATA_DIR)
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()