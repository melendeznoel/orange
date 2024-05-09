"""Description of identifier"""
from typing import List
from fhir_coding import FhirCoding

class FhirTypeClass:
    """	CodeableConcept"""
    coding: List[FhirCoding]

    def __init__(self, coding: List[FhirCoding]) -> None:
        self.coding = coding
