from dataclasses import dataclass


@dataclass
class CreateCountryParams:
    name: str
    country_code: str
    currency_code: str
