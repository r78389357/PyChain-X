from crypto import Crypto
from address import Address

class Wallet:
    """
    钱包类
    管理密钥对和余额
    """
    def __init__(self):
        self.private_key, self.public_key = Crypto.generate_key_pair()
        self.address = Address.from_public_key(self.public_key)
        self.balance = 0.0

    def get_address(self):
        return self.address

    def get_balance(self, blockchain):
        # 遍历链计算余额
        total = 0.0
        for block in blockchain.chain:
            for tx in block.transactions:
                for output in tx.outputs:
                    if output['address'] == self.address:
                        total += output['amount']
                for inp in tx.inputs:
                    if inp.get('address') == self.address:
                        total -= inp.get('amount', 0)
        self.balance = total
        return total
