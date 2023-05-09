from django.contrib import admin

from .models import Hra, Kategorie, Vyvojar

# Register your models here.

admin.site.register(Hra)
admin.site.register(Vyvojar)
admin.site.register(Kategorie)