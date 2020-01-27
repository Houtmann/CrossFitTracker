from django.contrib import admin
from crossfit.models import TypeOf


class TypeOfAdmin(admin.ModelAdmin):
    pass


admin.site.register(TypeOf, TypeOfAdmin)
