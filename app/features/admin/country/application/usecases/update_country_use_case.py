from typing import override
from app.common.use_case import UseCase
from app.features.admin.country.application.contracts.country_datasource import CountryDatasource
from app.features.admin.country.domain.country_entity import Country
from app.features.admin.country.domain.update_country_params import UpdateCountryParams


class UpdateCountry(UseCase[UpdateCountryParams, Country]):
    def __init__(self, country_datasource: CountryDatasource):
        self.country_datasource = country_datasource

    @override
    def execute(self, params: UpdateCountryParams) -> Country:
        return self.country_datasource.update_country(params)
