from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Rooms, Conversations, RoomMembers, Users
from sqlalchemy.orm import Session


class UserExistsException(Exception):
    """Raise when user with given email exists"""


class UserNotFoundException(Exception):
    """Raise when user with given id doesn't exist"""


# TODO create middleware like object to check if passed external arguments are correct (Pydantic)


class UserCRUD:

    @staticmethod
    def create_user(**kwargs) -> Users:
        user_obj = Users(**kwargs)
        with Session(bind=engine) as session:
            session.add(user_obj)
        print(f"Created user object with params: {kwargs}")  # TODO replace with logs
        return user_obj

    @staticmethod
    def give_user_by(**kwargs) -> Users:
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(**kwargs).one()
            return user_obj

    @staticmethod
    def alter_user(id_=None, **kwargs):
        if id_ is None:
            return False
        else:
            with Session(bind=engine) as session:
                user_obj = session.query(Users).filter(Id=id_).one()
                user_obj.update(kwargs)
            print(f"Set new values with {kwargs} of user with id {id_}")

    @staticmethod
    def delete_user(id_=None):
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Id=id_).one()
            user_obj.delete()  # TODO add cascade delete
            print(f"Successfully deleted User with params {user_obj}")


class UserInteractions(UserCRUD):

    def check_user_with(self, **kwargs):
        usr = super(UserCRUD).give_user_by(**kwargs)
        return usr is None

    def create_insert_user(self, **kwargs): # TODO think if created object ID is needed or not
        """
        This function checks if user with given email exists and if not,
        then creates it
        :param kwargs:
        :return:
        """
        usr_email = kwargs.get('email')
        if self.check_user_with(email=usr_email):
            raise UserExistsException(f"User with email {usr_email} already exists !")
        user_obj = super(UserCRUD).create_user(**kwargs)
        return user_obj.Id

    def delete_user_with_params(self, **kwargs):
        usr_obj = super().give_user_by(**kwargs)
        if usr_obj is not None:
            super().delete_user(id_=usr_obj.Id)
        else:
            raise UserNotFoundException(f"User not found with params {kwargs}")

    def alter_user_with_id(self, user_id, **kwargs):
        super().alter_user(id_=user_id, **kwargs)

    def alter_user_with_email(self, user_email, **kwargs):
        super().give_user_by(id_=user_email, **kwargs)
