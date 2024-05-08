"""A string, typically numeric or alphanumeric, that is associated with a single object or entity within a given system."""
from typing import Any
from dataclasses import dataclass
from fhir_assigner import FhirAssigner
from fhir_period import FhirPeriod
from fhir_type_class import FhirTypeClass

@dataclass
class FhirIdentifier:
    """An identifier intended for computation"""
    use: str
    type: FhirTypeClass
    system: str
    value: int
    period: FhirPeriod
    assigner: FhirAssigner

    @staticmethod
    def from_dict(obj: Any) -> 'FhirIdentifier':
        """Mapper"""
        _use = str(obj.get("use"))
        _type = FhirTypeClass(obj.get("type"))
        _system = str(obj.get("system"))
        _value = int(obj.get("value"))
        _period = FhirPeriod(obj.get("period"))
        _assigner = FhirAssigner(obj.get("assigner"))

        return FhirIdentifier(_use, _type, _system, _value, _period, _assigner)
