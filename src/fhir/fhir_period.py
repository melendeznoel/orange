"""Time period when id is/was valid for use"""
from datetime import datetime

class FhirPeriod:
    """Time range defined by start and end date/time"""
    start: datetime

    def __init__(self, start: datetime) -> None:
        self.start = start
