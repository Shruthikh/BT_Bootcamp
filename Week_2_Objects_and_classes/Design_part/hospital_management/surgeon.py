# Base Surgeon class
class Surgeon:
    def __init__(self, name):
        self.name = name
        self.operations = []   # HAS-A Operation

    def perform_operation(self, operation):
        self.operations.append(operation)

    # 1️⃣ Total number of patients being operated
    def total_patients_operated(self):
        return len(self.operations)

    # 2️⃣ List patients operated by this surgeon
    def list_operated_patients(self):
        return [op.patient for op in self.operations]
