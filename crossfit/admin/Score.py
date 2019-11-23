from django.contrib import admin
from crossfit.models import Score


class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Score, ScoreAdmin)
