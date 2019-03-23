import graphene
from app.data import repository

class Position(graphene.Enum):
    EMPLOYEE = 1
    SENIOR = 2
    CEO = 3

class AdminRights(graphene.Enum):
    ADMIN = 1
    SA = 2

class UserSchema(graphene.Interface):
    name = graphene.String(required=True)
    age = graphene.Int()
    position = graphene.Field(Position)
    id = graphene.Int()

    @classmethod
    def resolve_type(cls, instance, info):
        if instance.rights is None:
            return Member
        else:
            return Admin

class Member(graphene.ObjectType):
    class Meta:
        interfaces = (UserSchema, )

class Admin(graphene.ObjectType):
    class Meta:
        interfaces = (UserSchema, )

    rights = graphene.Field(AdminRights, required=True)    

class Query(graphene.ObjectType):
    users = graphene.List(UserSchema, required=True)
    user = graphene.Field(UserSchema, name=graphene.String())

    def resolve_users(self, info):
        return repository.get_all_users()

    def resolve_user(self, info, name):
        return repository.get_user(name)

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        position = graphene.Argument(Position)

    successful = graphene.Boolean()
    user = graphene.Field(lambda: UserSchema)

    def mutate(self, info, name, age, position):
        user = repository.add_user(name, age, position)
        successful = True
        return CreateUser(successful=successful, user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations, types=[Member, Admin])
    