from crud.models import TypeReport, SubCategory
from django.contrib import admin
from .models import Report, Coordinate

# Register your models here.
class ReportsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

admin.site.register(Report, ReportsAdmin)
admin.site.register(Coordinate, ReportsAdmin)

