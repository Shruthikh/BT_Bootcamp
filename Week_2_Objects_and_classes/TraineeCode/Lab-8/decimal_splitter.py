class DecimalSplitter:
    """
    Method to get the whole number from a decimal number
    """
    @staticmethod
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a decimal number
    """
    @staticmethod
    def get_fraction(number):
        return number - int(number)
