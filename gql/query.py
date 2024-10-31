from graphene import ObjectType, List, Field, Int
from graphql import GraphQLError

from database.connection import db_session
from database.models import MissionsModel
from gql.types import MissionsType


class Query(ObjectType):
    mission_by_id = Field(MissionsType, mission_id=Int(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        mission = db_session.query(MissionsModel).get(mission_id)
        if mission is None:
            raise GraphQLError('Mission not found')
        return mission