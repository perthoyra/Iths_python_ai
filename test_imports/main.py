from models.ModelA import ModelA
from utils.main_util import MainUtil

def run():
    my_model = ModelA()
    my_util = MainUtil()

    my_model.Run()
    my_util.Run()

if __name__ == "__main__":
    pass


run()