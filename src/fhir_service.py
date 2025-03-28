import logging

from .base_service import BaseService
from .database import Database


class FhirService(BaseService):
    """FHIR Resources"""
    def save_resource(self, data):
        """insert a new resource"""
        try:
            result = None

            pantry = self.__pantry_collection__()

            result = pantry.insert_one(data).inserted_id

            return str(result)
        except Exception as e:
            logging.exception('error inserting a new fhir resource')
            raise e

    def __pantry_collection__(self):
        db = Database()

        recipes = db.col("ingredients")

        return recipes

    def search_resource(self, data):
        """search resource"""
        try:
            result = None

            pantry = self.__pantry_collection__()

            result = pantry.find()

            return str(result)
        except Exception as e:
            logging.exception('error inserting a new fhir resource')
            raise e
