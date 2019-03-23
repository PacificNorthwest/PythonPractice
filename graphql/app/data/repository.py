from enum import Enum

class Position(Enum):
    EMPLOYEE = 1
    SENIOR = 2
    CEO = 3

class AdminRights(Enum):
    ADMIN = 1
    SA = 2

class User:
    def __init__(self, *, id, name, age, position, rights=None):
        self.id = id
        self.name = name
        self.age = age
        self.position = position
        self.rights = rights

users = [
    User(id=0, name='John', age=33, position=Position.EMPLOYEE),
    User(id=1, name='Lisa', age=45, position=Position.SENIOR),
    User(id=2, name='Adolf', age=1488, position=Position.CEO, rights=AdminRights.SA)
]

def get_all_users():
    return users

def get_user(name):
    return next(user for user in users if user.name == name)

def add_user(name, age, position):
    user = User(id=users[-1].id + 1, name=name, age=age, position=position)
    users.append(user)
    return user