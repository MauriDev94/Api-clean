from dataclasses import dataclass
from datetime import datetime


@dataclass
class Country:
    """
    Domain Entity representing a Country.

    This entity models the core business concept of a country and is intended
    to live in the Domain layer. It contains no infrastructure or framework
    dependencies and should encapsulate business identity and attributes.
    """

    id: int
    name: str
    country_code: str
    currency_code: str
    created_at: datetime
    updated_at: datetime
