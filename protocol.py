class Protocol:
    """
    通信协议定义
    """
    MAGIC = 0xD9B4BEF9
    
    @staticmethod
    def encode_message(command, payload):
        # 构建二进制消息
        return f"{Protocol.MAGIC}{command}{len(payload)}{payload}"

    @staticmethod
    def decode_message(data):
        # 解析二进制消息
        return "CMD", "PAYLOAD"
