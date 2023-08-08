from django.contrib import admin
from window_sill import models

admin.site.register(models.SillCategory)
admin.site.register(models.WindowSill)
admin.site.register(models.SillThickness)
admin.site.register(models.SillWidth)
admin.site.register(models.AdditionalOption)