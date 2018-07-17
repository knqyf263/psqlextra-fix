from django.db import models
from psqlextra.models import PostgresModel


class Group(PostgresModel):
    name = models.CharField(max_length=200)
    description = models.TextField()


class User(PostgresModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="user")
    age = models.IntegerField()
    bmi = models.FloatField()

