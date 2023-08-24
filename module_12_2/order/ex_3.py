import json


class User:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age

    def info(self):
        return f'User(name:{self.name} age: {self.age})'

    def serialize(self):
        json_str = json.dumps(self, default=lambda o: o.__dict__)
        # type(json_str): <class 'str'>
        print(f'type(json_str): {type(json_str)}')
        print(type(json.loads(json_str)))  # <class 'dict'>
        return json.loads(json_str)

    @classmethod
    def deserialize(cls, data):
        return cls(**data)


user = User(name="Ivan", age=25)
print(user.info())  # User(name:Ivan age: 25)
serialize_user = user.serialize()
print(type(serialize_user))  # <class 'dict'>
print(serialize_user)  # {'name': 'Ivan', 'age': 25}

deserialize_user = User.deserialize(serialize_user)
print(deserialize_user.info())  # User(name:Ivan age: 25)
