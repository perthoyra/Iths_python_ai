from pathlib import Path

class Text_Handler: 

    _read_mode = "rt"
    _write_mode = "wt"
    _encoding = "utf-8" 

    def __init__(self, directory: str) -> None:
        self._directory = directory

    def read_from_file(self, filename: str, read_all:bool = True):
        # Example of manual  way of reading file, do not forget to close the file when done.
        # file_reader = open(filename, Text_Handler._read_mode)
        # file_data = file_reader.read()
        # file_reader.close()

        fullPath = self._directory + "/" + filename

        print(fullPath)

        if not Path.exists(self._directory / filename):
            raise "Invalid file filename, file does not extist."

        if read_all:
            with open(filename, Text_Handler._read_mode, encoding = Text_Handler._encoding) as file_reader:
                file_data = file_reader.read()
        else:
            with open(filename, Text_Handler._read_mode, Text_Handler._encoding) as file_reader:
                file_data = file_reader.readlines().strip("\n")

        return file_data

    def write_to_file(self, filename:str) -> None:
        pass

    def append_to_file(self, filename:str) -> None:
        pass

    def create_file(self, filename:str) -> None:
        pass

    def main():
        print("\n")
        print("Text_Handler now initialized via main().")
        print("\n")

    if __name__ == '__main__':
        main()