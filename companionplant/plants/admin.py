from django.contrib import admin
from plants.models import Plant, Pest, PlantMatch, PestMatch

# Register your models here.

admin.site.register(Plant)
admin.site.register(Pest)
admin.site.register(PlantMatch)
admin.site.register(PestMatch)