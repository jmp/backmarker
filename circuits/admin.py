from django.contrib import admin

from .models import Circuit


class CircuitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Circuit, CircuitAdmin)
