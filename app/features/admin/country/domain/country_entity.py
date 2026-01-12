from dataclasses import dataclass
from datetime import datetime


@dataclass
class Country:
    id: int
    name: str
    country_code: str
    currency_code: str
    created_at: datetime
    updated_at: datetime
