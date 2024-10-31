from datetime import datetime

from graphene import Mutation, Int, String, Field, Boolean, Date, Float, ObjectType

from database.connection import db_session
from database.models import MissionsModel
from gql.types import MissionsType


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = String()  # data
        airborne_aircraft = Float()  # float
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()  # float

    success = Boolean()
    mission = Field(MissionsType)

    @staticmethod
    def mutate(root, info, mission_id, mission_date, airborne_aircraft=None, attacking_aircraft=None, bombing_aircraft=None, aircraft_returned=None, aircraft_failed=None, aircraft_damaged=None, aircraft_lost=None):
        date = datetime.strptime(mission_date, '%Y-%m-%d').date()

        insert_mission = MissionsModel(mission_id=mission_id,
                                       mission_date=date,
                                       airborne_aircraft=airborne_aircraft,
                                       attacking_aircraft=attacking_aircraft,
                                       bombing_aircraft=bombing_aircraft,
                                       aircraft_returned=aircraft_returned,
                                       aircraft_failed=aircraft_failed,
                                       aircraft_damaged=aircraft_damaged,
                                       aircraft_lost=aircraft_lost)
        db_session.add(insert_mission)
        db_session.commit()
        return AddMission(success=True, mission=insert_mission)


class ConfMutation(ObjectType):
    add_Mission = AddMission.Field()