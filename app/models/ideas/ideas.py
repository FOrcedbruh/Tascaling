from tortoise import Model, fields



class Idea(Model):
    id = fields.BigIntField(pk=True)

    created_at = fields.DatetimeField(auto_now_add=True, null=False)
    title = fields.CharField(null=False, max_length=100)
    descritpion = fields.CharField(null=True, max_length=500)
    location = fields.CharField(null=False, max_length=100)
    user = fields.ForeignKeyField("models.User", related_name="ideas")


    class Meta:
        table = "ideas"