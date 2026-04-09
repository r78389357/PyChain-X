import json
import time

class Utils:
    """
    通用工具类
    """
    @staticmethod
    def json_serialize(obj):
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)

    @staticmethod
    def json_deserialize(json_str):
        return json.loads(json_str)

    @staticmethod
    def get_timestamp():
        return int(time.time())

    @staticmethod
    def hex_to_bytes(hex_str):
        return bytes.fromhex(hex_str)
