file_name = "output.txt"
txt = input("Enter text to write to the file:")
with open(file_name, "w") as file:
    file.write(txt + "\n")
    print(f"Data Successfully written to {file_name}")

txt = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(txt)
    print(f"Data successfully appended.")

print(f"Final content of {file_name}:")
with open(file_name, "r") as file:
    print(file.read(), end="")
