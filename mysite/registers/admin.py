from django.contrib import admin
from .models import Register
from crud.models import Category, SubCategory

# Register your models here.
class RegistersAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

    class Media:
        css = {
            'all': ('registers/css/custom_ckeditor.css',)
        }

admin.site.register(Register, RegistersAdmin)
