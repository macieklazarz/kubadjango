from django.contrib import admin
from .models import Tuz, Marka
from realizacje.models import Realizacje
from akcesoria.models import Akcesoria
from uslugi.models import Uslugi

# Register your models here.

class TuzAdmin(admin.ModelAdmin):
	list_display = ['nazwa', 'marka', 'foto', 'opis']

	
admin.site.register(Tuz, TuzAdmin)
admin.site.register(Marka)
admin.site.register(Realizacje)
admin.site.register(Akcesoria)
admin.site.register(Uslugi)
