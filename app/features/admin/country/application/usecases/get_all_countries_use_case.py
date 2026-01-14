from typing import override
from app.common.use_case_no_params import UseCaseNoParams
from app.features.admin.country.application.contracts.country_datasource import CountryDatasource
from app.features.admin.country.domain.country_entity import Country


class GetAllCountries(UseCaseNoParams[list[Country]]):

    def __init__(self, country_datasource: CountryDatasource):
        self.country_datasource = country_datasource

    @override
    def execute(self) -> list[Country]:

        return self.country_datasource.get_all_countries()
