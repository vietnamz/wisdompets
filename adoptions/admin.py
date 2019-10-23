from django.contrib import admin
from adoptions.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
