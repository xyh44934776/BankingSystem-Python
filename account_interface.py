import abc


class AccountInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def validate_pin(self, attempted_pin):
        pass

    @abc.abstractmethod
    def credit_account(self, amount):
        pass

    @abc.abstractmethod
    def debit_account(self, amount):
        pass
