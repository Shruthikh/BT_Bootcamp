# -------------------------------------------------------
# HealWell Care Hospital Billing System
# Covers Level 1 to Level 8 with full edge case handling
# -------------------------------------------------------

# -------------------------------
# Level 7: Admin sets services of the day
# -------------------------------
SERVICES = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

COSTS = [500, 300, 800, 1500, 4000, 7000]

GST_RATE = 0.18
SENIOR_DISCOUNT = 0.10
HIGH_BILL_DISCOUNT = 0.05


# -------------------------------
# Level 1: Patient Walks In and Shares Their Details
# -------------------------------
def get_patient_details():
    name = input("Enter patient name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty")

    try:
        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Invalid age entered")

    gender = input("Enter gender: ").strip()
    if not gender:
        raise ValueError("Gender cannot be empty")

    contact = input("Enter contact number: ").strip()
    if not (contact.isdigit() and len(contact) == 10):
        raise ValueError("Contact must be a 10-digit number")

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact
    }


# -------------------------------
# Level 2: Displaying Services for Patient Selection
# -------------------------------
def display_services():
    print("\nAvailable Services:")
    for i in range(len(SERVICES)):
        print(f"{i + 1}. {SERVICES[i]} - ₹{COSTS[i]}")


# -------------------------------
# Level 2 (continued): Patient selects services
# -------------------------------
def get_selected_services():
    raw_input = input("\nEnter service numbers (comma separated, e.g. 1,4): ")

    if not raw_input.strip():
        raise ValueError("At least one service must be selected")

    try:
        selected_indexes = list(set(int(x.strip()) for x in raw_input.split(",")))
    except ValueError:
        raise ValueError("Invalid service selection format")

    for idx in selected_indexes:
        if idx < 1 or idx > len(SERVICES):
            raise ValueError("Selected service number out of range")

    return selected_indexes


# -------------------------------
# Level 3: Fetching Costs of Selected Services
# -------------------------------
def fetch_selected_services(indexes):
    selected_services = []
    selected_costs = []

    for idx in indexes:
        selected_services.append(SERVICES[idx - 1])
        selected_costs.append(COSTS[idx - 1])

    return selected_services, selected_costs


# -------------------------------
# Level 4: Calculating the Total Cost
# -------------------------------
def calculate_subtotal(costs):
    return sum(costs)


# -------------------------------
# Level 8: Providing Discounts (Optional Enhancements)
# -------------------------------
def apply_discounts(age, subtotal):
    discount = 0

    # Senior citizen discount
    if age >= 60:
        discount += subtotal * SENIOR_DISCOUNT

    # High bill discount (applied after senior discount)
    if subtotal > 5000:
        discount += (subtotal - discount) * HIGH_BILL_DISCOUNT

    return discount


# -------------------------------
# Level 5: Applying GST to the Bill
# -------------------------------
def calculate_gst(amount):
    return amount * GST_RATE


# -------------------------------
# Level 6: Generating and Displaying the Invoice
# -------------------------------
def generate_invoice(patient, services, costs, subtotal, discount):
    taxable_amount = subtotal - discount
    gst = calculate_gst(taxable_amount)
    grand_total = taxable_amount + gst

    print("\n" + "-" * 50)
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-" * 50)

    print("\nPatient Information:")
    print(f"Name   : {patient['name']}")
    print(f"Age    : {patient['age']}")
    print(f"Gender : {patient['gender']}")
    print(f"Contact: {patient['contact']}")

    print("\nServices Availed:")
    for i in range(len(services)):
        print(f"{i + 1}. {services[i]}: ₹{costs[i]}")

    print(f"\nSubtotal        : ₹{subtotal}")
    print(f"Discount Applied: ₹{discount:.2f}")
    print(f"GST (18%)       : ₹{gst:.2f}")
    print(f"Grand Total     : ₹{grand_total:.2f}")

    print("\nThank you for choosing HealWell Care Hospital!")
    print("-" * 50)


# -------------------------------
# Main Program Execution
# -------------------------------
if __name__ == "__main__":
    try:
        # Level 1
        patient = get_patient_details()

        # Level 2
        display_services()
        selected_indexes = get_selected_services()

        # Level 3
        selected_services, selected_costs = fetch_selected_services(selected_indexes)

        # Level 4
        subtotal = calculate_subtotal(selected_costs)

        # Level 8
        discount = apply_discounts(patient["age"], subtotal)

        # Level 5 & Level 6
        generate_invoice(patient, selected_services, selected_costs, subtotal, discount)

    except Exception as e:
        print("\nError:", e)


