"""Base"""
from abc import ABC

class BaseService(ABC):
    """Base Service"""
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
