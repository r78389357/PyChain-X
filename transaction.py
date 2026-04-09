import time
import hashlib
from crypto import Crypto

class Transaction:
    """
    交易模型
    支持输入输出模型
    """
    def __init__(self, tx_id, inputs, outputs, timestamp=None):
        self.tx_id = tx_id
        self.inputs = inputs
        self.outputs = outputs
        self.timestamp = timestamp or int(time.time())
        self.signature = None

    def calculate_hash(self):
        data = f"{self.tx_id}{str(self.inputs)}{str(self.outputs)}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def sign(self, private_key):
        """使用私钥对交易进行签名"""
        data_hash = self.calculate_hash()
        self.signature = Crypto.sign(data_hash, private_key)

    def verify(self, public_key):
        """验证交易签名"""
        if not self.signature:
            return False
        data_hash = self.calculate_hash()
        return Crypto.verify(data_hash, self.signature, public_key)

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "timestamp": self.timestamp,
            "signature": self.signature
        }
