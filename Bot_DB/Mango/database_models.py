import mongoengine


class User(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.IntField()