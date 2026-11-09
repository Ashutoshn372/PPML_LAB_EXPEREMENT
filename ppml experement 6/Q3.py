class Calculator:
    def add(self, first, second=0, third=0):
        return first + second + third


class Animal:
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


calculator = Calculator()
print("Adding two numbers:", calculator.add(10, 20))
print("Adding three numbers:", calculator.add(10, 20, 30))

print("Method overriding:")
Animal().speak()
Dog().speak()