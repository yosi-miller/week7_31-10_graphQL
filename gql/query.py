from datetime import datetime

from graphene import ObjectType, List, Field, Int, String
from graphql import GraphQLError

from database.connection import db_session
from database.models import MissionsModel, TargetsModel
from gql.types import MissionsType, TargetsType


class Query(ObjectType):
    # Q - 1
    mission_by_id = Field(MissionsType, mission_id=Int(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        try:
            mission = db_session.query(MissionsModel).get(mission_id)
            if mission is None:
                raise GraphQLError('Mission not found')
            return mission
        except GraphQLError as err:
            return err

    # Q -2
    mission_by_date_range = List(MissionsType, start_date=String(required=True), end_date=String(required=True))

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
        try:
            missions = (db_session.query(MissionsModel)
                        .filter(MissionsModel.mission_date
                                .between(start, end))
                        .all())
            if not missions:
                raise GraphQLError('No missions found in the given date range')
            return missions
        except GraphQLError as err:
            raise err

    # Q - 3

    # Q - 4
    missions_by_target = List(TargetsType, target=String(required=True))

    @staticmethod
    def resolve_missions_by_target(root, info, target):

        # SELECT target_industry, mission_date
        # FROM targets
        # INNER JOIN missions ON targets.mission_id = missions.mission_id\
        # WHERE targets.target_industry = "CITIES TOWNS AND URBAN AREAS ";

        try:
            target = (db_session.query(TargetsModel)
                      .join(TargetsModel.missions)
                      .filter(TargetsModel.target_industry == target)
                      .all()
                      )
            if not target:
                raise GraphQLError('No missions found for the given target')
            return target
        except GraphQLError as err:
            return err
