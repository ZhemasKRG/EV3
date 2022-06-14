from django.contrib import admin
from .models import Carro, Persona, PersonaUsuario, Producto

# Register your models here.

admin.site.register(Carro)
admin.site.register(Persona)
admin.site.register(PersonaUsuario)
admin.site.register(Producto)