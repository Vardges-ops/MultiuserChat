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
    def give_user_by(**kwargs) -> Users:
        """
        Return user object by keyword
        :param kwargs:
        :return: user object
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(**kwargs).one()
            return user_obj

    @staticmethod
    def alter_user(id_=None, **kwargs) -> bool:
        """
        Change user with given id
        :param id_: user object id
        :param kwargs: new params
        :return: None if id_ doesn't exist
        """
        if id_ is None:
            return False
        else:
            with Session(bind=engine) as session:
                user_obj = session.query(Users).filter(Id=id_).one()
                user_obj.update(kwargs)
                session.commit()
            print(f"Set new values with {kwargs} of user with id {id_}")

    @staticmethod
    def delete_user(id_=None):
        """
        Delete User with given id parameter
        :param id_: under delete user's id
        :return:
        """
        with Session(bind=engine) as session:
            user_obj = session.query(Users).filter(Id=id_).one()
            user_obj.delete()  # TODO add cascade delete
            session.commit()
            print(f"Successfully deleted User with params {user_obj}")


class UserInteractions(UserCRUD):

    def check_user_with(self, **kwargs):
        """
        This function accepts keyword arguments and returns true if user exists
        :param kwargs:
        :return: True if user exists, else false
        """
        usr = super(UserCRUD).give_user_by(**kwargs)
        return usr is None

    def create_insert_user(self, **kwargs):
        """
        This function checks if user with given email exists and if not,
        then creates it
        :param kwargs:
        :return: created user id
        """
        usr_email = kwargs.get('email')
        if self.check_user_with(email=usr_email):
            raise UserExistsException(f"User with email {usr_email} already exists !")
        user_obj = super(UserCRUD).create_user(**kwargs)
        return user_obj.Id

    def delete_user_with_params(self, **kwargs):
        """
        This function receives keyword arguments and deletes user with given params
        :param kwargs:
        :return:
        """
        usr_obj = super().give_user_by(**kwargs)
        if usr_obj is not None:
            super().delete_user(id_=usr_obj.Id)
        else:
            raise UserNotFoundException(f"User not found with params {kwargs}")

    def alter_user_with_id(self, user_id, **kwargs):
        """
        This function takes user id which should be changed and new keyword argument
        :param user_id: user's id which params should be updated
        :param kwargs:
        :return:
        """
        super().alter_user(id_=user_id, **kwargs)

    def alter_user_with_email(self, user_email, **kwargs):
        """
        This function takes user email which should be changed and new keyword argument
        :param user_email:
        :param kwargs:
        :return:
        """
        super().give_user_by(id_=user_email, **kwargs)
