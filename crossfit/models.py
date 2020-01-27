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
    descrition = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.upper()


# class Skill(models.Model):
#     mouvements = models.ManyToManyField(Mouvement)
#     description = models.TextField(blank=True, null=True)
#     description_json = JSONField(default=dict)
#     exercices = models.ManyToManyField(Mouvement)



class WodExercices(models.Model):
    mouvement = models.ForeignKey(Mouvement, on_delete=models.PROTECT)
    position = models.IntegerField()
    metrics = JSONField(default=dict)


class ScoreType(models.Model):
    name = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        return self.name


class Score(models.Model):
    type = models.ForeignKey(ScoreType, on_delete=models.PROTECT)
    score = models.TextField()
    score_json = JSONField(default=dict)


class Wod(models.Model):
    type = models.ForeignKey(TypeOf, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    description_json = JSONField(default=dict)
    exercices = models.ManyToManyField(WodExercices)
    score = models.ForeignKey(Score, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.type, self.description)


# class RestPause(models.Model):
#     time = models.DurationField(blank=True, null=True)
#     position = models.IntegerField(blank=True, null=True)


# class Workout(models.Model):
#     exercices = models.ManyToManyField(Exercices)
#     rest = models.ManyToManyField(RestPause)
#
#     def __str__(self):
#         exercices = ", ".join(str(exercice.mouvement.name) for exercice in self.exercices.all())
#
#         return exercices


class Log(models.Model):
    # workout = models.ForeignKey(Workout, on_delete=models.PROTECT, null=True, blank=True)
    # skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)
    wod = models.ForeignKey(Wod, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(default=now)
    done = models.BooleanField()

    def __str__(self):
        return str(self.date)

class CrossFitWebSite(models.Model):
    url = models.CharField(max_length=500)

class WodScraping(models.Model):
    wod = models.TextField()
    date = models.DateField()
    url = models.ForeignKey(CrossFitWebSite, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        unique_together = [['date', 'url']]

