from tortoise import Model, fields
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import Task
    from app.models import Idea

class User(Model):
    id = fields.BigIntField(pk=True)

    username = fields.CharField(max_length=12, unique=True)
    age = fields.IntField()
    avatar = fields.CharField(null=True, max_length=100000)

    tasks = fields.ReverseRelation["Task"]
    ideas = fields.ReverseRelation["Idea"]

    created_at = fields.DatetimeField(null=False, auto_now_add=True)


    class Meta:
        table = "users"