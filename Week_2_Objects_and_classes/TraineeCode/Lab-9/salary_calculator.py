class SalaryCalculator:
    """
    Method to get allowance for an employee
    """
    @staticmethod
    def get_allowance(emp):
        return emp.basic * emp.allowance_percentage / 100.0

    """
    Method to calculate the salary of an employee
    salary = basic + hra + allowance
    """
    @staticmethod
    def get_salary(emp):
        allowance = SalaryCalculator.get_allowance(emp)
        return emp.basic + emp.hra + allowance
