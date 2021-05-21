from django.contrib import admin
from .models import TypeDocument
from .models import City
from .models import Country
from .models import Sexe
from .models import Category
from .models import SubCategory
from .models import Departament
from .models import Person
from .models import TypeReport
from .models import Report
from .models import Registre
from .models import CodeQR
from .models import Coordinate

class CrudAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

admin.site.register(TypeDocument, CrudAdmin)
admin.site.register(City, CrudAdmin)
admin.site.register(Country, CrudAdmin)
admin.site.register(Sexe, CrudAdmin)
admin.site.register(Category, CrudAdmin)
admin.site.register(SubCategory, CrudAdmin)
admin.site.register(Departament, CrudAdmin)
admin.site.register(Person, CrudAdmin)
admin.site.register(TypeReport, CrudAdmin)
admin.site.register(Report, CrudAdmin)
admin.site.register(Registre, CrudAdmin)
admin.site.register(CodeQR, CrudAdmin)
admin.site.register(Coordinate, CrudAdmin)
