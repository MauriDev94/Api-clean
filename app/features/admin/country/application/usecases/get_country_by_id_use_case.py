from typing_extensions import override
from app.common.use_case import UseCase
from app.features.admin.country.application.contracts.country_datasource import CountryDatasource
from app.features.admin.country.domain.entities.country_entity import Country


class GetCountryById(UseCase[int, Country]):

    def __init__(self, country_datasource: CountryDatasource):
        self.country_datasource = country_datasource

    @override
    def execute(self, params: int) -> Country:
        return self.country_datasource.get_country_by_id(params)
