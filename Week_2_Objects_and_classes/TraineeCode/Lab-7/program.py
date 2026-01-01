from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
        # Accept marks from command line arguments
        marks1 = int(args[0])
        marks2 = int(args[1])
        marks3 = int(args[2])

        # Create ResultFinder object
        finder = ResultFinder()

        # Store marks using setter methods
        finder.marks1 = marks1
        finder.marks2 = marks2
        finder.marks3 = marks3

        # Display results
        finder.display_marks()
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + finder.get_result())

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
