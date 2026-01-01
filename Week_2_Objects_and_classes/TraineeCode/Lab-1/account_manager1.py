class AccountManager1:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        # Setter NOT used – private variables assigned directly
        acc._acc_no = "004701"
        acc._name = "Nitesh"
        acc._balance = 45000.0

        # Correct way (Setter used)
        # acc.acc_no = "004701"
        # acc.name = "Nitesh"
        # acc.balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        # Getter NOT used – private variables accessed directly
        print("AccNo : " + acc._acc_no)
        print("Name : " + acc._name)
        print("Balance : " + str(acc._balance))

        # Correct way (Getter used)
        # print("AccNo : " + acc.acc_no)
        # print("Name : " + acc.name)
        # print("Balance : " + str(acc.balance))
