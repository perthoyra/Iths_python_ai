import os

class Python_Handler:

    _read_mode = "rt"
    _write_mode = "wt"
    _encoding = "UTF8"

    def __init__(self) -> None:
        pass

    def read_from_file(self, filename: str) -> None:
        
        if not os.path.exists(filename):
            raise "Invalid file filename, file does not extist."

        pass

    def write_to_file(self, filename:str) -> None:
        pass

    def append_to_file(self, filename:str) -> None:
        pass


    def create_file(self, filename:str) -> None:
        pass