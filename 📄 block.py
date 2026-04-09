import time
import hashlib
from utils import Utils

class Block:
    """
    区块结构体
    包含区块头与交易列表
    """
    def __init__(self, index, timestamp, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
        self.merkle_root = self.calculate_merkle_root()

    def calculate_hash(self):
        """计算区块哈希"""
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.nonce}{self.merkle_root}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def calculate_merkle_root(self):
        """计算交易默克尔根"""
        if not self.transactions:
            return "0" * 64
        # 简化版默克尔树计算
        tx_hashes = [tx.tx_id for tx in self.transactions]
        if len(tx_hashes) == 1:
            return tx_hashes[0]
        
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])
            next_level = []
            for i in range(0, len(tx_hashes), 2):
                combined = tx_hashes[i] + tx_hashes[i+1]
                next_level.append(hashlib.sha256(combined.encode()).hexdigest())
            tx_hashes = next_level
            
        return tx_hashes[0]

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "nonce": self.nonce
        }
