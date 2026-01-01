from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = [None] * 4

        print("Enter employee information")

        for i in range(len(employees)):
            emp = Employee()
            print("Employee No :", i + 1)

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
            emp.role = int(input())

            employees[i] = emp

        report_date = input("Enter report date (dd/mm/yyyy) : ")

        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    Program.main([])
