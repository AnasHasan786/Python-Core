class AtmFacility:

    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.menu()

    def menu(self):
        print(
            "Welcome to the Automated Teller Machine. Kindly choose a service below.\n"
        )

        while True:
            user_input = input(
                "Choose the service you want to use: \n"
                + """
        1. Create your pin
        2. Change your pin
        3. Check your balance
        4. Withdraw
        5. Exit
      \n"""
            )

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw()
            elif user_input == "5":
                print("Thank you for using ATM.")
                break
            else:
                print("Invalid choice.")

    def create_pin(self):
        input_pin = input("Enter pin to use your account: ")
        self.pin = input_pin
        print("Pin created successfully!!\n")

    def change_pin(self):
        input_old_pin = input("Enter your old pin: ")

        if self.pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to change it.\n"
            )
        elif input_old_pin == self.pin:
            input_new_pin = input("Enter your new pin: ")

            if input_new_pin == input_old_pin:
                print("New pin cannot be same as old pin.\n")

            else:
                self.pin = input_new_pin
                print("Pin changed successfully!!\n")
        else:
            print("You are entering wrong pin. Please try again.\n")

    def check_balance(self):
        input_pin = input("Enter pin to access your balance: ")

        if self.pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to enter it.\n"
            )
        elif input_pin == self.pin:
            print(f"The balance in your account is Rs {self.balance}\n")
        else:
            print("You are entering wrong pin. Please try again.\n")

    def withdraw(self):
        input_pin = input("Enter pin to withdraw the required amount: ")

        if self.pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to enter it.\n"
            )
        elif input_pin == self.pin:
            withdrawl_amount = int(input("Enter the amount you want to withdraw: "))

            if withdrawl_amount > 0 and withdrawl_amount <= self.balance:
                self.balance = self.balance - withdrawl_amount
                print("Withdrawl operation done successfully!!\n")
                print(f"The remaining balance is now Rs {self.balance}\n")
            elif withdrawl_amount > self.balance:
                print("Transaction declined: Insufficient funds!!\n")
            else:
                print("Invalid amount. Please enter a valid withdrawl amount!!\n")
        else:
            print("You are entering wrong pin. Please try again.\n")


user = AtmFacility()
