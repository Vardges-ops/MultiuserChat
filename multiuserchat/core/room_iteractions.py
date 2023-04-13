from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Rooms, Conversations, RoomMembers, Users
from sqlalchemy.orm import Session


with Session(bind=engine) as session:
    session.add()
    session.commit()


class RoomInterface:

    def create_room(self):
        room = Rooms()
