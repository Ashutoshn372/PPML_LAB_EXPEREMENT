class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        print(f"Constructor called for {self.name}.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_number}")

    def __del__(self):
        print(f"Destructor called for {self.name}.")


student = Student("Asha", 101)
student.display()
del student