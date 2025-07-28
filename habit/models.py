from django.db import models
from django.utils.timezone import now


class Habit(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        verbose_name="Создатель привычки",
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=50, verbose_name="Место выполнения привычки", null=True, blank=True
    )
    time_lead = models.TimeField(
        default=now,
        editable=False,
        verbose_name="Время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=200, verbose_name="Действие, которое представляет собой привычка"
    )

    time_complete = models.PositiveSmallIntegerField(
        default=120,
        verbose_name="Время на выполнение",
        null=True,
        blank=True,
    )
    frequency = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность выполнения привычки",
        null=True,
        blank=True,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Выберите связанную приятную привычку, в качестве награды. Важно указывать для полезных привычек, но не для приятных",
        blank=True,
        null=True,
    )
    pleasant_habit_sign = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Признак, указывающий на то, что привычка является приятной, а не полезной",
    )
    reward = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Награда пользователю после выполнения полезной привычки",
    )
    in_publicity = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Признак публичности",
        help_text="Укажите признак публичности",
    )

    def __str__(self):
        return f"{self.place, self.time_lead, self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
