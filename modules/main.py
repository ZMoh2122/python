from doctor import Doctor
from patient import Patient

# Create 5 doctors
doctor1 = Doctor("Alice Johnson", "Cardiology")
doctor2 = Doctor("Bob Smith", "Neurology")
doctor3 = Doctor("Catherine Lee", "Pediatrics")
doctor4 = Doctor("David Brown", "Orthopedics")
doctor5 = Doctor("Evelyn Carter", "Dermatology")

# List to store doctors
doctors = [doctor1, doctor2, doctor3, doctor4, doctor5]

# Display information about each doctor
for doctor in doctors:
    print(f"Dr. {doctor.name} specializes in {doctor.specialty}.")

patient1 = Patient("John Doe", 45, "Heart Disease")
patient2 = Patient("Jane Smith", 30, "Migraine")
patient3 = Patient("Mike Brown", 60, "Diabetes")
patient4 = Patient("Emily White", 25, "Asthma")
patient5 = Patient("Robert Green", 50, "Arthritis")
patient6 = Patient("Laura Black", 40, "Hypertension")
patient7 = Patient("Daniel Gray", 35, "Back Pain")
patient8 = Patient("Sophia Blue", 20, "Allergy")
patient9 = Patient("Chris Yellow", 55, "Cholesterol")
patient10 = Patient("Mia Purple", 28, "Flu")

patients = [patient1, patient2, patient3, patient4, patient5]

# Display information about each patient
for patient in patients:
    print(f"Patient {patient.name} is {patient.age} years old and has {patient.ailment}.")