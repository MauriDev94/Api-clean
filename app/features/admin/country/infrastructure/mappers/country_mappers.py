from app.features.admin.country.domain.country_entity import Country
from app.features.admin.country.infrastructure.models.country_model import CountryModel


def map_country_model_to_entity(model: CountryModel) -> Country:
    return Country(
        id=model.id,
        name=model.name,
        country_code=model.country_code,
        currency_code=model.currency_code,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def map_country_entity_to_model(country: Country) -> CountryModel:
    return CountryModel(
        id=country.id,
        name=country.name,
        country_code=country.country_code,
        currency_code=country.currency_code,
        created_at=country.created_at,
        updated_at=country.updated_at,
    )
