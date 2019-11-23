from django.contrib import admin
from crossfit.models import Mouvement

class MouvementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mouvement, MouvementAdmin)