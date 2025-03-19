from tortoise import Model, fields



class Statistics(Model):
    id = fields.BigIntField(pk=True)

    completed_tasks = fields.IntField(default=0)
    total_ideas = fields.IntField(default=0)
    total_tasks = fields.IntField(default=0)
    activity = fields.IntField(default=0)
    user = fields.OneToOneField("models.User", related_name="statistics", on_delete=fields.CASCADE)

    class Meta:
        table = "statistics"