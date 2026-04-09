class Contract:
    """
    智能合约基类
    """
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
