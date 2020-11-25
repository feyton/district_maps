from django.contrib import admin

from .models import (
    District, Example, Member, ShapeDeleteRequest, ShapeImage, Species,
    Testimony)

admin.site.site_header = 'GIS - FEYTON'


def approve(ModelAdmin, request, queryset):
    for q in queryset:
        try:
            q.approve()
        except Exception:
            pass


approve.short_description = 'Approve deletion request'


@admin.register(ShapeDeleteRequest)
class DeleteShapeAdmin(admin.ModelAdmin):
    list_display = ('user', 'shape')
    actions = [approve]
    list_filter = ('shape', )


admin.site.register(District)
admin.site.register(Species)
admin.site.register(ShapeImage)
admin.site.register(Member)
admin.site.register(Testimony)
admin.site.register(Example)
# Register your models here.
