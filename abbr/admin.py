from django.contrib import admin

from .models import Abbr


class AbbrAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "wiki", "modified")
    search_fields = ["name", "description"]
    list_filter = ["modified"]


admin.site.register(Abbr, AbbrAdmin)
