class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def treat_patient(self, patient):
        print(f"Dr. {self.name}, a specialist in {self.specialty}, is treating {patient.name}.")
