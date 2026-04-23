class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

    def describe(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}")

