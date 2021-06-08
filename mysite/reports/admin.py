from django.contrib import admin
from .models import *

class CrudAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

admin.site.register(Report, CrudAdmin)
admin.site.register(Coordinate, CrudAdmin)
