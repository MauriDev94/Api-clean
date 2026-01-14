from dataclasses import dataclass


@dataclass
class UpdateCountryParams:
    id: int
    name: str
    country_code: str
    currency_code: str
