from abc import ABC, abstractmethod


class BankApp(ABC):

    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass


class MobileApp(BankApp):

    def security(self):
        print("Mobile App secured")


mob = MobileApp()
mob.database()
mob.security()
