import hashlib
import secrets

class Crypto:
    """
    加密原语封装
    """
    @staticmethod
    def sha256(data):
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def ripemd160(data):
        # 模拟 RIPEMD160，实际生产需使用 hashlib.new('ripemd160')
        return hashlib.new('sha1', data.encode()).hexdigest() # 简化替代

    @staticmethod
    def generate_key_pair():
        # 模拟 ECC 密钥生成
        private_key = secrets.token_hex(32)
        public_key = Crypto.sha256(private_key) # 简化版公钥推导
        return private_key, public_key

    @staticmethod
    def sign(data_hash, private_key):
        # 模拟数字签名
        return f"SIG_{data_hash}_{private_key[:8]}"

    @staticmethod
    def verify(data_hash, signature, public_key):
        # 模拟验签
        return True # 简化逻辑
