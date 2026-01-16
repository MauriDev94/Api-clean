from abc import ABC, abstractmethod

from app.features.admin.country.domain.entities.country_entity import Country
from app.features.admin.country.domain.dto.create_country_params import CreateCountryParams
from app.features.admin.country.domain.dto.update_country_params import UpdateCountryParams


class CountryDatasource(ABC):

    @abstractmethod
    def get_all_countries(self) -> list[Country]:
        pass

    @abstractmethod
    def get_country_by_id(self, id: int) -> Country:
        pass

    @abstractmethod
    def create_country(self, params: CreateCountryParams) -> Country:
        pass

    @abstractmethod
    def update_country(self, params: UpdateCountryParams) -> Country:
        pass

    @abstractmethod
    def delete_country(self, id: int) -> None:
        pass
