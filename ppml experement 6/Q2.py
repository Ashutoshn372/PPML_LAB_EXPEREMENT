class Person:
    def show_person(self):
        print("Person: basic personal information")


class Student(Person):
    def show_student(self):
        print("Student: enrolled in a course")


class Employee:
    def show_employee(self):
        print("Employee: works at the institution")


class GraduateStudent(Student):
    def show_graduate_student(self):
        print("Graduate student: studying at an advanced level")


class TeachingAssistant(Student, Employee):
    def show_teaching_assistant(self):
        print("Teaching assistant: supports course instruction")


print("Multilevel inheritance:")
graduate_student = GraduateStudent()
graduate_student.show_person()
graduate_student.show_student()
graduate_student.show_graduate_student()

print("\nMultiple inheritance:")
teaching_assistant = TeachingAssistant()
teaching_assistant.show_person()
teaching_assistant.show_student()
teaching_assistant.show_employee()
teaching_assistant.show_teaching_assistant()