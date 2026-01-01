from salary_calculator import SalaryCalculator

class Employee:
    """
    Employee class with parameterized constructor
    """
    def __init__(self, emp_id, name, basic, hra, allowance_percentage, role):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = hra
        self.allowance_percentage = allowance_percentage
        self.role = role

    # Calls SalaryCalculator internally
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    # Calls SalaryCalculator internally
    def get_salary(self):
        return SalaryCalculator.get_salary(self)
