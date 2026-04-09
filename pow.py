import hashlib

class PoW:
    """
    工作量证明算法
    """
    @staticmethod
    def mine(block, difficulty):
        target = "0" * difficulty
        block.nonce = 0
        while True:
            block.hash = block.calculate_hash()
            if block.hash.startswith(target):
                break
            block.nonce += 1
        return block

    @staticmethod
    def validate(block, difficulty):
        target = "0" * difficulty
        return block.hash.startswith(target)
