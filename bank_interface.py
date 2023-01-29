import abc


class BankInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def open_commercial_account(self, company, pin, starting_deposit):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def open_consumer_account(self, person, pin, starting_deposit):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def authenticate_user(self, company, pin, starting_deposit):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def credit(self, company, pin, starting_deposit):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def debit(self, company, pin, starting_deposit):
        pass
