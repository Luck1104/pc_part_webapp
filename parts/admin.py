from django.contrib import admin
from parts.models import Brand, CPU, GPU, Storage, RAM, Build

# Register your models here.

admin.site.register(Brand)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Storage)
admin.site.register(RAM)
admin.site.register(Build)