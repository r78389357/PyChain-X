class Address:
    """
    地址编码工具
    """
    PREFIX = "PYC"

    @staticmethod
    def from_public_key(public_key):
        # 简单的地址生成逻辑
        encoded = public_key[:20]
        return f"{Address.PREFIX}{encoded}"

    @staticmethod
    def is_valid(address):
        return address.startswith(Address.PREFIX) and len(address) == 24
