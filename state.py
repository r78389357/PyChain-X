class StateManager:
    """
    状态管理
    维护账户余额的世界状态
    """
    def __init__(self):
        self.accounts = {}

    def update(self, address, amount):
        if address not in self.accounts:
            self.accounts[address] = 0
        self.accounts[address] += amount

    def get_state_root(self):
        # 计算状态根哈希
        return "STATE_ROOT_HASH"
