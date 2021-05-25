from django.contrib import admin
from .models import TypeDocument, City, Country, Sexe, Departament, Person, TypeReport, Report, Coordinate

class CrudAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

admin.site.register(TypeDocument, CrudAdmin)
admin.site.register(City, CrudAdmin)
admin.site.register(Country, CrudAdmin)
admin.site.register(Sexe, CrudAdmin)
admin.site.register(Departament, CrudAdmin)
admin.site.register(Person, CrudAdmin)
admin.site.register(TypeReport, CrudAdmin)
admin.site.register(Report, CrudAdmin)
admin.site.register(Coordinate, CrudAdmin)
