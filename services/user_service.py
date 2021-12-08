from daos.user_dao import UserDao
from models.user import User

from flask import Request

'''
User 服務
'''
class UserService:

    @classmethod
    def add_user(cls, user: User):

        UserDao.add_user(user)

        return "OK"


    @classmethod
    def update_user(cls, user: User):

        UserDao.update_user(user)

        return "OK"


    @classmethod
    def get_all_user(cls):

        users = UserDao.get_all_user()

        return users


    @classmethod
    def get_user(cls, user_id: str):

        user = UserDao.get_user(user_id)

        return user
