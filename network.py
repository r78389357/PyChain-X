class Network:
    """
    网络广播层
    """
    def __init__(self, node):
        self.node = node

    def broadcast_block(self, block):
        # 序列化并发送区块
        data = block.to_dict()
        for peer in self.node.peers:
            self.send(peer, "BLOCK", data)

    def broadcast_transaction(self, tx):
        # 发送交易
        data = tx.to_dict()
        for peer in self.node.peers:
            self.send(peer, "TX", data)

    def send(self, peer, msg_type, data):
        print(f"Sending {msg_type} to {peer}: {data}")
