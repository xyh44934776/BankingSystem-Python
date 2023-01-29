import  bank_interface


class Bank(bank_interface.BankInterface):
    def __init__(self, account):
        self.account = account

    def open_commercial_account(self, company, pin, starting_deposit):
        return -1

    def open_consumer_account(self, person, pin, starting_deposit):
        return -1

    def authenticate_user(self, company, pin, starting_deposit):
        return False

    def credit(self, company, pin, starting_deposit):
        return

    def debit(self, company, pin, starting_deposit):
        return True