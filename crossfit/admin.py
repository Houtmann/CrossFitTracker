
# class Score(models.Model):
#     score = JSONField()
#     comment = models.TextField()
#
# class Workout(models.Model):
#     skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
#     wod = models.ForeignKey(Wod, on_delete=models.PROTECT)
#     date = models.DateField(default=now())
#     comment = models.TextField()
#     score = models.ForeignKey(Score)
from django.contrib import admin
from crossfit.models import Mouvement, Skill, TypeOfWod, Wod, Score, Workout

class MouvementAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class TypeOfWodAdmin(admin.ModelAdmin):
    pass

class WodAdmin(admin.ModelAdmin):
    pass
class ScoreAdmin(admin.ModelAdmin):
    pass

class WorkoutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mouvement, MouvementAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(TypeOfWod, TypeOfWodAdmin)
admin.site.register(Wod, WodAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Workout, WorkoutAdmin)