from pathlib import Path


file_path = Path(__file__).with_name("experiment6_file.txt")

with file_path.open("w", encoding="utf-8") as file:
    file.write("File handling in Python.\n")
    file.write("This file demonstrates writing, reading, and file pointers.\n")

print("File created and written:", file_path.name)

with file_path.open("r", encoding="utf-8") as file:
    print("Pointer position at start:", file.tell())
    print("First line:", file.readline().strip())
    print("Pointer position after reading one line:", file.tell())

    file.seek(0)
    print("Pointer position after seek(0):", file.tell())
    print("Complete file contents:")
    print(file.read(), end="")