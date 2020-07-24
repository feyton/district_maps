from django.contrib import admin

from .models import District, Example, Member, ShapeImage, Species, Testimony

admin.site.register(District)
admin.site.register(Species)
admin.site.register(ShapeImage)
admin.site.register(Member)
admin.site.register(Testimony)
admin.site.register(Example)
# Register your models here.
