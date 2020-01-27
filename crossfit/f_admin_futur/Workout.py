from django.contrib import admin
from crossfit.models import Workout



class WorkoutAdmin(admin.ModelAdmin):
    pass


admin.site.register(Workout, WorkoutAdmin)