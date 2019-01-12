import datetime

import mongoengine


class User(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.IntField()


class Users(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.IntField()
    multiplier = mongoengine.IntField(min_value=1, max_value=3, default=1)
    time_stamp = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
