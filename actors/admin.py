from django.contrib import admin


class ActorsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_nale", "gender")
    search_fields = ("first_name", "last_name", "age", "gender")
    ordering = ("first_name",)
