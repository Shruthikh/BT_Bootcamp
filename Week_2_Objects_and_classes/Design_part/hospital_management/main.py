from hospital import Hospital
from ward import Ward
from patient import Patient
from operation import Operation
from senior_surgeon import SeniorSurgeon
from nonsenior_surgeon import NonSeniorSurgeon

# -----------------------------
# Create Hospital and Wards
# -----------------------------
hospital = Hospital("City Hospital")

icu = Ward("ICU")
general = Ward("General Ward")

hospital.add_ward(icu)
hospital.add_ward(general)

# -----------------------------
# Create Patients (Girls)
# -----------------------------
p1 = Patient("Sita")
p2 = Patient("Kavya")
p3 = Patient("Ananya")

icu.add_patient(p1)
icu.add_patient(p2)
general.add_patient(p3)

# -----------------------------
# Create Surgeons (CATEGORIES)
# -----------------------------
senior = SeniorSurgeon("Dr. Meera")
junior = NonSeniorSurgeon("Dr. Nisha")

# -----------------------------
# Perform Operations
# -----------------------------
senior.perform_operation(Operation(1, p1))
junior.perform_operation(Operation(2, p3))

# -----------------------------
# OUTPUTS (QUESTION ASKED)
# -----------------------------

# 1️⃣ Total patients being operated (by both surgeons)
total = senior.total_patients_operated() + junior.total_patients_operated()
print("Total patients being operated:", total)

# 2️⃣ Patients operated by each surgeon
print("\nPatients operated by surgeons:")

print("\nSenior Surgeon:", senior.name)
for p in senior.list_operated_patients():
    print("-", p.name)

print("\nNon-Senior Surgeon:", junior.name)
for p in junior.list_operated_patients():
    print("-", p.name)

# 3️⃣ Patients admitted to wards
print("\nPatients admitted to wards:")
for ward in hospital.wards:
    print("\nWard:", ward.name)
    for patient in ward.patients:
        print("-", patient.name)
