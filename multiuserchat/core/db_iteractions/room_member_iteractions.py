from typing import List

from multiuserchat.db_models import engine
from multiuserchat.db_models.models import RoomMembers
from sqlalchemy.orm import Session
from sqlalchemy import and_


class RoomMemberInterface:

    @staticmethod
    def get_room_members(room_id: int) -> List[int]:
        with Session(bind=engine) as session:
            room_users = session.query(RoomMembers).filter(RoomMembers.room_id == room_id).all()
        return [row.member_id for row in room_users]

    @staticmethod
    def get_user_rooms(user_id: int) -> List[int]:
        with Session(bind=engine) as session:
            user_rooms = session.query(RoomMembers).filter(RoomMembers.member_id == user_id).all()
        return [row.room_id for row in user_rooms]

    @staticmethod
    def delete_user_from_room(user_id: int, room_id: int):
        with Session(bind=engine) as session:
            res = session.query(RoomMembers).filter(and_(RoomMembers.room_id == room_id, RoomMembers.member_id == user_id))
            res.delete()

    @staticmethod
    def delete_room_rows(room_id: int):
        with Session(bind=engine) as session:
            room_rows = session.query(RoomMembers).filter(RoomMembers.room_id == room_id)
            room_rows.delete()

    @staticmethod
    def delete_user_rows(member_id: int):
        with Session(bind=engine) as session:
            user_rows = session.query(RoomMembers).filter(RoomMembers.member_id == member_id)
            user_rows.delete()
