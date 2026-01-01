# MarineCompany HAS-A Ship
class MarineCompany:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    # 1️⃣ Total amount collected by company
    def total_amount_collected(self):
        return sum(ship.total_amount() for ship in self.ships)

    # 2️⃣ Total amount collected by each ship
    def amount_per_ship(self):
        return {ship.name: ship.total_amount() for ship in self.ships}

    # 3️⃣ List all customers for a particular cruise ship
    def customers_for_cruise(self, cruise_name):
        for ship in self.ships:
            if ship.name == cruise_name:
                return [b.customer for b in ship.bookings]
        return []
