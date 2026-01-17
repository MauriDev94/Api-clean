from typing_extensions import override
from app.common.use_case import UseCase
from app.features.admin.country.domain.entities.country_entity import Country
from app.features.admin.country.application.contracts.country_datasource import CountryDatasource
from app.features.admin.country.domain.dto.create_country_params import CreateCountryParams


class CreateCountry(UseCase[CreateCountryParams, Country]):

    def __init__(self, country_datasource: CountryDatasource):
        self.country_datasource = country_datasource

    @override
    def execute(self, params: CreateCountryParams) -> Country:
        return self.country_datasource.create_country(params)
