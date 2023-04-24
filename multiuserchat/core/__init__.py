from multiuserchat.db_models import create_db
import user_iteractions, message_reaction_iteractions
from user_iteractions import UserCRUD
from message_reaction_iteractions import MessageReactionInterface, ReactionInterface
from datetime import datetime

create_db()

if __name__ == "__main__":
    UserCRUD.create_user(first_name='Name', last_name='Surname', email='test@mail.com', password='pwd', picture_link='pic_link', last_seen=datetime.now(), status='out of office')
    us1 = UserCRUD.give_user_by_id(obj_id=1)
    nn = UserCRUD.give_user_by_id(obj_id=2)
    us2 = UserCRUD.give_user_by_email(email='test@mail.com')
    us_list = UserCRUD.give_user_by_name(first_name='Name')
    UserCRUD.update_user_email(id_=1, new_email='newemail@mail.com')
    ReactionInterface.add_new_reaction(content='reaction_ref1')
    ReactionInterface.add_new_reaction(content='reaction_ref2')
    MessageReactionInterface.new_message_reaction(1, 1, 1)  # TODO this function should be tested with message interface
    MessageReactionInterface.get_user_reaction_message(1, 1)  # TODO this function should be tested with message interface
    MessageReactionInterface.get_custom_message_reactions(1)  # TODO this function should be tested with message interface