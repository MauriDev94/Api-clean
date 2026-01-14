from sqlalchemy.orm import Session
from typing import override
from app.features.admin.country.application.contracts.country_datasource import (
    CountryDatasource,
)
from app.features.admin.country.domain.country_entity import Country
from app.features.admin.country.domain.create_country_params import CreateCountryParams
from app.features.admin.country.domain.update_country_params import UpdateCountryParams
from app.features.admin.country.infrastructure.mappers.country_mappers import (
    map_country_model_to_entity,
    map_create_country_params_to_model,
)
from app.features.admin.country.infrastructure.models.country_model import CountryModel


class CountryRepository(CountryDatasource):

    def __init__(self, session: Session):
        self.session: Session = session

    @override
    def get_all_countries(self) -> list[Country]:
        countries_model: list[CountryModel] = self.session.query(CountryModel).all()
        countries: list[Country] = [map_country_model_to_entity(country_model) for country_model in countries_model]
        return countries

    @override
    def get_country_by_id(self, id: int) -> Country:

        country_model = self.session.query(CountryModel).filter(CountryModel.id == id).first()

        country: Country = map_country_model_to_entity(country_model)

        return country

    @override
    def create_country(self, params: CreateCountryParams) -> Country:
        country_model: CountryModel = map_create_country_params_to_model(params)
        self.session.add(country_model)
        self.session.commit()
        self.session.refresh(country_model)
        return map_country_model_to_entity(country_model)

    @override
    def update_country(self, params: UpdateCountryParams) -> Country:
        country_model = self.session.query(CountryModel).filter(CountryModel.id == params.id).first()

        country_model.name = params.name
        country_model.country_code = params.country_code
        country_model.currency_code = params.currency_code
        self.session.commit()
        self.session.refresh(country_model)
        return map_country_model_to_entity(country_model)

    @override
    def delete_country(self, id: int) -> None:
        country_model = self.session.query(CountryModel).filter(CountryModel.id == id).first()
        # TODO: raise exception if country is not found
        self.session.delete(country_model)
        self.session.commit()
        return None
