"""A text note which also contains information about who made the statement and when."""
from typing import Any
from dataclasses import dataclass

@dataclass
class FhirAnnotation:
    """A text note"""
    author_reference: str
    author_string: str
    time: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'FhirAnnotation':
        """Mapper"""
        _author_reference = str(obj.get("author_reference"))
        _author_string = str(obj.get("author_string"))
        _time = str(obj.get("time"))
        _text = str(obj.get("text"))

        return FhirAnnotation(_author_reference, _author_string, _time, _text)
