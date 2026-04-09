import hashlib

class MerkleTree:
    """
    默克尔树实现
    用于快速验证交易是否存在于区块中
    """
    def __init__(self, data_list):
        self.data_list = data_list
        self.tree = self.build_tree()

    def hash_leaf(self, data):
        return hashlib.sha256(f"0{data}".encode()).hexdigest()

    def hash_node(self, left, right):
        return hashlib.sha256(f"1{left}{right}".encode()).hexdigest()

    def build_tree(self):
        if not self.data_list:
            return None
        
        current_level = [self.hash_leaf(d) for d in self.data_list]
        tree_levels = [current_level]
        
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i+1 < len(current_level) else left
                next_level.append(self.hash_node(left, right))
            current_level = next_level
            tree_levels.append(current_level)
            
        return tree_levels

    def get_root(self):
        return self.tree[-1][0] if self.tree else None
