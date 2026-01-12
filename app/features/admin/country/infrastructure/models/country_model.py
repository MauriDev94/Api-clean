from app.core.data.source.local.sql_alchemy_base import SqlAlchemyBase
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func


class CountryModel(SqlAlchemyBase):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country_code = Column(String, unique=True, nullable=False)
    currency_code = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
