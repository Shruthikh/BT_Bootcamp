from marine_company import MarineCompany
from cruise_ship import CruiseShip
from cargo_ship import CargoShip
from customer import Customer
from booking import Booking

# -----------------------------
# Create Marine Company
# -----------------------------
company = MarineCompany("SeaWave Marine")

# -----------------------------
# Create Ships (CHANGED NAMES)
# -----------------------------
cruise_ship = CruiseShip(1, "Ocean Star")
cargo_ship = CargoShip(2, "Heavy Loader")

company.add_ship(cruise_ship)
company.add_ship(cargo_ship)

# -----------------------------
# Create Customers (CHANGED GIRL NAMES)
# -----------------------------
c1 = Customer("Aishwarya", "9876543210")
c2 = Customer("Pooja", "9123456789")
c3 = Customer("Radhika", "9001122334")

# -----------------------------
# Create Bookings
# -----------------------------
cruise_ship.add_booking(Booking(c1, 7000))
cruise_ship.add_booking(Booking(c2, 6500))
cargo_ship.add_booking(Booking(c3, 9000))

# -----------------------------
# OUTPUTS (3 REQUIRED)
# -----------------------------

# 1️⃣ Total amount collected
print("Total amount collected:", company.total_amount_collected())

# 2️⃣ Amount collected by each ship
print("\nAmount collected by each ship:")
for ship_name, amount in company.amount_per_ship().items():
    print("-", ship_name, ":", amount)

# 3️⃣ Customers for a particular cruise ship
print("\nCustomers travelling in Ocean Star:")
for customer in company.customers_for_cruise("Ocean Star"):
    print("-", customer.name, customer.contact)
