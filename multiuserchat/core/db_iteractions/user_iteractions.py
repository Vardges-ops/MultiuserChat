from multiuserchat.db_models import engine
from multiuserchat.db_models.models import Users
from sqlalchemy.orm import Session


class UserExistsException(Exception):
    """Raise when user with given email exists"""


class UserNotFoundException(Exception):
    """Raise when user with given id doesn't exist"""


class UserCRUD:

    @staticmethod
    def create_user(**kwargs) -> Users:
        """
        User creation function
        :param kwargs: user object params
        :return: created user object
        """
        user_obj = Users(**kwargs)
        with Session(bind=engine) as session:
            session.add(user_obj)
            session.commit()
        print(f"Created user object with params: {kwargs}")
        return user_obj

    @staticmethod
    def get_user_by_id(obj_id: int) -> Users:
        """
        Return user object by Id
        :Id: Filtered Users object id_ parameter
        :return: user object
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Users.Id == obj_id).one_or_none()
            return user_obj

    @staticmethod
    def get_user_by_email(email: str) -> Users:
        """
        Return user object by Id
        :email: Filtered Users object email parameter
        :return: user object
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Users.email == email).one_or_none()
            return user_obj

    @staticmethod
    def get_user_by_name(first_name: str) -> Users:
        """
        Return user object by keyword
        :first_name: Filtered Users object first_name parameter
        :return: user object
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Users.first_name == first_name).all()
            return user_obj

    @staticmethod
    def update_user_email(id_, new_email) -> bool:
        """
        Change user with given id
        :param id_: user object id
        :param new_email: user object new email
        :return: None if id_ doesn't exist
        """
        if id_ is None:
            return False
        else:
            with Session(bind=engine) as session:
                session.query(Users).filter(Users.Id == id_).update({Users.email: new_email})
                session.commit()
            print(f"Set new email with {new_email} for user with id {id_}")

    @staticmethod
    def delete_user(id_=None):
        """
        Delete User with given id parameter
        :param id_: under delete user's id
        :return:
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Users.Id == id_).one()
            user_obj.delete()  # TODO add cascade delete
            session.commit()
            print(f"Successfully deleted User with params {user_obj}")

    @staticmethod
    def get_users_by_id(*id_list):
        with Session(bind=engine) as session:
            user_objects = session.query(Users).filter(Users.id.in_(id_list)).all()
            return user_objects


class UserInteractions(UserCRUD):

    @staticmethod
    def create_insert_user(**kwargs):
        """
        This function checks if user with given email exists and if not,
        then creates it
        :param kwargs:
        :return: created user id
        """
        usr_email = kwargs.get('email')
        if UserCRUD.get_user_by_email(email=usr_email):
            raise UserExistsException(f"User with email {usr_email} already exists !")
        user_obj = super(UserCRUD).create_user(**kwargs)
        return user_obj.Id
