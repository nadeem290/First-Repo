def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    print(read_file("sample.txt"))
