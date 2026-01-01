from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder

# NEW in Lab-11:
# Employee created using empty constructor
class Employee:
    def __init__(self):
        self.emp_id = ""
        self.name = ""
        self.basic = 0.0
        self.hra = 0.0
        self.allowance_percentage = 0.0
        self.role = None

    # NEW in Lab-11:
    # Employee provides salary instead of EmployeeReport
    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    # NEW in Lab-11:
    # Employee provides allowance instead of EmployeeReport
    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    # NEW in Lab-11:
    # Employee provides role description
    def get_role_description(self):
        return RoleBuilder.get_role_description(self.role)
