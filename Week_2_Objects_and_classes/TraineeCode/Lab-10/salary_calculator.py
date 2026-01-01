class SalaryCalculator:
    """
    Salary calculation logic
    """
    @staticmethod
    def get_allowance(emp):
        return emp.basic * emp.allowance_percentage / 100.0

    @staticmethod
    def get_salary(emp):
        allowance = SalaryCalculator.get_allowance(emp)
        return emp.basic + emp.hra + allowance
