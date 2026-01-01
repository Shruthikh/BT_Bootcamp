# NEW in Lab-11:
# EmployeeReport uses parameterized constructor
class EmployeeReport:
    def __init__(self, dt_report):
        self.report_date = dt_report

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

    # NEW in Lab-11:
    # Salary, allowance, role fetched via Employee methods
    def display_employees(self, employees):
        self.display_header()
        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        for emp in employees:
            print(
                emp.emp_id + "\t" +
                emp.name + "\t" +
                emp.get_role_description() + "\t" +
                str(emp.basic) + "\t" +
                str(emp.hra) + "\t" +
                str(emp.get_allowance()) + "\t" +
                str(emp.get_salary())
            )

        self.display_footer(len(employees))
