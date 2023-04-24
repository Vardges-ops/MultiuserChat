from typing import Optional, List

from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Reactions, MessageReactions, Users
from sqlalchemy.orm import Session


class ReactionInterface:

    @staticmethod
    def add_new_reaction(content) -> Reactions:
        """
        Reaction creation function
        :param kwargs: user object params
        :return: created user object
        """
        reaction_obj = Reactions(content=content)
        with Session(bind=engine) as session:
            session.add(reaction_obj)
            session.commit()
        return reaction_obj

    @staticmethod
    def get_all_reactions():
        with Session(bind=engine) as session:
            reactions = session.query(Reactions).all()
        return reactions


class MessageReactionInterface:

    @staticmethod
    def get_user_reaction_message(msg_id: int, user_id: int) -> Optional[MessageReactions]:
        """
        This function returns user message reactions if exists else None is returned
        :param msg_id: message id for filtering
        :param user_id: reaction id for filtering
        :return: filtered MessageReactions object or None
        """
        with Session(bind=engine) as session:
            react_usr_obj = session.query(MessageReactions).filter(
                MessageReactions.message_id == msg_id,
                Users.Id == user_id
            ).one_or_none()
        return react_usr_obj

    @staticmethod
    def new_message_reaction(message_id: int, user_id: int, reaction_id: int):
        """
        This function takes message id, user id and reaction id,
        checks if there is no object, then creates it
        else updates the reaction id with found object
        :param message_id: new or existing MessageReactions object's message id
        :param user_id: new or existing MessageReactions object's user id
        :param reaction_id: MessageReactions object's new reaction id
        :return:
        """
        msg_react_obj = MessageReactionInterface.get_user_reaction_message(message_id, user_id)
        with Session(bind=engine) as session:
            if msg_react_obj is None:
                session.add(MessageReactions(message_id=message_id, user_id=user_id, reaction_id=reaction_id))
            else:
                msg_react_obj.update({'reaction_id': reaction_id})

    @staticmethod
    def get_custom_message_reactions(message_id: int) -> List[MessageReactions]:
        """
        This method returns all user's reactions for given message id
        :param message_id: message id which should be checked for users reactions
        :return: List of MessageReactions object for message id, if found
        """
        with Session(bind=engine) as session:
            message_reactions = session.query(MessageReactions).filter(
                MessageReactions.message_id == message_id
            ).all()
        return message_reactions
