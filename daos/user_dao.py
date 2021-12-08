from models.user import User

import json

'''
User 物件對資料庫的操作
提供 新增、修改、查詢
模擬用本地 users.json 檔當資料庫
'''
class UserDao:

    @classmethod
    def add_user(cls, user: User) -> None:

        # 準備好使用者資料，用 json object 存
        user_list = []
        user_dict = user.to_dict()
        user_list.append(user_dict)

        # 存資料至 users.json
        with open("users.json", 'r') as fr:
            data = fr.read
            users = json.loads(data)
        with open("users.json", 'w') as fo:
            json.dump(users + user_list, fo, indent=2)

        return "OK"


    @classmethod
    def update_user(cls, user: User) -> None:

        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            data = fr.read
            users = json.loads(data)

        for single_user in users:
            if single_user['user_id'] is user.user_id:
                single_user = user.to_dict()

        with open("users.json", 'w') as fo:
            json.dump(data, fo, indent=2)

        return "OK"


    @classmethod
    def get_all_user(cls):
        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            data = fr.read
            users = json.loads(data)

        return users


    @classmethod
    def get_user(cls, user_id: str) -> User:
        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            data = fr.read
            users = json.loads(data)

        for single_user in users:
            if single_user['user_id'] is user_id:
                user = User.from_dict(single_user)

        return user
