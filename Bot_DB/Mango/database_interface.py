import mongoengine

class database_connection:
  def __init__(self, name, age):
    self.name = name
    self.age = age