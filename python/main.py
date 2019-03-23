import json

registry = { }
class RegistryMeta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        registry[name] = cls
        return cls

class Serializable(metaclass=RegistryMeta):
    def to_json(self):
        scheme = dict(self.__dict__)
        scheme['class'] = self.__class__.__name__
        return json.dumps(scheme)

class Deserializable():
    @classmethod
    def from_dict(cls, scheme):
        name = scheme.pop('class', None)
        if name:
            cls = registry[cls]
        
        instance = cls.__new__(cls)
        instance.__dict__ = scheme
        return instance


class Employee(Serializable, Deserializable):
    def __init__(self, name, position):
        self.name = name
        self.position = position

staff = []
with open('staff.json', 'r') as file:
    staff = [Employee.from_dict(scheme=e) for e in json.load(file)]

    for index, employee in enumerate(sorted(staff, key=lambda entry: entry.score, reverse=True), 1):
        print(f'{index}: {employee.name} - {employee.position}. {employee.score} points')

print()

for employee in staff:
    print(employee.to_json())
