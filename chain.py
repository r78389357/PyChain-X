from block import Block
from genesis import Genesis
from transaction import Transaction
from pow import PoW

class Blockchain:
    """
    区块链主类
    管理链的状态、交易池和验证
    """
    def __init__(self):
        self.chain = [Genesis.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 4  # 初始难度
        self.max_supply = 21000000

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if self.is_valid_block(block):
            self.chain.append(block)
            # 难度调整逻辑可在此添加
            return True
        return False

    def is_valid_block(self, block):
        # 验证父哈希
        if block.previous_hash != self.get_latest_block().hash:
            return False
        # 验证工作量证明
        if not PoW.validate(block, self.difficulty):
            return False
        # 验证交易
        for tx in block.transactions:
            if not self.is_valid_transaction(tx):
                return False
        return True

    def is_valid_transaction(self, tx):
        # 简单的交易验证逻辑
        return True

    def create_block(self, miner_address):
        # 打包交易
        txs = [Transaction(tx_id="COINBASE", inputs=[], outputs=[{"address": miner_address, "amount": 50}], timestamp=0)]
        txs.extend(self.pending_transactions)
        
        new_block = Block(
            index=len(self.chain),
            timestamp=Utils.get_timestamp(),
            transactions=txs,
            previous_hash=self.get_latest_block().hash
        )
        
        # 挖矿
        PoW.mine(new_block, self.difficulty)
        self.add_block(new_block)
        self.pending_transactions = []
        return new_block

    def add_transaction(self, tx):
        if tx.verify(tx.inputs[0].get('public_key')): # 假设输入包含公钥
            self.pending_transactions.append(tx)
            return True
        return False
