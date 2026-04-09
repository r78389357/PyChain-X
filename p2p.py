import socket
import threading

class P2PNode:
    """
    P2P 网络节点
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, peer_host, peer_port):
        try:
            self.socket.connect((peer_host, peer_port))
            self.peers.append((peer_host, peer_port))
            print(f"Connected to {peer_host}:{peer_port}")
        except Exception as e:
            print(f"Connection failed: {e}")

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Listening on {self.host}:{self.port}")
        while True:
            client, addr = self.socket.accept()
            threading.Thread(target=self.handle_client, args=(client, addr)).start()

    def handle_client(self, client, addr):
        # 处理消息逻辑
        pass
