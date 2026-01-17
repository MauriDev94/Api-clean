from dataclasses import dataclass


@dataclass
class CreateCountryParams:
    """
    Data Transfer Object used to carry the required data
    to create a new Country entity.

    This DTO belongs to the Domain layer and represents
    a validated set of input values for the creation use case.
    """

    name: str
    country_code: str
    currency_code: str
