from datetime import datetime
from multiuserchat.core.db_iteractions import *


if __name__ == "__main__":
    UserCRUD.create_user(first_name='Name', last_name='Surname', email='test@mail.com', password='pwd', picture_link='pic_link', last_seen=datetime.now(), status='out of office')
    us1 = UserCRUD.get_user_by_id(obj_id=1)
    nn = UserCRUD.get_user_by_id(obj_id=2)
    us2 = UserCRUD.get_user_by_email(email='test@mail.com')
    us_list = UserCRUD.get_user_by_name(first_name='Name')
    UserCRUD.update_user_email(id_=1, new_email='newemail@mail.com')
    ReactionInterface.add_new_reaction(content='reaction_ref1')
    ReactionInterface.add_new_reaction(content='reaction_ref2')
    RoomsInterface.create_room(type_name='Group', name='Test group room')
    RoomsInterface.create_room(type_name='Direct', name='Test direct room')
    RoomsInterface.get_room_by_id(2)
    RoomsInterface.add_pinned_message(1, 2)
    ConversationsInterface.create_conversation(start_timestamp=datetime.now(), end_timestamp=None, room_id=1)
    ConversationsInterface.create_conversation(start_timestamp=datetime.now(), end_timestamp=None, room_id=2)
    ConversationsInterface.end_conversation(conv_id=1)

    MessageReactionInterface.new_message_reaction(1, 1, 1)  # TODO this function should be tested with message interface
    MessageReactionInterface.get_user_reaction_message(1, 1)  # TODO this function should be tested with message interface
    MessageReactionInterface.get_custom_message_reactions(1)  # TODO this function should be tested with message interface