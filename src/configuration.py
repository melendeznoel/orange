from yaml import load, CLoader as Loader

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._data = load(open("env_config.yaml"), Loader=Loader)

        return cls._instance

    def db(self):
        return self._data.get("database")

    def db_mongodb(self):
        return self.db().get("mongodb")

    def db_mongodb_uri(self):
        return self.db_mongodb().get("uri")
