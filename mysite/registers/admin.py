from django.contrib import admin
from .models import Register, Category, SubCategory, CodeQR

# Register your models here.
class RegistersAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')

    class Media:
        css = {
            'all': ('registers/css/custom_ckeditor.css',)
        }

admin.site.register(Register, RegistersAdmin)
admin.site.register(Category, RegistersAdmin)
admin.site.register(SubCategory, RegistersAdmin)
admin.site.register(CodeQR, RegistersAdmin)