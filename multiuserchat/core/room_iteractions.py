from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Rooms
from sqlalchemy.orm import Session


class RoomsInterface:

    @staticmethod
    def create_room(**kwargs):
        room_obj = Rooms(**kwargs)
        with Session(bind=engine) as session:
            session.add(room_obj)
            session.commit()
        print(f"Created room object with params at {kwargs}")

    @staticmethod
    def get_room_by_id(room_id: int) -> Rooms:
        with Session(bind=engine) as session:
            room_obj = session.query(Rooms).filter(Rooms.Id == room_id).one_or_none()
        return room_obj

    @staticmethod
    def add_pinned_message(room_id: int, pin_msg_id: int):
        with Session(bind=engine) as session:
            session.query(Rooms).filter(Rooms.Id == room_id).update({'pinned_message_id': pin_msg_id})
            session.commit()
