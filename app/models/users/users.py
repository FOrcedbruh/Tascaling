from tortoise import Model, fields
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import Task
    from app.models import Idea
    from app.models import Statistics


class User(Model):
    id = fields.BigIntField(pk=True)

    username = fields.CharField(max_length=12, unique=True)
    age = fields.IntField()
    email = fields.CharField(max_length=100, null=False)
    avatar = fields.CharField(null=True, max_length=100000)
    password = fields.BinaryField(null=False)

    tasks = fields.ReverseRelation["Task"]
    ideas = fields.ReverseRelation["Idea"]
    statistics = fields.OneToOneRelation["Statistics"]

    created_at = fields.DatetimeField(null=False, auto_now_add=True)


    class Meta:
        table = "users"