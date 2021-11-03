from django.contrib import admin
from .models import Tuz, Marka
from realizacje.models import Realizacje

# Register your models here.

class TuzAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'marka', 'foto']

	
admin.site.register(Tuz, TuzAdmin)
admin.site.register(Marka)
admin.site.register(Realizacje)
