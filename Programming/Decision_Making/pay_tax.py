def check_tax_eligibility(salary):
    if salary > 300000:
        return "must pay tax"
    return "does not need to pay tax"


if __name__ == "__main__":
    try:
        name = input("Enter name: ")
        salary = float(input("Enter annual salary: "))

        if salary < 0:
            print("Invalid salary")
        else:
            print(name, check_tax_eligibility(salary))
    except ValueError:
        print("Error: Enter numeric salary.")
