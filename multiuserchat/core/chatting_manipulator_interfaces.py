from multiuserchat.core.db_iteractions import *


class SystemActionInitiator: # TODO run this class method when DB is initiated

    @staticmethod
    def create_system_user():
        UserCRUD.create_user(
            first_name="System", last_name="System", email="SystemMail@email.com", password='syspass',
            picture_link='syspicturelink', last_seen=None, status=None
        )

    @staticmethod
    def fill_message_reaction():
        ReactionInterface.add_new_reaction(content='reaction_ref1')
        ReactionInterface.add_new_reaction(content='reaction_ref2')

    @classmethod
    def initiate_system_methods(cls):
        cls.create_system_user()
        cls.fill_message_reaction()


class SystemMessageCreator:

    @staticmethod
    def creating_chat_message(chat_creator_id: int) -> str:
        user = UserInteractions.get_user_by_id(chat_creator_id)
        msg = f"{user.first_name}, {user.last_name} has created the chat"
        return msg

    @staticmethod
    def adding_user_message(new_user_id: int) -> str:
        user = UserInteractions.get_user_by_id(new_user_id)
        msg = f"{user.first_name}, {user.last_name} was added to the chat"
        return msg

    @staticmethod
    def removing_user_message(old_user_id: int) -> str:
        user = UserInteractions.get_user_by_id(old_user_id)
        msg = f"{user.first_name}, {user.last_name} was removed from chat"
        return msg

    @staticmethod
    def user_leaving_message(old_user_id: int) -> str:
        user = UserInteractions.get_user_by_id(old_user_id)
        msg = f"{user.first_name}, {user.last_name} has left the chat"
        return msg


class SystemMessageActions:

    def flush_message_to_chat(self, message):
        pass  # Send message to chat


class ChatStreams:

    def __init__(self, user_id):
        self.user_id = user_id

    def create_direct_chat(self, member_id): # TODO change session usage type
        room_id = RoomsInterface.create_room(
            type_name=RoomsInterface.ROOM_TYPES, name=None, pinned_message_id=None
        )
        room = RoomsInterface.get_room_by_id(room_id=room_id)
        user = UserInteractions.get_user_by_id(member_id)
        room.users.add(user)

    def create_group_chat(self, *members_id):
        # TODO add system user to the chat as well
        pass


class ENDtoENDConnector:
    def __init__(self, socket_server, socket_port):
        pass
