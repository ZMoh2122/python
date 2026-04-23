from doctor import Doctor
from patient import Patient

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Added Dr. {doctor.name}, specializing in {doctor.specialty}, to {self.name}.")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Admitted patient {patient.name}, suffering from {patient.ailment}, to {self.name}.")



hospital1 = Hospital ("Robbinsdale Hospital","Minneapolis",)