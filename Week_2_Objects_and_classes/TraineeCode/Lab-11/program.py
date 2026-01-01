from employee import Employee
from employee_report import EmployeeReport
from roles import Roles

class Program:
    @staticmethod
    def main(args):
        employees = []

        print("Enter employee information")

        for i in range(4):
            print("Employee No :", i + 1)

            # NEW in Lab-11:
            # Create empty Employee object
            emp = Employee()

            emp.emp_id = input("Id : ")
            emp.name = input("Name : ")
            emp.basic = float(input("Basic : "))
            emp.hra = float(input("HRA : "))
            emp.allowance_percentage = float(input("Allowance Percentage : "))

            print("Enter Role Id :")
            print("1. DEVELOPER")
            print("2. TEST_ENGINEER")
            print("3. SR_DEVELOPER")
            print("4. DESIGNER")
            role_id = int(input())

            # NEW in Lab-11:
            # Enum used instead of integer constants
            emp.role = Roles(role_id)

            employees.append(emp)

        report_date = input("Enter report date (dd/mm/yyyy) : ")

        # NEW in Lab-11:
        # Parameterized constructor used
        report = EmployeeReport(report_date)
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    Program.main([])
