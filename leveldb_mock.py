class LevelDBMock:
    """
    模拟 LevelDB 键值存储
    """
    def __init__(self, path):
        self.path = path
        self.db = {}

    def put(self, key, value):
        self.db[key] = value

    def get(self, key):
        return self.db.get(key)

    def delete(self, key):
        if key in self.db:
            del self.db[key]
