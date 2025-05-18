file_path = "sample.txt"
try:
    with open(file_path, "r") as file:
        no_of_lines = 0
        for line in file:
            no_of_lines += 1
            print(f"Line {no_of_lines} : {line}", end='')
except FileNotFoundError as FIFE:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as E:
    print(f"Error: {E}")