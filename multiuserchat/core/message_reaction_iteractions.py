from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Reactions
from sqlalchemy.orm import Session


class ReactionInterface:

    @staticmethod
    def add_new_reaction(**kwargs) -> Reactions:
        """
        Reaction creation function
        :param kwargs: user object params
        :return: created user object
        """
        reaction_obj = Reactions(**kwargs)
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
    def new_message_reaction(**kwargs):
        msg_id = kwargs.get('message_id')
        user_id = kwargs.get('user_id')
        reaction_id = kwargs.get('reaction_id')
        # TODO implement the else

    @staticmethod
    def get_user_reaction_message():
        pass

    @staticmethod
    def replace_with_new_user_reaction():
        pass

    @staticmethod
    def get_custom_message_reactions():
        pass
