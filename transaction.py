import transaction_interface


class Transaction(transaction_interface.TransactionInterface):
    def __init__(self, bank, account_number, attempted_pin):
        self.bank = bank
        self.account_number = account_number
        self.attempted_pin = attempted_pin

    def get_balance(self):
        return -1

    def credit(self, amount):
        pass

    def debit(self, amount):
        return True
