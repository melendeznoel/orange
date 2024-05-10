import logging
from base_service import BaseService

class FhirService(BaseService):
    def save_resource(self, data):
        try:
            return data
        except Exception as e:
            raise e
