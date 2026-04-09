from abc import ABC, abstractmethod

class Consensus(ABC):
    """
    共识算法抽象基类
    """
    @abstractmethod
    def select_leader(self, nodes):
        pass

    @abstractmethod
    def validate_block(self, block):
        pass

class PoWConsensus(Consensus):
    def select_leader(self, nodes):
        # PoW 不需要显式选主，算力竞争
        return None
    
    def validate_block(self, block):
        return True
