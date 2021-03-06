from django.contrib import admin

from .models import CommonName, Description, Picture, Plant, Service


class PictureInline(admin.TabularInline):
    model = Picture


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [PictureInline, ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "internal_id", "external_id")
    search_fields = ("plant",)


admin.site.register(CommonName)
admin.site.register(Description)
admin.site.register(Picture)
