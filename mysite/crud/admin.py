from django.contrib import admin
from .models import TypeDocument, City, Country, Sexe, Departament, Person

class CrudAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

admin.site.register(TypeDocument, CrudAdmin)
admin.site.register(City, CrudAdmin)
admin.site.register(Country, CrudAdmin)
admin.site.register(Sexe, CrudAdmin)
admin.site.register(Departament, CrudAdmin)
admin.site.register(Person, CrudAdmin)

