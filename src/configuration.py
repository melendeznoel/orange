from yaml import load, CLoader as Loader

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._data = load(open("../env_config.yaml"), Loader=Loader)

        return cls._instance

    def db(self):
        return self._data.get("database")

    def db_address(self):
        return self.db().get("address")

    def db_port(self):
        return self.db().get("port")

    def is_prod(self):
        return self._data.get("runtime_config").get("env").get("prod")

    def apis(self):
        return self._data.get("resources").get("api")

    def food_api(self):
        return self.apis().get("food").get("prod").get("address")
