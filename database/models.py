from sqlalchemy import String, Column, Integer, Date, Table, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class CountriesModel(Base):
    __tablename__ = 'countries'

    country_id = Column(Integer, primary_key=True) # PK
    country_name = Column(String)

    cities = relationship('CitiesModel', back_populates='country')


class CitiesModel(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)# PK
    city_name = Column(String)
    country_id  = Column(Integer, ForeignKey("countries.country_id")) # FK
    latitude = Column(Float)
    longitude = Column(Float)

    country = relationship("CountriesModel", back_populates="cities")

class MissionsModel(Base):
    __tablename__ = "missions"

    mission_id = Column(Integer, primary_key=True) # PK int
    mission_date = Column(Date)# data
    airborne_aircraft = Column(Float) # float
    attacking_aircraft = Column(Float)
    bombing_aircraft = Column(Float)
    aircraft_returned = Column(Float)
    aircraft_failed = Column(Float)
    aircraft_damaged = Column(Float)
    aircraft_lost = Column(Float)# float

    # target = relationship('TargetsModel', back_populates='missions')

class TargetsModel(Base):
    __tablename__ = "targets"

    target_id = Column(Integer, primary_key=True) # PK
    mission_id = Column(Integer, ForeignKey("missions.missions_id"))# FK
    target_industry = Column(String)# string
    city_id = Column(Integer, ForeignKey("cities.city_id")) # FK
    target_type_id = Column(Integer, ForeignKey("cities.city_id"))# FK
    target_priority = Column(Integer)# int

    # missions = relationship("TargetsModel", back_populates="target")
    # city = relationship("Cities", back_populates="targets")
    # target_type = relationship("TargetTypes", back_populates="targets")


class TargetTypesModel(Base):
    __tablename__ = "targettypes"

    target_type_id = Column(Integer, primary_key=True) # PK
    target_type_name = Column(String) # stringq