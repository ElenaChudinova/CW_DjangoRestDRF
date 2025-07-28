from django.template.defaultfilters import title
from rest_framework import serializers
from habit.validators import Validator

from habit.models import Habit

class UserHabitViewSet(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["user"]

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["user"]
        validators = [Validator(field=title)]
