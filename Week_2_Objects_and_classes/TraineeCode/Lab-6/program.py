from swap_data import SwapData

class Program:
    @staticmethod
    def main(args):
        # Read values from console
        number1 = int(input("Enter Number 1 : "))
        number2 = int(input("Enter Number 2 : "))

        # Store values inside SwapData object
        obj = SwapData()
        obj.number1 = number1
        obj.number2 = number2

        # Display before swapping
        obj.display_values("Numbers before Swapping :")

        # Perform swapping
        obj.swap_values()

        # Display after swapping
        obj.display_values("Numbers after Swapping :")

        input()


if __name__ == "__main__":
    Program.main([])
