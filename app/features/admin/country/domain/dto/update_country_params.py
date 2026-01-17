from dataclasses import dataclass


@dataclass
class UpdateCountryParams:
    """
    Data Transfer Object used to carry the required data
    to update an existing Country entity.

    This DTO represents the intent to modify a Country
    identified by its unique identifier.
    """

    id: int
    name: str
    country_code: str
    currency_code: str
