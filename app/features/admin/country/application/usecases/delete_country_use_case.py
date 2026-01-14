from typing import override
from app.common.use_case import UseCase
from app.features.admin.country.application.contracts.country_datasource import CountryDatasource


class DeleteCountry(UseCase[int, None]):

    def __init__(self, country_datasource: CountryDatasource):
        self.country_datasource = country_datasource

    @override
    def execute(self, params: int) -> None:
        self.country_datasource.delete_country(params)
