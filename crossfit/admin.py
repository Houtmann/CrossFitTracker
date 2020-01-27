from django.contrib import admin
from crossfit.models import Mouvement
# from crossfit.models import Skill
from crossfit.models import TypeOf
from crossfit.models import Wod
# from crossfit.models import Workout
# from crossfit.models import Exercices, RestPause
from crossfit.models import Log, Score, ScoreType



class MouvementAdmin(admin.ModelAdmin):
    pass


# class SkillAdmin(admin.ModelAdmin):
#     pass
#
# class TypeOfAdmin(admin.ModelAdmin):
#     pass


class WodAdmin(admin.ModelAdmin):
    pass


# class WorkoutAdmin(admin.ModelAdmin):
#     list_display = ['get_exercice']
#
#     def get_exercice(self, obj):
#         return "\n".join([exos.mouvement.name for exos in obj.exercices.all()])

# class ExercicesAdmin(admin.ModelAdmin):
#     list_display = ['mouvement', 'number_of_reps', 'number_of_series', 'ris', 'position']

class RestPauseAdmin(admin.ModelAdmin):
    pass

class LogAdmin(admin.ModelAdmin):
    list_display = ['wod', 'date']

class ScoreAdmin(admin.ModelAdmin):
    pass

class ScoreTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


# admin.site.register(Workout, WorkoutAdmin)
#
# admin.site.register(TypeOf, TypeOfAdmin)
# admin.site.register(Skill, SkillAdmin)
# admin.site.register(Exercices, ExercicesAdmin)
# admin.site.register(RestPause, RestPauseAdmin)

admin.site.register(Wod, WodAdmin)

admin.site.register(Mouvement, MouvementAdmin)

admin.site.register(Log, LogAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(ScoreType, ScoreTypeAdmin)