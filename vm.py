class VirtualMachine:
    """
    简易虚拟机
    执行合约逻辑
    """
    def __init__(self):
        self.stack = []

    def execute(self, bytecode):
        for op in bytecode:
            if op == "PUSH":
                pass # 压栈
            elif op == "ADD":
                pass # 加法
        return self.stack
