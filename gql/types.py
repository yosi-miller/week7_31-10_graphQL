import graphene as g
from graphene_sqlalchemy import SQLAlchemyObjectType

from database.models import CountriesModel, TargetTypesModel, TargetsModel, MissionsModel, CitiesModel


class CountriesType(SQLAlchemyObjectType):
    class Meta:
        model = CountriesModel
        interfaces = (g.relay.Node,)


class CitiesType(SQLAlchemyObjectType):
    class Meta:
        model = CitiesModel
        interfaces = (g.relay.Node,)


class MissionsType(SQLAlchemyObjectType):
    class Meta:
        model = MissionsModel
        interfaces = (g.relay.Node,)


class TargetsType(SQLAlchemyObjectType):
    class Meta:
        model = TargetsModel
        interfaces = (g.relay.Node,)


class TargetTypesType(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypesModel
        interfaces = (g.relay.Node,)