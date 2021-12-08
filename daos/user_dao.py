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

        print(user)

        # 準備好使用者資料，用 json object 存
        user_list = []
        user_dict = user.to_dict()
        user_list.append(user_dict)

        print(user_list)

        # 存資料至 users.json
        with open("users.json", 'r') as fr:
            users = json.load(fr)
            print(users)
        with open("users.json", 'w') as fo:
            json.dump(users + user_list, fo, indent=2)

        return "OK"


    @classmethod
    def update_user(cls, user: User, user_id: int) -> None:

        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            users = json.load(fr)

        for single_user in users:
            print(f"*** {single_user}")
            if single_user['user_id'] == user_id:
                single_user['last_name'] = user.last_name
                single_user['first_name'] = user.first_name
                single_user['nickname'] = user.nickname
                single_user['birthday'] = user.birthday
                single_user['gender'] = user.gender
                single_user['status'] = user.status
                single_user['skill'] = user.skill
                single_user['is_delete'] = user.is_delete

        with open("users.json", 'w') as fo:
            json.dump(users, fo, indent=2)

        return "OK"


    # TODO 取得所有使用者，偷吃步直接使用 json 傳遞資料，要轉成物件傳遞
    @classmethod
    def get_all_user(cls):
        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            users = json.load(fr)

        return users


    @classmethod
    def get_user(cls, user_id: int) -> User:
        # 將檔案讀出來
        with open("users.json", 'r') as fr:
            users = json.load(fr)

        for single_user in users:
            if single_user['user_id'] == user_id:
                user = User.from_dict(single_user)
                print(users)
                return user
            else:
                pass


