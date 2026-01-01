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

            emp_id = input("Id : ")
            name = input("Name : ")
            basic = float(input("Basic : "))
            hra = float(input("HRA : "))
            allowance_percentage = float(input("Allowance Percentage : "))

            print("Enter Role Id :")
            print("1. DEVELOPER")
            print("2. TEST_ENGINEER")
            print("3. SR_DEVELOPER")
            print("4. DESIGNER")
            role = int(input())

            # Parameterized constructor 
            emp = Employee(emp_id, name, basic, hra, allowance_percentage, role)
            employees.append(emp)

        report_date = input("Enter report date (dd/mm/yyyy) : ")

        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    Program.main([])
