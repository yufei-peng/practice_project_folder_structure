from __future__ import annotations

'''
使用者的實體定義
提供 from_dict 和 to_dict 方法，方便快速轉換
'''
class User(object):

    # User 的建構式
    # TODO user_id 應該要自動產生 @@，目前是靠 request 的時候給值
    def __init__(self, user_id, last_name, first_name, nickname, birthday, gender, status, skill, is_delete=False):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.nickname = nickname
        self.birthday = birthday
        self.gender = gender
        self.status = status
        self.skill = skill
        self.is_delete = is_delete

    @staticmethod
    def from_dict(user_dict: dict) -> User:
        user = User(
            user_id=user_dict.get("user_id"),
            last_name=user_dict.get("last_name"),
            first_name=user_dict.get("first_name"),
            nickname=user_dict.get("nickname"),
            birthday=user_dict.get("birthday"),
            gender=user_dict.get("gender"),
            status=user_dict.get("status"),
            skill=user_dict.get("skill"),
            is_delete=user_dict.get("is_delete"),
        )
        return user

    def to_dict(self):
        user_dict = {
            "user_id": self.user_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "nickname": self.nickname,
            "birthday": self.birthday,
            "gender": self.gender,
            "status": self.status,
            "skill": self.skill,
            "is_delete": self.is_delete
        }
        return user_dict
