from datetime import datetime

from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Messages
from sqlalchemy.orm import Session


class MessageInterface:

    @staticmethod
    def create_message(**kwargs):
        """
        This method receives arguments needed for message object and creates it
        :param kwargs: keyword arguments for message object
        :return:
        """
        msg_obj = Messages(**kwargs)
        with Session(bind=engine) as session:
            session.add(msg_obj)
            session.commit()

    @staticmethod
    def edit_message_content(msg_id: int, new_content: str):
        """
        This method is called for message content edit
        :param msg_id: message object id
        :param new_content: message new content
        :return:
        """
        with Session(bind=engine) as session:
            session.query(Messages).filter(Messages.Id == msg_id).update(
                {'text_content': new_content, 'is_edited': True}
            )
            session.commit()

    @staticmethod
    def update_message_sent_status(msg_id: int, is_sent: bool):
        """
        This method is called when message hasn't been sent and it's being retried to be sent.
        It receives params for message object id and sent status
        :param msg_id: message object id
        :param is_sent: message being sent status
        :return:
        """
        with Session(bind=engine) as session:
            session.query(Messages).filter(Messages.Id == msg_id).update(
                {'is_sent': is_sent, 'timestamp': datetime.now()}
            )
            session.commit()

    @staticmethod
    def delete_message(msg_id: int):
        """
        This method is called for message deletion
        :param msg_id: message object id
        :return:
        """
        with Session(bind=engine) as session:
            msg_res = session.query(Messages).filter(Messages.Id == msg_id)
            msg_res.delete()  # TODO cascade delete, also for forwarded message connected with this
            session.commit()
