class ResultFinder:
    """
    Class to calculate total, average and result
    """
    def __init__(self):
        self._marks1 = 0
        self._marks2 = 0
        self._marks3 = 0

    # Getter and Setter for marks1
    @property
    def marks1(self):
        return self._marks1

    @marks1.setter
    def marks1(self, value):
        self._marks1 = value

    # Getter and Setter for marks2
    @property
    def marks2(self):
        return self._marks2

    @marks2.setter
    def marks2(self, value):
        self._marks2 = value

    # Getter and Setter for marks3
    @property
    def marks3(self):
        return self._marks3

    @marks3.setter
    def marks3(self, value):
        self._marks3 = value

    # Display marks
    def display_marks(self):
        print("Marks entered------------- ")
        print("Marks 1 : " + str(self._marks1))
        print("Marks 2 : " + str(self._marks2))
        print("Marks 3 : " + str(self._marks3))

    # Calculate total
    def get_total(self):
        return self._marks1 + self._marks2 + self._marks3

    # Calculate average
    def get_average(self):
        return self.get_total() / 3

    # Determine result
    def get_result(self):
        if self._marks1 >= 40 and self._marks2 >= 40 and self._marks3 >= 40:
            return "PASS"
        else:
            return "FAIL"
