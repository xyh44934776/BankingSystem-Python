import abc


class TransactionInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def get_balance(self):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def credit(self, amount):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def debit(self, amount):
        pass
