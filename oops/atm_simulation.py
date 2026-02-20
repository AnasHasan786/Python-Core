class AtmFacility:

    __counter = 1

    def __init__(self):
        self.__pin = ""
        self.__balance = 10000
        self.cid = AtmFacility.__counter
        AtmFacility.__counter = AtmFacility.__counter + 1
        self.menu()

    @staticmethod
    def get_counter():
        return AtmFacility.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            return "You have entered invalid value!! Please try again."

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
        self.__pin = input_pin
        print("Pin created successfully!!\n")

    def change_pin(self):
        input_old_pin = input("Enter your old pin: ")

        if self.__pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to change it.\n"
            )
        elif input_old_pin == self.__pin:
            input_new_pin = input("Enter your new pin: ")

            if input_new_pin == input_old_pin:
                print("New pin cannot be same as old pin.\n")

            else:
                self.__pin = input_new_pin
                print("Pin changed successfully!!\n")
        else:
            print("You are entering wrong pin. Please try again.\n")

    def check_balance(self):
        input_pin = input("Enter pin to access your balance: ")

        if self.__pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to enter it.\n"
            )
        elif input_pin == self.__pin:
            print(f"The balance in your account is Rs {self.__balance}\n")
        else:
            print("You are entering wrong pin. Please try again.\n")

    def withdraw(self):
        input_pin = input("Enter pin to withdraw the required amount: ")

        if self.__pin == "":
            print(
                "You have not even created your pin. Please create it first and then try to enter it.\n"
            )
        elif input_pin == self.__pin:
            withdrawl_amount = int(input("Enter the amount you want to withdraw: "))

            if withdrawl_amount > 0 and withdrawl_amount <= self.__balance:
                self.__balance = self.__balance - withdrawl_amount
                print("Withdrawl operation done successfully!!\n")
                print(f"The remaining balance is now Rs {self.__balance}\n")
            elif withdrawl_amount > self.__balance:
                print("Transaction declined: Insufficient funds!!\n")
            else:
                print("Invalid amount. Please enter a valid withdrawl amount!!\n")
        else:
            print("You are entering wrong pin. Please try again.\n")


AtmFacility.get_counter()

c1 = AtmFacility()
