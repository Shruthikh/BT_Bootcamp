from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        # Store employee details
        emp.emp_id = "E101"
        emp.emp_name = "Nitesh"
        emp.emp_gender = "Male"

        # Create Address object
        addr = Address()
        addr.addr1 = "MG Road"
        addr.addr2 = "Near Metro Station"
        addr.city = "Bangalore"
        addr.pincode = "560001"

        # Store address inside employee object
        emp.address = addr

    @staticmethod
    def show_data(emp):
        # Display employee information
        print("Employee Id : ", emp.emp_id)
        print("Employee Name : ", emp.emp_name)
        print("Employee Gender : ", emp.emp_gender)

        print("Employee Address : --------------")
        print("Address 1 : ", emp.address.addr1)
        print("Address 2 : ", emp.address.addr2)
        print("City : ", emp.address.city)
        print("PinCode : ", emp.address.pincode)
        print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
