from django.contrib import admin
from crossfit.models import Skill


class SkillAdmin(admin.ModelAdmin):
    pass



admin.site.register(Skill, SkillAdmin)
