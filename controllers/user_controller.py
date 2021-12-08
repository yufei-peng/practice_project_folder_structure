from flask import Request

from services.user_service import UserService
from models.user import User

import json

'''
處理所有 User 相關的 request
'''
class UserController:

    @classmethod
    def add_user(cls, request: Request):
        user_string = request.data
        user = User.from_dict(json.loads(user_string))
        UserService.add_user(user)
        return "Add User Success"

    @classmethod
    def update_user(cls, request: Request):

        user_string = request.data
        user = User.from_dict(json.loads(user_string))
        UserService.update_user(user)
        return "Update User Success"

    @classmethod
    def get_all_user(cls):

        users = UserService.get_all_user()
        return users

    @classmethod
    def get_user(cls, request:Request):

        user_id = request.args.get("user_id")
        user = UserService.get_user(user_id)
        return user.to_dict()
