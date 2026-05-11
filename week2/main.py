from os import system, name
from time import sleep
import pandas as pd
import menu
import json

def clear_screen() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def read_menu_data():
    df = pd.read_json("week2\data\menu_data.json")
    return dict(df["options"])
               
def handle_response(choice: int, menu_items: dict) -> bool:
    match choice:
        case 0:
            print("Terminating program...")
            return False
        case 1 | 2:
            print("\n")
            print(menu_items[choice])
            print("\n")
            sleep(2)
    
    # it is a bit quick, so the resulkt is not visible long enough
    _ = input()
    return True
        
def run(mymenu: menu) -> None:
    
    while True:
        clear_screen()
        mymenu.draw_menu()
        selected = mymenu.get_input()
        
        if not handle_response(selected, mymenu.get_menu_items()):
            break
        
def main():
    thisdict = read_menu_data()

    if thisdict:
        myMenu = menu.MyMenu(thisdict)
        run(myMenu)
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()