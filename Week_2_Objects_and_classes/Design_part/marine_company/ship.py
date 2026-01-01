# Base Ship class
class Ship:
    def __init__(self, ship_id, name):
        self.ship_id = ship_id
        self.name = name
        self.bookings = []   # HAS-A Booking

    def add_booking(self, booking):
        self.bookings.append(booking)

    # Total amount collected by this ship
    def total_amount(self):
        return sum(b.amount for b in self.bookings)
