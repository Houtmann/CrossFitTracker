from django.contrib import admin
from crossfit.models import Wod

class WodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wod, WodAdmin)