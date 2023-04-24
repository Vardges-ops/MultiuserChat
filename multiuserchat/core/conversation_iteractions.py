from datetime import datetime

from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Conversations
from sqlalchemy.orm import Session


class ConversationsInterface:

    @staticmethod
    def create_conversation(**kwargs):
        """
        This method receives arguments needed for conversation and creates it
        :param kwargs: keyword arguments for conversation object
        :return:
        """
        conv_obj = Conversations(**kwargs)
        with Session(bind=engine) as session:
            session.add(conv_obj)
            session.commit()

    @staticmethod
    def end_conversation(conv_id: int):
        """
        This method receives conversation object id and updates that object by
        setting closing time to function call moment.
        The function is called when one of users in direct chat closes the chat or
        when the day changes and conversation is being closed.
        :param conv_id: conversation object id to be updated
        :return:
        """
        with Session(bind=engine) as session:
            session.query(Conversations).filter(Conversations.Id == conv_id).update({'end_timestamp': datetime.now()})
            session.commit()

    @staticmethod
    def delete_conversation(conversation_id: int):
        pass  # TODO call this function when chat room object is deleted
