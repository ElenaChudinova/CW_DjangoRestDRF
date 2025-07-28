from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "user",
        "place",
        "time_lead",
        "action",
        "pleasant_habit_sign",
        "reward",
        "in_publicity",
    )
