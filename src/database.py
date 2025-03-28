"""Database"""
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from src.configuration import Configuration


class Database:
    """Data Store"""
    __instance = None
    _mongo_client_instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def col(self, name):
        col = self.db()[name]

        return col

    def client(self):
        if self._mongo_client_instance is None:
            config = Configuration()

            uri = config.db_mongodb_uri()

            self._mongo_client_instance = MongoClient(uri, server_api=ServerApi('1'))

            try:
                self._mongo_client_instance.admin.command('ping')
                print("Pinged your deployment. You successfully connected to MongoDB!")
            except Exception as e:
                print(e)

        return self._mongo_client_instance

    def db(self):
        database = self.client()["coconut"]

        return database