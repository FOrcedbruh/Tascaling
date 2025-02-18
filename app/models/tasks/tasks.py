from tortoise import Model, fields



class Task(Model):
    id = fields.BigIntField(pk=True)

    title = fields.CharField(null=False, max_length=100, db_index=True)
    description = fields.CharField(null=True, max_length=600)
    date_to_complete = fields.DatetimeField(null=True)
    complete = fields.BooleanField(default=False)

    user = fields.ForeignKeyField("models.User", related_name="tasks")

    created_at = fields.DatetimeField(auto_now_add=True, null=False)

    class Meta:
        table ="tasks"