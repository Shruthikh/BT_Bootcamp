from role_builder import RoleBuilder
from salary_calculator import SalaryCalculator

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self):
        self.report_date = ""

    def print_line(self):
        print("---------------------------------------------------------------")

    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT")
        print("Date : " + self.report_date)
        self.print_line()

    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        for emp in employees:
            role_desc = RoleBuilder.get_role_description(emp.role)
            allowance = SalaryCalculator.get_allowance(emp)
            salary = SalaryCalculator.get_salary(emp)

            print(
                emp.emp_id + "\t" +
                emp.name + "\t" +
                role_desc + "\t" +
                str(emp.basic) + "\t" +
                str(emp.hra) + "\t" +
                str(allowance) + "\t" +
                str(salary)
            )

        self.display_footer(len(employees))
