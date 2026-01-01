from decimal_splitter import DecimalSplitter

class Program:
    @staticmethod
    def main(args):
        # Read number from command line argument
        number = float(args[0])

        print("Number entered is : " + str(number))

        # Call static methods of DecimalSplitter
        print("Whole part of the given number is : " +
              str(DecimalSplitter.get_whole(number)))

        print("Fractional part of the given number is : " +
              str(DecimalSplitter.get_fraction(number)))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
