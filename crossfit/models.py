import json

from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.forms import widgets
from django.utils.timezone import now


class Mouvement(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class TypeOf(models.Model):
    name = models.CharField(max_length=100)
    description = JSONField

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.upper()

class Skill(models.Model):
    type = models.ForeignKey(TypeOf, on_delete=models.PROTECT)
    mouvements = models.ManyToManyField(Mouvement)


class Wod(models.Model):
    type = models.ForeignKey(TypeOf, on_delete=models.PROTECT)


class Score(models.Model):
    score = JSONField()
    comment = models.TextField()


class Workout(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    wod = models.ForeignKey(Wod, on_delete=models.PROTECT)
    date = models.DateField(default=now())
    comment = models.TextField()
    score = models.ForeignKey(Score, on_delete=models.PROTECT)