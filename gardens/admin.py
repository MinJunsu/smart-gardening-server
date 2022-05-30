from django.contrib import admin
from .models import Garden, Diary


# Register your models here.
@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    pass


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    pass
