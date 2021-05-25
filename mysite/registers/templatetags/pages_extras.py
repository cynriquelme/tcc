from django import template
from registers.models import Register

register = template.Library()

@register.simple_tag
def get_register_list():
    registers = Register.objects.all()
    return registers