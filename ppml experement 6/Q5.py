import csv
from pathlib import Path


csv_path = Path(__file__).with_name("students.csv")
students = [
    ["Name", "Age", "Grade"],
    ["Asha", 18, "A"],
    ["Ravi", 19, "B"],
    ["Mina", 18, "A"],
]

with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(students)

print("CSV file created and written:", csv_path.name)
print("Data read from the CSV file:")

with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(", ".join(row))
