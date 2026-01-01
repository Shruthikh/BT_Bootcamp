# BillingService is USED by Restaurant
class BillingService:
    def calculate_total(self, items):
        return sum(item.price for item in items)
